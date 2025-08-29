import pytest

from playwright.sync_api import expect
from pages.home_page import StartPage
from pages.devices_page import DevicesPage
from helpers.constants import DeviceCredentials


class TestDeviceConfig:
    @pytest.mark.smoke
    # @pytest.mark.skip_browser('chromium')
    # @pytest.mark.only_browser('chromium')
    # @pytest.mark.parametrize('url', [WebPageUrl.START_PAGE])
    # @pytest.mark.parametrize('device_id', [DeviceCredentials.DEVICEID,
    #                                        pytest.param(DeviceCredentials.DEVICEID_2, marks=pytest.mark.xfail)])

    @pytest.mark.parametrize('device_id', [DeviceCredentials.DEVICEID])
    def test_ip_address(self,
                        page,
                        device_id: str,
                        login_set_up,
                        start_page: StartPage,
                        devices_page: DevicesPage,
                        assert_snapshot) -> None:

        # Proceed to devices tab
        # assert_snapshot(page.screenshot())
        start_page.proceed_to_devices_tab()

        # Proceed to device details page
        devices_page.select_device(device_id)

        # Validate device IP address
        expect(devices_page.device_ip_address).to_be_visible()

