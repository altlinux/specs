%define pypi_name pocketlint

%def_enable check

Name: python3-module-%pypi_name
Version: 0.25
Release: alt1

Summary: Addon for Pylint
Group: Development/Python3
License: GPLv2+
Url: https://pypi.org/project/%pypi_name

Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pylint) python3(packaging)}

%description
Addon pylint modules and configuration settings for checking the validity
of Python-based source projects.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
python3 -v tests/pylint/runpylint.py

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README


%changelog
* Mon Oct 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25-alt1
- 0.25
- ported to %%pyproject* macros

* Thu Jul 14 2022 Yuri N. Sedunov <aris@altlinux.org> 0.24-alt1
- 0.24

* Fri Jul 01 2022 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt1
- 0.23

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22

* Tue Apr 20 2021 Yuri N. Sedunov <aris@altlinux.org> 0.21-alt1
- 0.21

* Sun Sep 01 2019 Yuri N. Sedunov <aris@altlinux.org> 0.20-alt1
- 0.20

* Thu May 02 2019 Yuri N. Sedunov <aris@altlinux.org> 0.19-alt1
- first build for Sisyphus

