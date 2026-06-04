app.background = gradient('lightBlue', 'lightCyan', 'gray')
app.flashcards = [
    ['Algorithm', 'A step by step\n proccess to solve\n a problem'],
    ['Abstraction', 'Hiding details to\n focus on the main idea'],
    ['Binary', 'A number system\n using only 0 and 1'],
    ['Bit', 'The smallest unit of digital\n information, representing\n a single 0 or 1'],
    ['Byte', 'A goup of 8 bits used to\n storen a single character,\n number, or small piece of\n data'],
    ['Input', 'Any information a\n computer receives from\n a user, device, or program\n to process'],
    ['Output', 'Any information a\n computer sends out,\n such as text, images,\n sounds, or results'],
    ['Processing', 'The computer working on\n input to make output'],
    ['Variable', 'A named storage location\n in a program that holds\n a value that can change'],
    ['Boolean', 'A data type that stores\n only two possible values:\n True or False'],
    ['Iteration', 'Repeating a block of code\n multiple times, usually\n using loops like "for" or\n "while"'],
    ['Selection', 'Using condition (if/else)\n to choose which code\n runs based on whether\n something is true'],
    ['Sequencing', 'Running code in a\n specific order,\n step by step,\n from top to bottom'],
    ['Event', 'An action like a click,\n tap, or key press that\n triggers a specific piece of\n code'],
    ['Debugging', 'Finding, understanding,\n and fixing mistakes or\n unexpected behavior in a\n program']
]

def countFlashcards():
    total = 0
    for card in app.flashcards:
        if len(card) == 2:
            total += 1
        else:
            total += 0
    return total
    
print(countFlashcards())
app.currentCard = 0
app.showAnswer = False  
app.flipping = False
app.flipStage = 0
Label('Click next for the next vocab word', 100, 380, size=12)
titleLabel = Label('Flashcard Study App', 200, 40, size = 25, bold=True)
card = Rect(90, 90, 210, 180, fill='cornsilk', border='black', borderWidth = 3)
wordLabel = Label('', 195, 180, size=22, align='center')
definition1 = Label('', 200, 150, size=17, align='center')
definition2 = Label('', 200, 175, size=17, align='center')
definition3 = Label('', 200, 200, size=17, align='center')
definition4 = Label('', 200, 225, size=17, align='center')

definition1.visible = False
definition2.visible = False
definition3.visible = False
definition4.visible = False

tapLabel = Label('Tap the card to flip', 200, 280, size=14, fill='darkgray')
tapLabel.opacity = 100
app.fadeDirection =-3 
app.fadeEnabled = True


nextButton = Rect(130, 310, 140, 40, fill='white', border='black')
nextLabel = Label('Next', 200, 330, size=18)


def wrapText(text, maxChars):
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if len(current + w) <= maxChars:
            current += w + " "
        else:
            lines.append(current)
            current = w + " "
    lines.append(current)
    return "\n".join(lines)
            
def showCard():
    question, answer = app.flashcards[app.currentCard]
    if app.showAnswer:
        wordLabel.visible = False
        
        definition1.visible = True
        definition2.visible = True
        definition3.visible = True
        definition4.visible = True

        
        lines = answer.split("\n")
        
        definition1.value = lines[0] if len(lines) > 0 else ""
        definition2.value = lines[1] if len(lines) > 1 else ""
        definition3.value = lines[2] if len(lines) > 2 else ""
        definition4.value = lines[3] if len(lines) > 3 else ""
    else:
        wordLabel.visible = True
        
        definition1.visible = False
        definition2.visible = False
        definition3.visible = False
        definition4.visible = False
        
        wordLabel.value = question


def startFlip():
    app.flipping = True
    app.flipStage = 0 

def onStep():
    if app.flipping:
        if app.flipStage == 0:
            card.width -=15
            card.centerX = 200
            if card.width <= 20:
                app.showAnswer = not app.showAnswer
                showCard()
                app.flipStage = 1
        elif app.flipStage == 1:
            card.width += 15
            card.centerX = 200
            if card.width >= 210:
                card.width = 210
                app.flipping = False
                
    if app.fadeEnabled:
        newOpacity = tapLabel.opacity + app.fadeDirection
        if newOpacity > 100 or newOpacity < 30:
            app.fadeDirection *= -1
            newOpacity = tapLabel.opacity + app.fadeDirection
        tapLabel.opacity = newOpacity
            
def onMousePress(x,y):
    if card.hits(x,y) and not app.flipping:
        app.fadeEnabled = False
        tapLabel.opacity = 100
        startFlip()
        
    elif nextButton.hits(x,y):
        app.currentCard = (app.currentCard + 1) % len(app.flashcards)
        app.showAnswer = False
        app.fadeEnabled = True
        showCard()
showCard()
