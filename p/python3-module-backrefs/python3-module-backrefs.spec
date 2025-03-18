%define pypi_name backrefs

%def_with check

Name:    python3-module-%pypi_name
Version: 5.8
Release: alt1

Summary: Wrapper around re or regex that adds additional back references
License: MIT
Group:   Development/Python3
URL:     https://github.com/facelessuser/backrefs

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-regex
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Backrefs is a wrapper around Python's built-in Re and the 3rd party Regex
library. Backrefs adds various additional back references (and a couple other
features) that are known to some regular expression engines, but not to Python's
Re and/or Regex. The supported back references actually vary depending on the
regular expression engine being used as the engine may already have support
for some.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Mar 14 2025 Alexander Burmatov <thatman@altlinux.org> 5.8-alt1
- Initial build for Sisyphus.
