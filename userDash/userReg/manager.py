from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migration = True


    def create_user(self, phoneNo, password = None, **extra_fields):
        if not phoneNo:
            raise ValueError('Phone Number Required')

        user = self.model(phoneNo = phoneNo, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phoneNo, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(phoneNo, password, **extra_fields)