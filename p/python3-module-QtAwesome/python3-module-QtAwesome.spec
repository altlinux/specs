Name: python3-module-QtAwesome
Version: 1.2.2
Release: alt1

License: MIT
Group: Development/Python
Url: https://github.com/spyder-ide/qtawesome

Summary: Iconic fonts in PyQt and PySide applications

# Source-url: https://github.com/spyder-ide/qtawesome/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

%description
QtAwesome enables iconic fonts such as Font Awesome and Elusive Icons in PyQt and PySide applications.

It started as a Python port of the QtAwesome C++ library by Rick Blommers.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/*

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Mon Apr 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.3-alt1
- new version 0.7.3 (with rpmrb script)

* Thu Jul 30 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.2-alt1
- new version (0.7.2)

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version (0.6.1) with rpmgs script

* Fri Jan 31 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.6-alt1
- initial build for ALT Sisyphus (python3 version)
