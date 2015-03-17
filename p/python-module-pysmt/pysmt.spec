%define oname pysmt

%def_without python3

Name: python-module-%oname
Version: 0.2.5
Release: alt1.dev.git20150315
Summary: A library for SMT Formulae manipulation and solving
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pySMT/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pysmt/pysmt.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-CVC4 python-module-pycudd
BuildPreReq: python-module-nose python-module-picosat
# BuildPreReq: python-module-pyeda - python3 only now
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-CVC4 python3-module-pycudd
BuildPreReq: python3-module-pyeda python-tools-2to3
BuildPreReq: python3-module-nose python3-module-picosat
%endif

%py_provides %oname
%py_requires CVC4 pycudd _picosat
#py_requires pyeda - python3 only now
%add_python_req_skip mathsat

%description
pySMT makes working with Satisfiability Modulo Theory simple.

Among others, you can:

* Define formulae in a solver independent way in a simple and inutitive
  way,
* Write ad-hoc simplifiers and operators,
* Dump your problems in the SMT-Lib format,
* Solve them using one of the native solvers, or by wrapping any SMT-Lib
  complaint solver.

NOTE: if You want to enable support of Z3 and Yices 2, install packages
python-module-z3 and python-module-pyices manually (because of non-free
licenses).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
pySMT makes working with Satisfiability Modulo Theory simple.

Among others, you can:

* Define formulae in a solver independent way in a simple and inutitive
  way,
* Write ad-hoc simplifiers and operators,
* Dump your problems in the SMT-Lib format,
* Solve them using one of the native solvers, or by wrapping any SMT-Lib
  complaint solver.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: A library for SMT Formulae manipulation and solving
Group: Development/Python3
%py3_provides %oname
%py3_requires CVC4 pycudd _picosat
%py3_requires pyeda
%add_python3_req_skip mathsat

%description -n python3-module-%oname
pySMT makes working with Satisfiability Modulo Theory simple.

Among others, you can:

* Define formulae in a solver independent way in a simple and inutitive
  way,
* Write ad-hoc simplifiers and operators,
* Dump your problems in the SMT-Lib format,
* Solve them using one of the native solvers, or by wrapping any SMT-Lib
  complaint solver.

NOTE: if You want to enable support of Z3 and Yices 2, install packages
python3-module-z3 and python3-module-pyices manually (because of non-free
licenses).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
pySMT makes working with Satisfiability Modulo Theory simple.

Among others, you can:

* Define formulae in a solver independent way in a simple and inutitive
  way,
* Write ad-hoc simplifiers and operators,
* Dump your problems in the SMT-Lib format,
* Solve them using one of the native solvers, or by wrapping any SMT-Lib
  complaint solver.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pySMT makes working with Satisfiability Modulo Theory simple.

Among others, you can:

* Define formulae in a solver independent way in a simple and inutitive
  way,
* Write ad-hoc simplifiers and operators,
* Dump your problems in the SMT-Lib format,
* Solve them using one of the native solvers, or by wrapping any SMT-Lib
  complaint solver.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pySMT makes working with Satisfiability Modulo Theory simple.

Among others, you can:

* Define formulae in a solver independent way in a simple and inutitive
  way,
* Write ad-hoc simplifiers and operators,
* Dump your problems in the SMT-Lib format,
* Solve them using one of the native solvers, or by wrapping any SMT-Lib
  complaint solver.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
./run_all_tests.sh
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' run_all_tests.sh
./run_all_tests.sh
popd
%endif

%files
%doc NOTICE *.rst examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%_bindir/*.py3
%doc NOTICE *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.dev.git20150315
- Initial build for Sisyphus

