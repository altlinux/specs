%define oname intervals

%def_with python3

Name: python-module-%oname
Version: 0.3.2
Release: alt1.git20141209
Summary: Python tools for handling intervals (ranges of comparable objects)
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/intervals/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/intervals.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-infinity python-module-six
BuildPreReq: python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-infinity python3-module-six
BuildPreReq: python3-module-Pygments
%endif

%py_provides %oname

%description
Python tools for handling intervals (ranges of comparable objects).

%package -n python3-module-%oname
Summary: Python tools for handling intervals (ranges of comparable objects)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python tools for handling intervals (ranges of comparable objects).

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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
#py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141209
- New snapshot

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141021
- Initial build for Sisyphus

