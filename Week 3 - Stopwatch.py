# Week 3 - "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
total = 0
current = 0
stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    return "%d:%02d.%d" %(t//600, (t//10)%60, t%10)    

def reflex_score():
    return "%d/%d" %(current, total)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopped
    timer.start()
    stopped = False
        
def stop():
    global current, total, stopped
    if not stopped:
        total += 1
        if counter % 10 == 0:
            current += 1
    stopped = True
    timer.stop()
    
    
def restart():
    global counter, current, total
    counter = 0
    timer.stop()
    current = 0
    total = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter, seconds, minutes
    counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), [118, 120], 64, "White")
    canvas.draw_text(reflex_score(), [300, 50], 32, "Red")
                    
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 200)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Restart", restart, 100)

# register event handlers


# start frame
frame.start()
timer.start()
timer.stop()

# Please remember to review the grading rubric
