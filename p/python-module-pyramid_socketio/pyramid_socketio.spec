%define oname pyramid_socketio
Name: python-module-%oname
Version: 0.8
Release: alt1.1
Summary: Gevent-based Socket.IO pyramid integration and helpers
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_socketio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid gevent gevent-socketio

%description
Gevent-based Socket.IO integration for Pyramid (and WSGI frameworks).

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

