%define modulename geventutil

Name: python-module-geventutil
Version: 0.0.1
Release: alt1.1

Summary: Random utilities for gevent

Group: Development/Python

License: MIT
Url: https://bitbucket.org/denis/gevent-playground/overview

Packager: Vitaly Lipatov <lav@altlinux.ru>

# hg clone https://bitbucket.org/denis/gevent-playground
Source: %name-%version.tar

BuildPreReq: rpm-build-python

BuildArch: noarch

%setup_python_module %modulename

%description
Random utilities for gevent.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%{modulename}*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt1.1
- Rebuild with Python-2.7

* Thu Oct 13 2011 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus