%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-httpbin

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.2
Release: alt2

Summary: Easily test your HTTP library against a local copy of httpbin
License: MIT
Group: Development/Python3
# Source-git: https://github.com/kevin1024/pytest-httpbin.git
Url: https://pypi.org/project/pytest-httpbin

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# runtime dependencies
BuildRequires: python3(httpbin)
BuildRequires: python3(six)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %pypi_name
Provides: python3-module-pytest_httpbin = %EVR

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

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/pytest_httpbin/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Sep 26 2022 Danil Shein <dshein@altlinux.org> 1.0.2-alt2
 - NMU: fix FTBFS due to Flask library version update

* Tue Jul 26 2022 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
