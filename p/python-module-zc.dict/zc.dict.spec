%define oname zc.dict

%def_with python3

Name: python-module-%oname
Version: 1.3b1
Release: alt3.1
Summary: BTree-based persistent dict-like objects that can be used as base classes
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.dict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.interface ZODB3 zc.blist

%description
BTree-based persistent dict-like objects (regular dict and ordered) that
can be used as base classes. This is a bit of a heavyweight solution, as
every zc.dict.Dict (and zc.dict.OrderedDict) is at least 3 persistent
objects. Keep this in mind if you intend to create lots and lots of
these.

%package -n python3-module-%oname
Summary: BTree-based persistent dict-like objects that can be used as base classes
Group: Development/Python3
%py3_requires zope.interface ZODB3 zc.blist

%description -n python3-module-%oname
BTree-based persistent dict-like objects (regular dict and ordered) that
can be used as base classes. This is a bit of a heavyweight solution, as
every zc.dict.Dict (and zc.dict.OrderedDict) is at least 3 persistent
objects. Keep this in mind if you intend to create lots and lots of
these.

%package -n python3-module-%oname-tests
Summary: Tests for zc.dict
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
BTree-based persistent dict-like objects (regular dict and ordered) that
can be used as base classes. This is a bit of a heavyweight solution, as
every zc.dict.Dict (and zc.dict.OrderedDict) is at least 3 persistent
objects. Keep this in mind if you intend to create lots and lots of
these.

This package contains tests for zc.dict.

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
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3b1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3b1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3b1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3b1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3b1-alt1
- Initial build for Sisyphus

