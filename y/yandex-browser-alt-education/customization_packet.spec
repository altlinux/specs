Name: yandex-browser-alt-education
Version: 1.0
Release: alt3

Summary: Yandex Browser addon for Alt Education
License: ALT-YANDEX-BROWSER
Group: Networking/WWW
Vendor: YANDEX LLC
Url: http://browser.yandex.ru/

ExclusiveArch: x86_64
Source0: customization_packet.tar

Requires: yandex-browser
Conflicts: yandex-browser-customisation, yandex-browser-customization

%description
Yandex Browser addon for Alt Education

The package is intended for installing the browser from scratch, or for profiles created after installing the package.

%description -l ru_RU.UTF-8
Пакет кастомизации Яндекс Браузера для Альт Образование

Пакет предназначен для установки браузера с нуля, или для созданных после установки пакета профилей.

%prep
%setup -n customization_packet

%build
cp -a . "%buildroot"

%files
%{_sharedstatedir}/yandex/browser-customization
%{_datadir}/appdata/yandex-browser-alt-education.appdata.xml

%changelog
* Thu Jun 20 2024 Vasiliy Tsukanov <palar@altlinux.org> 1.0-alt3
- updated description

* Fri Jun 14 2024 Vasiliy Tsukanov <palar@altlinux.org> 1.0-alt2
- review fixes

* Wed Jun  5 2024 Vasiliy Tsukanov <palar@altlinux.org> 1.0-alt1
- initial commit for ALT
