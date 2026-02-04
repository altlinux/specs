%define pypi_name mpv
%def_disable check

Name: python3-module-%pypi_name
Version: 1.0.8
Release: alt1

Summary: Python interface to the awesome mpv media player
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/jaseg/python-mpv.git

Source: https://pypi.io/packages/source/m/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

Requires: libmpv2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest) libmpv2
BuildRequires: xvfb-run python3(pyvirtualdisplay)}

%description
python-mpv is a ctypes-based python interface to the mpv media player.
It gives you more or less full control of all features of the player,
just as the lua interface does.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir_noarch/%pypi_name.py
%python3_sitelibdir_noarch/__pycache__/*
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Wed Feb 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- first build for Sisyphus



