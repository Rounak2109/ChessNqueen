Make sure you have Docker installed.

To build this the first time you simply have to run:

$ git clone git@github.com:rounak2109/ChessNqueen.git

$ cd ChessNqueen

$ docker-compose up --build


Visit 0.0.0.0:8000/chess/ and You will be able to see Hello World (Voila), Your Django Server is Up and running

Now, You will be needing PostMan or Insomnia installed on your PC, which will be able to test API endpoints

Use 0.0.0.0:8000/chess/queen/ with POST method and in JSON body send 

{"positions": {"Queen": "H1", "Bishop": "B7", "Rook":"H8", "Knight": "F2"}}
in this FORMAT to get the valid positions of queen

Output - {"valid_moves":["A1", "B1", "C1", "E1", "F1", "G1", "B7", "H8"]}

Use 0.0.0.0:8000/chess/knight/ with POST method and in JSON body send
{"positions": {"Queen": "H1", "Bishop": "B7", "Rook":"H8", "Knight": "F2"}}
in this FORMAT to get the valid positions of knight

Available endpoints 

0.0.0.0:8000/chess/queen
0.0.0.0:8000/chess/knight
0.0.0.0:8000/chess/rook
0.0.0.0:8000/chess/bishop





