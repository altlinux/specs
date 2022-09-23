%define _unpackaged_files_terminate_build 1
%define modulename limits

Name: python3-module-%modulename
Version: 2.7.0
Release: alt1
Summary: Python module to implement rate limiting 
License: MIT
URL: https://limits.readthedocs.io/en/stable/
VCS: https://github.com/alisaifee/limits.git

BuildArch: noarch
Group: Development/Python

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Python module to implement rate limiting using various strategies and
storage backends such as redis & memcached.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst LICENSE.txt
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info/

%changelog
* Thu Sep 22 2022 Danil Shein <dshein@altlinux.org> 2.7.0-alt1
- new version 2.7.0
  + migrate to pyproject macroses

* Mon Sep 09 2019 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- first build for ALT

