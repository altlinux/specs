Name: slade
Version: 3.2.0_b3
Release: alt3

Summary: SLADE3 Doom editor
License: GPLv2
Group: Games/Arcade

Url: https://slade.mancubus.net/

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: libfmt-devel
BuildRequires: libmpg123-devel
BuildRequires: cmake
BuildRequires: ImageMagick-tools
BuildRequires: p7zip
BuildRequires: bzlib-devel
BuildRequires: libfreeimage-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libwxGTK3.0-devel
BuildRequires: libfluidsynth-devel
BuildRequires: libftgl-devel
BuildRequires: libglvnd
BuildRequires: libGLEW-devel
BuildRequires: libgtk+3-devel
BuildRequires: libcurl-devel
BuildRequires: libSFML-devel
BuildRequires: libX11-devel
BuildRequires: jackit-devel
BuildRequires: liblua5.3-devel

ExclusiveArch: %ix86 x86_64

%description
SLADE3 is a modern editor for Doom-engine based games and source
ports. It has the ability to view, modify, and write many different
game-specific formats, and even convert between some of them, or
from/to other generic formats such as PNG.

%prep
%setup -n %name-%version

%__subst '/#include <FreeImage.h>/a #undef _WINDOWS_ ' src/common.h

# std::filesystem components can be used without -lstdc++fs with gcc >= 9
%__subst '/lstdc++fs/d' src/CMakeLists.txt

%build
%cmake_insource \
	-DUSE_WX_EXCEPTION_HANDLER=0 \
	-DWX_GTK3:BOOL=ON

%make_build

%install
%makeinstall_std

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=SLADE3
Comment=Doom editor
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert dist/res/logo_icon.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%dir %_iconsdir/hicolor/64x64
%dir %_iconsdir/hicolor/64x64/apps
%dir %_iconsdir/hicolor/128x128
%dir %_iconsdir/hicolor/128x128/apps
%doc README.md LICENSE
%_bindir/%name
%_datadir/slade3/
%_desktopdir/%name.desktop

%changelog
* Sun Aug 15 2021 Artyom Bystrov <arbars@altlinux.org> 3.2.0_b3-alt3
- removing fix to build for non-x86 arch
- add ExclusiveArch :-( (my apologizes to RPi4 owners)

* Sun Aug 15 2021 Artyom Bystrov <arbars@altlinux.org> 3.2.0_b3-alt2
- Add fix to build for non-x86 arch

* Sat Aug 14 2021 Artyom Bystrov <arbars@altlinux.org> 3.2.0_b3-alt1
- initial build for ALT Sisyphus
