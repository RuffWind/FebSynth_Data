
COPULA_CONFIG = {
    'enforce_min_max_values': True,
    'enforce_rounding': True,
    'default_distribution': None,
    'verbose': True,
}

CTGAN_CONFIG = {
    'epochs': 300,
    'batch_size': 500,
    'generator_dim': (256, 256),
    'discriminator_dim': (256, 256),
    'generator_lr': 2e-4,
    'discriminator_lr': 2e-4,
    'discriminator_steps': 1,
    'cuda': True,
    'verbose': True
}

TVAE_CONFIG = {
    'epochs': 300,
    'batch_size': 500,
    'embedding_dim': 128,
    'compress_dims': (128, 128),
    'decompress_dims': (128, 128),
    'l2scale': 1e-5,
    'loss_factor': 2,
    'cuda': True,
    'verbose': True
}

TABDDPM_CONFIG = {
    'epochs': 300,
    'batch_size': 256,
    'lr': 0.002,
    'num_timesteps': 2000,
    'd_in': None,
    'num_classes': None,
    'is_y_cond': False,
    'rtdl_params': {
        'd_layers': [256, 256, 256],
        'dropout': 0.0,
    },
    'verbose': True,
    'device': 'cuda'
}

MODEL_CONFIGS = {
    'copula': COPULA_CONFIG,
    'ctgan': CTGAN_CONFIG,
    'tvae': TVAE_CONFIG,
    'tabddpm': TABDDPM_CONFIG,
}

def get_config(model_name: str) -> dict:
    model_name_lower = model_name.lower()

    if model_name_lower not in MODEL_CONFIGS:
        available = ', '.join(MODEL_CONFIGS.keys())
        raise ValueError(
            f"未知的模型: {model_name}\n"
            f"可用的模型: {available}"
        )

    return MODEL_CONFIGS[model_name_lower].copy()
