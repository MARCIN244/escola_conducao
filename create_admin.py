import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'escola_conducao.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Elimina o admin2 anterior se existir
User.objects.filter(username='admin2').delete()

# Cria um novo
User.objects.create_superuser('admin2', 'admin@example.com', 'admin123')
print("✓ Superuser admin2 criado com sucesso!")