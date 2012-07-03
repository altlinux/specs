%define oname cvxmod
Name: python-module-%oname
Version: 0.4.6
Release: alt3.1
Summary: Tool for expressing and solving convex optimization problems
License: GPL v3 or higher
Group: Development/Python
Url: http://cvxmod.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://cvxmod.net/dist/cvxmod-0.4.6.tar.gz
BuildArch: noarch

%setup_python_module %oname
BuildPreReq: python-devel libatlas-devel liblapack-devel
BuildPreReq: python-module-cvxopt

%description
CVXMOD is a Python-based tool for expressing and solving convex
optimization problems. It uses CVXOPT as its solver. It is developed by
Jacob Mattingley, as PhD work under Stephen Boyd at Stanford University.

CVXMOD is primarily a modeling layer for CVXOPT. While it is possible to
use CVXOPT directly, CVXMOD makes it faster and easier to build and
solve problems. Advanced users who want to see or manipulate how their
problems are being solved should consider using CVXOPT directly.
Additional features are being added to CVXMOD beyond just modeling.
These are currently experimental.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc LICENSE PKG-INFO
%python_sitelibdir/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.6-alt3.1
- Rebuild with Python-2.7

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt3
- Rebuilt with python 2.6

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt2
- Rebuilt with python-module-cvxopt-1.1.1-alt2

* Tue Aug 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1
- Initial build for Sisyphus

