%define  oname radon

%def_with check

Name:    python3-module-%oname
Version: 6.0.1
Release: alt1

Summary: Various code metrics for Python code

License: MIT
Group:   Development/Python3
URL:     https://github.com/rubik/radon

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-tox python3-module-mando
BuildRequires: python3-module-flake8-polyfill python3-module-pytest-mock
%endif

BuildArch: noarch

Source:  %oname-%version.tar

%description
Radon is a Python tool that computes various metrics from the source code.
Radon can compute:

* McCabe's complexity**, i.e. cyclomatic complexity
* raw metrics (these include SLOC, comment lines, blank lines, &c.)
* Halstead metrics (all of them)
* Maintainability Index (the one used in Visual Studio)

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%check
export LANG=en_US.UTF-8
py.test3 -vv

%files
%doc CHANGELOG README.rst
%_bindir/radon
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info/
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Mon Mar 27 2023 Grigory Ustinov <grenka@altlinux.org> 6.0.1-alt1
- Automatically updated to 6.0.1.

* Mon Aug 09 2021 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Automatically updated to 5.1.0.

* Fri Jun 18 2021 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt1
- Automatically updated to 5.0.1.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 4.5.2-alt1
- Automatically updated to 4.5.2.

* Wed May 12 2021 Grigory Ustinov <grenka@altlinux.org> 4.5.1-alt1
- Automatically updated to 4.5.1.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1
- Automatically updated to 4.5.0.

* Mon Sep 21 2020 Grigory Ustinov <grenka@altlinux.org> 4.3.2-alt1
- Automatically updated to 4.3.2.

* Sun Sep 13 2020 Grigory Ustinov <grenka@altlinux.org> 4.3.1-alt1
- Automatically updated to 4.3.1.

* Wed Aug 26 2020 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Automatically updated to 4.2.0.

* Wed Feb 12 2020 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Build new version.
- Add test subpackage.
- Add check section.

* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.0.0-alt2
- build for python2 disabled

* Mon Sep 23 2019 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Build new version.

* Mon May 20 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.3-alt1
- Build new version.

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus.
