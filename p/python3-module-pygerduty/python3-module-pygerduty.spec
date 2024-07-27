%define pypi_name pygerduty

%def_with check

Name: python3-module-%pypi_name
Version: 0.38.3
Release: alt1

Summary: Python Client Library for PagerDuty's REST API
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pygerduty
VCS: https://github.com/dropbox/pygerduty

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-httpretty
BuildRequires: python3-module-six
%endif

%description
Python Library for PagerDuty's REST API and Events API. This library was
originally written to support v1 and is currently being updated to be compatible
with v2 of the API. See "Migrating from v1 to v2" for more details.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%_bindir/grab_oncall.py
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jul 23 2024 Anton Vyatkin <toni@altlinux.org> 0.38.3-alt1
- Initial build for Sisyphus.
