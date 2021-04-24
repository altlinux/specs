%define oname Flask-Migrate

Name: python3-module-flask-migrate
Version: 2.7.0
Release: alt1

Summary: SQLAlchemy database migrations for Flask applications using Alembic

License: MIT
Group: Development/Python
Url: https://github.com/miguelgrinberg/flask-migrate/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro >= 2.2.5

%py3_use flask
%py3_use alembic
%py3_use flask-sqlalchemy
%py3_use flask-script

%description
Flask-Migrate is an extension that handles SQLAlchemy database migrations
for Flask applications using Alembic.
The database operations are provided as command-line arguments
under the flask db command.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
%python3_test

%files
%python3_sitelibdir/*

%changelog
* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 2.7.0-alt1
- new version 2.7.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.5.3-alt3
- use flask-sqlalchemy normalized name

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.5.3-alt2
- cleanup spec

* Mon Apr 13 2020 Eugene Omelyanovich <regatio@etersoft.ru> 2.5.3-alt1
- new version (2.5.3) with rpmgs script
