%define pypi_name bluepy
# TODO
%def_with bundled_lib

%def_without check

Name:    python3-module-%pypi_name
Version: 1.3.0
Release: alt1.git7ad5652

Summary: Python interface to Bluetooth LE on Linux
License: GPL-2.0
Group:   Development/Python3
URL:     https://github.com/IanHarvey/bluepy

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: glib2-devel
%if_without bundled_lib
BuildRequires: libbluez-devel
%endif

Source: %pypi_name-%version.tar
Patch0: %pypi_name-alt-fix-provides.patch
Patch1: %pypi_name-alt-system-bluez.patch

%description
This is a project to provide an API to allow access to Bluetooth Low Energy
devices from Python.

%prep
%setup -n %pypi_name-%version
%patch0 -p1
%if_without bundled_lib
%patch1 -p1
%endif

%build
%pyproject_build

%install
%pyproject_install
%ifnarch armh %ix86
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%check
%tox_check_pyproject

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Dec 07 2023 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1.git7ad5652
- Initial build for Sisyphus.
