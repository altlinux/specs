%define oname zope.index

%def_with python3

Name: python-module-%oname
Version: 4.1.1
Release: alt1.dev0.git20150402.1.1
Summary: Indices for using with catalog like text, field, etc.
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.index/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-ZODB3 python-module-zope.testrunner
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-ZODB3 python3-module-zope.testrunner
%endif

%py_requires zope ZODB3 zope.interface

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-BTrees python-module-ZODB python-module-cffi python-module-cryptography python-module-enum34 python-module-extras python-module-linecache2 python-module-mimeparse python-module-numpy python-module-pbr python-module-persistent python-module-pyasn1 python-module-pytest python-module-serial python-module-setuptools python-module-six python-module-subunit python-module-testtools python-module-traceback2 python-module-transaction python-module-twisted-core python-module-unittest2 python-module-zc.lockfile python-module-zdaemon python-module-zodbpickle python-module-zope python-module-zope.event python-module-zope.exceptions python-module-zope.interface python-module-zope.proxy python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python3 python3-base python3-dev python3-module-BTrees python3-module-ZODB python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-extras python3-module-genshi python3-module-linecache2 python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-persistent python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-subunit python3-module-testtools python3-module-traceback2 python3-module-transaction python3-module-unittest2 python3-module-zc.lockfile python3-module-zdaemon python3-module-zope python3-module-zope.event python3-module-zope.exceptions python3-module-zope.interface python3-module-zope.proxy python3-module-zope.testing
BuildRequires: python-module-ZEO python-module-setuptools-tests python-module-zope.testrunner python3-module-ZEO python3-module-html5lib python3-module-setuptools-tests python3-module-zope.testrunner rpm-build-python3

%description
The zope.index package provides several indices for the Zope catalog.
These include:

  * a field index (for indexing orderable values),
  * a keyword index,
  * a topic index,
  * a text index (with support for lexicon, splitter, normalizer, etc.)

%package -n python3-module-%oname
Summary: Indices for using with catalog like text, field, etc.
Group: Development/Python3
%py3_requires zope ZODB3 zope.interface

%description -n python3-module-%oname
The zope.index package provides several indices for the Zope catalog.
These include:

  * a field index (for indexing orderable values),
  * a keyword index,
  * a topic index,
  * a text index (with support for lexicon, splitter, normalizer, etc.)

%package -n python3-module-%oname-tests
Summary: Tests for zope.index
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The zope.index package provides several indices for the Zope catalog.
These include:

  * a field index (for indexing orderable values),
  * a keyword index,
  * a topic index,
  * a text index (with support for lexicon, splitter, normalizer, etc.)

This package contains tests for zope.index.

%package tests
Summary: Tests for zope.index
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The zope.index package provides several indices for the Zope catalog.
These include:

  * a field index (for indexing orderable values),
  * a keyword index,
  * a topic index,
  * a text index (with support for lexicon, splitter, normalizer, etc.)

This package contains tests for zope.index.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|PyInt_AsLong|PyLong_AsLong|g' \
	../python3/src/zope/index/text/okascore.c
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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests*
%exclude %python_sitelibdir/*/*/*/tests*

%files tests
%python_sitelibdir/*/*/tests*
%python_sitelibdir/*/*/*/tests*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests*
%exclude %python3_sitelibdir/*/*/*/tests*
%exclude %python3_sitelibdir/*/*/*/*/tests*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests*
%python3_sitelibdir/*/*/*/tests*
%python3_sitelibdir/*/*/*/*/tests*
%endif

%changelog
* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150402.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt1.dev0.git20150402.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150402
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.3-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Version 3.6.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

