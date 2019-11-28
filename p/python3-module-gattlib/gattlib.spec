Name: python3-module-gattlib
Version: 0.20150805
Release: alt1

Summary: Python library to access Bluetooth LE devices
License: BSD
Group: Development/Python
Url: https://pypi.org/project/gattlib/

Source0: %name-%version-%release.tar

BuildRequires: gcc-c++ boost-python3-devel
BuildRequires: pkgconfig(bluez) pkgconfig(glib-2.0)
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/gattlib.cpython-3*.so
%python3_sitelibdir/gattlib-%version-*-info

%changelog
* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20150805-alt1
- initial
