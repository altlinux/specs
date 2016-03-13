%define oname lamson

%def_with python3

Name: python-module-%oname
Version: 1.3.4
Release: alt2.1
Summary: Lamson is a modern Pythonic mail server built like a web application server
License: BSD or GPLv3
Group: Development/Python
Url: http://pypi.python.org/pypi/lamson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif
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

%package -n python3-module-%oname
Summary: Lamson is a modern Pythonic mail server built like a web application server
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip config

%description -n python3-module-%oname
Lamson is a pure Python SMTP server designed to create robust and
complex mail applications in the style of modern web frameworks such as
Django. Unlike traditional SMTP servers like Postfix or Sendmail, Lamson
has all the features of a web application stack (ORM, templates,
routing, handlers, state machines, Python) without needing to configure
alias files, run newaliases, or juggle tons of tiny fragile processes.
Lamson also plays well with other web frameworks and Python libraries.

%package -n python3-module-%oname-tests
Summary: Tests for lamson SMTP server
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Lamson is a pure Python SMTP server designed to create robust and
complex mail applications in the style of modern web frameworks such as
Django. Unlike traditional SMTP servers like Postfix or Sendmail, Lamson
has all the features of a web application stack (ORM, templates,
routing, handlers, state machines, Python) without needing to configure
alias files, run newaliases, or juggle tons of tiny fragile processes.
Lamson also plays well with other web frameworks and Python libraries.

This package contains tests for lamson mail server.

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

%if_with python3
cp -fR . ../python3
for i in $(find ../python3 -type f -name '*.py' |grep -v 'scripts/setup.py')
do
	2to3 -w -n $i
done
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc LICENSE
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing.*

%files tests
%doc tests
%python_sitelibdir/*/testing.*

%files docs
%doc doc/lamsonproject.org/output/*
%doc examples

%if_with python3
%files -n python3-module-%oname
%doc LICENSE
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing.*
%exclude %python3_sitelibdir/*/*/testing.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/testing.*
%python3_sitelibdir/*/*/testing.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt2
- Added module for Python 3

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1
- Version 1.3.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added %_bindir/lamson

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

