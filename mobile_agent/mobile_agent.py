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
    d.swipe(start_x, start_y, end_x, end_y, duration=0.6)
    
    behavior.human_delay(target_seconds=1.5)
    d.app_stop_all()

if __name__ == "__main__":
    run_human_mobile_agent()
