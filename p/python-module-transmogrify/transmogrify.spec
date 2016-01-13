%define oname transmogrify

Name: python-module-%oname
Version: 1.0.1
Release: alt3.beta2.git20130913
Summary: Allows for the dynamic alteration of images using the URL
License: ASL
Group: Development/Python
Url: https://pypi.python.org/pypi/transmogrify/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/callowayproject/Transmogrify.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Pillow python-modules-wsgiref
BuildPreReq: python-module-gunicorn
BuildPreReq: python-module-numpy python-module-webob
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-unittest2

%py_provides %oname

%description
Transmogrify is a Python-based image manipulator. It allows for dynamic
alteration of images using the URL of the image. The biggest benefit is
to the web designer, as images can be scaled to fit the design on the
fly.

Transmogrify is a library to dynamically alter images. Its biggest
impact is probably how it frees up the designer from resizing images for
different designs.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip autodetect processors wsgi_handler settings

%description tests
Transmogrify is a Python-based image manipulator. It allows for dynamic
alteration of images using the URL of the image. The biggest benefit is
to the web designer, as images can be scaled to fit the design on the
fly.

Transmogrify is a library to dynamically alter images. Its biggest
impact is probably how it frees up the designer from resizing images for
different designs.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc CREDITS README* TODO.txt example docs
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/example
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%changelog
* Wed Jan 13 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.1-alt3.beta2.git20130913
- remove erronous dependensy to python(settings)

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.beta2.git20130913
- Set as archdep

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.beta2.git20130913
- Initial build for Sisyphus

