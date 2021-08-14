%define oname la

%def_without docs

Name: python3-module-%oname
Version: 0.6.0
Release: alt4

Summary: Label the rows, columns, any dimension, of your NumPy arrays
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/la

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires: python3-module-sphinx
%endif
BuildRequires: python-tools-2to3


%description
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

%package tests
Summary: Tests for la
Group: Development/Python3
Requires: %name = %EVR

%description tests
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains tests for la.

%if_with docs
%package pickles
Summary: Pickles for la
Group: Development/Python3

%description pickles
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains pickles for la.

%package docs
Summary: Documentation for la
Group: Development/Documentation
BuildArch: noarch

%description docs
The main class of the la package is a labeled array, larry. A larry
consists of data and labels. The data is stored as a NumPy array and the
labels as a list of lists (one list per dimension).

This package contains documentation for la.
%endif

%prep
%setup

## py2 -> py3
%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile
sed -i 's|= file(|= open(|' doc/source/conf.py
%endif

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
##

rm -f ./la/src/*.c

%build
%python3_build_debug

%if_with docs
%make -C doc pickle
%make -C doc html
%endif

%install
%python3_install

%if_with docs
cp -fR doc/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/test*
# %exclude %python3_sitelibdir/%oname/pickle

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/test*

%if_with docs
%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc doc/build/html/*
%endif


%changelog
* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt4
- drop unused BR: rpm-macros-sphinx

* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.0-alt3
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.0-alt2.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt2.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added module for Python 3

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

