%define pypi_name astropy-iers-data

# bootstrap for astropy
%def_without check

Name:    python3-module-%pypi_name
Version: 0.2025.6.30.0.39.40
Release: alt1

Summary: IERS Earth Rotation and Leap Second tables for the astropy core package
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/astropy-iers-data
VCS:     https://github.com/astropy/astropy-iers-data

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

BuildArch: noarch

Source: %name-%version.tar

%description
Note: This package is not currently meant to be used directly by users,
and only meant to be used from the core astropy package.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/astropy_iers_data
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Jul 06 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.6.30.0.39.40-alt1
- Initial build for Sisyphus.
