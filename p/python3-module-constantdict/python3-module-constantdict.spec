%define pypi_name constantdict

Name: python3-module-%pypi_name
Version: 2025.3
Release: alt1

Summary: An immutable dict class
License: MIT
Group: Development/Python3
Url: https://github.com/matthiasdiener/constantdict

# No sdist on PyPI
# Source-url: https://github.com/matthiasdiener/constantdict/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_disabled check
%else
BuildRequires: python3-module-pytest
%endif

%description
constantdict provides an immutable dictionary class (a hashable,
read-only mapping) for Python, similar to frozendict and immutabledict.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 2025.3-alt1
- initial build for Sisyphus

