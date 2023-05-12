%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-httpbin

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1
Summary: Easily test your HTTP library against a local copy of httpbin
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-httpbin
Vcs: https://github.com/kevin1024/pytest-httpbin
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
httpbin is an amazing web service for testing HTTP libraries. It has several
great endpoints that can test pretty much everything you need in a HTTP library.
The only problem is: maybe you don't want to wait for your tests to travel
across the Internet and back to make assertions against a remote web service.

Enter pytest-httpbin. Pytest-httpbin creates a pytest "fixture" that is
dependency-injected into your tests. It automatically starts up a HTTP server in
a separate thread running httpbin and provides your test with the URL in the
fixture.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.md
%python3_sitelibdir/pytest_httpbin/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu May 11 2023 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.0.2 -> 2.0.0.

* Mon Sep 26 2022 Danil Shein <dshein@altlinux.org> 1.0.2-alt2
 - NMU: fix FTBFS due to Flask library version update

* Tue Jul 26 2022 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
