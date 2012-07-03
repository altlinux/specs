%define oname pywsgi
Name: python-module-%oname
Version: 0.9.0
Release: alt1.1
Summary: A high-level class-based API around WSGI, CGI, and mod_python
License: GPLv2
Group: Development/Python
Url: http://pypi.python.org/pypi/pywsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_provides %oname

%description
pywsgi provides the following features:

 - An abstraction from low-level gateway interface handlers like WSGI,
   CGI, and mod_python.
 - A consistent high-level, class-based interface.
 - Session handling.
 - Cookie handling.
 - GET/POST data handling.
 - Error handling.
 - A pywsgi.util namespace with useful tools.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus

