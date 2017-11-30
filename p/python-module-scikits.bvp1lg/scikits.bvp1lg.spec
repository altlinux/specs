%define mname scikits
%define oname %mname.bvp1lg

%def_without python3

Name: python-module-%oname
Version: 0.2.8
Release: alt1
Summary: Boundary value problem (legacy) solvers for ODEs
License: Noncommercial
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.bvp1lg/

Source: %name-%version.tar
Source1: http://netlib.org/ode/colnew.f
Source2: http://netlib.org/ode/mus1.f
Source3: http://netlib.org/ode/mus2.f
Source4: http://netlib.org/ode/mus3.f
Patch1: %oname-%version-alt-build.patch

BuildRequires: gcc-fortran liblapack-devel
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-scipy libnumpy-devel
BuildRequires: python-module-nose python2.7(matplotlib)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-scipy libnumpy-py3-devel
BuildRequires: python3-module-nose python3(matplotlib)
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
%patch1 -p1

install -p -m644 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 ./
for i in *.f; do
	cp $i lib/$i.orig
done

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
%doc *.rst
%python_sitelibdir/%mname/bvp1lg
%python_sitelibdir/*.egg-info
%python_sitelibdir/*-nspkg.pth
%exclude %python_sitelibdir/%mname/bvp1lg/tests
%exclude %python_sitelibdir/%mname/bvp1lg/examples.py*

%files tests
%python_sitelibdir/%mname/bvp1lg/tests
%python_sitelibdir/%mname/bvp1lg/examples.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/bvp1lg
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%exclude %python3_sitelibdir/%mname/bvp1lg/tests
%exclude %python3_sitelibdir/%mname/bvp1lg/examples.py
%exclude %python3_sitelibdir/%mname/bvp1lg/__pycache__/examples.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/bvp1lg/tests
%python3_sitelibdir/%mname/bvp1lg/examples.py
%python3_sitelibdir/%mname/bvp1lg/__pycache__/examples.*
%endif

%changelog
* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.8-alt1
- Updated to upstream version 0.2.8.

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt1
- Version 0.2.7

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus

