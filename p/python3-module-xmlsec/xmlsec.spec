%define oname xmlsec

%def_with check

Name: python3-module-%oname
Version: 1.3.17
Release: alt3

Summary: Python bindings for the XML Security Library

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/xmlsec
VCS: https://github.com/mehcode/python-xmlsec

Source: %name-%version.tar

# xmlsec 1.3.11 support
Patch: 5e8b4e6aa133c358b8aaf8e17ceb5b3b7fea78e8.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libxmlsec1-openssl-devel
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pkgconfig
BuildRequires: python3-module-lxml

%description
%summary.

%prep
%setup
%patch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README* LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname.*.so
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Apr 28 2026 Grigory Ustinov <grenka@altlinux.org> 1.3.17-alt3
- Fixed tests with xmlsec 1.3.11.

* Mon Jan 26 2026 Grigory Ustinov <grenka@altlinux.org> 1.3.17-alt2
- Built with check.

* Mon Jan 19 2026 Grigory Ustinov <grenka@altlinux.org> 1.3.17-alt1
- Automatically updated to 1.3.17.

* Thu Jul 24 2025 Grigory Ustinov <grenka@altlinux.org> 1.3.16-alt1
- Automatically updated to 1.3.16.

* Mon Mar 10 2025 Grigory Ustinov <grenka@altlinux.org> 1.3.15-alt1
- Automatically updated to 1.3.15.

* Wed Nov 13 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.14-alt2
- Fixed FTBFS.

* Fri Apr 19 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.14-alt1
- Automatically updated to 1.3.14.

* Wed Mar 29 2023 Grigory Ustinov <grenka@altlinux.org> 1.3.13-alt1
- Build new version.

* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.6-alt2
- build for python2 disabled

* Sun Jan 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt1
- Build new version.

* Tue May 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt2
- NMU: Add URL (Closes: #34693).

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 1.3.3-alt1
- Autobuild version bump to 1.3.3
- Introduce documentation

* Wed Jul 27 2016 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Fresh build from Pypi
- Thanks real@ for old python-module-mehcode-xmlsec

