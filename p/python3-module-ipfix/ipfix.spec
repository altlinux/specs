%define oname ipfix
Name: python3-module-%oname
Version: 0.9.7
Release: alt1.git20140704.1
Summary: IPFIX implementation for Python 3.3+
License: LGPLv3+
Group: Development/Python3
Url: https://pypi.python.org/pypi/ipfix
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/britram/python-ipfix.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel

%description
This module provides a Python interface to IPFIX message streams, and
provides tools for building IPFIX Exporting and Collecting Processes. It
handles message framing and deframing, encoding and decoding IPFIX data
records using templates, and a bridge between IPFIX ADTs and appopriate
Python data types.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This module provides a Python interface to IPFIX message streams, and
provides tools for building IPFIX Exporting and Collecting Processes. It
handles message framing and deframing, encoding and decoding IPFIX data
records using templates, and a bridge between IPFIX ADTs and appopriate
Python data types.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt *.md docs/*
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testutils.*
%exclude %python3_sitelibdir/*/*/testutils.*

%files tests
%python3_sitelibdir/*/testutils.*
%python3_sitelibdir/*/*/testutils.*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.7-alt1.git20140704.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.git20140704
- Initial build for Sisyphus

