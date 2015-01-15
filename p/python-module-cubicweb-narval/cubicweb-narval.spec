%define oname cubicweb-narval
Name: python-module-%oname
Version: 4.1.1
Release: alt1
Summary: CubicWeb based framework to run automated tests
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-narval/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-localperms
BuildPreReq: python-module-cubicweb-file
BuildPreReq: python-module-cubicweb-signedrequest
BuildPreReq: python-module-Pygments python-module-requests
BuildPreReq: python-module-markdown

Requires: cubicweb python-module-cubicweb-localperms
Requires: python-module-cubicweb-file
Requires: python-module-cubicweb-signedrequest
%py_requires pygments requests

%description
Narval is a CubicWeb based framework to run automated tests. It consists
in 2 parts:

* the narval cube which implements the schema and some web UIs to
  create, configure and run test campaigns, and
* the narval bot which waits for jobs to execute. It polls the CubicWeb
  application for new tasks to run (called Plans in narval's jargon),
  and executes them when some are waiting for exectution.

The narval bot communicates with the web application by doing HTTP(S)
requests.

%prep
%setup

%build
%python_build_debug

%install
%python_install

install -d %buildroot%_sysconfdir/narval
install -p -m644 examples/*.ini %buildroot%_sysconfdir/narval/
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=%buildroot%python_sitelibdir
narval rcfile > %buildroot%_sysconfdir/narval/narval.ini

install -d %buildroot/var/log/narval

%check
python setup.py test

%pre
/usr/sbin/groupadd -r -f narval ||:
/usr/sbin/useradd -g narval -c 'cubicweb-narvar user' \
	-d /var/log/narval -s /dev/null -r narval >/dev/null 2>&1 ||:

%files
%doc README examples
%dir %_sysconfdir/narval
%config(noreplace) %_sysconfdir/narval/*
%_bindir/*
%python_sitelibdir/*
%_datadir/narval
%_datadir/cubicweb/*
%dir %attr(0775,narval,narval) /var/log/narval

%changelog
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Initial build for Sisyphus

