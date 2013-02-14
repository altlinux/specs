%define oname gunicorn
Name: python-module-%oname
Version: 0.17.2
Release: alt1.git20130210
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

%package pickles
Summary: Pickles for gunicorn
Group: Development/Python

%description pickles
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a
pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn
server is broadly compatible with various web frameworks, simply
implemented, light on server resource usage, and fairly speedy.

This package contains pickles for gunicorn.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html
%make -C docs pickle

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc NOTICE THANKS *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files docs
%doc docs/build/html examples

%files pickles
%python_sitelibdir/*/pickle

%changelog
* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.2-alt1.git20130210
- Version 0.17.2
- Added pickles

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt1.git20120604
- Initial build for Sisyphus

