Summary: A Python library to address multiple cloud provider APIs
Name: python-module-libcloud
Version: 0.15.1
Release: alt1
Url: http://libcloud.apache.org/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: ASL 2.0
Group: Development/Python

BuildArch: noarch
BuildRequires: python-dev python-module-setupdocs python-module-setuptools

%description
libcloud is a client library for interacting with many of the popular cloud 
server providers.  It was created to make it easy for developers to build 
products that work between any of the services that it supports.

%package tests
Summary: Unit tests
Group: Development/Python

%description tests
Unit tests for python-module-libcloud


%prep
%setup


%build
%python_build

%install
#__python setup.py install --prefix=/usr --root=%buildroot
%python_build_install --prefix=/usr

%files tests
%dir %python_sitelibdir/libcloud/test
%python_sitelibdir/libcloud/test/*

%files
%doc CHANGES.rst CONTRIBUTING.rst NOTICE README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/libcloud/test

%changelog
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

