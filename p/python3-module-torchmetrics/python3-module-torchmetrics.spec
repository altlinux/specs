%define _unpackaged_files_terminate_build 1

%define pypi_name torchmetrics

%def_without check

Name:    python3-module-%pypi_name
Version: 1.8.2
Release: alt1

Summary: Machine learning metrics for distributed, scalable PyTorch applications.
License: Apache-2.0
Group:   Development/ML
URL:     https://lightning.ai/docs/torchmetrics
Vcs:     https://github.com/Lightning-AI/torchmetrics.git

BuildRequires(pre): rpm-build-python3 rpm-macros-ml
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-test
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-doctestplus
%endif

%remove_torch_deps
Requires: pytorch

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar

%description
TorchMetrics is a collection of 100+ PyTorch metrics implementations and
an easy-to-use API to create custom metrics. It offers:

  - A standardized interface to increase reproducibility
  - Reduces boilerplate
  - Automatic accumulation over batches
  - Metrics optimized for distributed-training
  - Automatic synchronization between multiple devices

You can use TorchMetrics with any PyTorch model or with PyTorch Lightning
to enjoy additional features such as:

  - Module metrics are automatically placed on the correct device.
  - Native support for logging metrics in Lightning to reduce even
  more boilerplate.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%python3_install "--install-purelib" "%python3_sitelibdir"

%check
%pyproject_run_pytest -v

%files
%doc *.md LICENSE 
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version-*.egg-info

%changelog
* Tue Mar 03 2026 Nikita Shmatko <nash@altlinux.org> 1.8.2-alt1
- Initial build for Sisyphus.
