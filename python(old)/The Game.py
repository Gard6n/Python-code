import sys
print('-----------------------------------------')
print('Welcome to a short text based game!!')
print()
print('Things to know before starting')
print('When you get to a cross road, you have the choice of entering somthing in the (),')
#Things to know for people looking at my code!!!!!
#If you see anything with Control = input() that is for user input......... Anything else is just so the program won't close 
#sys.exit() are at the end of some paths so the program will force it self to die (exit)
print()
print('Press Anything to Enter the Game')
print('-----------------------------------------')
Start = input()
#^^^^^-Buffer so game wont start without input AKA Start Button

print('___________________________________________________')
print()
print('You wake up on a dirt floor, inside a rusty house.')
print()
print('You get to your feet and see a door before you. Do you enter? (YES) or (NO) ')
Control1 = input()
#takes input from user

if Control1.lower() == 'yes':
 #If you Enter yes it will print whats below
    print('--------------------------------------------------------------------------------------------------------------------')
    print('You walk outside and you feel the cold breeze hit your skin, its night. You see trees all around')
    print()
    print('You try to remeber how you got here BANG!! BANG!! You drop to your knees as your head feels as if its going explode')
    print()
    print('You wake up covered in snow, your on the verge of death. Before death takes you, you remeber the reason why.... with your last breath you curse Davids name...')
    print()
    print('You have Die!') 
    bad_end = input() 
    #input is here so it doesn't close the program as soon as you enter yes
    sys.exit()
    #kills program

if Control1.lower() == 'no':
 #If you Enter no it will print whats below

   print('--------------------------------------------------------------------------------------------------------------------')
   print('You walk around this house searching for clues')
   print()
   print('As you look around you spot a note on a chair. Do you read it? (YES) or (NO) ')
   Control2 = input()
   #takes input from user

   if Control2.lower() == 'yes':
   #If you Enter yes it will print whats below
    print('--------------------------------------------------------------------------------------------------------------------')
    print('As you read the note you come across the name david, you remeber the reason why.')
    print()
    print('You get the urge to stop living')
    print()
    print('You find a large piece of glass, you pick it up and it instantly makes your hand bleed')
    print()
    print('You grip the piece of glass tightly in your hand as you point it at your neck. With one thrust, you lay on the ground bleeding')
    print()
    print('As life escapes your body, you regret the choices that had leaded up to this moment')
    print()
    print('You are DEAD')
    bad_end2 = input()
    sys.exit()

   if Control2.lower() == 'no':
    print('--------------------------------------------------------------------------------------------------------------------')
    print('You decide not to read the note.')
    print()
    print('You walk around the room, seeing if you can find anything useful')
    print()
    print('You see a small square device on the ground next to the bed. Do you pick it up? (YEAH) (NAH) (STUDY IT)')
    Control3 = input()

   if Control3.lower() == 'yeah':
      print('--------------------------------------------------------------------------------------------------------------------')
      print('You pick the device up. You hold it in your hand, its cold to the touch.')
      print()
      print('You try playing with it, but to no avail. It doesnt do anything.')
      print()
      print('You took it along with you as it might come in handy later.')
      print()
      print('You decided to walk out of the room and down stairs.')
      print()
      print('As you walk around the down stairs, you spot stairs leading into a basement')
      print()
      print('You walk down the stairs of the basement, as you walk each step quack like a duck.')
      print()
      print('You walk into the enteral darkness of the basement. As you step off the last step, the stairs behind you vanish.')
      print()
      print('You are surrounded by darkness. You walk aimlessly around in the dark.')
      print()
      print('As you walk you see a dim light ahead of you, trying to reach it. you make it to the light.')
      print()
      print('The light blinds you, it takes time for you to readjust to things around you.')
      print()
      print('When you finally adjust, you see large gates in front of you. You wonder how you got here.')
      print()
      print('Looking in front of the gate, you see a sign on the gate. It reads -')
      print()
      print()
      print()
      print('------------------------------------------------------------------------------')
      print()
      print('ENTER (ghvcsesdvbnjmlkljdewxsdfcvb) TO MERGE ALL TIMELINES!')
      Control4 = input()

   if Control3.lower() == 'nah':
      print('--------------------------------------------------------------------------------------------------------------------')
      print('You decided not to touch it. You leave it there.')
      print()
      print('You decided to walk out of the room and down stairs.')
      print()
      print('As you walk around the down stairs, you spot stairs leading into a basement')
      print()
      print('You walk down the stairs of the basement, as you walk each step quack like a duck.')
      print()
      print('You walk into the enteral darkness of the basement. As you step off the last step, the stairs behind you vanish.')
      print()
      print('You are surrounded by darkness. You walk aimlessly around in the dark.')
      print()
      print('As you walk you see a dim light ahead of you, trying to reach it. you make it to the light.')
      print()
      print('The light blinds you, it takes time for you to readjust to things around you.')
      print()
      print('When you finally adjust, you see large gates in front of you. You wonder how you got here.')
      print()
      print('Looking in front of the gate, you see a sign on the gate. It reads -')
      print()
      print()
      print()
      print('------------------------------------------------------------------------------')
      print()
      print('ENTER (ghvcsesdvbnjmlkljdewxsdfcvb) TO MERGE ALL TIMELINES!')
      Control4 = input()


   if Control3.lower() == 'study it':
      print('--------------------------------------------------------------------------------------------------------------------')
      print('You decided to study this weird square object; you picked up the square object and licked it, smelled it.')
      print()
      print('You even tried to eat it. But to no avail, you decide to give up on this strange little object.')
      print()
      print('You decided to walk out of the room and down stairs.')
      print()
      print('As you walk around the down stairs, you spot stairs leading into a basement')
      print()
      print('You walk down the stairs of the basement, as you walk each step quack like a duck.')
      print()
      print('You walk into the enteral darkness of the basement. As you step off the last step, the stairs behind you vanish.')
      print()
      print('You are surrounded by darkness. You walk aimlessly around in the dark.')
      print()
      print('As you walk you see a dim light ahead of you, trying to reach it. you make it to the light.')
      print()
      print('The light blinds you, it takes time for you to readjust to things around you.')
      print()
      print('When you finally adjust, you see large gates in front of you. You wonder how you got here.')
      print()
      print('Looking in front of the gate, you see a sign on the gate. It reads -')
      print()
      print()
      print()
      print('------------------------------------------------------------------------------')
      print()
      print('ENTER (ghvcsesdvbnjmlkljdewxsdfcvb) TO MERGE ALL TIMELINES!')
      Control4 = input()

   if Control4.lower() == 'ghvcsesdvbnjmlkljdewxsdfcvb':
      print('--------------------------------------------------------------------------------------------------------------------')
      print('You understand...')
      print()
      print('Every path, Every Death, Everything now makes sense.')
      print()
      print('You use the small square deivce and You break free of the si6m8ul3at4io6nfkj ;dgfklsdfl;ksdjgkld;fjgm ;kldfjgfld;')
      no = input()
      print('ksajdfjij983piewmfvjfmpifsjcvhferijckfsvjtiugklernfmd')
      no = input()
      print('kjdfklsdjafkadjsfkl;sdjgkfdljgkld;fsjgkdfsljgdskfljglksdf;g')
      System_end = input()
      sys.exit()

   else:
      print('--------------------------------------------------------------------------------------------------------------------')
      print('You look at the window next to the bed')
      print()
      print('You get a running start and leap through the glass window')
      print()
      print('Your in the air for a few seconds before smashing into the ground')
      print()
      print('You are now a big lump of meat on the ground')
      print()
      print('YOU ARE DEAD!')
      Control4 = input()
      sys.exit()



else:
 print('--------------------------------------------------------------------------------------------------------------------')
 print('Unable to put thought into action, you stumble around the old house like a drunk')
 print()
 print('You somehow fall down the stairs.')
 print()
 print('You wake up in a cold sweat in the darkness, trying to find your way out of the enteral darkness you find yourself in.')
 print()
 print('You feel as if you walked for hours. But you soon find some fainting light ahead. Do you go towards the light? (YES)')
Control_alt = input()

if Control_alt.lower()== 'yes':
  print('--------------------------------------------------------------------------------------------------------------------')
  print('You go towards the light but soon realized that it was a mistake')
  print()
  print('The light blinds you, it takes time for you to readjust to things around you.')
  print()
  print('When you finally adjust, you see large gates in front of you. You wonder how you got here.')
  print()
  print('You decide to walk towards the large gate. You try peering through the gate bars but all you see a field that spans across miles.')
  print()
  print('You decided to see how far the gate expands across. As you start walking you feel a chill down your spine.')
  print()
  print('As you walk you feel as if it has been days since you last eaten something.')
  print()
  print('You walk and walk and walk and walk. You start to feel the urge to give up on this never ending journey.')
  print()
  print('You slowly lose energy to be able to go any further. You decided to take a rest. You set down and slowly close your eyes.')
  print()
  print('YOU HAVE DIED')
  alt = input()
  sys.exit()

else:
  print('--------------------------------------------------------------------------------------------------------------------')
  print('WOW')
  print()
  print('Am just gonna kill ya off because your entering things that arnt programed in this game so ya dieeeeeeeeeeeeeeee!')
  print()
  print('You are DEAD!')
  yourfault = input()
  sys.exit()






