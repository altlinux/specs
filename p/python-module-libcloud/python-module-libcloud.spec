%define oname libcloud

%def_with python3

Summary: A Python library to address multiple cloud provider APIs
Name: python-module-%oname
Version: 1.4.0
Release: alt1
Url: http://libcloud.apache.org/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: ASL 2.0
Group: Development/Python

Patch1: python-module-libcloud-1.1.0-alt2-drop-pysphere.patch

BuildArch: noarch
BuildRequires: python-devel python-module-setupdocs python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setupdocs python3-module-setuptools
%endif

%description
libcloud is a client library for interacting with many of the popular cloud 
server providers.  It was created to make it easy for developers to build 
products that work between any of the services that it supports.

%package -n python3-module-%oname
Summary: A Python library to address multiple cloud provider APIs
Group: Development/Python3

%description -n python3-module-%oname
libcloud is a client library for interacting with many of the popular cloud 
server providers.  It was created to make it easy for developers to build 
products that work between any of the services that it supports.


%package tests
Summary: Unit tests
Group: Development/Python

%description tests
Unit tests for python-module-%oname-tests

%package -n python3-module-%oname-tests
Summary: Unit tests
Group: Development/Python3

%description -n python3-module-%oname-tests
Unit tests for python-module-libcloud


%prep
%setup

%if_with python3
cp -fR . ../python3
%patch1 -p1
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif


%install
#__python setup.py install --prefix=/usr --root=%buildroot
%python_build_install --prefix=/usr

%if_with python3
pushd ../python3
%python3_install
popd
rm -rf libcloud/compute/drivers/vsphere.py
%endif


%files tests
%dir %python_sitelibdir/libcloud/test
%python_sitelibdir/libcloud/test/*

%files
%doc CHANGES.rst CONTRIBUTING.rst NOTICE README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/libcloud/test

%if_with python3
%files -n python3-module-%oname-tests
%dir %python3_sitelibdir/libcloud/test
%python3_sitelibdir/libcloud/test/*

%files -n python3-module-%oname
%doc CHANGES.rst CONTRIBUTING.rst NOTICE README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/libcloud/test
%exclude %python3_sitelibdir/libcloud/compute/drivers/vsphere.py
%endif


%changelog
* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.0-alt1
- New version

* Thu Jul 28 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.1.0-alt3
- Dropped pysphere for build with python3

* Thu Jul 28 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.1.0-alt2
- Build with python3 (ALT 32321)

* Mon Jul 25 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.1.0-alt1
- New version
- Build with python3

* Mon Feb 29 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.20.1-alt1
- New version

* Mon Aug 31 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.18.0-alt1
- New version

* Wed Feb 25 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.17.0-alt1
- New version

* Mon Nov 17 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.16.0-alt1
- New version
- Dropped py3 module caused dependiences issues

* Wed Oct 29 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.15.1-alt2
- Added module for Python 3

* Fri Jul 11 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.15.1-alt1
- New version

* Sat Jul 05 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.15.0-alt1
- New version

* Tue Jul 01 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.14.1-alt2
- Add %dir for unit tests, just a little fix

* Fri Jun 20 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.14.1-alt1
- New version
- Add subpackages python-module-libcloud-tests

* Thu Jan 23 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.14-alt1
- Initial build for ALT

