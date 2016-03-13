%define oname cvxmod

%def_with python3

Name: python-module-%oname
Version: 0.4.6
Release: alt4.1.1
Summary: Tool for expressing and solving convex optimization problems
License: GPL v3 or higher
Group: Development/Python
Url: http://cvxmod.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://cvxmod.net/dist/cvxmod-0.4.6.tar.gz
BuildArch: noarch

%setup_python_module %oname
#BuildPreReq: python-devel libatlas-devel liblapack-devel
#BuildPreReq: python-module-cvxopt
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python-tools-2to3
#BuildPreReq: python3-module-cvxopt
%endif

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

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

%package -n python3-module-%oname
Summary: Tool for expressing and solving convex optimization problems
Group: Development/Python3

%description -n python3-module-%oname
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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc LICENSE PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.6-alt4.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt4.1
- NMU: Use buildreq for BR.

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt4
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.6-alt3.1
- Rebuild with Python-2.7

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt3
- Rebuilt with python 2.6

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt2
- Rebuilt with python-module-cvxopt-1.1.1-alt2

* Tue Aug 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1
- Initial build for Sisyphus

