%define oname pyclipper

%def_with python3

Name: python-module-%oname
Version: 0.9.2
Release: alt1.b0.git20150320
Summary: Cython wrapper for the C++ translation of the Angus Johnson's Clipper library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyclipper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/greginvm/pyclipper.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ libclipper-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython
%endif

%py_provides %oname

%description
Pyclipper is a Cython wrapper exposing public functions and classes of
the C++ translation of the Angus Johnson's Clipper library.

%if_with python3
%package -n python3-module-%oname
Summary: Cython wrapper for the C++ translation of the Angus Johnson's Clipper library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Pyclipper is a Cython wrapper exposing public functions and classes of
the C++ translation of the Angus Johnson's Clipper library.
%endif

%prep
%setup

rm -f %oname/clipper.*

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing -I%_includedir/polyclipping
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
CFLAGS="-I%_includedir/polyclipping" python setup.py test
%if_with python3
pushd ../python3
CFLAGS="-I%_includedir/polyclipping" python3 setup.py test
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
* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.b0.git20150320
- Initial build for Sisyphus

