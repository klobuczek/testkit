import unittest

from tests.shared import new_backend, get_driver_name
from tests.tls.shared import TlsServer, try_connect


class TestUnixDomainSocket(unittest.TestCase):

    def setUp(self):
        self._backend = new_backend()
        self._server = None
        self._driver = get_driver_name()

    def tearDown(self):
        if self._server:
            # If test raised an exception this will make sure that the stub
            # server is killed and it's output is dumped for analys.
            self._server.reset()
            self._server = None
        self._backend.close()

    def test_connect_with_unix_domain_socket(self):
        if self._driver not in ["go"]:
            self.skipTest("No support for connecting over Unix domain socket")

        self._server = TlsServer(
                "trustedRoot_thehost",
                disableTls=True, network="unix", bind="tmp/whatever.sock")
        self.assertTrue(try_connect(
            self._backend, self._server, "bolt+unix",
            "unix?path=%2ftestkit%2ftmp%2fwhatever.sock", port=""))
