%define pypi_name mesonpy

%def_with check

Name:    python3-module-%pypi_name
Version: 0.16.0
Release: alt2

Summary: Meson PEP 517 Python build backend
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/meson-python
vCS:     https://github.com/mesonbuild/meson-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-packaging
BuildRequires: python3-module-pyproject-metadata
BuildRequires: meson

%if_with check
BuildRequires: git
BuildRequires: patchelf
BuildRequires: python3-module-Cython
BuildRequires: python3-module-pytest-mock
%endif

BuildArch: noarch

Source: %name-%version.tar
Patch: 225a26d8c854987897448b17478166570c7be777.patch
Patch1: mesonpy-0.16.0-adjust-for-changes-in-pyproject-metadata-0.9.0.patch
# mapping from PyPI name (actual PyPI name is meson-python)
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-meson-python = %EVR

%description
meson-python is a Python build backend built on top of the Meson build system.
It enables to use Meson for the configuration and build steps of Python packages.
Meson is an open source build system meant to be both extremely fast, and, even
more importantly, as user friendly as possible. meson-python is best suited for
building Python packages containing extension modules implemented in languages
such as C, C++, Cython, Fortran, Pythran, or Rust. Consult the documentation
for more details.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject -- -k'not test_pep518 and not test_limited_api'

%files
%doc LICENSE *.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo meson_python}

%changelog
* Wed Oct 23 2024 Stanislav Levin <slev@altlinux.org> 0.16.0-alt2
- Fixed FTBFS (pyproject-metadata 0.9.0).

* Fri Apr 19 2024 Grigory Ustinov <grenka@altlinux.org> 0.16.0-alt1
- Automatically updated to 0.16.0.

* Tue Feb 20 2024 Stanislav Levin <slev@altlinux.org> 0.15.0-alt2.1
- NMU: mapped PyPI name to distro's one.

* Wed Jan 24 2024 Grigory Ustinov <grenka@altlinux.org> 0.15.0-alt2
- Fixed FTBFS.

* Mon Oct 30 2023 Grigory Ustinov <grenka@altlinux.org> 0.15.0-alt1
- Automatically updated to 0.15.0.

* Thu Sep 07 2023 Grigory Ustinov <grenka@altlinux.org> 0.14.0-alt1
- Automatically updated to 0.14.0.

* Fri Jun 30 2023 Grigory Ustinov <grenka@altlinux.org> 0.13.2-alt1
- Automatically updated to 0.13.2.

* Tue Jun 13 2023 Grigory Ustinov <grenka@altlinux.org> 0.13.1-alt1
- Initial build for Sisyphus.
