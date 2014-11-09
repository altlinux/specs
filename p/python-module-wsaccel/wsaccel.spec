%define oname wsaccel

%def_with python3

Name: python-module-%oname
Version: 0.6.2
Release: alt1.git20131112
Summary: Accelerator for ws4py and AutobahnPython
License: Apache
Group: Development/Python
Url: https://pypi.python.org/pypi/wsaccel/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/methane/wsaccel.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython
%endif

%py_provides %oname

%description
WSAccell is WebSocket accelerator for AutobahnPython, ws4py and Tornado.

%package -n python3-module-%oname
Summary: Accelerator for ws4py and AutobahnPython
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
WSAccell is WebSocket accelerator for AutobahnPython, ws4py and Tornado.

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
python setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20131112
- Initial build for Sisyphus

