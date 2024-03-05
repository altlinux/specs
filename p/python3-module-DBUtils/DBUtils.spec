%define _unpackaged_files_terminate_build 1
%define pypi_name DBUtils
%def_with check

Name: python3-module-%pypi_name
Version: 3.0.3
Release: alt1

Summary: Database connections for multi-threaded environments
License: MIT
Group: Development/Python3
Url: https://github.com/WebwareForPython/DBUtils
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
Requires: python3-module-PyGreSQL
# mapping of PyPI name to distro name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
DBUtils is a suite of tools providing solid, persistent and
pooled connections to a database that can be used in all kinds
of multi-threaded environments.

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
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/dbutils/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Sat Feb 24 2024 Ajrat Makhmutov <rauty@altlinux.org> 3.0.3-alt1
- First build for ALT.
