%define pypi_name pyasynchat

Name: python3-module-%pypi_name
Version: 1.0.2
Release: alt1

Summary: Make asynchat available for Python 3.12 onwards

License: Python-2.0.1
Group: Development/Python3
Url: https://pypi.org/project/pyasynchat

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
This package contains the asynchat module as found in Python versions
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

%files
%doc LICENSE *.md
%python3_sitelibdir/asynchat
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
