%define pypi_name lightning-utilities
%define modulename lightning_utilities

%def_with check

Name:    python3-module-%pypi_name
Version: 0.15.2
Release: alt1

Summary: Common Python utilities and GitHub Actions in Lightning Ecosystem
License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/lightning-utilities
VCS:     https://github.com/Lightning-AI/utilities

Source: %name-%version.tar

Patch0: 0001-repalce-distutils-with-setuptools.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-tomlkit
%endif

BuildArch: noarch

%description
This repository covers the following use-cases:
    1.Reusable GitHub workflows
    2.Shared GitHub actions
    3.General Python utilities in lightning_utilities.core
    4.CLI python -m lightning_utilities.cli --help

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests \
    --ignore=tests/unittests/cli/test_command_line.py \
    --ignore=tests/scripts/test_adjust_torch_versions.py

%files
%doc *.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Thu Sep 09 2025 Roman Efimenkov <trogjan@altlinux.org> 0.15.2-alt1
- Initial build for Sisyphus.
