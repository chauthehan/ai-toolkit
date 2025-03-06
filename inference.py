import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained("/root/ai-toolkit/output/ban_chi_hai_1_flux_lora_v1/ban_chi_hai_1_flux_lora_v1_000000250.safetensors", torch_dtype=torch.bfloat16)
pipe.enable_model_cpu_offload()

prompt = "tok is sleeping"
out = pipe(
    prompt=prompt,
    guidance_scale=3.5,
    height=1024,
    width=1024,
    num_inference_steps=50,
).images[0]
out.save("image.png")