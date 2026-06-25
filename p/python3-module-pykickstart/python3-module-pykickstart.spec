%define pypi_name pykickstart

%def_without check

Name:    python3-module-%pypi_name
Version: 3.75
Release: alt1

Summary: python module for parsing and writing kickstart configs
License: GPL-2.0
Group:   Development/Python3
Url:     https://pypi.org/project/pykickstart/
Vcs:     https://github.com/pykickstart/pykickstart

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

%description
%summary

%package -n %pypi_name
Summary: Python utilities for manipulating kickstart files
Group:   Development/Python
Provides: python-kickstart-utils = %EVR
Requires: %name = %EVR

%description -n %pypi_name
Python utilities for manipulating kickstart files.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files -n %pypi_name
%doc CONTRIBUTING COPYING README.*
%_bindir/ks*
%_man1dir/ks*

%files
%doc CONTRIBUTING COPYING README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jun 25 2026 Sergey Palcheh <minergenon@altlinux.org> 3.75-alt1
- new version 3.75

* Fri Jun 12 2026 Sergey Palcheh <minergenon@altlinux.org> 3.74-alt1
- new version 3.74

* Fri Jan 24 2025 Sergey Palcheh <minergenon@altlinux.org> 3.61-alt1
- Initial build for Sisyphus
