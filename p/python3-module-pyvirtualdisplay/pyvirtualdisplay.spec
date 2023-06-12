# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

#%%def_disable check

%define pypi_name PyVirtualDisplay
%define modulename pyvirtualdisplay

Name: python3-module-%modulename
Version: 3.0
Release: alt1
Summary: Python wrapper for Xvfb, Xephyr and Xvnc
Group: Development/Python3
License: BSD
URL: https://github.com/ponty/PyVirtualDisplay
# Source-url: %url/archive/refs/tags/%version.tar.gz
Source: %pypi_name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_disabled check
%else
BuildRequires: python3-module-easyprocess
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-psutil
BuildRequires: pytest3
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
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
pytest3 -v

%files
%doc README.md
%python3_sitelibdir/%pypi_name-%version.dist-info/
%python3_sitelibdir/%modulename/

%changelog
* Mon Jun 12 2023 Anton Midyukov <antohami@altlinux.org> 3.0-alt1
- new version (3.0) with rpmgs script

* Sun Mar 06 2022 Anton Midyukov <antohami@altlinux.org> 2.2-alt1
- initial build
