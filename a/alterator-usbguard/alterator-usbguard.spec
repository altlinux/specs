%define _altdata_dir %_datadir/alterator

Name: alterator-usbguard
Version: 0.1.1
Release: alt1
Summary: alterator module to control usb devices
Group: System/Configuration/Other
License: %gpl2plus
Url: https://gitlab.basealt.space/proskurinov/alterator_usbguard

Source: %name-%version.tar
Source1: %name-%version-thirdparty-cppcodec.tar
Source2: %name-%version-thirdparty-rapidcsv.tar

Requires: usbids usbguard alterator
BuildPreReq: gcc-c++ cmake ninja-build rpm-macros-cmake rpm-build-licenses 

BuildRequires: usbguard-devel libusbguard1 boost-devel-headers  libsdbus-cpp-devel libsystemd-devel gettext-tools


%description
Alterator Module to control USB devices via USBGuard.

%prep
%setup -a0 -a1 -a2  

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release -DUSBGUARD=1 -G Ninja
%cmake_build

%install
%cmake_install --config Release

%files
%_altdata_dir/applications/USBGuard.desktop
%_altdata_dir/design/scripts/alt-usb-guard.js
%_altdata_dir/design/styles/alt_usb_guard.css
%_altdata_dir/ui/usbguard/ajax.scm
%_altdata_dir/ui/usbguard/index.html
%_altdata_dir/help/ru_RU/usbguard.html
%_usr/lib/alterator/backend3/usbguard
%_sysconfdir/usbguard/android_vidpid.json
%lang(ru)  %_datadir/locale/ru/LC_MESSAGES/alterator-usbguard.mo


%changelog
* Tue May 07 2024 Oleg Proskurin <proskur@altlinux.org> 0.1.1-alt1
- New version

* Mon Mar 04 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build
