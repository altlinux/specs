Name:    grafx2
Version: 2.9
Release: alt2

Summary: The ultimate 256 color painting program
License: GPL-2.0+
Group:   Graphics
Url:     https://gitlab.com/GrafX2/grafX2

Source: %name-%version.tar
Source1: submodules.tar
Patch0: grafx2-2.9-mga-hicolor-icon.patch
Patch1: grafx2-2.8-mga-desktop.patch
Patch2: grafx2-2.8-mga-sdl2.patch

BuildRequires: libSDL2-devel
BuildRequires: libSDL2_image-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libfreetype-devel
BuildRequires: liblua-devel

%description
GrafX2 is a bitmap paint program inspired by the Amiga programs a..Deluxe
Paint and Brilliance. Specialized in 256-color drawing, it includes a very
large number of tools and effects that make it particularly suitable
for pixel art, game graphics, and generally any detailed graphics painted
with a mouse.

%prep
%setup
%autopatch -p1
tar xf %SOURCE1

%build
%make_build API=sdl2

%install
%makeinstall_std -C src PREFIX=%_prefix
install -Dpm0644 misc/unix/grafx2.1 %buildroot%_man1dir/grafx2.1
install -Dpm0644 misc/unix/grafx2.fr.1 %buildroot%_mandir/fr/man1/grafx2.1

%check
make check

%files
%doc doc/README.txt
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/*.metainfo.xml
%_man1dir/*.1*
%_mandir/fr/man1/*.1*

%changelog
* Fri Sep 12 2025 Andrey Cherepanov <cas@altlinux.org> 2.9-alt2
- Initial build for Sisyphus (ALT #53666).
