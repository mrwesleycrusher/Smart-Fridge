# Kill gdbserver if it's running
ssh pi@10.42.0.253 killall gdbserver &> /dev/null

# Compile myprogram and launch gdbserver, listening on port 9091
ssh \
  -L52698:localhost:52698 \
  pi@10.42.0.253 \
  "zsh -l -c 'cd /home/pi/projects/Smart-Fridge/LCD && make && gdbserver :52698 /home/pi/projects/Smart-Fridge/LCD/lcd'"