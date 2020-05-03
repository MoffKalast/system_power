# system_power
Easily send system poweroff or reboot commands through a ros topic. Requires the following setup in sudoers:

    %sudo   ALL=NOPASSWD: /bin/systemctl reboot, /bin/systemctl poweroff

Run:

    rosrun system_power power.py
