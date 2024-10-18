%define pypi_name proto-plus

%def_without check

Name:    python3-module-%pypi_name
Version: 1.25.0
Release: alt1

Summary: Beautiful, idiomatic protocol buffers in Python
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/googleapis/proto-plus-python

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/proto
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Oct 18 2024 Andrey Cherepanov <cas@altlinux.org> 1.25.0-alt1
- New version.

* Fri Sep 20 2024 Andrey Cherepanov <cas@altlinux.org> 1.24.0-alt1
- Initial build for Sisyphus.
