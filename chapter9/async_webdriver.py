from chapter9.async_http_client import Command
from aiohttp import ClientSession
from chapter9.async_element import Element


class AsyncBrowser(Command):

    @classmethod
    async def start(cls,
                    remote_driver_server: str,
                    capabilities: dict,
                    http_session: ClientSession,
                    reconnect_server_session: [None, str] = None):
        self = cls()
        self._http_session = http_session
        self._remote_driver_server = remote_driver_server
        self._desired_capabilities = capabilities
        if reconnect_server_session is None:
            async with self._http_session.post(f'{self._remote_driver_server}/session', json=self._desired_capabilities) as resp:
                r = await resp.json()
            self._browser_session_id = r['value'].get('sessionId', None) or r.get('sessionId', None)
        else:
            self._browser_session_id = reconnect_server_session
        self.url = f'{self._remote_driver_server}/session/{self._browser_session_id}'
        return self

    @property
    def _session_id(self):
        return getattr(self, '_browser_session_id')
    
    @property
    def _url(self):
        return getattr(self, 'url') 
    
    @property
    def _session(self):
        return getattr(self, '_http_session')

    async def command(self, method: str, endpoint: str, **kwargs):
        return await super(AsyncBrowser, self).command(method, self._url + endpoint, self._session, **kwargs)

    async def get(self, url: str):
        body = {
            'url': url
        }
        return await self.command('POST', endpoint='/url', json=body)

    async def find_element(self, strategy: str, value: str, endpoint: str = '/element'):
        if strategy == 'id':
            strategy = 'css selector'
            value = '[id="%s"]' % value
        elif strategy == 'name':
            strategy = 'css selector'
            value = '[name="%s"]' % value
        elif strategy == 'class':
            strategy = 'css selector'
            value = '.%s' % value
        body = {
            'using': strategy,
            'value': value
        }
        element = await self.command('POST', endpoint=endpoint, json=body)
        return Element(element, self._url, self._session)

    async def click(self, *location):
        element = await self.find_element(*location)
        return await element.click()

    async def clear(self, *location):
        element = await self.find_element(*location)
        return await element.clear()

    async def send_keys(self, *location, text: str):
        element = await self.find_element(*location)
        return await element.send_keys(text)

    async def text(self, *location):
        element = await self.find_element(*location)
        return await element.text()

    async def get_title(self):
        return await self.command('GET', endpoint='/title')

    async def current_url(self):
        return await self.command('GET', endpoint='/url')

    async def screenshot(self):
        return await self.command('GET', endpoint='/screenshot')

    async def quit(self):
        return await self.command('DELETE', endpoint='')

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.quit()
