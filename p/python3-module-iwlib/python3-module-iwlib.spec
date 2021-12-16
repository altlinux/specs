%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-iwlib
Version: 1.7.0
Release: alt1

Summary: iwlib library for Python, for interacting with wireless devices.
License: GPL-2.0
Group: Development/Python3

Url: https://github.com/nhoad/python-iwlib
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-cffi
BuildRequires: libwireless-devel

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
iwlib is a package for interfacing with iwlib, providing an
implementation to the wireless tools in Linux.

While very incomplete at the moment, it aims to eventually become a
complete implementation, as features become necessary. If you find
some functionality missing, feel free to contribute to the project, or
create an issue on the bug tracker.

Currently it provides what I consider the bare minimum to become
useful - scanning, setting the ESSID of a device, and getting the
current configuration back from a device.

%prep
%setup
%patch0 -p1

%build
%__python3 ./iwlib/_iwlib_build.py
%python3_build

%install
%python3_install
# FIXME
mv %buildroot%python3_sitelibdir/iwlib/_iwlib.abi3.so %buildroot%python3_sitelibdir/iwlib/_iwlib.so

%check
%__python3 -m pytest test

%files
%doc COPYING AUTHORS README.rst
%python3_sitelibdir/iwlib
%python3_sitelibdir/*.egg-info

%changelog
* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 1.7.0-alt1
- First build for ALT
