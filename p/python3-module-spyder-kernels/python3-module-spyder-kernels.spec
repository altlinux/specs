%def_without test

Name: python3-module-spyder-kernels
Version: 2.4.2
Release: alt1

License: MIT
Group: Development/Python
Url: https://github.com/spyder-ide/spyder-kernels

Summary: Jupyter Kernels for the Spyder console

# Source-url: https://github.com/spyder-ide/spyder-kernels/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

BuildRequires: python3-module-cloudpickle python3-module-flaky

%description
Package that provides Jupyter kernels for use with the consoles of Spyder,
the Scientific Python Development Environment.

These kernels can launched either through Spyder itself
or in an independent Python session, and allow for interactive
or file-based execution of Python code inside Spyder.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if_with test
%check
%python3_test
%endif

%files
%python3_sitelibdir/*

%changelog
* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)

* Sun Sep 11 2022 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (with rpmrb script)

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- new version 2.3.2 (with rpmrb script)

* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script)

* Tue Jun 08 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script)

* Mon Apr 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.10.2-alt1
- new version 1.10.2 (with rpmrb script)

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1.10.1-alt1
- new version 1.10.1 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt1
- new version 1.9.4 (with rpmrb script)

* Tue Feb 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- initial build for ALT Sisyphus
