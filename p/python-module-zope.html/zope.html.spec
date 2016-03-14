%define oname zope.html

%def_with python3

Name: python-module-%oname
Version: 2.4.2
Release: alt1.1
Summary: HTML and XHTML Editing Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.html/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools perl-CGI
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope pytz zc.resourcelibrary ZODB3 zope.annotation
%py_requires zope.app.form zope.component zope.event zope.file
%py_requires zope.formlib zope.i18nmessageid zope.interface
%py_requires zope.lifecycleevent zope.mimetype zope.publisher
%py_requires zope.schema

%description
This package contains support for editing HTML and XHTML inside a web
page using the FCKeditor as a widget. This is a fairly simple
application of FCKeditor, and simply instantiates a pre-configured
editor for each widget. There are no options to control the editors
individually.

%package -n python3-module-%oname
Summary: HTML and XHTML Editing Support
Group: Development/Python3
%py3_requires zope pytz zc.resourcelibrary ZODB3 zope.annotation
%py3_requires zope.app.form zope.component zope.event zope.file
%py3_requires zope.formlib zope.i18nmessageid zope.interface
%py3_requires zope.lifecycleevent zope.mimetype zope.publisher
%py3_requires zope.schema

%description -n python3-module-%oname
This package contains support for editing HTML and XHTML inside a web
page using the FCKeditor as a widget. This is a fairly simple
application of FCKeditor, and simply instantiates a pre-configured
editor for each widget. There are no options to control the editors
individually.

%package -n python3-module-%oname-tests
Summary: Tests for HTML and XHTML Editing Support
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.authentication zope.app.debugskin zope.app.server
%py3_requires zope.app.testing zope.app.zcmlfiles zope.testing
%py3_requires zope.testbrowser

%description -n python3-module-%oname-tests
This package contains support for editing HTML and XHTML inside a web
page using the FCKeditor as a widget. This is a fairly simple
application of FCKeditor, and simply instantiates a pre-configured
editor for each widget. There are no options to control the editors
individually.

This package contains tests for HTML and XHTML Editing Support.

%package tests
Summary: Tests for HTML and XHTML Editing Support
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.authentication zope.app.debugskin zope.app.server
%py_requires zope.app.testing zope.app.zcmlfiles zope.testing
%py_requires zope.testbrowser

%description tests
This package contains support for editing HTML and XHTML inside a web
page using the FCKeditor as a widget. This is a fairly simple
application of FCKeditor, and simply instantiates a pre-configured
editor for each widget. There are no options to control the editors
individually.

This package contains tests for HTML and XHTML Editing Support.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1
- Version 2.4.2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1
- Version 2.4.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus

