%define oname slimit

%def_with python3

Name: python-module-%oname
Version: 0.8.1
Release: alt1.git20130425.1
Summary: SlimIt - a JavaScript minifier/parser in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/slimit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rspivak/slimit.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-ply
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-ply python-tools-2to3
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3

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
%if_with python3
pushd ../python3
python3 setup.py test
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1.git20130425.1
- NMU: Use buildreq for BR.

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20130425
- Initial build for Sisyphus

