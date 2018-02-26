%define oname cvxpy

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt2.svn20111127
Summary: Python package for modeling optimization problems
License: GPLv3
Group: Development/Python
Url: http://www.stanford.edu/~ttinoco/cvxpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://cvxpy.googlecode.com/svn/trunk/
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-cvxopt libnumpy-devel
BuildPreReq: python-module-scipy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-cvxopt libnumpy-py3-devel
BuildPreReq: python3-module-scipy python-tools-2to3
%endif

%description
CVXPY is a free software package for modeling optimization problems in
Python. It provides a modeling framework that allows users to describe
optimization problems in a natural mathematical form and solve them.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 package for modeling optimization problems
Group: Development/Python3

%description -n python3-module-%oname
CVXPY is a free software package for modeling optimization problems in
Python. It provides a modeling framework that allows users to describe
optimization problems in a natural mathematical form and solve them.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build_debug
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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed May 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt2.svn20111127
- Added module for Python 3

* Wed Dec 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.svn20111127
- Initial build for Sisyphus

