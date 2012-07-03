%define oname gunicorn
Name: python-module-%oname
Version: 0.14.4
Release: alt1.git20120604
Summary: WSGI HTTP Server for UNIX
License: Mit
Group: Development/Python
Url: http://pypi.python.org/pypi/gunicorn
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/benoitc/gunicorn.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-jinja2
BuildPreReq: python-module-docutils

%description
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a
pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn
server is broadly compatible with various web frameworks, simply
implemented, light on server resource usage, and fairly speedy.

%package docs
Summary: Documentation for gunicorn
Group: Development/Documentation
BuildArch: noarch

%description docs
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a
pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn
server is broadly compatible with various web frameworks, simply
implemented, light on server resource usage, and fairly speedy.

This package contains documentation for gunicorn.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc NOTICE THANKS *.rst
%_bindir/*
%python_sitelibdir/*

%files docs
%doc doc/htdocs examples

%changelog
* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt1.git20120604
- Initial build for Sisyphus

