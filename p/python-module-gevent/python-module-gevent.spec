%define oname gevent

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt2.hg20120529

Summary: Python network library that uses greenlet and libevent for easy and scalable concurrency

Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

%py_requires greenlet

# hg clone http://bitbucket.org/denis/gevent
Source: %oname-%version.tar

# Automatically added by buildreq on Wed Feb 03 2010
BuildRequires: libevent1.4-devel python-devel python-modules-ctypes

BuildPreReq: python-module-sphinx-devel python-module-greenlet
BuildPreReq: python-module-OpenSSL python-module-Cython unifdef

%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-greenlet
BuildPreReq: python3-module-distribute python3-module-Cython
BuildPreReq: python3-module-OpenSSL python-tools-2to3
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
%python3_build_debug
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
for i in $(find %buildroot%python3_sitelibdir -name '*.py')
do
	2to3 -w -n $i
done
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

%files doc
%doc doc/_build/html
%doc examples

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS LICENSE* TODO *.rst
%python3_sitelibdir/*
%endif

%changelog
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
