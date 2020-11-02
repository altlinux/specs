%define oname sqlsoup
Name: python3-module-%oname
Version: 0.9.1
Release: alt2

Summary: A one step database access tool, built on the SQLAlchemy ORM.

License: MIT License
Group: Development/Python
Url: https://github.com/pyradius/pyrad

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

%py3_use SQLAlchemy
%py3_use nose

%description
SQLSoup provides a convenient way to map Python objects to relational
database tables, with no declarative code of any kind.   It's built on top
of the `SQLAlchemy <http://www.sqlalchemy.org>`_ ORM and provides a super-
minimalistic interface to an existing database.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%python3_test

%files
%python3_sitelibdir/*

%changelog
* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt2
- cleanup spec

* Sat Apr 11 2020 Eugene Omelyanovich <regatio@etersoft.ru> 0.9.1-alt1
- new version (0.9.1) with rpmgs script
