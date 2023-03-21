%define _unpackaged_files_terminate_build 1
%define oname Flask-Migrate

%def_enable check

Name: python3-module-flask-migrate
Version: 4.0.4
Release: alt1

Summary: SQLAlchemy database migrations for Flask applications using Alembic

License: MIT
Group: Development/Python3
Url: https://github.com/miguelgrinberg/Flask-Migrate
VCS: https://github.com/miguelgrinberg/Flask-Migrate

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_enabled check
BuildRequires: python3-module-flask
BuildRequires: python3-module-alembic >= 1.7.0
BuildRequires: python3-module-flask-sqlalchemy
BuildRequires: python3-module-greenlet
%endif

%description
Flask-Migrate is an extension that handles SQLAlchemy database migrations
for Flask applications using Alembic.
The database operations are provided as command-line arguments
under the flask db command.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject -- -vra tests

%files
%python3_sitelibdir/*

%changelog
* Tue Mar 21 2023 Danil Shein <dshein@altlinux.org> 4.0.4-alt1
- new version 4.0.4
  + fix FTBFS
  + migrate to pyproject_installer

* Sat Mar 05 2022 Danil Shein <dshein@altlinux.org> 3.1.0-alt1
- new version 3.1.0
  + enable test
  + remove Flask-Script dependency

* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 2.7.0-alt1
- new version 2.7.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.5.3-alt3
- use flask-sqlalchemy normalized name

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.5.3-alt2
- cleanup spec

* Mon Apr 13 2020 Eugene Omelyanovich <regatio@etersoft.ru> 2.5.3-alt1
- new version (2.5.3) with rpmgs script
