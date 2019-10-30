%define oname pyeq2

Name: python3-module-%oname
Version: r243
Release: alt2

Summary: A collection of Python equations
License: BSD
Group: Development/Python3
Url: http://code.google.com/p/pyeq2/
# http://pyeq2.googlecode.com/svn/trunk/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python-tools-2to3


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
Group: Development/Python3
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

%prep
%setup

for i in $(find ./ -type d); do
	touch $i/__init__.py
done

%install
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
install -d %buildroot%python3_sitelibdir/%oname
cp -fR * %buildroot%python3_sitelibdir/%oname/

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*.txt
%exclude %python3_sitelibdir/*/Examples
%exclude %python3_sitelibdir/*/UnitTests

%files examples
%python3_sitelibdir/*/Examples

%files tests
%python3_sitelibdir/*/UnitTests


%changelog
* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> r243-alt2
- disable python2, enable python3

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> r243-alt1.svn20150119.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> r243-alt1.svn20150119.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> r243-alt1.svn20150119.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r243-alt1.svn20150119
- New snapshot

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r187-alt1.svn20140706
- Initial build for Sisyphus

