### chatServet
A Simple chat server with python using sockets

Run the server:
`python3 chat.py`
Then connect to server using netcat
`nc localhost 7777`

This chat server contain commands:
- MSG “message”: Simply resend this message to all users.
- NICK “nickname”: Add a nickname.
- WHO: Get the list of all connected users.
- QUIT “message”: properly disconnect the server by broadcast a farewell message.
- KILL '<nick> <message>': To kick an unpleasant user, after having sent him a farewell message.
