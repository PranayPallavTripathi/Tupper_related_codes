# Tupper_related_codes
This repository is for code files related to Tupper's self referential formula

reverse_tupper.py script when run presents user with a grid have height 17 cells and width 106 cells (all cells are square in shape). When the user clicks on a cell it changes colour. When the user clicks again on the same cell it comes back to its previous colour. The user can draw any two coloured pixelated drawing. After the drawing is completed the user can close the grid using the close button on the grid window. This will close the grid window and print on the terminal the value of N (the lower bound of the allowed value of y in the tupper's self referential formula i.e. N < y < N + 17) and exits. If the user then plots Tupper's formula for the range of y derived from N printed by this script, he will get back whatever he had drawn on the grid. In essence this script, encodes any two coloured pixelated image that can fit in 17pixels height and 106 pixels width into a decimal number which can then be used along with popular Tupper's formula to get back the image.

The code in reverse_tupper.py file was tested in Ubuntu Desktop 16.04 LTS with Python 3.5.2 and pygame version 1.9.3 but since it was created in haste it does not necessarily follow python best practises like pep 8, etc (Please forgive me for that!). Reference code for this script was taken from https://shreevatsa.wordpress.com/2011/04/12/how-does-tuppers-self-referential-formula-work/  and  http://programarcadegames.com/python_examples/f.php?file=array_backed_grid.py

reverse_tupper.py can be used to find the value of N from the Tupper's self referential formuala for any image. So for example you want to propose to your dream girl but you don't have enough guts to do so then instead of asking "will u marry me?", just send the following number:
588334940994006933239881717160526694330719013574310338764455874678932389012766047093716881906027373175764773907938580155764945554491645876489449024999003098943301100067189111022452790753539563018474936154464806925395224401090155796761911860065791180462554601619520303476636885452720397146726120234053198125278282156962970878157693465223739398023686931267364004495893043103018025506273490103922746411665041990517518094992534300002259319789209569948986706938304359085403007832372012284127679321573693708240600913824650584133648006071027101593600
and ask her to plot Tupper's self referential formula with the above number as N in the range of y (i.e. N < y < N + 17). When she does it she will see the following:
![Screenshot from 2022-10-03 20-35-08](https://user-images.githubusercontent.com/86939849/193611628-13bba692-fe1a-4234-8bee-a22dae4b90c3.png)
This is probably the most mathematical way to propose to your dream girl. Good luck!!!
