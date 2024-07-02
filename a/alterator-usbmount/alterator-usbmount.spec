%define _altdata_dir %_datadir/alterator

Name: alterator-usbmount
Version: 0.1.1
Release: alt1
Summary: Alterator module to control mountpoints of USB block devices
Group: System/Configuration/Other
License: %gpl2plus
Url: https://gitlab.basealt.space/proskurinov/alterator_usbmount

Source: %name-%version.tar

Requires: alterator %name-daemon
BuildPreReq: gcc-c++ cmake ninja-build rpm-macros-cmake rpm-build-licenses 

BuildRequires: boost-devel-headers libsdbus-cpp-devel libsystemd-devel gettext-tools 
BuildRequires: libudev-devel libacl-devel libspdlog-devel libfmt-devel

%description
Alterator module to control mountpoints of USB block devices.

%package daemon
Summary: The usbmount-daemon contains a systemd service to apply mount policies
Group: System/Configuration/Hardware
Requires: dbus polkit
%description daemon
The usbmount-daemon contains a systemd service to apply mount policies

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release -DUSBMOUNT=1 -G Ninja -DUNITDIR=%_unitdir
%cmake_build

%install

%cmake_install --config Release
%__mkdir -p %buildroot%_logdir/alt-usb-automount 

%files
%_usr/lib/alterator/backend3/usbmount
%_altdata_dir/applications/USBMount.desktop
%_altdata_dir/design/scripts/alt_usb_mount.js
%_altdata_dir/design/styles/alt_usb_mount.css
%_altdata_dir/ui/usbmount/ajax.scm
%_altdata_dir/ui/usbmount/index.html
%_altdata_dir/help/ru_RU/usbmount.html
%lang(ru) %_datadir/locale/ru/LC_MESSAGES/alterator-usbmount.mo

%files daemon
%_sysconfdir/polkit-1/rules.d/alt-usb-mount.rules
%_datadir/dbus-1/system.d/ru.alterator.usbd.conf
%_usr/libexec/altusbmount_askdbus
%_unitdir/altusbd.service
%_sbindir/altusbd
%dir %_logdir/alt-usb-automount/

%changelog
* Tue Jul 02 2024 Oleg Proskurin <proskur@altlinux.org> 0.1.1-alt1
- Bugfixing (Closes: #50666, #50604, #50665 )

* Thu Jun 06 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt2
- Add Help File

* Tue May 07 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build
