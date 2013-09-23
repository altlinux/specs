%define oname repoze.sendmail
Name: python-module-%oname
Version: 4.1
Release: alt1.git20130722
Summary: Send e-mails transactionally (originally cloned from zope.sendmail)
License: Repoze Public License
Group: Development/Python
Url: https://github.com/repoze/repoze.sendmail
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.sendmail.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-repoze.sphinx.autointerface

%py_requires repoze zope.interface transaction

%description
`repoze.sendmail` allows coupling the sending of email messages with a
transaction, using the Zope transaction manager.  This allows messages to
only be sent out when and if a transaction is committed, preventing users
from receiving notifications about events which may not have completed
successfully.  Messages may be sent directly or stored in a queue for later
sending.  The queued mail approach is the more common and recommended path.  A
console application which can flush the queue, sending the messages that it
finds, is included for convenience.

`repoze.sendmail` is a fork of `zope.sendmail`.  Functionality that was
specific to running in a Zope context has been removed, making this version
more generally useful to users of other frameworks.

%package tests
Summary: Tests for repoze.sendmail
Group: Development/Python
Requires: %name = %version-%release

%description tests
`repoze.sendmail` allows coupling the sending of email messages with a
transaction, using the Zope transaction manager.  This allows messages to
only be sent out when and if a transaction is committed, preventing users
from receiving notifications about events which may not have completed
successfully.  Messages may be sent directly or stored in a queue for later
sending.  The queued mail approach is the more common and recommended path.  A
console application which can flush the queue, sending the messages that it
finds, is included for convenience.

`repoze.sendmail` is a fork of `zope.sendmail`.  Functionality that was
specific to running in a Zope context has been removed, making this version
more generally useful to users of other frameworks.

This package contains tests for repoze.sendmail.

%package pickles
Summary: Pickles for repoze.sendmail
Group: Development/Python

%description pickles
`repoze.sendmail` allows coupling the sending of email messages with a
transaction, using the Zope transaction manager.  This allows messages to
only be sent out when and if a transaction is committed, preventing users
from receiving notifications about events which may not have completed
successfully.  Messages may be sent directly or stored in a queue for later
sending.  The queued mail approach is the more common and recommended path.  A
console application which can flush the queue, sending the messages that it
finds, is included for convenience.

`repoze.sendmail` is a fork of `zope.sendmail`.  Functionality that was
specific to running in a Zope context has been removed, making this version
more generally useful to users of other frameworks.

This package contains pickles for repoze.sendmail.

%package docs
Summary: Documentation for repoze.sendmail
Group: Development/Documentation
BuildArch: noarch

%description docs
`repoze.sendmail` allows coupling the sending of email messages with a
transaction, using the Zope transaction manager.  This allows messages to
only be sent out when and if a transaction is committed, preventing users
from receiving notifications about events which may not have completed
successfully.  Messages may be sent directly or stored in a queue for later
sending.  The queued mail approach is the more common and recommended path.  A
console application which can flush the queue, sending the messages that it
finds, is included for convenience.

`repoze.sendmail` is a fork of `zope.sendmail`.  Functionality that was
specific to running in a Zope context has been removed, making this version
more generally useful to users of other frameworks.

This package contains documentation for repoze.sendmail.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%make -C docs pickle
%make -C docs html

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1.git20130722
- Version 4.1

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.git20130329
- Version 4.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4-alt1.git20110519.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.git20110519.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.git20110519
- Initial build for Sisyphus

