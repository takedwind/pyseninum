from aiohttp import ClientSession
from selenium.webdriver.remote.errorhandler import ErrorHandler, ErrorCode


class Command:

    _error_handler = ErrorHandler()

    async def command(self, method: str, url: str, session: ClientSession, **kwargs):
        async with session.request(method, url, **kwargs) as resp:
            status_code = resp.status
            if 300 <= status_code < 304:
                return self.command('GET', resp.headers.get('location', ''), session)

            res_json = await resp.json()

            if 399 < status_code <= 500:
                res_json['status'] = status_code
            if 199 < status_code < 300:
                res_json['status'] = ErrorCode.SUCCESS
            else:
                res_json['status'] = ErrorCode.UNKNOWN_ERROR

            self._error_handler.check_response(res_json)
            return res_json['value']
