%def_without python3
%define oname zeroconf

Name: python-module-zeroconf
Version: 0.19.1
Release: alt3
Summary: Pure Python Multicast DNS Service Discovery Library (Bonjour/Avahi compatible)

License: LGPLv2
Group: Development/Python
Url: https://github.com/jstasiak/python-zeroconf
Packager: Python Development Team <python at packages.altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif
BuildPreReq: python-devel python-module-setuptools
%py_provides %oname
%py_requires enum34

%description
This is fork of pyzeroconf, Multicast DNS Service Discovery for Python,
originally by Paul Scott-Murphy (https://github.com/paulsm/pyzeroconf),
modified by William McBrine (https://github.com/wmcbrine/pyzeroconf).

%package -n python3-module-%oname
Summary: Pure Python Multicast DNS Service Discovery Library (Bonjour/Avahi compatible)
Group: Development/Python
%py3_provides %oname
%py3_requires enum
BuildArch: noarch

%description -n python3-module-%oname
This is fork of pyzeroconf, Multicast DNS Service Discovery for Python,
originally by Paul Scott-Murphy (https://github.com/paulsm/pyzeroconf),
modified by William McBrine (https://github.com/wmcbrine/pyzeroconf).
Python 3 version.

%prep
%setup
# Remove bundled egg-info
rm -rf %oname.egg-info

sed -i '/enum-compat/d' setup.py

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
* Mon Dec 02 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.1-alt3
- rebuilt as python2 only

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.1-alt2
- Rebuilt to regenerate dependencies.

* Fri Oct 20 2017 Anton Midyukov <antohami@altlinux.org> 0.19.1-alt1
- new version 0.19.1

* Mon Sep 19 2016 Anton Midyukov <antohami@altlinux.org> 0.17.6-alt1
- Initial build for Alt Linux Sisiphus.
