import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    # ==========================================
    # 1. Chrome Configuration
    # ==========================================

    options = Options()

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )

    # ==========================================
    # 2. Parallel Execution Support
    # ==========================================

    # Get PyTest xdist worker name
    # Normal execution  -> master
    # Parallel execution -> gw0 / gw1 / gw2 / ...
    worker = os.getenv(
        "PYTEST_XDIST_WORKER",
        "master"
    )

    # Create separate Chrome profile for each worker
    profile_path = os.path.join(
        r"C:\Selenium\ChromeProfiles",
        worker
    )

    # Create profile folder if it does not exist
    os.makedirs(
        profile_path,
        exist_ok=True
    )

    # Pass worker-specific profile to Chrome
    options.add_argument(
        f"--user-data-dir={profile_path}"
    )

    # ==========================================
    # 3. Launch Browser
    # ==========================================

    driver = webdriver.Chrome(
        options=options
    )

    driver.maximize_window()

    # ==========================================
    # 4. Execute Test
    # ==========================================

    yield driver

    # ==========================================
    # 5. Close Browser
    # ==========================================

    driver.quit()


# ==========================================================
# Screenshot on Test Failure
# ==========================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # Allow PyTest to execute the test/report process
    outcome = yield

    # Get test execution result
    report = outcome.get_result()

    # Take screenshot only when actual test body fails
    if report.when == "call" and report.failed:

        # Get WebDriver from fixture
        driver = item.funcargs.get("driver")

        if driver:

            # ==========================================
            # Create Screenshot Folder
            # ==========================================

            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            # ==========================================
            # Create Timestamp
            # ==========================================

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            # ==========================================
            # Create Screenshot Path
            # ==========================================

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}_{timestamp}.png"
            )

            # ==========================================
            # Capture Screenshot
            # ==========================================

            driver.save_screenshot(
                screenshot_path
            )

            # ==========================================
            # Print Screenshot Location
            # ==========================================

            print(
                f"\nScreenshot saved: {screenshot_path}"
            )