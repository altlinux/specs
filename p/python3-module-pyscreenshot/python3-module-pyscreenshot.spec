%define oname pyscreenshot
%def_without check

Name: python3-module-%oname
Version: 3.1
Release: alt1.1

Summary: An extension module for click to enable registering CLI commands via setuptools entry-points.
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/click-plugins
VCS: https://github.com/click-contrib/click-plugins.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-flake8
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pillow
BuildRequires: python3-module-pygame
BuildRequires: python3-module-pytest
BuildRequires: python3-module-python-xlib
BuildRequires: python3-module-pyvirtualdisplay

BuildRequires: python3-module-easyprocess
BuildRequires: python3-module-entrypoint2
BuildRequires: python3-module-jeepney
BuildRequires: python3-module-mss
%endif

%description
An extension module for click to enable registering CLI commands
via setuptools entry-points.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.1-alt1.1
- Demodernized packaging.

* Tue Dec 12 2023 Mikhail Chernonog <snowmix@altlinux.org> 3.1-alt1
- Initial build for Sisyphus
