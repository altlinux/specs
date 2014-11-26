%define oname fortpy

%def_with python3

Name: python-module-%oname
Version: 1.2.9
Release: alt1.git20141125
Summary: Fortran Parsing, Unit Testing and Intellisense
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Fortpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rosenbrockc/fortpy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: gcc-fortran
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-epc python-module-argparse
BuildPreReq: python-module-pyparsing python-module-dateutil
BuildPreReq: python-module-paramiko python-module-termcolor
BuildPreReq: python-module-pypandoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-epc python3-module-argparse
BuildPreReq: python3-module-pyparsing python3-module-dateutil
BuildPreReq: python3-module-paramiko python3-module-termcolor
BuildPreReq: python3-module-pypandoc
%endif

%py_provides %oname

%description
Fortpy is a python based parsing, unit testing and auto-complete
framework for supporting Fortran 2003 including object oriented
constructs. Auto-completion integration currently only available for
emacs (needs python-module-epc).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Fortpy is a python based parsing, unit testing and auto-complete
framework for supporting Fortran 2003 including object oriented
constructs. Auto-completion integration currently only available for
emacs (needs python-module-epc).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Fortran Parsing, Unit Testing and Intellisense
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Fortpy is a python based parsing, unit testing and auto-complete
framework for supporting Fortran 2003 including object oriented
constructs. Auto-completion integration currently only available for
emacs (needs python3-module-epc).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Fortpy is a python based parsing, unit testing and auto-complete
framework for supporting Fortran 2003 including object oriented
constructs. Auto-completion integration currently only available for
emacs (needs python-module-epc).

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Fortpy is a python based parsing, unit testing and auto-complete
framework for supporting Fortran 2003 including object oriented
constructs. Auto-completion integration currently only available for
emacs.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
%endif

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
	mv $i ${i}3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files docs
%doc docs/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.9-alt1.git20141125
- Version 1.2.9

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt1.git20141113
- Initial build for Sisyphus

