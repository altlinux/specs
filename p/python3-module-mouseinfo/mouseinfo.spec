%define _unpackaged_files_terminate_build 1
%define modulename mouseinfo
%define pypi_name MouseInfo

%def_with check

Name: python3-module-%modulename
# Due to upstream doesn't make tags we need to pull version
# from scr/mouseinfo/__init__.py (based on setup.py version discovery).
Version: 0.1.4
Release: alt1
Summary: An application to display XY position and RGB color information for the pixel currently under the mouse. 
License: GPL-3.0-or-later
Group: Development/Python3
Url: https://pypi.org/project/MouseInfo/
Vcs: https://github.com/asweigart/mouseinfo
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pyperclip)
BuildRequires: python3-module-xlib

%if_with check
BuildRequires: python3(pytest)
%endif

%description
%summary

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
%doc LICENSE* README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Apr 16 2024 Pavel Shilov <zerospirit@altlinux.org> 0.1.4-alt1
- initial build for Sisyphus
