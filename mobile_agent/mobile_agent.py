import uiautomator2 as u2
import behavior  # Works instantly now!

def run_human_mobile_agent():
    print("[Agent] Connecting to the Emulator...")
    d = u2.connect() 
    
    print("[Agent] Opening Calculator...")
    d.app_start("com.google.android.calculator")
    
    # Use our human brain for the delay
    behavior.human_delay(target_seconds=2.5)
    
    # Calculate humanized swipe path with variance
    start_x, start_y = behavior.human_coordinates(500, 1600, variance=10)
    end_x, end_y = behavior.human_coordinates(500, 400, variance=10)
    
    print("[Agent] Executing humanized screen swipe...")
    # 1. We start a bit higher up (1400 instead of 1600) so we are firmly on the screen
    # 2. We push the end point higher up (300 instead of 400) to ensure the menu snaps open
    start_x, start_y = behavior.human_coordinates(500, 1400, variance=10)
    end_x, end_y = behavior.human_coordinates(500, 300, variance=10)
    
    # 3. Increase duration to 1.2 seconds so the emulator registers the drag smoothly
    d.swipe(start_x, start_y, end_x, end_y, duration=1.2)
    
    behavior.human_delay(target_seconds=1.5)
    d.app_stop_all()

if __name__ == "__main__":
    run_human_mobile_agent()
