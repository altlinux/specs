%define _unpackaged_files_terminate_build 1

Name: python3-module-gattlib
Version: 0.20150805
Release: alt2

Summary: Python library to access Bluetooth LE devices
License: BSD
Group: Development/Python
Url: https://pypi.org/project/gattlib/

Source: %name-%version.tar
Patch1: alt-boost-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ boost-python3-devel
BuildRequires: pkgconfig(bluez) pkgconfig(glib-2.0)
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup
%patch1 -p2

sed -i -e "s:@PY3VER@:%{python_version_nodots python3}:g" setup.py

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/gattlib.cpython-3*.so
%python3_sitelibdir/gattlib-%version-*-info

%changelog
* Tue May 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.20150805-alt2
- Rebuilt with boost-1.76.0.

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20150805-alt1
- initial
