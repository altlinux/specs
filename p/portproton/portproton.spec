Name: portproton
Version: 1.0
Release: alt3

Summary: Installer for PortProton

License: MIT
Group: Games/Other
Url: https://github.com/Castro-Fidel/PortWINE

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://github.com/Castro-Fidel/PortWINE/raw/master/portwine_install_script/PortProton_%version
Source1: https://github.com/Castro-Fidel/PortWINE/raw/master/data_from_portwine/img/gui/port_proton.png
Source2: https://raw.githubusercontent.com/Castro-Fidel/PortProton_dpkg/main/usr/share/applications/portproton.desktop

Requires: libvulkan1 vulkan-tools libd3d libMesaOpenCL
Requires: bubblewrap cabextract curl wget zstd gawk tar xz wget fontconfig xrdb pciutils bc coreutils file gamemode
Requires: icoutils wmctrl zenity xdg-utils desktop-file-utils
Requires: /usr/bin/convert

ExclusiveArch: x86_64

%description
Installer PortProton for Windows games.


%prep

%build

%install
mkdir -p %buildroot%_desktopdir

install -m755 -D %SOURCE0 %buildroot%_bindir/%name
install -m644 -D %SOURCE1 %buildroot%_pixmapsdir/%name.png
install -m644 -D %SOURCE2 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
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

