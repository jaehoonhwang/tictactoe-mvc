# tictactoe-mvc

It's finished! (Only with terminal interface)

In order to play, just downlad this and type `python play.py`

I was inspired by how many Model-View-Controller are around us in our software engineering life.

I've decided to make a tic-tac-toe game with MVC design.

I hope this helps people who is trying to learn MVC. Though this might not be a perfect MVC structure, but I'd like to think it has some resemblance of MVC strcuture.

I will start comment/documment files so that people can understand the purpose of certain files.

For me, it was funny that one file tic-tac-toe game, which only resulted in 130 lines of code can be "bloated" into hundreds line of code. But, if you think about it, it's good for extensibility while sacrificing the number of lines.

Disclaimer: I'm not so good at naming at functions and class, whic resulted in confusing and repeated names such as `grid` and `board`. I should fix it in the future. But now wheeeee.

### Future To-Do

- [ ]  Document all of them classes.
- [ ]  Safety measures for dubious input and better view organization.
- [ ]  Uncoupling of `board.py` error message into view.
- [ ]  Better exceptions (Such as invalid user input)
- [ ]  Better handling of empty string.

### Hierarchy of the code

Honestly, if you want to go through the project, this is the recommended route.

1. Start with `space.py` and `utils.py`
    1. It explains a single space of grid and `utils.py` helps with `enum` classes
2. Then go onto `grid.py`.
    1. Grid is depended on with both `board.py` and `rule.py`
3. There isn't anything special with `Controller/` or `View/`

Honestly, this progrma is a very simple program.
