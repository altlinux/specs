Summary: CaPriCe32 - Amstrad CPC Emulator
Name: caprice32
Version: 4.6.0
Release: alt1
#v2, except for cpc roms, which just are just allowed be distributed
License: GPLv2+
Group: Emulators
Url: https://github.com/ColinPitrat/caprice32/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: https://github.com/ColinPitrat/caprice32/archive/v%version.tar.gz?/%name-%version.tar.gz
Source1: %name.png
#this is the same icon as xcpc, but converted in png
Source2: %name

Patch0: caprice32-4.6.0-iostream.patch
Patch1: caprice32-4.6.0-string.patch

BuildRequires: gcc-c++ make
BuildRequires: ImageMagick-tools
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(zlib)

%description
CaPriCe32 emulates the Amstrad CPC home computer models 464, 664 and 6128
faithfully on your PC. Detailed usage instructions can be found in the
included documentation.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build

%make RELEASE=true APP_PATH=%_datadir/%name

%install
%makeinstall_std prefix=%prefix
# wrapper
install -m 755 %SOURCE2 %buildroot%_bindir
# install menu icons
for N in 16 32 48;
do
convert %SOURCE1 -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

# xdg menu
install -d -m 755 %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=CaPriCe32
Comment=Amstrad CPC Emulator
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

%files
%doc README.md
%config(noreplace) %_sysconfdir/cap32.cfg
%_bindir/cap32
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_man6dir/cap32.6*

%changelog
* Wed Apr 26 2023 Artyom Bystrov <arbars@altlinux.org> 4.6.0-alt1
- initial build for ALT Sisyphus

