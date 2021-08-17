Name: panzerchasm
Version: 0.3
Release: alt1

Summary: Free software reconstruction of game "Chasm: The Rift"
License: GPL-3.0-only
Group: Games/Arcade

Url: https://github.com/Panzerschrek/Chasm-Reverse

Packager: Artyom Bystrov <arbars@altlinux.org>

Source0: %name-%version.tar
Source1: panzerchasm-wrapper.sh

Patch0: in_udp_port.patch

BuildRequires(pre): ImageMagick-tools

BuildRequires: cmake rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: libSDL2-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel

%description
"PanzerChasm" is a free software reconstruction
of game "Chasm: The Rift" by "ActionForms",
see https://en.wikipedia.org/wiki/Chasm:_The_Rift.

NOTE: To play Chasm with PanzerChasm you need the CSM.BIN file
from your GOG/Steam/CD-ROM installation of the game.
Demo files are not supported.
You have to put them under '~/.config/panzerchasm/'.

%prep
%setup -n %name-%version

%patch0 -p1

%build

mkdir BUILD
cd BUILD
cmake ..
%make


%install 

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=PanzerChasm
Comment=Free software reconstruction of game "Chasm: The Rift"
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Games/Arcade;
EOF

mkdir -p %buildroot%_iconsdir

install -D -m0755 BUILD/PanzerChasm/PanzerChasm %{buildroot}/%{_libexecdir}/%{name}/%{name}
install -D -m0755 %{SOURCE1} %{buildroot}/%{_bindir}/%{name}
install -D -m0644 PanzerChasm/PanzerChasm.ico %buildroot%_iconsdir/%name.ico

%files

%doc README.md docs/* PanzerChasm/readme.txt
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name
%_iconsdir/%name.ico
%_desktopdir/%name.desktop

%changelog
* Thu Jan 07 2021 Artyom Bystrov <arbars@altlinux.org> 0.3-alt1
- initial build for ALT Sisyphus
