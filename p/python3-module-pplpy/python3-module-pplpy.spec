%define modname pplpy

%def_enable pyproject

Name: python3-module-%modname
Version: 0.9.0
Release: alt1

Summary: Python interface to PPL

License: GPL-3.0+
Group: Development/Python3
Url: https://pypi.org/project/pplpy
VCS: https://github.com/sagemath/pplpy

# Source-url: https://pypi.io/packages/source/a/%modname/%modname-%version.tar.gz
Source: %modname-%version.tar

BuildRequires: meson rpm-build-python3 python3-module-wheel python3-module-mesonpy
BuildRequires: python3-module-Cython python3-module-cysignals python3-module-gmpy2
BuildRequires: gcc-c++ libgmp-devel libgmpxx-devel ppl-devel libmpfr-devel libmpc-devel

%description
A Python interface to the C++ Parma Polyhedra Library (PPL),
which allows computations with polyhedra and grids, like mixed
integer linear programming.

%prep
%setup -n %modname-%version

%build
%if_enabled pyproject
%pyproject_build
%else
%meson
%meson_build
%endif

%install
%if_enabled pyproject
%pyproject_install
%else
%meson_install
%endif

%files -n python3-module-%modname
%doc README.rst LICENSE.txt CHANGES.txt
%python3_sitelibdir/ppl/
%if_enabled pyproject
%python3_sitelibdir/pplpy-%{version}*/
%endif

%changelog
* Wed Mar 25 2026 Leontiy Volodin <lvol@altlinux.org> 0.9.0-alt1
- New version 0.9.0.

* Sat Dec 28 2024 Leontiy Volodin <lvol@altlinux.org> 0.8.10-alt1
- New version 0.8.10.
- Added vcs tag.

* Wed Sep 06 2023 Leontiy Volodin <lvol@altlinux.org> 0.8.8-alt1
- New version 0.8.8.
- NMU:
  + Switch to pyproject macros.
  + Cleanup spec.

* Mon Dec 06 2021 Leontiy Volodin <lvol@altlinux.org> 0.8.7-alt1
- Initial build for ALT Sisyphus.
- Built as require for sagemath.

