%define _unpackaged_files_terminate_build 1
%define modulename pyautogui
%define pypi_name PyAutoGUI

%def_with check

Name: python3-module-%modulename
# Due to upstream doesn't make tags we need to pull version
# from pyautogui/__init__.py (based on setup.py version discovery).
Version: 0.9.54
Release: alt1
Summary: Used to programmatically control the mouse & keyboard.
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/PyAutoGUI/
Vcs: https://github.com/asweigart/pyautogui
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-xlib
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3-module-Pillow
BuildRequires: python3(pymsgbox)
BuildRequires: python3(pytest)
BuildRequires: python3(pytweening)
BuildRequires: python3(pyscreeze)
BuildRequires: python3(mouseinfo)
%endif

%add_python3_req_skip AppKit

%description
PyAutoGUI is a cross-platform GUI automation Python module for human beings.
Used to programmatically control the mouse & keyboard.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
#imposible run tests witout graphical interface
#pyproject_run_pytest

%files
%doc README.md LICENSE*
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Apr 16 2024 Pavel Shilov <zerospirit@altlinux.org> 0.9.54-alt1
- initial build for Sisyphus
