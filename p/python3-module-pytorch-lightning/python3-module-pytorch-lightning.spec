%define _unpackaged_files_terminate_build 1

%define modulename lightning
%define pypi_name pytorch-%modulename

%def_with check

Name:    python3-module-%pypi_name
Version: 2.6.5
Release: alt1

Summary: PyTorch framework for high-performance AI research
License: Apache-2.0
Group:   Development/ML
Url:     https://lightning.ai/pytorch-lightning
Vcs:     https://github.com/Lightning-AI/pytorch-lightning


BuildRequires(pre): rpm-build-pyproject rpm-macros-ml
BuildRequires: python3-module-setuptools python3-module-wheel

BuildRequires: python3-module-torch-cpu
BuildRequires: python3-module-yaml
BuildRequires: python3-module-tqdm
BuildRequires: python3-module-fsspec
BuildRequires: python3-module-torchmetrics
BuildRequires: python3-module-packaging
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-lightning-utilities
# Required by .actions/assistant.py used during prep.
BuildRequires: python3-module-jsonargparse

%if_with check
# Required by the enabled LightningCLI tests.
BuildRequires: python3-module-jsonargparse+signatures
# torch.compile tests use TorchInductor, which requires a C++ compiler.
BuildRequires: gcc-c++
BuildRequires: python3-module-psutil
BuildRequires: python3-module-tensorboardX
%endif

# Use ALT's generic PyTorch dependency instead of automatic torch requirements.
%remove_torch_deps
Requires: pytorch

# LightningCLI requires the jsonargparse signatures support.
Requires: python3-module-jsonargparse+signatures

# Limited to architectures supported by PyTorch.
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar

Patch1: pytorch-lightning-2.6.5-upstream-checkpoint-security.patch
Patch2: pytorch-lightning-2.6.5-upstream-persistent-workers-shutdown.patch
Patch3: pytorch-lightning-2.6.5-upstream-torch-compile-logging.patch
Patch4: pytorch-lightning-2.6.5-upstream-lr-finder-weights-only.patch

%description
Why PyTorch Lightning?
Training models in plain PyTorch is tedious and error-prone -
you have to manually handle things like backprop, mixed precision,
multi-GPU, and distributed training, often rewriting code for every
new project. PyTorch Lightning organizes PyTorch code to automate those
complexities so you can focus on your model and data, while keeping
full control and scaling from CPU to multi-node without changing your
core code. But if you want control of those things, you can still
opt into more DIY.

Fun analogy: If PyTorch is Javascript, PyTorch Lightning is ReactJS or NextJS.

%prep
%setup
%autopatch -p1

# TensorBoard is used only by the deselected logger test, but imported
# at module scope. Remove these imports to run the remaining CLI tests.
grep -Fxq 'from tensorboard.backend.event_processing import event_accumulator' \
    tests/tests_pytorch/test_cli.py
grep -Fxq 'from tensorboard.plugins.hparams.plugin_data_pb2 import HParamsPluginData' \
    tests/tests_pytorch/test_cli.py

sed -i \
    -e '/^from tensorboard\.backend\.event_processing import event_accumulator$/d' \
    -e '/^from tensorboard\.plugins\.hparams\.plugin_data_pb2 import HParamsPluginData$/d' \
    tests/tests_pytorch/test_cli.py

# Adjust monorepo tests for the standalone pytorch-lightning package.
python3 .actions/assistant.py copy_replace_imports \
    --source_dir="./tests" \
    --source_import="lightning.fabric,lightning.pytorch" \
    --target_import="lightning_fabric,pytorch_lightning"

%build
export PACKAGE_NAME=pytorch
%pyproject_build

%install
%pyproject_install

# Install into the architecture-specific site-packages directory
# to keep the package layout consistent with the PyTorch stack.
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%check
# Run the upstream PyTorch test suite, excluding tests that require
# unavailable optional dependencies, external network access,
# unavailable test data, or unsupported hardware.

%pyproject_run_pytest -v \
    tests/tests_pytorch \
    --ignore=tests/tests_pytorch/models/test_onnx.py \
    --ignore=tests/tests_pytorch/serve/test_servable_module_validator.py \
    --deselect=tests/tests_pytorch/models/test_hparams.py::test_save_hparams_to_yaml \
    --deselect=tests/tests_pytorch/models/test_hparams.py::test_model_save_hyper_parameters_interpolation_with_hydra \
    --deselect=tests/tests_pytorch/helpers/test_datasets.py::test_mnist \
    --deselect=tests/tests_pytorch/helpers/test_datasets.py::test_trial_mnist \
    --deselect='tests/tests_pytorch/helpers/test_datasets.py::test_pickling_dataset_mnist[MNIST-args0]' \
    --deselect='tests/tests_pytorch/helpers/test_datasets.py::test_pickling_dataset_mnist[TrialMNIST-args1]' \
    --deselect='tests/tests_pytorch/helpers/test_models.py::test_models[None-BasicGAN]' \
    --deselect='tests/tests_pytorch/helpers/test_models.py::test_models[None-ParityModuleMNIST]' \
    --deselect=tests/tests_pytorch/plugins/precision/test_bitsandbytes.py::test_bitsandbytes_plugin \
    --deselect=tests/tests_pytorch/profilers/test_profiler.py::test_pytorch_profiler_describe \
    --deselect=tests/tests_pytorch/test_cli.py::test_lightning_cli_logger_save_config \
    --deselect=tests/tests_pytorch/test_cli.py::test_lightning_cli_jsonnet \
    -k 'not test_test_patch_legacy_imports_standalone'

%files
%doc *.md LICENSE
%python3_sitelibdir/%{modulename}_fabric
%python3_sitelibdir/pytorch_%modulename
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 26 2026 Nikita Shmatko <nash@altlinux.org> 2.6.5-alt1
- Updated to version 2.6.5.
- Enabled tests.
- Switched to standalone pytorch-lightning distribution.
- Removed /usr/bin/fabric, which belongs to the lightning umbrella distribution.
- Backported security fix (Fixes: CVE-2026-58659).
- Backported upstream runtime compatibility fixes.
- Added jsonargparse signature support for LightningCLI.

* Tue Mar 03 2026 Nikita Shmatko <nash@altlinux.org> 2.6.1-alt1
- Initial build for Sisyphus.
