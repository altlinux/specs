%define oname pyasn1

%def_with python3

Summary: Abstract Syntax Notation One (ASN.1), Python implementation
Name: python-module-%oname
Version: 0.1.8
Release: alt2.1.1
%setup_python_module %oname
Url: http://pyasn1.sourceforge.net/
Source0: %modulename-%version.tar.gz
License: BSD-style
Group: Development/Python
Packager: Python Development Team <python at packages.altlinux.org>
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python-modules-unittest python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
%endif

%description
This is an implementation of ASN.1 types and codecs in Python programming
language. It has been first written to support particular protocol (SNMP)
but then generalized to be suitable for a wide range of protocols
based on ASN.1 specification.

%if_with python3
%package -n python3-module-%oname
Summary: Abstract Syntax Notation One (ASN.1), Python 3 implementation
Group: Development/Python3

%description -n python3-module-%oname
This is an implementation of ASN.1 types and codecs in Python programming
language. It has been first written to support particular protocol (SNMP)
but then generalized to be suitable for a wide range of protocols
based on ASN.1 specification.

%package -n python3-module-%oname-tests
Summary: Tests for pyasn1 (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This is an implementation of ASN.1 types and codecs in Python programming
language. It has been first written to support particular protocol (SNMP)
but then generalized to be suitable for a wide range of protocols
based on ASN.1 specification.

This package contains tests for pyasn1.
%endif

%package tests
Summary: Tests for pyasn1
Group: Development/Python
Requires: %name = %version-%release

%description tests
This is an implementation of ASN.1 types and codecs in Python programming
language. It has been first written to support particular protocol (SNMP)
but then generalized to be suitable for a wide range of protocols
based on ASN.1 specification.

This package contains tests for pyasn1.

%package docs
Summary: Documentation for pyasn1
Group: Development/Documentation
BuildArch: noarch

%description docs
This is an implementation of ASN.1 types and codecs in Python programming
language. It has been first written to support particular protocol (SNMP)
but then generalized to be suitable for a wide range of protocols
based on ASN.1 specification.

This package contains docs for pyasn1.

%prep
%setup  -q -n %modulename-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --record=INSTALLED_FILES
cp -fR test %buildroot%python_sitelibdir/%modulename/

%if_with python3
pushd ../python3
%python3_install
cp -fR test %buildroot%python3_sitelibdir/%modulename/
popd
%endif

%files -f INSTALLED_FILES
%doc CHANGES LICENSE README THANKS TODO PKG-INFO

%files docs
%doc doc/*

%files tests
%python_sitelibdir/%modulename/test

%if_with python3
%files -n python3-module-%oname
%doc CHANGES LICENSE README THANKS TODO PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%modulename/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%modulename/test
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.8-alt2.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt2
- Version 0.1.8

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.rc1
- Version 0.1.8rc1

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7-alt1.rc2
- Version 0.1.7rc2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.1.4-alt1.rc4.1
- Rebuild with Python-3.3

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.rc4
- Version 0.1.4rc4

* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Version 0.1.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.11a-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.11a-alt1
- Version 0.0.11a
- Added docs and tests

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7a-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.0.7a-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 16 2007 Peter V. Saveliev <peet@altlinux.org> 0.0.7a-alt1
- initial build

