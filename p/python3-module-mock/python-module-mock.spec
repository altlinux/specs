%define _unpackaged_files_terminate_build 1
%define oname mock

%def_with check

Name: python3-module-mock
Version: 4.0.3
Release: alt2

Summary: A Python Mocking and Patching Library for Testing

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/mock

# Source-url: %__pypi_url %oname
Source: %name-%version.tar
Patch: mock-4.0.3-fix-tests-that-should-test-mock-but-were-testing-uni.patch

BuildArch: noarch

BuildRequires(pre):  rpm-build-intro >= 2.2.5
BuildRequires(pre):  rpm-build-python3
BuildRequires: python3-module-pbr python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
mock is a library for testing in Python.
It allows you to replace parts of your system under test with mock objects
and make assertions about how they have been used.

mock is now part of the Python standard library,
available as unittest.mock in Python 3.3 onwards.

This package contains a rolling backport of the standard library mock code
compatible with Python 3.6 and up.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install
%python3_prune

%check
export PYTHONPATH=$(pwd)
py.test3 -vv

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Sat Mar 05 2022 Stanislav Levin <slev@altlinux.org> 4.0.3-alt2
- Fixed FTBFS (Python 3.10).

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- new version 4.0.3 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- build python3 package separately, cleanup spec

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.git20150731.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1.git20150731.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20150731
- Snapshot from git

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Fri Aug 29 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt2
- Rebuild with Python-2.7

* Mon Oct 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Mon Mar 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt1
- Initial
