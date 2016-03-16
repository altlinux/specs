%define oname zope.i18nmessage

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt3.1
Summary: Message Identifiers for internationalization
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.i18nmessage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope

%description
To translate any text, we must be able to discover the source domain of
the text. A source domain is an identifier that identifies a project
that produces program source strings. Source strings occur as literals
in python programs, text in templates, and some text in XML data. The
project implies a source language and an application context.

We can think of a source domain as a collection of messages and
associated translation strings.

We often need to create unicode strings that will be displayed by
separate views. The view cannot translate the string without knowing its
source domain. A string or unicode literal carries no domain
information, therefore we use messages. Messages are unicode strings
which carry a translation source domain and possibly a more specific
translation context. They are created by a message factory. The message
factory is created by calling MessageFactory with the source domain.

This package provides facilities for declaring such messages within
program source text; translation of the messages is the responsibility
of the 'zope.i18n' package.

%package -n python3-module-%oname
Summary: Message Identifiers for internationalization
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
To translate any text, we must be able to discover the source domain of
the text. A source domain is an identifier that identifies a project
that produces program source strings. Source strings occur as literals
in python programs, text in templates, and some text in XML data. The
project implies a source language and an application context.

We can think of a source domain as a collection of messages and
associated translation strings.

We often need to create unicode strings that will be displayed by
separate views. The view cannot translate the string without knowing its
source domain. A string or unicode literal carries no domain
information, therefore we use messages. Messages are unicode strings
which carry a translation source domain and possibly a more specific
translation context. They are created by a message factory. The message
factory is created by calling MessageFactory with the source domain.

This package provides facilities for declaring such messages within
program source text; translation of the messages is the responsibility
of the 'zope.i18n' package.

%package -n python3-module-%oname-tests
Summary: Tests for Message Identifiers for internationalization
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
To translate any text, we must be able to discover the source domain of
the text. A source domain is an identifier that identifies a project
that produces program source strings. Source strings occur as literals
in python programs, text in templates, and some text in XML data. The
project implies a source language and an application context.

This package contains tests for Message Identifiers for
internationalization.

%package tests
Summary: Tests for Message Identifiers for internationalization
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
To translate any text, we must be able to discover the source domain of
the text. A source domain is an identifier that identifies a project
that produces program source strings. Source strings occur as literals
in python programs, text in templates, and some text in XML data. The
project implies a source language and an application context.

This package contains tests for Message Identifiers for
internationalization.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added module for Python 3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

