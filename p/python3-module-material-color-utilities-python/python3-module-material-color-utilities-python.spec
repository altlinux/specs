%define modname material-color-utilities-python
%define pypi_name material_color_utilities_python

%def_disable check

Name: python3-module-%modname
Version: 0.1.5
Release: alt1

Summary: Python port of material-color-utilities
Group: Development/Python3
License: Apache-2.0
Url: https://github.com/avanishsubbiah/material-color-utilities-python

Source: https://pypi.io/packages/source/m/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel python3-module-poetry-core

%description
Python port of material-color-utilities used for Material You colors.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- first build for Sisyphus




