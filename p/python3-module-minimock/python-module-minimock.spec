%define _name MiniMock

Name: python3-module-minimock
Version: 1.2.8
Release: alt1.1

Summary: The simplest possible mock library
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/MiniMock

Source: http://pypi.python.org/packages/source/M/%_name/%_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
MiniMock is a simple library for doing Mock objects with doctest

This library provides an easy and structured way to access the
my.gpodder.org web services. In addition to subscription list
synchronization and storage, the advanced API support allows to upload
and download episode status changes.

%prep
%setup -n %_name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%doc docs/*.txt

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.8-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.8-alt1
- Initial build for Sisyphus

