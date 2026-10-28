%define modulename dukpy

%def_with check

Name: python3-module-dukpy
Version: 0.6.0
Release: alt1.1

Summary: Simple JavaScript interpreter for Python

License: MIT License
Group: Development/Python3
URL: https://pypi.org/project/dukpy
VCS: https://github.com/amol-/dukpy

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mock
BuildRequires: python3-module-webassets
BuildRequires: python3-module-mutf8
%endif

%description
DukPy is a simple JavaScript interpreter for Python built on QuickJS.
It also provides common transpilers and WebAssets filters.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# These files confuse pytest
rm -rv dukpy
# TestPackageInstaller needs internet connection
%pyproject_run_pytest -k 'not TestPackageInstaller'

%files
%_bindir/%modulename
%_bindir/%modulename-install
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Wed Oct 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1.1
- New version 0.6.0.
- Drop BuildRequires: libduktape-devel; upstream now uses QuickJS.
- Move rpm-build-python3 to BuildRequires for build tools.

* Wed Oct 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- New version 0.6.0.
- Switch to QuickJS engine.
- Drop BuildRequires: libduktape-devel; upstream now uses QuickJS.
- Drop obsolete webassets test patch.
- Fix package build rules.

* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1.1
- NMU: fix tests with webassets 3.0.
- Package dukpy-install.

* Tue Jul 16 2024 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt1
- Automatically updated to 0.4.0.

* Fri May 24 2024 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt1
- Build new version.

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.2-alt2
- Build for python2 disabled.

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- new version 0.2.2 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2.qa1
- NMU: applied repocop patch

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.1.0-alt2
- Rebuild for aarch64

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 02 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial build for ALT Sisyphus

