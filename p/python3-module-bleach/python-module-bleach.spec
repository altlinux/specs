%def_without check

%define modulename bleach

Name: python3-module-bleach
Version: 4.1.0
Release: alt1

Summary: An easy whitelist-based HTML-sanitizing tool

Url: http://github.com/jsocol/bleach
License: ASL 2.0
Group: Development/Python3


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mozilla/bleach/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools

%description
Bleach is an HTML sanitizing library that escapes or strips markup and
attributes based on a white list.


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*


%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- new version 4.1.0 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- new version 3.3.0 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt2
- build python3 module separately

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.3-alt1.qa1
- NMU: applied repocop patch

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version 2.1.3 (with rpmrb script)

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- initial build for ALT Sisyphus

