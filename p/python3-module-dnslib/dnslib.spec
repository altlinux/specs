%define _unpackaged_files_terminate_build 1
%define oname dnslib

Name: python3-module-%oname
Version: 0.9.7
Release: alt3

Summary: Simple library to encode/decode DNS wire-format packets
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/dnslib

Source: %{oname}-%{version}.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
A library to encode/decode DNS wire-format packets supporting both
Python 2.7 and Python 3.2+.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A library to encode/decode DNS wire-format packets supporting both
Python 2.7 and Python 3.2+.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' setup.py

%build
%python3_build_debug

%install
%python3_install

%check
VERSIONS=python3 ./run_tests.sh -v

%files
%doc README* PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*


%changelog
* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.7-alt3
- python2 disabled

* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.7-alt2
- Fixed build.

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus

