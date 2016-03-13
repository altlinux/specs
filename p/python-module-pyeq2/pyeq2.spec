%define oname pyeq2

%def_with python3

Name: python-module-%oname
Version: r243
Release: alt1.svn20150119.1.1
Summary: A collection of Python equations
License: BSD
Group: Development/Python
Url: http://code.google.com/p/pyeq2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://pyeq2.googlecode.com/svn/trunk/
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python-tools-2to3
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-logging python3 python3-base
BuildRequires: python-modules-compiler python-modules-encodings python-tools-2to3 rpm-build-python3 time

%description
The fitting code for zunzun.com as a collection of Python equations that
can fit themselves to both 2D and 3D data sets (curve fitting and
surface fitting), output source code in several computing languages, and
run a genetic algorithm for initial parameter estimation. Includes
splines and user defined functions. Also fits data to over 80
statistical distributions. Passes all NIST tests for nonlinear fitting
(see the unit test directory). No compiler required.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The fitting code for zunzun.com as a collection of Python equations that
can fit themselves to both 2D and 3D data sets (curve fitting and
surface fitting), output source code in several computing languages, and
run a genetic algorithm for initial parameter estimation. Includes
splines and user defined functions. Also fits data to over 80
statistical distributions. Passes all NIST tests for nonlinear fitting
(see the unit test directory). No compiler required.

This package contains tests for %oname.

%package examples
Summary: Examples for %oname
Group: Development/Documentation
Requires: %name = %EVR

%description examples
The fitting code for zunzun.com as a collection of Python equations that
can fit themselves to both 2D and 3D data sets (curve fitting and
surface fitting), output source code in several computing languages, and
run a genetic algorithm for initial parameter estimation. Includes
splines and user defined functions. Also fits data to over 80
statistical distributions. Passes all NIST tests for nonlinear fitting
(see the unit test directory). No compiler required.

This package contains examples for %oname.

%package -n python3-module-%oname
Summary: A collection of Python equations
Group: Development/Python3

%description -n python3-module-%oname
The fitting code for zunzun.com as a collection of Python equations that
can fit themselves to both 2D and 3D data sets (curve fitting and
surface fitting), output source code in several computing languages, and
run a genetic algorithm for initial parameter estimation. Includes
splines and user defined functions. Also fits data to over 80
statistical distributions. Passes all NIST tests for nonlinear fitting
(see the unit test directory). No compiler required.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The fitting code for zunzun.com as a collection of Python equations that
can fit themselves to both 2D and 3D data sets (curve fitting and
surface fitting), output source code in several computing languages, and
run a genetic algorithm for initial parameter estimation. Includes
splines and user defined functions. Also fits data to over 80
statistical distributions. Passes all NIST tests for nonlinear fitting
(see the unit test directory). No compiler required.

This package contains tests for %oname.

%package -n python3-module-%oname-examples
Summary: Examples for %oname
Group: Development/Documentation
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-examples
The fitting code for zunzun.com as a collection of Python equations that
can fit themselves to both 2D and 3D data sets (curve fitting and
surface fitting), output source code in several computing languages, and
run a genetic algorithm for initial parameter estimation. Includes
splines and user defined functions. Also fits data to over 80
statistical distributions. Passes all NIST tests for nonlinear fitting
(see the unit test directory). No compiler required.

This package contains examples for %oname.

%prep
%setup

for i in $(find ./ -type d); do
	touch $i/__init__.py
done

%install
install -d %buildroot%python_sitelibdir/%oname
cp -fR * %buildroot%python_sitelibdir/%oname/

%if_with python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
install -d %buildroot%python3_sitelibdir/%oname
cp -fR * %buildroot%python3_sitelibdir/%oname/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*.txt
%exclude %python_sitelibdir/*/Examples
%exclude %python_sitelibdir/*/UnitTests

%files examples
%python_sitelibdir/*/Examples

%files tests
%python_sitelibdir/*/UnitTests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*.txt
%exclude %python3_sitelibdir/*/Examples
%exclude %python3_sitelibdir/*/UnitTests

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/Examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/UnitTests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> r243-alt1.svn20150119.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> r243-alt1.svn20150119.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r243-alt1.svn20150119
- New snapshot

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r187-alt1.svn20140706
- Initial build for Sisyphus

