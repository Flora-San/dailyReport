# Daily Email Report Automation

This project provides a Python script to automate the process of sending daily email reports. The script uses the `smtplib` and `email` libraries to send emails and the `schedule` library to run the task at a specified time each day.

## Prerequisites

- Python 3.x
- Gmail account (or another email service)
- The following Python libraries:
  - `smtplib` (built-in)
  - `email` (built-in)
  - `schedule`

You can install the `schedule` library using pip:

```bash
pip install schedule
```

## Setup Instructions

1. **Clone the repository or download the script:**
   ```bash
   git clone https://github.com/yourusername/daily-email-report.git
   cd daily-email-report
   ```

2. **Configure Email Credentials:**
   Update the email credentials and recipient email address in the script (`daily_report.py`):
   ```python
   sender_email = "your_email@gmail.com"
   sender_password = "your_password"
   recipient_email = "recipient_email@example.com"
   ```

3. **Enable "Less secure app access" in your Gmail account:**
   - Go to your Google Account.
   - Select Security.
   - Under "Less secure app access," turn on "Allow less secure apps."

4. **Run the script:**
   ```bash
   python daily_report.py
   ```

5. **(Optional) Set up the script to run on startup:**

   ### On Windows:
   1. Create a shortcut of the `daily_report.py` script.
   2. Press `Win + R`, type `shell:startup`, and press Enter.
   3. Copy the shortcut to the Startup folder.

   ### On macOS and Linux:
   1. Open the `Terminal`.
   2. Use `crontab -e` to edit the cron jobs.
   3. Add the following line (adjust the path as needed):
      ```bash
      @reboot python3 /path/to/daily_report.py
      ```

## Customization

- **Email Content:**
  Modify the `subject` and `body` variables in the script to customize the email content.
  ```python
  subject = "Daily Report"
  body = "This is your daily report."
  ```

- **Schedule:**
  Change the schedule timing as needed. The current setting sends the email daily at 09:00 AM.
  ```python
  schedule.every().day.at("09:00").do(send_email)
  ```

## Troubleshooting

- Ensure that the email credentials are correct.
- Make sure "Less secure app access" is enabled for your Gmail account.
- Check your internet connection.
- Review any error messages printed to the console for additional clues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [smtplib](https://docs.python.org/3/library/smtplib.html)
- [email](https://docs.python.org/3/library/email.html)
- [schedule](https://pypi.org/project/schedule/)


