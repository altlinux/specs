%define pypi_name astropy-iers-data

# bootstrap for astropy
%def_without check

Name:    python3-module-%pypi_name
Version: 0.2025.9.29.0.35.48
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
* Tue Sep 30 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.9.29.0.35.48-alt1
- Automatically updated to 0.2025.9.29.0.35.48.

* Tue Sep 23 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.9.22.0.37.25-alt1
- Automatically updated to 0.2025.9.22.0.37.25.

* Wed Sep 17 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.9.15.0.37.0-alt1
- Automatically updated to 0.2025.9.15.0.37.0.

* Mon Sep 08 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.9.8.0.36.17-alt1
- Automatically updated to 0.2025.9.8.0.36.17.

* Tue Sep 02 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.9.1.0.42.11-alt1
- Automatically updated to 0.2025.9.1.0.42.11.

* Mon Aug 18 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.8.18.0.40.14-alt1
- Automatically updated to 0.2025.8.18.0.40.14.

* Sun Aug 03 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.7.28.0.41.50-alt1
- Automatically updated to 0.2025.7.28.0.41.50.

* Thu Jul 24 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.7.21.0.41.39-alt1
- Automatically updated to 0.2025.7.21.0.41.39.

* Tue Jul 08 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.7.7.0.39.39-alt1
- Automatically updated to 0.2025.7.7.0.39.39.

* Sun Jul 06 2025 Grigory Ustinov <grenka@altlinux.org> 0.2025.6.30.0.39.40-alt1
- Initial build for Sisyphus.
