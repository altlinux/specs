%define _unpackaged_files_terminate_build 1
%define pypi_name PyGreSQL
%def_with check

Name: python3-module-%pypi_name
Version: 6.0.1
Release: alt1

Summary: PyGreSQL is a Python module that interfaces to a PostgreSQL database
License: PostgreSQL
Group: Development/Python3
Url: https://pygresql.org/
Vcs: https://github.com/PyGreSQL/PyGreSQL

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
# mapping of PyPI name to distro name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libpq5-devel
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
BuildRequires: postgresql16-server
%endif

%description
It wraps the lower level C API library libpq to
allow easy use of the powerful PostgreSQL features from Python.

%prep
%setup
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
# creating test postgresql database
mkdir -pv db
pushd db
initdb -D .
pg_ctl -D . -l logfile start
createdb test
psql -l
popd

# Don't append current directory to sys.path to
# avoid 'ModuleNotFoundError' error, because
# the package has modules which need compiling.
%pyproject_run -- pytest -vra ./tests --import-mode=append

%files
%python3_sitelibdir/pg
%python3_sitelibdir/pgdb
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Thu May 16 2024 Ajrat Makhmutov <rauty@altlinux.org> 6.0.1-alt1
- New version.

* Sat Feb 24 2024 Ajrat Makhmutov <rauty@altlinux.org> 6.0-alt1
- First build for ALT.
