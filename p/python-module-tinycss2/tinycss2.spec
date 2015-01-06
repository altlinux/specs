%define oname tinycss2

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.git20140819
Summary: Modern CSS parser for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tinycss2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/SimonSapin/tinycss2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-webencodings
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-webencodings
%endif

%py_provides %oname
%py_requires webencodings

%description
tinycss2 is a rewrite of tinycss with a simpler API, based on the more
recent CSS Syntax Level 3 specification.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
tinycss2 is a rewrite of tinycss with a simpler API, based on the more
recent CSS Syntax Level 3 specification.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Modern CSS parser for Python
Group: Development/Python3
%py3_provides %oname
%py3_requires webencodings

%description -n python3-module-%oname
tinycss2 is a rewrite of tinycss with a simpler API, based on the more
recent CSS Syntax Level 3 specification.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
tinycss2 is a rewrite of tinycss with a simpler API, based on the more
recent CSS Syntax Level 3 specification.

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGES TODO *.rst docs/*.rst css_diagram_role.py
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES TODO *.rst docs/*.rst css_diagram_role.py
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20140819
- Initial build for Sisyphus

