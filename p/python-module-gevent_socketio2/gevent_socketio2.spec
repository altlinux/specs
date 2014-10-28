%define oname gevent_socketio2
Name: python-module-%oname
Version: 0.1.5
Release: alt1.git20141027
Summary: A gevent implementation for socketio protocol 1.0
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/gevent_socketio2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/shuoli84/gevent_socketio2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-greenlet python-module-webob
BuildPreReq: python-module-gevent-websocket python-module-pyee
BuildPreReq: python-module-requests

%py_provides socketio
Conflicts: python-module-gevent-socketio
%py_requires geventwebsocket greenlet webob pyee

%description
We love socketio, implements socketio 0.7, this project intend to bring
socketio 1.0 to python(gevent) world. It started as a fork of
gevent_socketio. This project mainly is a port of socketiojs project, so
you can see EventEmitter in code. Some code not that clean due to the
port, which needs further refine.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc AUTHORS NOTES *.rst docs/*.rst
%python_sitelibdir/*

%changelog
* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20141027
- Initial build for Sisyphus

