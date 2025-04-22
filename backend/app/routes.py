from flask import Blueprint
from app.auth import register, login

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/signup', methods=['POST'])(register)
auth_bp.route('/login', methods=['POST'])(login)
