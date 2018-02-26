%define oname zc.blist
Name: python-module-%oname
Version: 1.0b2
Release: alt1.1
Summary: ZODB-friendly BTree-based list implementation
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.blist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc ZODB3 zope.testing

%description
The sequence in this package has a list-like API, but stores its values
in individual buckets. This means that, for small changes in large
sequences, the sequence could be a big win. For instance, an ordered
BTree-based container might want to store order in a sequence, so that
moves only cause a bucket or two--around 50 strings or less--to be
rewritten in the database, rather than the entire contents (which might
be thousands of strings, for instance).

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b2-alt1.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b2-alt1
- Initial build for Sisyphus

