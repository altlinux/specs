%define mname scikits
%define oname %mname.bvp1lg

%def_without python3

Name: python-module-%oname
Version: 0.2.5
Release: alt1
Summary: Boundary value problem (legacy) solvers for ODEs
License: Noncommercial
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.bvp1lg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-fortran liblapack-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-scipy libnumpy-devel
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-scipy libnumpy-py3-devel
BuildPreReq: python3-module-nose
%endif

%py_provides %oname
%py_requires %mname numpy scipy

%description
Python-wrapped legacy solvers for boundary value problems for ODEs.

These are implemented by wrapping the COLNEW and MUS Fortran codes from
netlib.org.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python-wrapped legacy solvers for boundary value problems for ODEs.

These are implemented by wrapping the COLNEW and MUS Fortran codes from
netlib.org.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Boundary value problem (legacy) solvers for ODEs
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy scipy

%description -n python3-module-%oname
Python-wrapped legacy solvers for boundary value problems for ODEs.

These are implemented by wrapping the COLNEW and MUS Fortran codes from
netlib.org.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python-wrapped legacy solvers for boundary value problems for ODEs.

These are implemented by wrapping the COLNEW and MUS Fortran codes from
netlib.org.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%add_optflags %optflags_shared -fno-strict-aliasing
%add_optflags -I%_includedir/openblas

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%add_optflags %optflags_shared -fno-strict-aliasing
%add_optflags -I%_includedir/openblas

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%add_optflags %optflags_shared -fno-strict-aliasing
%add_optflags -I%_includedir/openblas

python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc LICENSE README TODO
%python_sitelibdir/%mname/bvp1lg
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/bvp1lg/tests

%files tests
%python_sitelibdir/%mname/bvp1lg/tests

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README TODO
%python3_sitelibdir/%mname/bvp1lg
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/bvp1lg/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/bvp1lg/tests
%endif

%changelog
* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus

