%define _name MiniMock

Name: python-module-minimock
Version: 1.2.6
Release: alt1.1

Summary: The simplest possible mock library
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/MiniMock

Source: http://pypi.python.org/packages/source/M/%_name/%_name-%version.tar.gz

BuildArch: noarch

BuildPreReq: rpm-build-python python-devel python-module-setuptools

%description
MiniMock is a simple library for doing Mock objects with doctest

This library provides an easy and structured way to access the
my.gpodder.org web services. In addition to subscription list
synchronization and storage, the advanced API support allows to upload
and download episode status changes.

%prep
%setup -q -n %_name-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%doc docs/*.txt

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6-alt1.1
- Rebuild with Python-2.7

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- first build for Sisyphus

