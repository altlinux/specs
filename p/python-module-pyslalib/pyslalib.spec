%define oname pyslalib

%def_with python3

Name: python-module-%oname
Version: 1.0.4
Release: alt1.git20150202
Summary: f2py and numpy wrappers of the fortran version of the astro library SLALIB
License: Free
Group: Development/Python
Url: https://github.com/scottransom/pyslalib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/scottransom/pyslalib.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests gcc-fortran
BuildPreReq: libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests gcc-fortran
BuildPreReq: libnumpy-py3-devel
%endif

%py_provides %oname
%py_requires numpy

%description
This is archive contains new f2py-generated (and hand-tweaked to
eliminate unnecessary function/subroutine arguments) wrappers for the
Fortran version of P.T. Wallace's SLALIB positional astronomy library.
SLALIB used to be hosted by the STARLINK site, although that service
has been suspended.  The version of SLALIB included here is 2.5-4

%package -n python3-module-%oname
Summary: f2py and numpy wrappers of the fortran version of the astro library SLALIB
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy

%description -n python3-module-%oname
This is archive contains new f2py-generated (and hand-tweaked to
eliminate unnecessary function/subroutine arguments) wrappers for the
Fortran version of P.T. Wallace's SLALIB positional astronomy library.
SLALIB used to be hosted by the STARLINK site, although that service
has been suspended.  The version of SLALIB included here is 2.5-4

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags %optflags_shared -fno-strict-aliasing
export FFLAGS="%optflags"
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
export PYTHONPATH=%buildroot%python_sitelibdir
python test/test_slalib.py
#if_with python3
%if 0
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 test/test_slalib.py
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.git20150202
- Initial build for Sisyphus

