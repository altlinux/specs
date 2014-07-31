%define oname pyramid_beaker

%def_with python3

Name: python-module-%oname
Version: 0.8
Release: alt2
Summary: Beaker session factory backend for Pyramid
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_beaker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pyramid beaker

%description
Provides a session factory for the Pyramid web framework backed by the
Beaker sessioning system.

%package -n python3-module-%oname
Summary: Beaker session factory backend for Pyramid
Group: Development/Python3
%py3_requires pyramid beaker

%description -n python3-module-%oname
Provides a session factory for the Pyramid web framework backed by the
Beaker sessioning system.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_beaker
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Provides a session factory for the Pyramid web framework backed by the
Beaker sessioning system.

This package contains tests for pyramid_beaker.

%package tests
Summary: Tests for pyramid_beaker
Group: Development/Python
Requires: %name = %version-%release

%description tests
Provides a session factory for the Pyramid web framework backed by the
Beaker sessioning system.

This package contains tests for pyramid_beaker.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt2
- Added module for Python 3

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Version 0.8

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Version 0.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

