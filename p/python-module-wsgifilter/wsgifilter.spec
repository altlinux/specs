%define oname wsgifilter

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt2.svn20090925.1
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
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

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

%package -n python3-module-%oname
Summary: Framework for building output-filtering WSGI middleware
Group: Development/Python3

%description -n python3-module-%oname
A framework (in the form of an abstract base class) for building
output-filtering WSGI middleware.

Features:

* You can filter just some content types (e.g., text/html) with low
  overhead for unfiltered output.

* Handles issues of decoding and encoding responses using the
  `HTTPEncode <http://pythonpaste.org/httpencode/>`_ system of
  formats.

* Does all the hard stuff with WSGI output filtering.

%package -n python3-module-%oname-examples
Summary: Examples for framework for building output-filtering WSGI middleware
Group: Development/Documentation
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-examples
A framework (in the form of an abstract base class) for building
output-filtering WSGI middleware.

This package contains examples for framework.

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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/examples

%files examples
%python_sitelibdir/*/examples

%if_with python3
%files -n python3-module-%oname
%doc docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/examples
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt2.svn20090925.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2.svn20090925
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.svn20090925.2.1
- Rebuild with Python-2.7

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.svn20090925.2
- Extracted examples into separate package

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.svn20090925.1
- Rebuilt with python 2.6

* Sat Sep 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.svn20090925
- Initial build for Sisyphus

