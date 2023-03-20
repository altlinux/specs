Name: portproton
Version: 1.0
Release: alt1

Summary: Installer for PortProton

License: MIT
Group: Games/Other
Url: https://github.com/Castro-Fidel/PortWINE

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://github.com/Castro-Fidel/PortWINE/raw/master/portwine_install_script/PortProton_%version
Source1: https://github.com/Castro-Fidel/PortWINE/raw/master/data_from_portwine/img/gui/port_proton.png

Requires: bubblewrap cabextract curl gamemode icoutils libvulkan1 vulkan-tools wget zenity zstd

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
Exec=%name %F
Icon=%name
StartupNotify=false
Terminal=false
Categories=Game;
EOF

install -m755 -D %SOURCE0 %buildroot%_bindir/%name
install -m644 -D %SOURCE1 %buildroot%_pixmapsdir/%name.png

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Mon Mar 20 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus

