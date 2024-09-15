%define modname ManimPango
%define pypi_name manimpango

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1

Summary: Python bindings to Pango library
Group: Development/Python3
License: GPL-3.0
Url: https://pypi.python.org/pypi/%modname

Vcs: https://github.com/ManimCommunity/ManimPango/

Source: https://pypi.io/packages/source/m/%pypi_name/%pypi_name-%version.tar.gz

%define pango_ver 1.54
BuildRequires(pre): rpm-build-python3
BuildRequires: pkgconfig(pango) >= %pango_ver
BuildRequires: python3(cython) python3(wheel) python3(setuptools)

%description
Python3 bindings for Pango for using with Manim.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%modname-%version.dist-info
%doc README*


%changelog
* Sun Sep 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Sat Oct 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Wed Oct 11 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- first build for Sisyphus


