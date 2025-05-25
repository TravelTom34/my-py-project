import cv2
import numpy as np
from mss import mss
import time

def record_screen(output_filename="my_screen_record.avi", fps=20.0, duration=None, capture_region=None):
    """
    Records the screen and saves it to a video file.

    Args:
        output_filename (str): The name of the output video file (e.g., "my_screen_record.avi").
                                Ensure the extension matches the chosen codec (e.g., .avi for MJPG).
        fps (float): Frames per second for the recording.
        duration (int, optional): Duration of the recording in seconds. If None,
                                  recording continues until 'q' is pressed.
        capture_region (dict, optional): A dictionary defining the region to capture.
                                         e.g., {'top': 40, 'left': 0, 'width': 800, 'height': 640}.
                                         If None, the primary monitor is captured.
    """
    print(f"Starting screen recording to '{output_filename}'...")
    print("Press 'q' key to stop recording manually (if no duration is set).")

    with mss() as sct:
        # Get monitor dimensions
        # If no capture_region is specified, capture the primary monitor
        if capture_region is None:
            monitor_number = 1  # Often the primary monitor
            monitor = sct.monitors[monitor_number]
            capture_region = {
                "top": monitor["top"],
                "left": monitor["left"],
                "width": monitor["width"],
                "height": monitor["height"]
            }
        else:
            # Validate capture_region
            if not all(k in capture_region for k in ("top", "left", "width", "height")):
                raise ValueError("capture_region must contain 'top', 'left', 'width', and 'height' keys.")

        width = capture_region['width']
        height = capture_region['height']

        # Define the codec and create VideoWriter object
        # IMPORTANT CHANGE HERE: Using 'MJPG' for .avi container for better compatibility
        # If 'MJPG' doesn't work, consider 'XVID' or 'DIVX' for .avi
        # Or, if you want .mp4, you might try '*mp4v*' again after ensuring ffmpeg is robust,
        # but often '.avi' with 'MJPG' is more reliable in VMs.
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

        if not out.isOpened():
            print(f"Error: Could not open video writer for {output_filename}. Check file path/permissions and codec.")
            return

        start_time = time.time()
        frame_count = 0

        try:
            while True:
                # Get raw pixels from the screen
                sct_img = sct.grab(capture_region)

                # Convert to a NumPy array for OpenCV
                # mss returns BGRA, OpenCV expects BGR. Drop the Alpha channel.
                img = np.array(sct_img)[:, :, :3]

                # Write the frame to the video file
                out.write(img)
                frame_count += 1

                # Check for manual stop or duration limit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Manual stop requested.")
                    break
                if duration and (time.time() - start_time) >= duration:
                    print(f"Recording duration of {duration} seconds reached.")
                    break

        except Exception as e:
            print(f"An error occurred during recording: {e}")
        finally:
            # Release everything if job is finished or error occurred
            out.release()
            cv2.destroyAllWindows()
            print(f"Recording finished. Saved {frame_count} frames to '{output_filename}'.")

if __name__ == "__main__":
    # Example usage: Record the entire primary screen for 10 seconds at 20 FPS
    # IMPORTANT CHANGE HERE: Output filename changed to .avi
    record_screen(output_filename="my_first_screen_record.avi", fps=20, duration=10)

    # Example of capturing a specific region (uncomment to use)
    # capture_area = {'top': 100, 'left': 100, 'width': 640, 'height': 480}
    # record_screen(output_filename="my_region_record.avi", fps=15, duration=5, capture_region=capture_area)

    # Example of manual stop (uncomment to use)
    # record_screen(output_filename="manual_stop_record.avi", fps=25)