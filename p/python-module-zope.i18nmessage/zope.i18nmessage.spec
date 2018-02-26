%define oname zope.i18nmessage
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Message Identifiers for internationalization
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.i18nmessage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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
* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

