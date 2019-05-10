def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.apk']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


def validate_file_size(value):
    from django.core.exceptions import ValidationError
    filesize = value.size
    print(filesize)

    if filesize > 1024 * 1024 * 50:
        raise ValidationError(
            "The maximum file size that can be uploaded is 50MB")
