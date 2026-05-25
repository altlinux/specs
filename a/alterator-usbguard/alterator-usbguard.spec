%define _unpackaged_files_terminate_build 1
%define _altdata_dir %_datadir/alterator

Name: alterator-usbguard
Version: 0.2.4
Release: alt1

Summary: alterator module to control usb devices
Group: System/Configuration/Other
License: GPL-2.0-or-later
Url: https://gitlab.basealt.space/proskurinov/alterator_usbguard
VCS: https://gitlab.basealt.space/proskurinov/alterator_usbguard.git

Source: %name-%version.tar
Source2: %name-%version-thirdparty-rapidcsv.tar

BuildRequires(pre): rpm-macros-cmake
BuildPreReq: gcc-c++ cmake ninja-build
BuildRequires: usbguard-devel libusbguard1 boost-devel-headers cppcodec-devel
BuildRequires: libsdbus-cpp-devel libsystemd-devel gettext-tools

Requires: usbids usbguard alterator

%description
Alterator Module to control USB devices via USBGuard.

%prep
%setup -a0 -a2

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release -DUSBGUARD=1 -G Ninja
%cmake_build

%install
%cmake_install --config Release

%find_lang alterator-usbguard

%files -f alterator-usbguard.lang
%_altdata_dir/applications/USBGuard.desktop
%_altdata_dir/design/scripts/alt-usb-guard.js
%_altdata_dir/design/styles/alt_usb_guard.css
%_altdata_dir/ui/usbguard/ajax.scm
%_altdata_dir/ui/usbguard/index.html
%_altdata_dir/help/ru_RU/usbguard.html
%_usr/lib/alterator/backend3/usbguard
%_sysconfdir/usbguard/android_vidpid.json

%changelog
* Mon May 25 2026 Oleg Proskurin <proskur@altlinux.org> 0.2.4-alt1
- New Version
  + Use C++20 compiler by default
  + Remove the bundled cppcodec

* Mon Dec 29 2025 Oleg Proskurin <proskur@altlinux.org> 0.2.3-alt2
- Fix major mistakes in the .spec file.

* Wed Mar 26 2025 Oleg Proskurin <proskur@altlinux.org> 0.2.3-alt1
- Port to sdbus-c++ 2.1.0-alt1 aka libsdbus-cpp2

* Fri Feb 14 2025 Oleg Proskurin <proskur@altlinux.org> 0.2.2-alt1
- Translate the module title (Closes: #52833)

* Thu Jan 23 2025 Oleg Proskurin <proskur@altlinux.org> 0.2.1-alt1
- Bugfixing (Closes: #52767, #52745)
  + fix jump back (-10)
  + fix empty page at the end problem

* Wed Jan 15 2025 Oleg Proskurin <proskur@altlinux.org> 0.2-alt1
- New version (Closes: #51764 )

* Fri May 17 2024 Oleg Proskurin <proskur@altlinux.org> 0.1.2-alt1
- Fix usb interface rule validation

* Mon May 13 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.1.1-alt2
- e2k build fix

* Tue May 07 2024 Oleg Proskurin <proskur@altlinux.org> 0.1.1-alt1
- New version

* Mon Mar 04 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build
