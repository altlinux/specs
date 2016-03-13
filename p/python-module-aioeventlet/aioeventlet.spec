%define oname aioeventlet

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.hg20150304.1.1
Summary: asyncio event loop scheduling callbacks in eventlet
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aioeventlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/haypo/aioeventlet
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-eventlet python-module-coverage
#BuildPreReq: python-module-trollius python-module-futures
#BuildPreReq: python-module-mock python-module-aiotest
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-eventlet python3-module-coverage
#BuildPreReq: python3-module-asyncio
#BuildPreReq: python3-module-mock python3-module-aiotest
%endif

%py_provides %oname
%py_requires eventlet trollius

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-dns python-module-enum34 python-module-funcsigs python-module-futures python-module-genshi python-module-greenlet python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-markupsafe python-module-pbr python-module-psycopg2 python-module-pyasn1 python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-traceback2 python-module-trollius python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-OpenSSL python3-module-asyncio python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-dns python3-module-enum34 python3-module-genshi python3-module-greenlet python3-module-linecache2 python3-module-ntlm python3-module-pip python3-module-psycopg2 python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-traceback2
BuildRequires: python-module-aiotest python-module-alabaster python-module-coverage python-module-docutils python-module-eventlet python-module-html5lib python-module-mock python-module-objects.inv python-module-setuptools-tests python3-module-aiotest python3-module-coverage python3-module-eventlet python3-module-html5lib python3-module-pbr python3-module-setuptools-tests python3-module-unittest2 rpm-build-python3 time

%description
aioeventlet implements the asyncio API (PEP 3156) on top of eventlet. It
makes possible to write asyncio code in a project currently written for
eventlet.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
aioeventlet implements the asyncio API (PEP 3156) on top of eventlet. It
makes possible to write asyncio code in a project currently written for
eventlet.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
aioeventlet implements the asyncio API (PEP 3156) on top of eventlet. It
makes possible to write asyncio code in a project currently written for
eventlet.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: asyncio event loop scheduling callbacks in eventlet
Group: Development/Python3
%py3_provides %oname
%py3_requires eventlet asyncio

%description -n python3-module-%oname
aioeventlet implements the asyncio API (PEP 3156) on top of eventlet. It
makes possible to write asyncio code in a project currently written for
eventlet.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
#python runtests.py
python run_aiotest.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py
python3 run_aiotest.py
popd
%endif

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.hg20150304.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.hg20150304.1
- NMU: Use buildreq for BR.

* Mon Apr 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.hg20150304
- Version 0.5

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

