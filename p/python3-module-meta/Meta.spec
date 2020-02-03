%define oname meta

Name: python3-module-%oname
Version: 0.4.0
Release: alt3

Summary: Framework to manipulate and analyze python ast's and bytecode
License: BSD-like
Group: Development/Python3
Url: http://numba.pydata.org/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python-tools-2to3


%description
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

%package tests
Summary: Tests for Meta
Group: Development/Python3
Requires: %name = %EVR

%description tests
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

This package contains tests for Meta.

%package pickles
Summary: Pickles for Meta
Group: Development/Python3

%description pickles
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

This package contains pickles for Meta.

%package docs
Summary: Documentation for Meta
Group: Development/Documentation

%description docs
A Pure Python module containing a framework to manipulate and analyze
python ast's and bytecode.

This package contains documentation for Meta.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile
sed -i 's|, wr_long||' meta/decompiler/recompile.py

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR _build/pickle %buildroot%python3_sitelibdir/meta/

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing.py*
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc _build/html/*

%files tests
%python3_sitelibdir/*/testing.py*
%python3_sitelibdir/*/*/tests


%changelog
* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0-alt3
- Build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0-alt2.git20120510.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt2.git20120510.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt2.git20120510.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2.git20120510
- Added module for Python 3

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20120510
- Initial build for Sisyphus

