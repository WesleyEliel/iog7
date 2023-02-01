import os
import string

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.images import ImageFile
from django.utils.crypto import get_random_string

from core.models import VideoProof


@receiver(post_save, sender=VideoProof)
def genarate_thumbnail(sender, instance, created, **kwargs):
    if not isinstance(instance, VideoProof):
        return
    if created:
        img_output_path = instance.generate_thumbnail()
        with open(img_output_path, 'rb') as existing_file:
            django_image_file = ImageFile(file=existing_file, name=f'{get_random_string(21, string.ascii_lowercase)}.jpg')
            instance.thumbnail = django_image_file
            instance.save()
        try:
            if os.path.isfile(img_output_path) or os.path.islink(img_output_path):
                os.unlink(img_output_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (img_output_path, e))