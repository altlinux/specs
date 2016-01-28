%define oname ephem

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 3.7.6.0
Release: alt1.git20141124.1
Summary: Compute positions of the planets and stars
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ephem/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/brandon-rhodes/pyephem.git
Source: %name-%version.tar

#BuildPreReq: python-modules-json
#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python3-devel rpm-build-python3 python3-module-pytest

%description
PyEphem provides an ephem Python package for performing high-precision
astronomy computations. The underlying numeric routines are coded in C
and are the same ones that drive the popular XEphem astronomy
application, whose author, Elwood Charles Downey, generously gave
permission for their use in PyEphem. The name ephem is short for the
word ephemeris, which is the traditional term for a table giving the
position of a planet, asteroid, or comet for a series of dates.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
PyEphem provides an ephem Python package for performing high-precision
astronomy computations. The underlying numeric routines are coded in C
and are the same ones that drive the popular XEphem astronomy
application, whose author, Elwood Charles Downey, generously gave
permission for their use in PyEphem. The name ephem is short for the
word ephemeris, which is the traditional term for a table giving the
position of a planet, asteroid, or comet for a series of dates.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Compute positions of the planets and stars
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
PyEphem provides an ephem Python package for performing high-precision
astronomy computations. The underlying numeric routines are coded in C
and are the same ones that drive the popular XEphem astronomy
application, whose author, Elwood Charles Downey, generously gave
permission for their use in PyEphem. The name ephem is short for the
word ephemeris, which is the traditional term for a table giving the
position of a planet, asteroid, or comet for a series of dates.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
PyEphem provides an ephem Python package for performing high-precision
astronomy computations. The underlying numeric routines are coded in C
and are the same ones that drive the popular XEphem astronomy
application, whose author, Elwood Charles Downey, generously gave
permission for their use in PyEphem. The name ephem is short for the
word ephemeris, which is the traditional term for a table giving the
position of a planet, asteroid, or comet for a series of dates.

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
python setup.py build_ext -i
py.test
%if_with python3
pushd ../python3
rm -fR build
python setup.py build_ext -i
py.test-%_python3_version
popd
%endif

%files
%doc *.rst TODO issues
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst TODO issues
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.7.6.0-alt1.git20141124.1
- NMU: Use buildreq for BR.

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.6.0-alt1.git20141124
- Initial build for Sisyphus

