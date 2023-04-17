Server Status Checker
=====================

A Python script that checks the status of a Minecraft server using the `mcstatus.io` API, and sends a notification to a Discord channel when the server goes online.

Requirements
------------

-   Python 3.6 or higher
-   `requests` package
-   `dotenv` package
-   `discord` package
-   `mcstatus` package

Installation
------------

1.  Clone or download the repository.
2.  Install the required packages using `pip install -r requirements.txt`.
3.  Create a `.env` file at the root of the project with the following variables:
    -   `YOUR_SERVER_ADDRESS`: The IP address or domain name of your Minecraft server.
    -   `YOUR_DISCORD_WEBHOOK_URL`: The URL of your Discord webhook.
4.  Run the script using `python mcstatus_discord_notifier.py`.

Usage
-----

When the script runs, it will check the status of the Minecraft server every minute. If the server goes online and there are players connected, the script will send a notification to the specified Discord channel using the Discord webhook.

Customization
-------------

You can customize the behavior of the script by modifying the following variables in the `server_status_checker.py` file:

-   `url`: The URL of the `mcstatus.io` API, with the appropriate server type and address.
-   `discord_url`: The URL of the Discord webhook.
-   `prev_online`: The previous value of the number of players online.
-   `payload`: The payload of the Discord webhook message.

You can also modify the frequency of the server status checks by changing the value of the `time.sleep()` function at the end of the script.
