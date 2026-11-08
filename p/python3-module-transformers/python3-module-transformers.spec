%def_enable check

Name: python3-module-transformers
Version: 5.22.2
Release: alt1

Summary: State-of-the-art machine learning for text, vision and audio
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/transformers/
Vcs: https://github.com/huggingface/transformers
BuildArch: noarch

Source: transformers-%version.tar
Source1: .gear/check.py

BuildRequires(pre): rpm-build-pyproject >= 0.3.1
# The upstream testing extra pulls in GPU frameworks and network-only tests.
%pyproject_configure_without_autodiscovery
%pyproject_configure_pypi_package

# Checked unconditionally on import, but missing from upstream core metadata.
Requires: python3-module-filelock
%if_enabled check
BuildRequires: python3-module-filelock
BuildRequires: python3-module-tokenizers >= 0.23.1
BuildRequires: python3-module-tokenizers < 0.24.0
%endif

%description
Transformers provides pretrained model architectures and tools for natural
language processing, computer vision, audio and multimodal tasks.
Tokenizers and configuration utilities work without a machine-learning
backend. Model inference and training require PyTorch and, depending on the
model, additional optional dependencies. Pretrained weights are not included.

%prep
%setup -q -n transformers-%version
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%if_enabled check
# No model downloads or upstream conftest (which imports optional frameworks).
export HF_HUB_OFFLINE=1
export HF_HUB_DISABLE_TELEMETRY=1
export HF_HOME="$PWD/.hf-cache"
%pyproject_run -- python3 %SOURCE1
%endif

%files
%doc LICENSE README.md
%_bindir/transformers
%python3_sitelibdir/transformers/
%python3_sitelibdir/%pyproject_distinfo transformers

%changelog
* Sun Nov 08 2026 Anton Farygin <rider@altlinux.org> 5.22.2-alt1
- Initial build for Sisyphus.
