%define oname gevent-socketio

%def_with python3

Name: python-module-%oname
Version: 0.3.6
Release: alt2.git20140202.1.1.1
Summary: SocketIO server based on the Gevent pywsgi server, a Python network library
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/gevent-socketio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/abourget/gevent-socketio.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-versiontools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools python-module-versiontools python3-module-setuptools python3-module-versiontools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-versiontools python-tools-2to3
%endif

%py_provides %oname
%py_requires gevent-websocket

%description
SocketIO server based on the Gevent pywsgi server, a Python network
library.

%if_with python3
%package -n python3-module-%oname
Summary: SocketIO server based on the Gevent pywsgi server, a Python 3 network library
Group: Development/Python3
%py3_provides %oname
%py3_requires gevent-websocket

%description -n python3-module-%oname
SocketIO server based on the Gevent pywsgi server, a Python network
library.
%endif

%package docs
Summary: Documentation for gevent-socketio
Group: Development/Documentation

%description docs
SocketIO server based on the Gevent pywsgi server, a Python network
library.

This package contains documentation for gevent-socketio.

%package pickles
Summary: Pickles for gevent-socketio
Group: Development/Python

%description pickles
SocketIO server based on the Gevent pywsgi server, a Python network
library.

This package contains pickles for gevent-socketio.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

%make -C docs pickle
%make -C docs html

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR docs/build/pickle %buildroot%python_sitelibdir/socketio/

%files
%doc AUTHORS LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS LICENSE CHANGELOG *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.6-alt2.git20140202.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt2.git20140202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt2.git20140202.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt2.git20140202
- New snapshot

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt2.git20130915
- New snapshot

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt2.git20130201
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.3.6-alt1.git20130201.1
- Rebuild with Python-3.3

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20130201
- Version 0.3.6

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.beta.git20120514
- Version 0.3.5-beta
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

