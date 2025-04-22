from flask import request, jsonify
from app.models import User
from app import db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from flask_mail import Message
from app import mail
import hashlib

bcrypt = Bcrypt()

def register():
    try:
        print("📥 [SIGNUP] Request received")

        data = request.get_json()
        print("Received signup data:", data)

        email = data['email']
        password = data['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            print("User already exists!")
            return jsonify({"message": "User already exists"}), 409

        hashed = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, password=hashed)
        db.session.add(new_user)
        db.session.commit()

        print("User registered successfully!")
        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        print("Signup error:", str(e))
        return jsonify({"message": "Internal server error"}), 500


def login():
    try:
        print("📥 [LOGIN] Request received")
        data = request.get_json()
        print("Received login data:", data)

        user = User.query.filter_by(email=data['email']).first()
        if user and bcrypt.check_password_hash(user.password, data['password']):
            token = create_access_token(identity=user.email)
            print("✅ Login success. Token issued.")
            return jsonify({"token": token}), 200

        print("❌ Invalid credentials")
        return jsonify({"message": "Invalid credentials"}), 401

    except Exception as e:
        print("Login error:", str(e))
        return jsonify({"message": "Internal server error"}), 500


def forgot_password():
    try:
        print("📥 [FORGOT PASSWORD] Request received")

        data = request.get_json()
        email = data['email']

        # Check if the user exists
        user = User.query.filter_by(email=email).first()
        if not user:
            print("User not found!")
            return jsonify({"message": "User not found"}), 404

        # Generate a password reset token (could use JWT or a hash-based token)
        reset_token = hashlib.sha256(user.email.encode()).hexdigest()

        # Here, send an email with the reset token
        msg = Message('Password Reset Request', recipients=[email])
        msg.body = f'Click the link below to reset your password:\n\nhttp://localhost:3000/reset-password/{reset_token}'
        mail.send(msg)

        print("Password reset link sent!")
        return jsonify({"message": "Password reset link sent to your email"}), 200

    except Exception as e:
        print("Forgot Password error:", str(e))
        return jsonify({"message": "Internal server error"}), 500
