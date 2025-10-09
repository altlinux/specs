%define pypi_name pyyaml-ft

%def_without check

Name:    python3-module-%pypi_name
Version: 8.0.0
Release: alt1

Summary: Fork of PyYAML with support for free-threading
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/PyYAML-ft
VCS:     https://github.com/Quansight-Labs/pyyaml-ft

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython
BuildRequires: libyaml-devel

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/_yaml_ft
%python3_sitelibdir/yaml_ft
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 28 2025 Grigory Ustinov <grenka@altlinux.org> 8.0.0-alt1
- Initial build for Sisyphus.
