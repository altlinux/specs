%define oname slimit

%def_with python3

Name: python-module-%oname
Version: 0.8.1
Release: alt2.git20130425.1
Summary: SlimIt - a JavaScript minifier/parser in Python
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/slimit/

# https://github.com/rspivak/slimit.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-ply
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-ply python-tools-2to3
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
SlimIt is a JavaScript minifier written in Python. It compiles
JavaScript into more compact code so that it downloads and runs faster.

SlimIt also provides a library that includes a JavaScript parser, lexer,
pretty printer and a tree visitor.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
SlimIt is a JavaScript minifier written in Python. It compiles
JavaScript into more compact code so that it downloads and runs faster.

SlimIt also provides a library that includes a JavaScript parser, lexer,
pretty printer and a tree visitor.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: SlimIt - a JavaScript minifier/parser in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
SlimIt is a JavaScript minifier written in Python. It compiles
JavaScript into more compact code so that it downloads and runs faster.

SlimIt also provides a library that includes a JavaScript parser, lexer,
pretty printer and a tree visitor.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
SlimIt is a JavaScript minifier written in Python. It compiles
JavaScript into more compact code so that it downloads and runs faster.

SlimIt also provides a library that includes a JavaScript parser, lexer,
pretty printer and a tree visitor.

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

%check
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
# TODO: check why python-3 tests fail
#py.test3
popd
%endif

%files
%doc CHANGES CREDIT *.rst docs/source/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc CHANGES CREDIT *.rst docs/source/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt2.git20130425.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt2.git20130425
- Updated build dependencies, updated tests for python-2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.git20130425.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1.git20130425.1
- NMU: Use buildreq for BR.

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20130425
- Initial build for Sisyphus

