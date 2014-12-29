%define oname zope.index

%def_with python3

Name: python-module-%oname
Version: 4.1.0
Release: alt1
Summary: Indices for using with catalog like text, field, etc.
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.index/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope ZODB3 zope.interface

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

