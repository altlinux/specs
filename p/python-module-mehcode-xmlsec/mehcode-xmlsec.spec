%define mname xmlsec
%define oname mehcode-%mname

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20141212
Summary: Python bindings for the XML Security Library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/xmlsec/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mehcode/python-xmlsec.git
Source: %name-%version.tar

BuildPreReq: libxml2-devel libxmlsec1-devel libxmlsec1-openssl-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-pkgconfig
BuildPreReq: python-module-lxml python-module-setuptools_cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-pkgconfig
BuildPreReq: python3-module-lxml python3-module-setuptools_cython
%endif

%py_provides %oname %mname
Provides: python-module-%mname = 1:%version-%release
Conflicts: python-module-%mname < 1:%version-%release
Conflicts: python-module-%mname > 1:%version-%release
Conflicts: python-module-py%mname
%py_requires lxml

%description
Python bindings for the XML Security Library.

%package -n python3-module-%oname
Summary: Python bindings for the XML Security Library
Group: Development/Python3
%py3_provides %oname %mname
Provides: python3-module-%mname = 1:%version-%release
Conflicts: python3-module-%mname < 1:%version-%release
Conflicts: python3-module-%mname > 1:%version-%release
Conflicts: python3-module-py%mname
%py3_requires lxml

%description -n python3-module-%oname
Python bindings for the XML Security Library.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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
python setup.py test build_ext -i
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test build_ext -i
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141212
- Initial build for Sisyphus

