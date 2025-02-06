%define _unpackaged_files_terminate_build 1
%define pypi_name flask-migrate
%define mod_name flask_migrate
# setuptools-specific normalization
%define distinfo_name Flask_Migrate

%def_with check

Name: python3-module-%pypi_name
Version: 4.1.0
Release: alt1
Summary: SQLAlchemy database migrations for Flask applications using Alembic
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flask-Migrate/
VCS: https://github.com/miguelgrinberg/Flask-Migrate
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-%release.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Flask-Migrate is an extension that handles SQLAlchemy database migrations
for Flask applications using Alembic.
The database operations are provided as command-line arguments
under the flask db command.

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%distinfo_name-%version.dist-info/

%changelog
* Thu Feb 06 2025 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1
- 4.0.4 -> 4.1.0.

* Wed Feb 05 2025 Stanislav Levin <slev@altlinux.org> 4.0.4-alt1.1
- NMU: fixed FTBFS (tox 4).

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
