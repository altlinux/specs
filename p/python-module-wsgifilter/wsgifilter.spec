%define oname wsgifilter
Name: python-module-%oname
Version: 0.2.1
Release: alt1.svn20090925.2.1
Summary: Framework for building output-filtering WSGI middleware
License: MIT
Group: Development/Python
Url: http://pythonpaste.org/wsgifilter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.pythonpaste.org/Paste/WSGIFilter/trunk
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%setup_python_module %oname

%description
A framework (in the form of an abstract base class) for building
output-filtering WSGI middleware.

Features:

* You can filter just some content types (e.g., text/html) with low
  overhead for unfiltered output.

* Handles issues of decoding and encoding responses using the
  `HTTPEncode <http://pythonpaste.org/httpencode/>`_ system of
  formats.

* Does all the hard stuff with WSGI output filtering.

%package examples
Summary: Examples for framework for building output-filtering WSGI middleware
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
A framework (in the form of an abstract base class) for building
output-filtering WSGI middleware.

This package contains examples for framework.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/examples

%files examples
%python_sitelibdir/*/examples

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.svn20090925.2.1
- Rebuild with Python-2.7

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.svn20090925.2
- Extracted examples into separate package

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.svn20090925.1
- Rebuilt with python 2.6

* Sat Sep 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.svn20090925
- Initial build for Sisyphus

