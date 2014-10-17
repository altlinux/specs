%define oname http-parser

%def_with python3

Name: python-module-%oname
Version: 0.8.3
Release: alt1.git20140925
Summary: http request/response parser
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/http-parser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/benoitc/http-parser.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-pytest
BuildPreReq: python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-pytest
BuildPreReq: python3-module-py
%endif

%py_provides http_parser

%description
HTTP request/response parser for Python compatible with Python 2.x
(>=2.6), Python 3 and Pypy. If possible a C parser based on http-parser
from Ryan Dahl will be used.

%package -n python3-module-%oname
Summary: http request/response parser
Group: Development/Python3
%py3_provides http_parser

%description -n python3-module-%oname
HTTP request/response parser for Python compatible with Python 2.x
(>=2.6), Python 3 and Pypy. If possible a C parser based on http-parser
from Ryan Dahl will be used.

%prep
%setup

rm -f http_parser/parser.c

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
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc NOTICE *.rst *.md THANKS examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc NOTICE *.rst *.md THANKS examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20140925
- Initial build for Sisyphus

