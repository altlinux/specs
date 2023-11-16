%define pypi_name pytest-json-report
%define mod_name pytest_jsonreport

%def_with check

Name:    python3-module-%pypi_name
Version: 1.5.0
Release: alt1

Summary: Pytest plugin to report test results as JSON
License: MIT
Group:   Development/Python3
URL:     https://github.com/numirias/pytest-json-report

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-flaky
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-metadata
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch1: upgrade-to-pytest-metadata-3.patch

%description
This pytest plugin creates test reports as JSON. This makes it easy to process
test results in other applications.

%prep
%setup -n %pypi_name-%version
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 15 2023 Alexander Burmatov <thatman@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.
