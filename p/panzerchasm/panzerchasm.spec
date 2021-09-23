Name: panzerchasm
Version: 0.3
Release: alt2

Summary: Free software reconstruction of game "Chasm: The Rift"
License: GPL-3.0-only
Group: Games/Arcade

Url: https://github.com/Panzerschrek/Chasm-Reverse

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source1: panzerchasm-wrapper.sh

Patch0: in_udp_port.patch

# Adding <limits> to headers in map_bsp_tree.cpp, thanks to:
# https://github.com/onnx/onnx-tensorrt/issues/474
Patch1: add_limits.patch
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
%patch1 -p1

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

install -D -m0755 BUILD/PanzerChasm/PanzerChasm %buildroot/%_libexecdir/%name/%name
install -D -m0755 %SOURCE1 %buildroot/%_bindir/%name
install -D -m0644 PanzerChasm/PanzerChasm.ico %buildroot%_iconsdir/%name.ico

%files
%doc README.md docs/* PanzerChasm/readme.txt
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name
%_iconsdir/%name.ico
%_desktopdir/%name.desktop

%changelog
* Thu Sep 23 2021 Artyom Bystrov <arbars@altlinux.org> 0.3-alt2
- Add patch for adding <limits> headers in map_bsp_tree source file
- fix build on new GCC

* Thu Jan 07 2021 Artyom Bystrov <arbars@altlinux.org> 0.3-alt1
- initial build for ALT Sisyphus
