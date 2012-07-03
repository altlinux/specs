%define oname gevent-socketio

%def_with python3

Name: python-module-%oname
Version: 0.3.5
Release: alt1.beta.git20120514
Summary: SocketIO server based on the Gevent pywsgi server, a Python network library
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/gevent-socketio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/abourget/gevent-socketio.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-versiontools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-versiontools python-tools-2to3
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
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
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
%doc AUTHORS LICENSE CHANGELOG TODO *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.beta.git20120514
- Version 0.3.5-beta
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

