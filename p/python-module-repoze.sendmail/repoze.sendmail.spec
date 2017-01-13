%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname repoze.sendmail

%def_with python3

Name: python-module-%oname
Version: 4.3
#Release: alt2.git20140222.1.1
Summary: Send e-mails transactionally (originally cloned from zope.sendmail)
License: Repoze Public License
Group: Development/Python
Url: https://github.com/repoze/repoze.sendmail
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.sendmail.git
Source0: https://pypi.python.org/packages/54/60/102fdd3a16f3d42f6b3e429116ac190a2c78c629d50a82cbc7d4193c7cdc/%{oname}-%{version}.tar.gz

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-repoze.sphinx.autointerface
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze zope.interface transaction

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-repoze python-module-repoze.sphinx python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-repoze.sphinx.autointerface python3-module-setuptools rpm-build-python3 time

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

%package -n python3-module-%oname
Summary: Send e-mails transactionally (originally cloned from zope.sendmail)
Group: Development/Python3
%py3_requires repoze zope.interface transaction

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for repoze.sendmail
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
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
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%make -C docs pickle
%make -C docs html

%install
%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
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

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
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

