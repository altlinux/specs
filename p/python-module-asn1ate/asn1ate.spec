%define oname asn1ate

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.git20150314.1.1
Summary: ASN.1 translation library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/asn1ate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kimgr/asn1ate.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pyparsing python-module-pyasn1
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pyparsing python3-module-pyasn1
%endif

%py_provides %oname
%py_requires pyparsing

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python-module-pyasn1 python-module-pyparsing python3-module-pyasn1 python3-module-pyparsing rpm-build-python3

%description
asn1ate is a Python library for translating ASN.1 into other forms. It
is intended for code generation from formal ASN.1 definitions, and a
code generator for pyasn1 is included.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
asn1ate is a Python library for translating ASN.1 into other forms. It
is intended for code generation from formal ASN.1 definitions, and a
code generator for pyasn1 is included.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: ASN.1 translation library
Group: Development/Python3
%py3_provides %oname
%py3_requires pyparsing

%description -n python3-module-%oname
asn1ate is a Python library for translating ASN.1 into other forms. It
is intended for code generation from formal ASN.1 definitions, and a
code generator for pyasn1 is included.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
asn1ate is a Python library for translating ASN.1 into other forms. It
is intended for code generation from formal ASN.1 definitions, and a
code generator for pyasn1 is included.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
./basic_test.sh
%if_with python3
pushd ../python3
sed -i 's|python|python3|g' basic_test.sh
./basic_test.sh
popd
%endif

%files
%doc README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150314.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20150314.1
- NMU: Use buildreq for BR.

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150314
- Initial build for Sisyphus

