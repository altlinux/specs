%define oname gunicorn
Name: python3-module-%oname
Version: 0.14.4
Release: alt2.git20120604
Summary: WSGI HTTP Server for UNIX (Python 3)
License: Mit
Group: Development/Python3
Url: http://pypi.python.org/pypi/gunicorn
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/benoitc/gunicorn.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3

%add_python3_req_skip eventlet

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

for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done

%build
%python3_build

%install
%python3_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd

%files
%doc NOTICE THANKS *.rst
%_bindir/*
%python3_sitelibdir/*

%files docs
%doc doc/htdocs examples

%changelog
* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt2.git20120604
- Avoid conflict with python-module-%oname

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt1.git20120604
- Initial build for Sisyphus

