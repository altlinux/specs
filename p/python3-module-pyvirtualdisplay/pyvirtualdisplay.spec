# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

#%%def_disable check

%define pypi_name PyVirtualDisplay
%define modulename pyvirtualdisplay

Name: python3-module-%modulename
Version: 2.2
Release: alt1
Summary: Python wrapper for Xvfb, Xephyr and Xvnc
Group: Development/Python3
License: BSD
URL: https://github.com/ponty/PyVirtualDisplay
# Source-url: %url/archive/refs/tags/%version.tar.gz
Source: %pypi_name-%version.tar
BuildArch: noarch

BuildRequires: python3-dev
BuildRequires: python3-module-setuptools

%if_disabled check
%else
BuildRequires: python3-module-easyprocess
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-psutil
BuildRequires: python3-module-pytest
BuildRequires: xmessage
BuildRequires: xorg-xephyr
BuildRequires: xorg-xvfb 
BuildRequires: /proc
%endif

%description
pyvirtualdisplay is a python wrapper for Xvfb, Xephyr and Xvnc.

%prep
%setup -n %pypi_name-%version

# TODO: package entrypoint2 and vncdotool and enable these tests
rm tests/test_race.py
rm tests/test_xvnc.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v

%files
%doc README.md
%python3_sitelibdir/%pypi_name-%version-py*.egg-info/
%python3_sitelibdir/%modulename/

%changelog
* Sun Mar 06 2022 Anton Midyukov <antohami@altlinux.org> 2.2-alt1
- initial build
