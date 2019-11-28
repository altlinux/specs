%define oname asn1ate

Name: python3-module-%oname
Version: 0.5
Release: alt2

Summary: ASN.1 translation library
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/asn1ate/
BuildArch: noarch

# https://github.com/kimgr/asn1ate.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pyasn1 python3-module-pyparsing

%py3_provides %oname
%py3_requires pyparsing


%description
asn1ate is a Python library for translating ASN.1 into other forms. It
is intended for code generation from formal ASN.1 definitions, and a
code generator for pyasn1 is included.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
asn1ate is a Python library for translating ASN.1 into other forms. It
is intended for code generation from formal ASN.1 definitions, and a
code generator for pyasn1 is included.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
sed -i 's|python|python3|g' basic_test.sh
./basic_test.sh

%files
%doc README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5-alt1.git20150314.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150314.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20150314.1
- NMU: Use buildreq for BR.

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150314
- Initial build for Sisyphus

