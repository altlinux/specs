%define pypi_name colour
%def_enable check

Name: python3-module-%pypi_name
Version: 0.1.5
Release: alt4.1

Summary: Python module to convert and manipulate various color representations
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/vaab/colour
Source: https://pypi.io/packages/source/c/%pypi_name/%pypi_name-%version.tar.gz
Patch: %name-0.1.5-alt-setup.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-coverage}

%description
This Python module defines several color formats that can be converted to
one or another.

%prep
%setup -n %pypi_name-%version
%patch -b .orig
rm -r %pypi_name.egg-info

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --doctest-modules

%files
%python3_sitelibdir_noarch/%pypi_name.py
%python3_sitelibdir_noarch/__pycache__/%{pypi_name}*
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README.rst LICENSE CHANGELOG.rst

%changelog
* Thu May 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt4.1
- removed python3-module-nose from BR (ALT #46062)

* Thu Jul 21 2022 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt4
- ported to %%pyproject* macros, fixed BR

* Tue Jan 25 2022 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt3
- ported from deprecated d2to1 to setuptools
- enabled %%check

* Sat Jul 24 2021 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt2
- python3-only build

* Tue Jan 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- first build for Sisyphus


