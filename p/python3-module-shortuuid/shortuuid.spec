%define _unpackaged_files_terminate_build 1
%define oname shortuuid

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: A generator library for concise, unambiguous and URL-safe UUIDs

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/shortuuid/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.1.3
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%py3_provides %oname

%description
A library that generates short, pretty, unambiguous unique IDs by using
an extensive, case-sensitive alphabet and omitting similar-looking
letters and numbers.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A library that generates short, pretty, unambiguous unique IDs by using
an extensive, case-sensitive alphabet and omitting similar-looking
letters and numbers.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install
%python3_prune

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%if_with pack_test
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Aug 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version (1.0.0) with rpmgs script
- cleanup spec, disable packing tests

* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt2.git20140426.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2.git20140426
- Disabled test_pep8 (broken with new pep8)

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20140426
- Initial build for Sisyphus

