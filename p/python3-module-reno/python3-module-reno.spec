%define        pypiname reno
%def_disable   check
%def_disable   doc

Name:          python3-module-%pypiname
Version:       4.0.0
Release:       alt2
Summary:       RElease NOtes manager
License:       Apache-2.0
Group:         Development/Python3
Url:           https://opendev.org/openstack/reno
Vcs:           https://opendev.org/openstack/reno.git
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel)
BuildRequires: python3-module-pbr >= 1.4
BuildRequires: python3-module-yaml >= 3.10.0
BuildRequires: python3-module-packaging >= 20.4
%if_enabled    check
BuildRequires: gpg
BuildRequires: python3(pytest-cov)
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-dulwich >= 0.15.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 1.4.0
%endif
%if_enabled    doc
BuildRequires: python3(sphinx)
BuildRequires: python3-module-openstackdocstheme >= 2.2.1
%endif

%description
Reno is a release notes manager for storing
release notes in a git repository and then building documentation from them.

Managing release notes for a complex project over a long period
of time with many releases can be time consuming and error prone. Reno
helps automate the hard parts.

%package       tests
Summary:       Tests for %pypiname
Group:         Development/Python3
Requires:      %name = %EVR

%description   tests
This package contains tests for %pypiname.

%if_enabled    doc
%package       doc
Summary:       Documentation for %pypiname
Group:         Development/Documentation

%description   doc
This package contains documentation for %pypiname.
%endif

%prep
%setup
%autopatch -p1

%build
export PBR_VERSION=%version
%pyproject_build

%if_enabled    doc
export PYTHONPATH="$PWD"
sphinx-build-3 doc/source html
sphinx-build-3 -b man doc/source man
%endif

%install
%pyproject_install
%{?!_disable_doc:install -pDm 644 man/%pypiname.1 %buildroot%_man1dir/%pypiname.1}

%check
%pyproject_run_unittest
%pyproject_run_pytest

%files
%doc LICENSE *.rst
%_bindir/%pypiname
%python3_sitelibdir/%pypiname
%python3_sitelibdir/%pypiname-%version.dist-info
%exclude %python3_sitelibdir/%pypiname/tests

%files         tests
%doc LICENSE *.rst
%python3_sitelibdir/%pypiname/tests

%if_enabled    doc
%files         doc
%doc LICENSE *.rst
%doc html
%_man1dir/%pypiname.1.xz
%endif

%changelog
* Tue Feb 06 2024 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt2
- * revert removed required for other packages

* Mon May 15 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.

* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1.1
- Moved on modern pyproject macros.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Automatically updated to 3.5.0.
- Renamed spec file.

* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Build new version.

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- NMU: new version 3.2.0 (with rpmrb script)

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 2.11.3-alt1
- Automatically updated to 2.11.3.
- Build without python2.

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 2.11.2-alt1
- 2.11.2

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.2-alt1
- 1.6.2
- add git to requires

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial Package
