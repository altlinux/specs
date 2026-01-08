%define modname fortune-python
%define pypi_name fortune_python

%def_disable check

Name: python3-module-%modname
Version: 1.1.2
Release: alt1

Summary: A Fortune clone in Python
Group: Development/Python3
License: Apache-2.0
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://codeberg.org/jamesansley/fortune.git

Source: https://pypi.io/packages/source/f/%pypi_name/%pypi_name-%version.tar.gz
Patch1: %pypi_name-1.1.2-alt-file-list.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)

%description
A simple self-contained clone of fortune.

%prep
%setup -n %pypi_name-%version
%patch1

%build
%pyproject_build

%install
%pyproject_install

%files
# conflicts with fortune
#%_bindir/fortune
%python3_sitelibdir_noarch/fortune
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Tue Dec 23 2025 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- first build for Sisyphus


