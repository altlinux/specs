%define oname lamson
Name: python-module-%oname
Version: 1.1
Release: alt2.1
Summary: Lamson is a modern Pythonic mail server built like a web application server
License: BSD or GPLv3
Group: Development/Python
Url: http://pypi.python.org/pypi/lamson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildArch: noarch

%py_provides %oname

%description
Lamson is a pure Python SMTP server designed to create robust and
complex mail applications in the style of modern web frameworks such as
Django. Unlike traditional SMTP servers like Postfix or Sendmail, Lamson
has all the features of a web application stack (ORM, templates,
routing, handlers, state machines, Python) without needing to configure
alias files, run newaliases, or juggle tons of tiny fragile processes.
Lamson also plays well with other web frameworks and Python libraries.

%package tests
Summary: Tests for lamson SMTP server
Group: Development/Python
Requires: %name = %version-%release

%description tests
Lamson is a pure Python SMTP server designed to create robust and
complex mail applications in the style of modern web frameworks such as
Django. Unlike traditional SMTP servers like Postfix or Sendmail, Lamson
has all the features of a web application stack (ORM, templates,
routing, handlers, state machines, Python) without needing to configure
alias files, run newaliases, or juggle tons of tiny fragile processes.
Lamson also plays well with other web frameworks and Python libraries.

This package contains tests for lamson mail server.

%package docs
Summary: Documentation and examples for lamson SMTP server
Group: Development/Documentation

%description docs
Lamson is a pure Python SMTP server designed to create robust and
complex mail applications in the style of modern web frameworks such as
Django. Unlike traditional SMTP servers like Postfix or Sendmail, Lamson
has all the features of a web application stack (ORM, templates,
routing, handlers, state machines, Python) without needing to configure
alias files, run newaliases, or juggle tons of tiny fragile processes.
Lamson also plays well with other web frameworks and Python libraries.

This package contains documentation and examples for lamson mail server.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc LICENSE README
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing.*

%files tests
%doc tests
%python_sitelibdir/*/testing.*

%files docs
%doc doc/lamsonproject.org/output/*
%doc examples

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added %_bindir/lamson

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

