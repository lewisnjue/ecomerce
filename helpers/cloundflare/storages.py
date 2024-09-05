from storages.backends.s3 import S3Storage

class StaticFilesStorage(S3Storage):
    #helpers.cloundflare.storages.StaticFilesStorage
    location = 'static'

class MediaFilesStorage(S3Storage):
    location = 'media'
    #helpers.cloundflare.storages.MediaFilesStorage