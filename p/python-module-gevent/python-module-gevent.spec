%define oname gevent

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt2.b4.dev0.git20150825.1

Summary: Python network library that uses greenlet and libevent for easy and scalable concurrency

Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/%oname

%py_requires greenlet

%add_findreq_skiplist %python_sitelibdir/gevent/_socket3.py
%add_python_req_skip test

# https://github.com/surfly/gevent.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-gevent python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python-tools-2to3 python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-future python3-module-genshi python3-module-gevent python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface xz
BuildRequires: libev-devel python-module-Cython python-module-alabaster python-module-html5lib python-module-notebook python-module-objects.inv python3-module-Cython python3-module-cryptography python3-module-html5lib python3-module-notebook rpm-build-python3 time

#BuildPreReq: python-module-sphinx-devel python-module-greenlet
#BuildPreReq: python-module-OpenSSL python-module-Cython unifdef

%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-greenlet
#BuildPreReq: python3-module-distribute python3-module-Cython
#BuildPreReq: python3-module-OpenSSL python-tools-2to3
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
%py3_requires greenlet

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

rm -fR libev

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx doc

%build
%add_optflags -fno-strict-aliasing
%python_build_debug
%if_with python3
pushd ../python3
export CYTHON=cython3
sed -i 's|import mimetools|import email.message|' gevent/pywsgi.py
sed -i 's|mimetools.Message|email.message.Message|' gevent/pywsgi.py
sed -i 's|basestring|str|g' gevent/ares.pyx
%python3_build_debug || \
	(%make clean; %python3_build_debug || \
		(%make clean; %python3_build_debug ))
popd
%endif

%install
%python_install
cp -fR greentest %buildroot%python_sitelibdir/

%if_with python3
pushd ../python3
%python3_install
rm -fR greentest/2.*
cp -fR greentest %buildroot%python3_sitelibdir/
find %buildroot%python3_sitelibdir -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
