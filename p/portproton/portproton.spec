Name: portproton
Version: 1.0
Release: alt2

Summary: Installer for PortProton

License: MIT
Group: Games/Other
Url: https://github.com/Castro-Fidel/PortWINE

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://github.com/Castro-Fidel/PortWINE/raw/master/portwine_install_script/PortProton_%version
Source1: https://github.com/Castro-Fidel/PortWINE/raw/master/data_from_portwine/img/gui/port_proton.png

Requires: bubblewrap cabextract curl gamemode icoutils libvulkan1 vulkan-tools wget zenity zstd gawk tar libd3d libMesaOpenCL
Requires: /usr/bin/convert

ExclusiveArch: x86_64

%description
Installer PortProton for Windows games.


%prep

%build

%install
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Type=Application
Name=PortProton
Name[ru]=PortProton
Comment=Installer PortProton for Windows games
Comment[ru]=Установщик PortProton для Windows игр
Exec=%name %%F
Icon=%name
StartupNotify=false
Terminal=false
Categories=Game;
MimeType=application/x-wine-extension-msp;application/x-msi;application/x-ms-dos-executable;
EOF

install -m755 -D %SOURCE0 %buildroot%_bindir/%name
install -m644 -D %SOURCE1 %buildroot%_pixmapsdir/%name.png

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Sun Apr 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- fix Exec in desktop file
- add requires: gawk tar libd3d libMesaOpenCL /usr/bin/convert

* Sat Apr  1 2023 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1.1
- Add MimeType description in desktop file

* Mon Mar 20 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus

