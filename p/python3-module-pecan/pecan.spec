%define oname pecan

Name: python3-module-%oname
Version: 1.5.1
Release: alt1

Summary: A lean WSGI object-dispatching web framework

Group: Development/Python3
License: BSD-3-Clause
Url: http://github.com/pecan/pecan

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-webob >= 1.8
BuildRequires: python3-module-mako >= 0.4.0
BuildRequires: python3-module-webtest >= 1.3.1
BuildRequires: python3-module-logutils >= 0.3

Requires: python3-module-logutils >= 0.3
Requires: python3-module-webob >= 1.2
Requires: python3-module-mako >= 0.4.0

%description
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

rm -rf %buildroot%python3_sitelibdir/%oname/tests/config_fixtures/bad

%files
%doc LICENSE README.rst
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/*/testing.py
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/+package+/tests

%files tests
%python3_sitelibdir/*/testing.py
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/+package+/tests

%changelog
* Mon Jul 17 2023 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1
- Automatically updated to 1.5.1.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Automatically updated to 1.4.2.

* Tue May 24 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Build new version.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 1.4.0-alt2
- Dropped dependency on singledispatch(removed from Sisyphus).

* Tue Sep 15 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Build new version.

* Tue Jul 28 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt2
- Drop python2 support.

* Wed Jan 22 2020 Alexey Shabalin <shaba@altlinux.org> 1.3.3-alt1
- 1.3.3
- update requires

* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 1.3.2-alt2
- Dropped dependency on python argparse (use stdlib's one).

* Fri Jan 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.2-alt1
- 1.3.2
- add tests packages

* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt2.1
- NMU: Use buildreq for BR.

* Mon Nov 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt2
- update R:

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- 1.0.3
- add python3 package
- delete tests

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4.5-alt1
- First build for ALT (based on Fedora 0.4.5-4.fc21)

