%define _unpackaged_files_terminate_build 1
%define pypi_name requests-unixsocket2
%define mod_name requests_unixsocket

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.1
Release: alt1
Summary: Use requests to talk HTTP via a UNIX domain socket
License: ISC
Group: Development/Python3
Url: https://pypi.org/project/requests-unixsocket2
Vcs: https://gitlab.com/thelabnyc/requests-unixsocket2
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# drop in replacement for requests-unixsocket
Provides: python3-module-requests-unixsocket = %EVR
Obsoletes: python3-module-requests-unixsocket <= 0.3.0-alt2
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

# don't package tests
rm %buildroot%python3_sitelibdir/%mod_name/testutils.py
rm -r %buildroot%python3_sitelibdir/%mod_name/tests/

%check
%pyproject_run_pytest -ra -Wignore %mod_name/tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 01 2024 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.4.0 -> 0.4.1.

* Fri May 24 2024 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
