%define modname pplpy

Name: python3-module-%modname
Version: 0.8.7
Release: alt1

Summary: Python interface to PPL
Group: Development/Python3
License: GPL-3.0+
Url: https://pypi.org/project/%modname
# https://gitlab.com/videlec/pplpy

Source: https://pypi.io/packages/source/a/%modname/%modname-%version.tar.gz

BuildRequires: rpm-build-python3
BuildRequires: python3-module-Cython python3-module-cysignals python3-module-gmpy2
BuildRequires: gcc-c++ libgmp-devel libgmpxx-devel ppl-devel libmpfr-devel libmpc-devel

%description
A Python interface to the C++ Parma Polyhedra Library (PPL),
which allows computations with polyhedra and grids, like mixed
integer linear programming.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files -n python3-module-%modname
%doc README.rst LICENSE.txt CHANGES.txt
%python3_sitelibdir/ppl/
%python3_sitelibdir/pplpy-%{version}*.egg-info/

%changelog
* Mon Dec 06 2021 Leontiy Volodin <lvol@altlinux.org> 0.8.7-alt1
- Initial build for ALT Sisyphus.
- Built as require for sagemath.

