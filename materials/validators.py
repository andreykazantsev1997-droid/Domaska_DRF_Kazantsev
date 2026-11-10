from rest_framework.serializers import ValidationError

class RecordValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = value

        if not tmp_val:
            return

        if ('http://' in tmp_val or 'https://' in tmp_val) and 'youtube.com' not in tmp_val:
            raise ValidationError('Разрешены только ссылки на видеохостинг youtube.com')
