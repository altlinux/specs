%define oname webencodings

%def_with python3

Name: python-module-%oname
Version: 0.5.1
Release: alt1.1

Summary: Character encoding aliases for legacy web content

License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/webencodings/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: https://pypi.io/packages/source/w/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
This is a Python implementation of the WHATWG Encoding standard.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is a Python implementation of the WHATWG Encoding standard.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Character encoding aliases for legacy web content
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is a Python implementation of the WHATWG Encoding standard.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is a Python implementation of the WHATWG Encoding standard.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 04 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- switch to build from tarball
- new version (0.5.1) with rpmgs script

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20131224.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20131224
- Initial build for Sisyphus

