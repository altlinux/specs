%def_enable snapshot
%define modname sane
%define pypi_name python_%{modname}
%define oname py%modname

Name: python3-module-%modname
Version: 2.9.1
Release: alt2

Summary: Pyhon3 interface for Sane
Group: Development/Python3
License: MIT-CMU-style
Url: https://github.com/python-pillow/Sane

Vcs: https://github.com/python-pillow/Sane.git

%if_disabled sanpshot
Source: %url/archive/v%version/Sane-%version.tar.gz
%else
Source: %oname-%version.tar
%endif

Requires: python3-module-Pillow python3-module-numpy

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3(wheel) python3(setuptools)
BuildRequires: libsane-devel python3-module-Pillow
BuildRequires: python3-module-numpy

%description
Python3 interface for Sane.

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modname.py
%python3_sitelibdir/_%{modname}*.so
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jun 11 2025 Yuri N. Sedunov <aris@altlinux.org> 2.9.1-alt2
- updated to v2.9.1-39-g89df3d5

* Wed Feb 24 2021 Yuri N. Sedunov <aris@altlinux.org> 2.9.1-alt1
- updated to v2.9.1-3-g4155cda

* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 2.8.3-alt2
- NUM: fix build (drop BR: python3-module-Pillow-devel)

* Thu Apr 09 2020 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt1
- first build for Sisyphus (v2.8.3-46-gab32928)

