%define _unpackaged_files_terminate_build 1
%define pypi_name huggingface_hub
%define pypi_name_kebab huggingface-hub

Name: python3-module-%pypi_name_kebab
Version: 0.30.2
Release: alt1

Summary: The official Python client for the Huggingface Hub
License: Apache-2.0
Group: Development/Python3

Url: https://github.com/huggingface/huggingface_hub
Vcs: https://github.com/huggingface/huggingface_hub
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)

BuildArch: noarch

%description
Client library to download and publish models, datasets and other repos on the
huggingface.co hub

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/huggingface-cli
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info
%doc README.md

%changelog
* Mon Apr 14 2025 David Sultaniiazov <x1z53@altlinux.org> 0.30.2-alt1
- Initial build
