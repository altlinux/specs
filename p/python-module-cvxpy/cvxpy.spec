%define oname cvxpy

%def_with python3

Name: python-module-%oname
Version: 0.2.4
Release: alt1.git20140710
Summary: Python package for modeling optimization problems
License: GPLv3
Group: Development/Python
Url: https://github.com/cvxgrp/cvxpy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cvxgrp/cvxpy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-cvxopt libnumpy-devel
BuildPreReq: python-module-scipy python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-cvxopt libnumpy-py3-devel
BuildPreReq: python3-module-scipy python-tools-2to3
BuildPreReq: python3-module-setuptools
%endif

%description
CVXPY is a free software package for modeling optimization problems in
Python. It provides a modeling framework that allows users to describe
optimization problems in a natural mathematical form and solve them.

%package tests
Summary: Tests for CVXPY
Group: Development/Python
Requires: %name = %EVR

%description tests
CVXPY is a free software package for modeling optimization problems in
Python. It provides a modeling framework that allows users to describe
optimization problems in a natural mathematical form and solve them.

This package contains tests for CVXPY.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 package for modeling optimization problems
Group: Development/Python3

%description -n python3-module-%oname
CVXPY is a free software package for modeling optimization problems in
Python. It provides a modeling framework that allows users to describe
optimization problems in a natural mathematical form and solve them.

%package -n python3-module-%oname-tests
Summary: Tests for CVXPY
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
CVXPY is a free software package for modeling optimization problems in
Python. It provides a modeling framework that allows users to describe
optimization problems in a natural mathematical form and solve them.

This package contains tests for CVXPY.
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
find %oname -type f -name '*.py' -exec 2to3 -w '{}' +
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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20140710
- Version 0.2.4

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.svn20130211
- Fixed build

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.svn20130211
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1.svn20130211.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.svn20130211
- Version 0.1

* Wed May 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt2.svn20111127
- Added module for Python 3

* Wed Dec 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.svn20111127
- Initial build for Sisyphus

