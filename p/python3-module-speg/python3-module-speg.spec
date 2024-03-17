%define pypi_name speg
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 0.3
Release: alt1

Summary: A PEG-based parser interpreter with memoization (in time)

Url: https://pypi.org/project/speg
License: MIT
Group: Development/Python3

#Source-url: %__pypi_url %pypi_name
# Source-url: https://github.com/avakar/speg/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
A PEG-based parser interpreter with memoization.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Mar 17 2024 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- new version (0.3) with rpmgs script

* Sun Mar 17 2024 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- initial build for ALT Sisyphus

