%define oname uharfbuzz

%def_with check

Name:     python3-module-%oname
Version:  0.53.4
Release:  alt1

Summary:  An opinionated HarfBuzz Python binding

License:  Apache-2.0
Group:    Development/Python3
URL:      https://pypi.org/project/uharfbuzz
VCS:      https://github.com/harfbuzz/uharfbuzz

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++
BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-pkgconfig
BuildRequires: libharfbuzz-devel

%description
%summary.

%prep
%setup

%build
export USE_SYSTEM_LIBS=1
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sat Mar 28 2026 Grigory Ustinov <grenka@altlinux.org> 0.53.4-alt1
- Automatically updated to 0.53.4.

* Fri Jan 30 2026 Grigory Ustinov <grenka@altlinux.org> 0.53.3-alt1
- Automatically updated to 0.53.3.

* Sun Jan 18 2026 Grigory Ustinov <grenka@altlinux.org> 0.53.2-alt1
- Automatically updated to 0.53.2.

* Fri Oct 17 2025 Grigory Ustinov <grenka@altlinux.org> 0.51.7-alt1
- Build new version.

* Fri Aug 22 2025 Grigory Ustinov <grenka@altlinux.org> 0.51.2-alt1
- Build new version.

* Sun Aug 03 2025 Grigory Ustinov <grenka@altlinux.org> 0.51.1-alt1
- Build new version.

* Thu May 15 2025 Grigory Ustinov <grenka@altlinux.org> 0.50.2-alt1
- Build new version.

* Wed Apr 30 2025 Grigory Ustinov <grenka@altlinux.org> 0.50.0-alt1
- Build new version.

* Fri Apr 11 2025 Grigory Ustinov <grenka@altlinux.org> 0.49.0-alt1
- Build new version.
- Build with system harfbuzz.

* Wed Mar 12 2025 Grigory Ustinov <grenka@altlinux.org> 0.46.0-alt1
- Build new version.

* Mon Jan 20 2025 Grigory Ustinov <grenka@altlinux.org> 0.45.0-alt1
- Build new version.

* Wed Jan 01 2025 Grigory Ustinov <grenka@altlinux.org> 0.44.0-alt1
- Build new version.

* Wed Nov 27 2024 Grigory Ustinov <grenka@altlinux.org> 0.43.0-alt1
- Build new version.

* Wed Nov 06 2024 Grigory Ustinov <grenka@altlinux.org> 0.42.0-alt1
- Build new version.

* Mon Nov 04 2024 Grigory Ustinov <grenka@altlinux.org> 0.41.1-alt1
- Build new version.

* Tue Oct 01 2024 Grigory Ustinov <grenka@altlinux.org> 0.41.0-alt1
- Build new version.

* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 0.39.1-alt1
- Build new version.

* Mon Dec 04 2023 Grigory Ustinov <grenka@altlinux.org> 0.37.3-alt1
- Build new version.

* Fri Sep 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.30.0-alt1
- Initial build for Sisyphus.
- Build with bundled libharfbuzz, because aris@ dont want to enable
  experimental api in "his own" system libharfbuzz, and this package
  uses lots of it. See more here: https://bugzilla.altlinux.org/43094
