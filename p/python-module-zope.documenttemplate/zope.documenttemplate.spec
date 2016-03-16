%define oname zope.documenttemplate

%def_with python3

Name: python-module-%oname
Version: 3.4.3
Release: alt2.1
Summary: Document Templating Markup Language (DTML)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.documenttemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope zope.structuredtext

%description
This package implements the Document Templating Markup Language (DTML).
It uses custom SGML tags to implement simple programmatic feratures,
such as variable replacement, conditional logic and loops.

DTML was the first templating language developed for Zope 2 and is still
preferred by some over newer templating solutions due to its speed and
simplicity.

%package -n python3-module-%oname
Summary: Document Templating Markup Language (DTML)
Group: Development/Python3
%py3_requires zope zope.structuredtext

%description -n python3-module-%oname
This package implements the Document Templating Markup Language (DTML).
It uses custom SGML tags to implement simple programmatic feratures,
such as variable replacement, conditional logic and loops.

DTML was the first templating language developed for Zope 2 and is still
preferred by some over newer templating solutions due to its speed and
simplicity.

%package -n python3-module-%oname-tests
Summary: Tests for Document Templating Markup Language (DTML)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.security zope.testing

%description -n python3-module-%oname-tests
This package implements the Document Templating Markup Language (DTML).
It uses custom SGML tags to implement simple programmatic feratures,
such as variable replacement, conditional logic and loops.

DTML was the first templating language developed for Zope 2 and is still
preferred by some over newer templating solutions due to its speed and
simplicity.

This package contains tests for Document Templating Markup Language
(DTML).

%package tests
Summary: Tests for Document Templating Markup Language (DTML)
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.security zope.testing

%description tests
This package implements the Document Templating Markup Language (DTML).
It uses custom SGML tags to implement simple programmatic feratures,
such as variable replacement, conditional logic and loops.

DTML was the first templating language developed for Zope 2 and is still
preferred by some over newer templating solutions due to its speed and
simplicity.

This package contains tests for Document Templating Markup Language
(DTML).

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
%exclude %python_sitelibdir/*/*/tests*
%exclude %python_sitelibdir/*/*/*/tests*

%files tests
%python_sitelibdir/*/*/tests*
%python_sitelibdir/*/*/*/tests*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.3-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.3-alt1
- Version 3.4.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt1
- Initial build for Sisyphus

