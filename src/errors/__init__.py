from werkzeug.exceptions import HTTPException

class HymnDownloaderException(HTTPException):
    code = 500
    description = '赞美诗下载器异常'

class PlatformNotSupport(HymnDownloaderException):
    code = 400
    description = '不支持的平台'

class ParseFailed(HymnDownloaderException):
    code = 500
    description = '解析失败'
