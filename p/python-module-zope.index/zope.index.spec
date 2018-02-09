%define _unpackaged_files_terminate_build 1
%define oname zope.index
%def_with check

Name: python-module-%oname
Version: 4.3.0
Release: alt1%ubt

Summary: Indices for using with catalog like text, field, etc.
License: ZPLv2.1
Group: Development/Python
# Source-git: https://github.com/zopefoundation/zope.index.git
Url: http://pypi.python.org/pypi/zope.index

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python-module-ZODB
BuildRequires: python-module-transaction
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-ZODB
BuildRequires: python3-module-transaction

%if_with check
BuildRequires: python-module-BTrees
BuildRequires: python-module-persistent
BuildRequires: python-module-zope.interface
BuildRequires: python-module-zope.testrunner
BuildRequires: python3-module-BTrees
BuildRequires: python3-module-persistent
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.testrunner
%endif

%py_requires zope ZODB zope.interface

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
%py3_requires zope ZODB zope.interface

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
%patch0 -p1

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
python setup.py test -v

pushd ../python3
python3 setup.py test -v
popd

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests*
%exclude %python_sitelibdir/*/*/*/tests*

%files tests
%python_sitelibdir/*/*/tests*
%python_sitelibdir/*/*/*/tests*

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

%changelog
* Fri Feb 09 2018 Stanislav Levin <slev@altlinux.org> 4.3.0-alt1%ubt
- v4.1.1 -> v4.3.0

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150402.1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

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

