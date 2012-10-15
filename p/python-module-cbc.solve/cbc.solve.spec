%define pyname cbc
%define oname %pyname.solve
Name: python-module-%oname
Version: 0.1.0
Release: alt1.bzr20120913
Summary: Collection of FEniCS/DOLFIN-based solvers
Group: Development/Python
License: GPL v3
URL: http://www.fenics.org/
# bzr branch lp:cbc.solve
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname
BuildPreReq: libdolfin-real-devel
BuildArch: noarch

%description
CBC.Solve is a collection of FEniCS/DOLFIN-based solvers developed
primarily at the Center for Biomedical Computing hosted by Simula
Research Laboratory in Oslo (http://www.simula.no).

The current collection consists of the following three solvers:

  CBC.Beat  - solving the bidomain equations
  CBC.Flow  - solving the Navier-Stokes equations
  CBC.Twist - solving general hyperelastic models

%package demo
Summary: Demos for CBC.Solve
Group: Development/Python
Requires: %name = %version-%release

%description demo
CBC.Solve is a collection of FEniCS/DOLFIN-based solvers developed
primarily at the Center for Biomedical Computing hosted by Simula
Research Laboratory in Oslo (http://www.simula.no).

This package contains demos for CBC.Solve

%package tests
Summary: Tests for CBC.Solve
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-demo = %version-%release

%description tests
CBC.Solve is a collection of FEniCS/DOLFIN-based solvers developed
primarily at the Center for Biomedical Computing hosted by Simula
Research Laboratory in Oslo (http://www.simula.no).

This package contains tests for CBC.Solve

%prep
%setup

%build
%python_build

%install
%python_install

rm -f test/swing/fsinewton/convergence_tests/test_analytic_light.py*
cp -fR demo test %buildroot%python_sitelibdir/%pyname/
for i in $(find %buildroot%python_sitelibdir/%pyname -type d)
do
	touch $i/__init__.py
done

%files
%doc AUTHORS COPYING README TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/%pyname/demo
%exclude %python_sitelibdir/%pyname/test

%files demo
%python_sitelibdir/%pyname/demo

%files tests
%python_sitelibdir/%pyname/test

%changelog
* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.bzr20120913
- New snapshot

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.bzr20120814
- New snapshot

* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.bzr20120505
- New snapshot

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.bzr20111127
- New snapshot

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt1.bzr20110328.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.bzr20110328
- New snapshot

* Fri Dec 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.bzr20101126
- New snapshot

* Sat Dec 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.bzr20091201
- Initial build for Sisyphus

