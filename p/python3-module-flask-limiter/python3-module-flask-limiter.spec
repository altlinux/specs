%define _unpackaged_files_terminate_build 1
%define modulename flask_limiter

Name: python3-module-flask-limiter
Version: 2.6.2
Release: alt1
Summary: Python 3 module for rate limiting extension for flask applications
License: MIT
URL: https://flask-limiter.readthedocs.org/
VCS: https://github.com/alisaifee/flask-limiter.git

BuildArch: noarch
Group: Development/Python

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-flask
BuildRequires: python3-module-limits

%description
Flask-Limiter provides rate limiting features to flask routes. It has support
for a configurable backend for storage with current implementations for
in-memory, redis and memcache.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst LICENSE.txt
%python3_sitelibdir/%modulename
%python3_sitelibdir/*-%version.dist-info/

%changelog
* Thu Sep 22 2022 Danil Shein <dshein@altlinux.org> 2.6.2-alt1
- new version 2.6.2
  + migrate to pyproject macroses

* Mon Sep 09 2019 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- first build for ALT


