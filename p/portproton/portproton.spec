%add_findreq_skiplist %_bindir/portproton
AutoProv: no

%define i586_req_l1 libvulkan.so.1 libGL.so.1 libgio-2.0.so.0 libnm.so.0 libnss3.so libunwind.so.8
%define i586_req_l2 libVkLayer_MESA_device_select.so libgamemodeauto.so.0 libnsl.so.1

Name: portproton
Version: 1.5
Release: alt2

Summary: Installer for PortProton

License: MIT
Group: Games/Other
Url: https://github.com/Castro-Fidel/PortProton_ALT

Source: %name-%version.tar

Requires: bubblewrap cabextract zstd gawk tar xz pciutils coreutils file
Requires: curl wmctrl xdg-utils desktop-file-utils yad
Requires: libvulkan1 vulkan-tools libd3d libGL gamemode fontconfig xrdb
Requires: libcurl libgio libnm libnsl1 libnss glibc-nss glibc-pthread
Requires: /usr/bin/convert exiftool icoextract-thumbnailer

# Requires 32-bit meta package:
# Requires: portproton-dependency

ExclusiveArch: i586 x86_64

%description
Installer PortProton for Windows games.

%package dependency
Group: Games/Other
Summary: Metapackage for installing 32-bit dependencies for PortProton.
ExclusiveArch: i586
Provides: %name-dependency
%description dependency
%summary

%prep
%setup

%build
%install
# 32-bit dependencies:
%ifarch i586
mkdir -p %buildroot%_libdir/%name
for lib in %i586_req_l1 %i586_req_l2 ; do
    ln -s /usr/lib/$lib %buildroot%_libdir/%name/
done
ln -s /usr/lib/d3d/d3dadapter9.so.1.0.0 %buildroot%_libdir/%name/
ln -s /usr/lib/vdpau/libvdpau_gallium.so.1.0.0 %buildroot%_libdir/%name/
# ln -s /lib/libpthread.so.0 %buildroot%_libdir/%name/
# ln -s /lib/libnss_dns.so.2 %buildroot%_libdir/%name/
%endif

%ifarch x86_64
install -Dm755 %name %buildroot%_bindir/%name
install -Dm644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm644 %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
%endif

%ifarch i586
%files dependency
%_libdir/%name
%endif

%ifarch x86_64
%files
%doc LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%endif

%changelog
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
