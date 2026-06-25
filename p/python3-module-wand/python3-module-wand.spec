%def_disable snapshot

%define modname Wand
%define pypi_name wand
%ifarch %ix86 armh
%def_disable check
%else
%def_enable check
%endif

Name: python3-module-%pypi_name
Version: 0.7.2
Release: alt1

Summary: Ctypes-based simple MagickWand API binding for Python
Group: Development/Python3
License: MIT
Url: https://wand-py.org/

Vcs: https://github.com/emcconville/wand.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/w/%pypi_name/%pypi_name-%version.tar.gz
#Source: https://github.com/emcconville/wand/archive/%version/%modname-%version.tar.gz
%else
Source: %modname-%version.tar
%endif

BuildArch: noarch

Provides: python3(%pypi_name) = %EVR

Requires: ImageMagick-lib >= 7.1

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
BuildRequires: libImageMagick-devel
%{?_enable_check:BuildRequires: /proc python3(pytest)}

%description
Wand is a ctypes-based simple ImageMagick binding for Python, supporting
2.7, 3.3+, and PyPy. All functionalities of MagickWand API are
implemented in Wand.

%prep
%setup %{?_disable_snapshot:-n %pypi_name-%version} %{?_enable_snapshot:-n %modname-%version
%define version_tuple %(%__python3 -c 'print(f"{tuple(map(int, "%version".split(".")))}")')
sed -i -e 's/^\(VERSION_INFO[ \t]*=\).*/\1%version_tuple/' wand/version.py
}

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/
%doc README*

%changelog
* Thu Jun 25 2026 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Wed May 20 2026 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Mon Feb 23 2026 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Tue May 06 2025 Yuri N. Sedunov <aris@altlinux.org> 0.6.13-alt1.1
- fixed build with setuptools 75.8.1

* Wed Aug 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.13-alt1
- first build for Sisyphus




