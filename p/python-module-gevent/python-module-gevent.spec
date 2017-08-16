%define oname gevent

%def_with python3

Name: python-module-%oname
Version: 1.1.2
Release: alt1

Summary: Python network library that uses greenlet and libevent for easy and scalable concurrency

Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/gevent

%add_findreq_skiplist %python_sitelibdir/gevent/_socket3.py
%add_python_req_skip test

# https://github.com/surfly/gevent.git
Source: %oname-%version.tar
Patch1: %oname-%version-alt-build.patch
Patch2: %oname-%version-upstream-cython26.patch

BuildRequires(pre): rpm-macros-sphinx
BuildPreReq: libev-devel python-module-Cython python-module-alabaster python-module-html5lib python-module-objects.inv
BuildPreReq: python-module-greenlet

%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): python3-module-greenlet
BuildRequires(pre): python3-module-OpenSSL python-tools-2to3
BuildRequires: python3-module-Cython python3-module-cryptography python3-module-html5lib
%endif

%description
gevent is a coroutine-based Python networking library that uses greenlet
to provide a high-level synchronous API on top of libevent event loop.

Features include:
* convenient API around greenlets
* familiar synchronization primitives (gevent.event, gevent.queue)
* socket module that cooperates
* WSGI server on top of libevent-http
* DNS requests done through libevent-dns
* monkey patching utility to get pure Python modules to cooperate

%package -n python-module-greentest
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description -n python-module-greentest
gevent is a coroutine-based Python networking library that uses greenlet
to provide a high-level synchronous API on top of libevent event loop.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 network library that uses greenlet and libevent for easy and scalable concurrency
Group: Development/Python3

%description -n python3-module-%oname
gevent is a coroutine-based Python networking library that uses greenlet
to provide a high-level synchronous API on top of libevent event loop.

Features include:
* convenient API around greenlets
* familiar synchronization primitives (gevent.event, gevent.queue)
* socket module that cooperates
* WSGI server on top of libevent-http
* DNS requests done through libevent-dns
* monkey patching utility to get pure Python modules to cooperate

%package -n python3-module-greentest
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-greentest
gevent is a coroutine-based Python networking library that uses greenlet
to provide a high-level synchronous API on top of libevent event loop.

This package contains tests for %oname.
%endif

%package doc
Summary: Documentation for gevent
Group: Development/Documentation
BuildArch: noarch

%description doc
gevent is a coroutine-based Python networking library that uses greenlet
to provide a high-level synchronous API on top of libevent event loop.

This package contains documentation and examples for gevent.

%package pickles
Summary: Pickles for gevent
Group: Development/Documentation

%description pickles
gevent is a coroutine-based Python networking library that uses greenlet
to provide a high-level synchronous API on top of libevent event loop.

This package contains pickles for gevent.

%prep
%setup
%patch1 -p1
%patch2 -p2

rm -fR libev

%if_with python3
cp -a . ../python3
%endif

%prepare_sphinx doc

%build
%add_optflags -fno-strict-aliasing

rm -fR greentest/3.*
%python_build_debug

%if_with python3
pushd ../python3
export CYTHON=cython3
sed -i 's|import mimetools|import email.message|' gevent/pywsgi.py
sed -i 's|mimetools.Message|email.message.Message|' gevent/pywsgi.py
sed -i 's|basestring|str|g' gevent/ares.pyx
sed -i 's|test.script_helper|test.test_script_helper|g' greentest/*/test_threading.py
rm -fR greentest/2.*
find . -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build_debug
popd
%endif

%install
%python_install
cp -fR greentest %buildroot%python_sitelibdir/

%if_with python3
pushd ../python3
%python3_install
cp -fR greentest %buildroot%python3_sitelibdir/
popd
%endif

#doc

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc
%make pickle
%make html

cp -fR _build/pickle %buildroot%python_sitelibdir/%oname/
popd

%files
%doc AUTHORS LICENSE* TODO *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/greentest

%files -n python-module-greentest
%python_sitelibdir/greentest

%files doc
%doc doc/_build/html
%doc examples

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS LICENSE* TODO *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/greentest

%files -n python3-module-greentest
%python3_sitelibdir/greentest
%endif

%changelog
* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.2-alt1
- Updated to upstream version 1.1.2.

* Tue Apr 26 2016 Denis Medvedev <nbr@altlinux.org> 1.1.0-alt2.b4.dev0.git20150825.3
- (NMU) with sphinx changed.

* Thu Mar 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt2.b4.dev0.git20150825.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 24 2016 Denis Medvedev <nbr@altlinux.org> 1.1.0-alt2.b4.dev0.git20150825.2
- NMU dependencies organization.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt2.b4.dev0.git20150825.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2.b4.dev0.git20150825
- Version 1.1b4.dev0

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141213
- New snapshot
- Extracted greentest into separate package

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20140820
- New snapshot

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20140623
- Version 1.1.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4.git20130221
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sat Mar 23 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0-alt3.git20130221.1
- Rebuild with Python-3.3

* Thu Mar 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3.git20130221
- New snapshot

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2.hg20120529
- Fixed using email.message

* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20120529
- New snapshot
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.hg20110818.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.hg20110818.1
- Rebuild with Python-2.7

* Wed Aug 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20110818
- Version 1.0

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1.hg20110502
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1.hg20110325.1
- Rebuilt with python-module-sphinx-devel

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1.hg20110325
- Version 0.14.0

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.hg20100802
- New snapshot

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.hg20100621
- Version 0.13.0
- Added doc and pickles

* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 0.11.2-alt1
- initial build for ALT Linux Sisyphus
