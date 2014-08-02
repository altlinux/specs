%define oname pyramid_rpc

%def_with python3

Name: python-module-%oname
Version: 0.5.2
Release: alt2
Summary: RPC support for the Pyramid web framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_rpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pyramid

%description
pyramid_rpc is a package of RPC related add-on's to make it easier to
create RPC services.

%package -n python3-module-%oname
Summary: RPC support for the Pyramid web framework
Group: Development/Python3
%py3_requires pyramid
%add_python3_req_skip pyamf

%description -n python3-module-%oname
pyramid_rpc is a package of RPC related add-on's to make it easier to
create RPC services.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_rpc
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
pyramid_rpc is a package of RPC related add-on's to make it easier to
create RPC services.

This package contains tests for pyramid_rpc.

%package tests
Summary: Tests for pyramid_rpc
Group: Development/Python
Requires: %name = %version-%release

%description tests
pyramid_rpc is a package of RPC related add-on's to make it easier to
create RPC services.

This package contains tests for pyramid_rpc.

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
%doc *.txt *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt2
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Version 0.5.2

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Version 0.5.1

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

