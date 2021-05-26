%define oname wsgifilter

Name: python3-module-%oname
Version: 0.2.1
Release: alt3.svn20090925
Summary: Framework for building output-filtering WSGI middleware
License: MIT
Group: Development/Python3
Url: http://pythonpaste.org/wsgifilter/

# http://svn.pythonpaste.org/Paste/WSGIFilter/trunk
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3

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

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/examples

%changelog
* Wed May 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt3.svn20090925
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt2.svn20090925.2
- (NMU) rebuild with python3.6

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

