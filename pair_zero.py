import os
import torch
import sys
import asyncio
from dotenv import load_dotenv
load_dotenv()
main_dir = os.getenv("ROOT_DIRECTORY")
sys.path.append(f"{main_dir}/pairZero")
from pairZero.model import Model

async def pair_zero(prompt: str, fps: int=5, length: int=5):
    """
    Use's pair_zero Text2Video to generate videos
    :param prompt: prompt
    :param fps: frames per second of video you want to load
    :param 
    """
    model = Model(device="cuda", dtype=torch.float16)

    params = {
        "t0": 44,
        "t1": 47,
        "motion_field_strength_x": 12,
        "motion_field_strength_y": 12,
        "video_length": length,
    }

    out_path, fps = (f"{prompt.replace(' ','_')}.mp4", fps)
    model.process_text2video(prompt, fps=fps, path=out_path, **params)
    return out_path
