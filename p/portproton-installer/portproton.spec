%add_findreq_skiplist %_bindir/portproton
AutoProv: no

%define oname portproton
%define xdg_name ru.linux_gaming.PortProton

%define i586_req_l1 libvulkan.so.1 libGL.so.1 libgio-2.0.so.0 libnm.so.0 libnss3.so libunwind.so.8
%define i586_req_l2 libVkLayer_MESA_device_select.so libgamemodeauto.so.0 libnsl.so.1

Name: portproton-installer
Version: 1.7.0
Release: alt2

Summary: Installer for PortProton

License: MIT
Group: Games/Other
Url: https://github.com/Castro-Fidel/PortProton_ALT

Source: %name-%version.tar

Requires: bubblewrap cabextract zstd gawk tar xz pciutils coreutils file
Requires: curl wmctrl xdg-utils desktop-file-utils yad jq
Requires: libvulkan1 vulkan-tools libd3d libGL gamemode fontconfig xrdb
Requires: libcurl libgio libnm libnsl1 libnss glibc-nss glibc-pthread
Requires: /usr/bin/convert /usr/bin/exiftool /usr/bin/icoextract

ExclusiveArch: i586

Provides: portproton = %version-%release
Obsoletes: portproton <= 1.6.1-alt2

%description
Installer PortProton for Windows games.

%prep
%setup

%build
%install
mkdir -p %buildroot%_libdir/%oname
for lib in %i586_req_l1 %i586_req_l2 ; do
    ln -s /usr/lib/$lib %buildroot%_libdir/%oname/
done
ln -s /usr/lib/vdpau/libvdpau_gallium.so.1.0.0 %buildroot%_libdir/%oname/
# ln -s /usr/lib/d3d/d3dadapter9.so.1.0.0 %buildroot%_libdir/%oname/
# ln -s /lib/libpthread.so.0 %buildroot%_libdir/%oname/
# ln -s /lib/libnss_dns.so.2 %buildroot%_libdir/%oname/

install -Dm755 %oname %buildroot%_bindir/%oname
install -Dm644 %xdg_name.desktop %buildroot%_desktopdir/%xdg_name.desktop
install -Dm644 %xdg_name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
install -Dm644 %xdg_name.metainfo.xml %buildroot%_datadir/metainfo/%xdg_name.metainfo.xml

%files
%doc LICENSE
%_bindir/%oname
%_libdir/%oname
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_datadir/metainfo/%xdg_name.metainfo.xml

%changelog
* Wed Jul 17 2024 Mikhail Tergoev <fidel@altlinux.org> 1.7.0-alt2
- added requires jq for SteamGridDB

* Sun Jul 14 2024 Mikhail Tergoev <fidel@altlinux.org> 1.7.0-alt1
- updated to 1.7.0

* Sat Jul 13 2024 Mikhail Tergoev <fidel@altlinux.org> 1.6.2-alt1
- updated to 1.6.2

* Mon Jun 24 2024 Mikhail Tergoev <fidel@altlinux.org> 1.6.1-alt3
- renamed package to arepo portproton-installer (thanks glebfm@ and egori@)
- fixed automatic installation of 32 bit dependencies (ALT bug: 49278)
- dropped i586-portproton-dependency package

* Fri Jun 14 2024 Mikhail Tergoev <fidel@altlinux.org> 1.6.1-alt2
- fix build for branch p10

* Fri Jun 14 2024 Mikhail Tergoev <fidel@altlinux.org> 1.6.1-alt1
- updated to v1.6.1
- added metainfo

* Thu Jun 13 2024 Mikhail Tergoev <fidel@altlinux.org> 1.5-alt2
- added meta package for installation 32-bit dependencies

* Tue Feb 13 2024 Mikhail Tergoev <fidel@altlinux.org> 1.5-alt1
- updated to v1.5
- drop requires: libMesaOpenCL

* Fri Feb 09 2024 Mikhail Tergoev <fidel@altlinux.org> 1.4-alt1
- updated to v1.4
- update requires
- drop meta package 32-bit dependencies (it does not work as intended)

* Sun Dec 24 2023 Mikhail Tergoev <fidel@altlinux.org> 1.3-alt2
- added meta package for installation 32-bit dependencies
- update requires

* Fri Nov 24 2023 Mikhail Tergoev <fidel@altlinux.org> 1.3-alt1
- updated to v1.3

* Sat Nov 11 2023 Mikhail Tergoev <fidel@altlinux.org> 1.2-alt1
- updated to v1.2
- updated icon file (png to svg)

* Fri Nov 10 2023 Mikhail Tergoev <fidel@altlinux.org> 1.1-alt1
- updated to v1.1
- added gitlab.eterfund.ru for download scripts
- added installation path selection
- update desktop file

* Fri May 19 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt3
- install .desktop as a file
- add requires: fontconfig xrdb pciutils xdg-utils bc coreutils file desktop-file-utils wmctrl xz wget

* Sun Apr 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- fix Exec in desktop file
- add requires: gawk tar libd3d libMesaOpenCL /usr/bin/convert

* Sat Apr  1 2023 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1.1
- Add MimeType description in desktop file

* Mon Mar 20 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
