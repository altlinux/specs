%define _unpackaged_files_terminate_build 1
%define oname PyAMF
Name: python-module-%oname
Version: 0.8.0
Release: alt1.1
Summary: AMF support for Python
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/PyAMF/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/a0/06/43976c0e3951b9bf7ba0d7d614a8e3e024eb5a1c6acecc9073b81c94fb52/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools

Requires: python-module-django

%description
PyAMF provides Action Message Format (AMF) support for Python that is
compatible with the Adobe Flash Player. It includes integration with
Python web frameworks like Django, Pylons, Twisted, SQLAlchemy, web2py
and more.

The Adobe Integrated Runtime and Adobe Flash Player use AMF to
communicate between an application and a remote server. AMF encodes
remote procedure calls (RPC) into a compact binary representation that
can be transferred over HTTP/HTTPS or the RTMP/RTMPS protocol. Objects
and data values are serialized into this binary format, which increases
performance, allowing applications to load data up to 10 times faster
than with text-based formats such as XML or SOAP.

AMF3, the default serialization for ActionScript 3.0, provides various
advantages over AMF0, which is used for ActionScript 1.0 and 2.0. AMF3
sends data over the network more efficiently than AMF0. AMF3 supports
sending int and uint objects as integers and supports data types that
are available only in ActionScript 3.0, such as ByteArray,
ArrayCollection, ObjectProxy and IExternalizable.

%package tests
Summary: Tests for PyAMF
Group: Development/Python
Requires: %name = %version-%release

%description tests
PyAMF provides Action Message Format (AMF) support for Python that is
compatible with the Adobe Flash Player. It includes integration with
Python web frameworks like Django, Pylons, Twisted, SQLAlchemy, web2py
and more.

This package contains tests for PyAMF.

%package docs
Summary: Documentation for PyAMF
Group: Development/Documentation
BuildArch: noarch

%description docs
PyAMF provides Action Message Format (AMF) support for Python that is
compatible with the Adobe Flash Player. It includes integration with
Python web frameworks like Django, Pylons, Twisted, SQLAlchemy, web2py
and more.

This package contains documentation for PyAMF.

%prep
%setup -q -n %{oname}-%{version}

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files docs
%doc doc/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- automated PyPI update

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Fixed build

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt1.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

