from huggingface_hub import snapshot_download

from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys
import pathlib
import asyncio


async def proompt(proompt: str) -> str:
    """
    Input's your prompt and returns the path to generated video
    :param proompt: describe whatever you wanna generate
    :return: path to the generated video
    """
    model_dir = pathlib.Path("weights")
    snapshot_download(
        "damo-vilab/modelscope-damo-text-to-video-synthesis",
        repo_type="model",
        local_dir=model_dir,
    )

    pipe = pipeline("text-to-video-synthesis", model_dir.as_posix())
    test_text = {
        "text": proompt,
    }
    output_video_path = pipe(
        test_text,
    )[OutputKeys.OUTPUT_VIDEO]
    print("output_video_path:", output_video_path)
    return output_video_path
