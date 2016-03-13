%define oname bunch

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt2.git20120312.1
Summary: A dot-accessible dictionary (a la JavaScript objects)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bunch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dsc/bunch.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Bunch is a dictionary that supports attribute-style access, a la
JavaScript.

%package test
Summary: Test for %oname
Group: Development/Python
Requires: %name = %EVR

%description test
Bunch is a dictionary that supports attribute-style access, a la
JavaScript.

This package contains test for %oname.

%package -n python3-module-%oname
Summary: A dot-accessible dictionary (a la JavaScript objects)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Bunch is a dictionary that supports attribute-style access, a la
JavaScript.

%package -n python3-module-%oname-test
Summary: Test for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-test
Bunch is a dictionary that supports attribute-style access, a la
JavaScript.

This package contains test for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
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
%doc README*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.py*

%files test
%python_sitelibdir/*/test.py*

%if_with python3
%files -n python3-module-%oname
%doc README*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.py
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-test
%python3_sitelibdir/*/test.py
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt2.git20120312.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.git20120312
- Added provides for Python 3 module

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20120312
- Initial build for Sisyphus

