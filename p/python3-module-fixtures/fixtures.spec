%global oname fixtures

%def_with check

Name: python3-module-%oname
Version: 4.1.0
Release: alt1

Summary: Fixtures, reusable state for writing clean tests and more

License: Apache-2.0 or BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/fixtures

# https://github.com/testing-cabal/fixtures
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr

%if_with check
BuildRequires: python3-module-testtools
%endif

%description
Fixtures defines a Python contract for reusable state / support logic,
primarily for unit testing. Helper and adaption logic is included to
make it easy to write your own fixtures using the fixtures contract.
Glue code is provided that makes using fixtures that meet the Fixtures
contract in unittest compatible test cases easy and straight forward.

%prep
%setup

%build
export PBR_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst GOALS NEWS Apache-2.0 BSD COPYING
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Jun 13 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Build new version.
- Build with check.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt3
- Fixed BuildRequires.

* Tue Apr 27 2021 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt2
- build python3 module separately
- set requires from requirements.txt

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 1.3.1-alt2
- Rebuild with "def_disable check"
- Clean buildreq

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3.14-alt1
- First build for ALT (based on Fedora 0.3.14-3.fc21.src)
