%define oname webencodings

Name: python3-module-%oname
Version: 0.5.1
Release: alt2

Summary: Character encoding aliases for legacy web content
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/webencodings/

BuildArch: noarch

# Source-url: https://pypi.io/packages/source/w/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_provides %oname


%description
This is a Python implementation of the WHATWG Encoding standard.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This is a Python implementation of the WHATWG Encoding standard.

This package contains tests for %oname.

%prep
%setup

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug

%install
export LC_ALL=en_US.UTF-8
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5.1-alt2
- Build for python2 disabled.

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

