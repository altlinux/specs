%define _name mygpoclient

Name: python-module-%_name
Version: 1.6
Release: alt1.1

Summary: Python interface to the my.gpodder.org webservices
License: GPLv3+
Group: Development/Python
Url: http://thpinfo.com/2010/%_name/

Source: %url/%_name-%version.tar.gz

BuildArch: noarch

BuildPreReq: rpm-build-python python-devel python-module-setuptools

%description
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
%_bindir/bpsync
%python_sitelibdir/*
%doc AUTHORS README

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt1.1
- Rebuild with Python-2.7

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- 1.6

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- first build for Sisyphus

