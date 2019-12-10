%define _unpackaged_files_terminate_build 1

%define oname repoze.sendmail

Name: python3-module-%oname
Version: 4.4.1
Release: alt1

Summary: Send e-mails transactionally (originally cloned from zope.sendmail)
License: Repoze Public License
Group: Development/Python3
Url: https://github.com/repoze/repoze.sendmail

# https://github.com/repoze/repoze.sendmail.git
Source0: https://pypi.python.org/packages/54/60/102fdd3a16f3d42f6b3e429116ac190a2c78c629d50a82cbc7d4193c7cdc/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python3-module-repoze.sphinx.autointerface

%py3_requires repoze zope.interface transaction


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
Group: Development/Python3
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
Group: Development/Python3

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
%setup -q -n %{oname}-%{version}

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build

%make -C docs pickle
%make -C docs html

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc *.txt *.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/pickle

%files tests
%python3_sitelibdir/*/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.4.1-alt1
- version updated to 4.4.1
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2-alt2.git20140222.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2-alt2.git20140222.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.2-alt2.git20140222.1
- NMU: Use buildreq for BR.

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt2.git20140222
- Added module for Python 3

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1.git20140222
- Version 4.2

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1.git20131127
- New snapshot

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

