%define pypi_name dbussy

%def_without check

Name:    python3-module-%pypi_name
Version: 1.3
Release: alt1

Summary: Python-binding for D-Bus using asyncio
License: LGPL2.1-only
Group:   Development/Python3
URL:     https://gitlab.com/ldo/dbussy

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
%doc README COPYING
%python3_sitelibdir/__pycache__/dbussy.*.pyc
%python3_sitelibdir/__pycache__/ravel.*.pyc
%python3_sitelibdir/dbussy.py
%python3_sitelibdir/ravel.py
%python3_sitelibdir/dbussy-1.3.dist-info/METADATA

%changelog
* Mon Apr 20 2026 Artyom Bystrov <arbars@altlinux.org> 1.3-alt1
- Initial build for Sisyphus
