%define oname diffsim
Name: python-module-%oname
Version: 0.5
Release: alt1.bzr20100211.1.1
Summary: A framwork for solving coupled continuous and discrete equations
Group: Development/Python
License: LGPL v3
URL: http://www.fenics.org/
# bzr branch lp:diffsim
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname
BuildArch: noarch

BuildPreReq: python-module-tritetmesh libtritetmesh-devel

%description
DiffSim is a python library that provides a framwork for solving
coupled continuous and discrete equations. Using PyDOLFIN DiffSim
provides builtin functionalities to solve the diffusion equation,
using the finite elemement method.

DiffSim provides a declarative language to describe coupled diffusion
domains together with discrete (in time) variables.

%package demo
Summary: Demos for DiffSim
Group: Development/Python
Requires: %name = %version-%release

%description demo
DiffSim is a python library that provides a framwork for solving
coupled continuous and discrete equations. Using PyDOLFIN DiffSim
provides builtin functionalities to solve the diffusion equation,
using the finite elemement method.

This package contains demos for DiffSim.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc AUTHORS COPYING README TODO
%python_sitelibdir/*

%files demo
%doc demo
%doc test

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.bzr20100211.1.1
- Rebuild with Python-2.7

* Fri Dec 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.bzr20100211.1
- Disabled using python-module-pyMPI

* Fri Jun 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.bzr20100211
- New snapshot

* Sun Dec 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.bzr20090812
- Initial build for Sisyphus

