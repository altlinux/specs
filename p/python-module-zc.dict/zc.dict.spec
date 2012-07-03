%define oname zc.dict
Name: python-module-%oname
Version: 1.3b1
Release: alt2.1
Summary: BTree-based persistent dict-like objects that can be used as base classes
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.dict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface ZODB3 zc.blist

%description
BTree-based persistent dict-like objects (regular dict and ordered) that
can be used as base classes. This is a bit of a heavyweight solution, as
every zc.dict.Dict (and zc.dict.OrderedDict) is at least 3 persistent
objects. Keep this in mind if you intend to create lots and lots of
these.

%package tests
Summary: Tests for zc.dict
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
BTree-based persistent dict-like objects (regular dict and ordered) that
can be used as base classes. This is a bit of a heavyweight solution, as
every zc.dict.Dict (and zc.dict.OrderedDict) is at least 3 persistent
objects. Keep this in mind if you intend to create lots and lots of
these.

This package contains tests for zc.dict.

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
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3b1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3b1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3b1-alt1
- Initial build for Sisyphus

