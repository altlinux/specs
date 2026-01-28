%def_with check

%define pypi_name pyasyncore

Name: python3-module-%pypi_name
Version: 1.0.5
Release: alt1

Summary: Make asyncore available for Python 3.12 onwards

License: Python-2.0.1
Group: Development/Python3
Url: https://pypi.org/project/pyasyncore

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-test
%endif

%description
This package contains the asyncore module as found in Python versions
prior to 3.12. It is provided so that existing code relying on import
asyncore is able to continue being used without significant
refactoring.

%prep
%setup
# these should not be executable
chmod ugo-x README.md LICENSE

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/asyncore
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jan 28 2026 Grigory Ustinov <grenka@altlinux.org> 1.0.5-alt1
- Build new version.

* Tue Apr 16 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.4-alt1
- Build new version.

* Tue Nov 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
