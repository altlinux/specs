%define pypi_name mongomock

%def_with check

Name:    python3-module-%pypi_name
Version: 4.3.0
Release: alt1

Summary: Small library for mocking pymongo collection objects for testing purposes
License: ISC
Group:   Development/Python3
URL:     https://github.com/mongomock/mongomock

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-sentinels
BuildRequires: python3-module-pytz
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Mongomock is a small library to help testing Python code that interacts with
MongoDB via Pymongo.

%prep
%setup -n %pypi_name-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 28 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.0-alt1
- Initial build for Sisyphus.
