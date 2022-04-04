%define oname Flask-Caching
%def_disable check

Name: python3-module-flask-caching
Version: 1.10.1
Release: alt1

Summary: Cache support for Flask
License: BSD
Group: Development/Python3

URL: https://github.com/sh4nks/flask-caching
BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-flask
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pytest
BuildRequires: python3-module-redis-py

%description
Adds easy cache support to Flask.

This is a fork of the Flask-Cache extension.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc README.md PKG-INFO LICENSE
%python3_sitelibdir/*

%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.10.1-alt1
- new version 1.10.1 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- build python3 package separately

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
