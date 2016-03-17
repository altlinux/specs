%define oname zc.blist

%def_with python3

Name: python-module-%oname
Version: 1.0b2
Release: alt2.1
Summary: ZODB-friendly BTree-based list implementation
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.blist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc ZODB3 zope.testing

%description
The sequence in this package has a list-like API, but stores its values
in individual buckets. This means that, for small changes in large
sequences, the sequence could be a big win. For instance, an ordered
BTree-based container might want to store order in a sequence, so that
moves only cause a bucket or two--around 50 strings or less--to be
rewritten in the database, rather than the entire contents (which might
be thousands of strings, for instance).

%package -n python3-module-%oname
Summary: ZODB-friendly BTree-based list implementation
Group: Development/Python3
%py3_requires zc ZODB3 zope.testing

%description -n python3-module-%oname
The sequence in this package has a list-like API, but stores its values
in individual buckets. This means that, for small changes in large
sequences, the sequence could be a big win. For instance, an ordered
BTree-based container might want to store order in a sequence, so that
moves only cause a bucket or two--around 50 strings or less--to be
rewritten in the database, rather than the entire contents (which might
be thousands of strings, for instance).

%package -n python3-module-%oname-tests
Summary: Tests for zc.blist
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The sequence in this package has a list-like API, but stores its values
in individual buckets. This means that, for small changes in large
sequences, the sequence could be a big win. For instance, an ordered
BTree-based container might want to store order in a sequence, so that
moves only cause a bucket or two--around 50 strings or less--to be
rewritten in the database, rather than the entire contents (which might
be thousands of strings, for instance).

This package contains tests for zc.blist.

%package tests
Summary: Tests for zc.blist
Group: Development/Python
Requires: %name = %version-%release

%description tests
The sequence in this package has a list-like API, but stores its values
in individual buckets. This means that, for small changes in large
sequences, the sequence could be a big win. For instance, an ordered
BTree-based container might want to store order in a sequence, so that
moves only cause a bucket or two--around 50 strings or less--to be
rewritten in the database, rather than the entire contents (which might
be thousands of strings, for instance).

This package contains tests for zc.blist.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
rm -f %buildroot%python3_sitelibdir/*/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0b2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b2-alt1.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b2-alt1
- Initial build for Sisyphus

