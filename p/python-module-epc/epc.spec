%define oname epc

%def_with python3

Name: python-module-%oname
Version: 0.0.5
Release: alt1.git20140308
Summary: EPC (RPC stack for Emacs Lisp) implementation in Python
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/epc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tkf/python-epc.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sexpdata python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-sexpdata python3-module-nose
%endif

%py_provides %oname

%description
EPC is an RPC stack for Emacs Lisp and Python-EPC is its server side and
client side implementation in Python. Using Python-EPC, you can easily
call Emacs Lisp functions from Python and Python functions from Emacs.
For example, you can use Python GUI module to build widgets for Emacs
(see examples/gtk/server.py for example).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
EPC is an RPC stack for Emacs Lisp and Python-EPC is its server side and
client side implementation in Python. Using Python-EPC, you can easily
call Emacs Lisp functions from Python and Python functions from Emacs.
For example, you can use Python GUI module to build widgets for Emacs
(see examples/gtk/server.py for example).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: EPC (RPC stack for Emacs Lisp) implementation in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
EPC is an RPC stack for Emacs Lisp and Python-EPC is its server side and
client side implementation in Python. Using Python-EPC, you can easily
call Emacs Lisp functions from Python and Python functions from Emacs.
For example, you can use Python GUI module to build widgets for Emacs
(see examples/gtk/server.py for example).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
EPC is an RPC stack for Emacs Lisp and Python-EPC is its server side and
client side implementation in Python. Using Python-EPC, you can easily
call Emacs Lisp functions from Python and Python functions from Emacs.
For example, you can use Python GUI module to build widgets for Emacs
(see examples/gtk/server.py for example).

This package contains tests for %oname.

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

%check
rm -fR build
py.test
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc *.rst doc/source/*.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/source/*.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20140308
- Initial build for Sisyphus

