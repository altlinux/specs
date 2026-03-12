%define _unpackaged_files_terminate_build 1

%define modulename lightning
%define pypi_name pytorch-%modulename

%def_without check

Name:    python3-module-%pypi_name
Version: 2.6.1
Release: alt1

Summary: Pretrain, finetune ANY AI model of ANY size on multiple GPUs, TPUs with zero code changes.
License: Apache-2.0
Group:   Development/ML
URL:     https://lightning.ai/pytorch-lightning
VCS:     https://github.com/Lightning-AI/pytorch-lightning


BuildRequires(pre): rpm-build-python3 rpm-macros-ml
BuildRequires: python3-module-setuptools python3-module-wheel

BuildRequires: python3-module-torch-cuda-devel
BuildRequires: python3-module-pyaml
BuildRequires: python3-module-tqdm
BuildRequires: python3-module-fsspec
BuildRequires: python3-module-torchmetrics
BuildRequires: python3-module-packaging 
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-lightning-utilities

%remove_torch_deps
Requires: pytorch

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar

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
%setup -n %name-%version

%build
%pyproject_build

%install
%python3_install "--install-purelib" "%python3_sitelibdir"

%if_with check
%check
%pyproject_run_pytest -v
%endif

%files
%doc *.md LICENSE
%_bindir/fabric
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Tue Mar 03 2026 Nikita Shmatko <nash@altlinux.org> 2.6.1-alt1
- Initial build for Sisyphus.
