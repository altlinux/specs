%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-remotedata

%def_with check
Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1
License: MIT
Source: %pypi_name-%version.tar
# those tests require internet access
Patch0: %pypi_name-alt-disable-broken-tests.patch
# https://github.com/astropy/pytest-remotedata/pull/69
Patch1: %pypi_name-replace-deprecated-code.patch
Group: Development/Python3
BuildArch: noarch
Summary: Pytest plugin to control whether tests are run that have remote data
Url: https://pypi.org/project/%pypi_name/

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
This package provides a plugin for the pytest framework that allows developers
to control unit tests that require access to data from the internet. It was
originally part of the astropy core package, but has been moved to a separate
package in order to be of more general use.

%prep
%setup -n %pypi_name-%version
%patch0 -p2
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/pytest_remotedata/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Aug 05 2023 L.A. Kostis <lakostis@altlinux.ru> 0.4.0-alt1
- Disable tests which require internet access (see upstream issue #41).
- Initial build for ALTLinux.
