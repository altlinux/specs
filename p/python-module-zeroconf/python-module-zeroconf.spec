%def_with python3
%define oname zeroconf

Name: python-module-zeroconf
Version: 0.17.6
Release: alt1
Summary: Pure Python Multicast DNS Service Discovery Library (Bonjour/Avahi compatible)

License: LGPLv2
Group: Development/Python
Url: https://github.com/jstasiak/python-zeroconf
Packager: Python Development Team <python at packages.altlinux.org>

Source: %name-%version.tar
Patch: python-zeroconf-0.17.4-enum34-instead-of-enum-compat.patch
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif
BuildPreReq: python-devel python-module-setuptools
%py_provides %oname

%description
This is fork of pyzeroconf, Multicast DNS Service Discovery for Python,
originally by Paul Scott-Murphy (https://github.com/paulsm/pyzeroconf),
modified by William McBrine (https://github.com/wmcbrine/pyzeroconf).

%package -n python3-module-%oname
Summary: Pure Python Multicast DNS Service Discovery Library (Bonjour/Avahi compatible)
Group: Development/Python
%py3_provides %oname
BuildArch: noarch

%description -n python3-module-%oname
This is fork of pyzeroconf, Multicast DNS Service Discovery for Python,
originally by Paul Scott-Murphy (https://github.com/paulsm/pyzeroconf),
modified by William McBrine (https://github.com/wmcbrine/pyzeroconf).
Python 3 version.

%prep
%setup
%patch -p1

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 19 2016 Anton Midyukov <antohami@altlinux.org> 0.17.6-alt1
- Initial build for Alt Linux Sisiphus.
