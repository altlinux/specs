%set_verify_elf_method textrel=relaxed

%global orgname gens
Name:           %{orgname}-gs
Version:        2.16.7
Release:        alt1
Summary:        Sega Genesis, Sega CD, and Sega 32X emulator

Group:		Emulators
Url:            http://segaretro.org/Gens/GS
#Most source files are GPLv2+ excludding the following, which are LGPLv2+:
#Source files for 2xsai, hq*x, super_eagle, super_2xsai, blargg_ntsc filters found in src/mdp/render/
#src/gens/ui/gtk/gtk-uri.h and src/gens/ui/gtk/gtk-uri.c
#As well, code in src/starscream uses the starscream license (non-free)
License:        GPLv2+ and LGPLv2+ and MIT and BSD and Starscream (Nonfree)
Source0:        http://segaretro.org/images/6/6d/Gens-gs-r7.tar.gz
#Found via Arch Linux: https://www.archlinux.org/packages/community/i686/gens-gs/
#Replaces deprecated gtk functions with working ones
#Cannot be sumbitted upstream, as upcomming version no longers uses GTK
Patch0:         %name-gtk.patch
Patch1:		%name-fix-define.patch

ExclusiveArch:  %ix86

BuildRequires:  nasm
BuildRequires:  gcc-c++
BuildRequires:  ImageMagick-tools
BuildRequires:  libGL-devel
BuildRequires:  libgtk+2-devel
BuildRequires:  libminizip-devel
BuildRequires:  libpng-devel
BuildRequires:  libSDL-devel
BuildRequires:  desktop-file-utils

Requires:       %{name}-doc

%description
#taken from here: http://segaretro.org/Gens/GS 
Gens/GS is a Sega Mega Drive emulator derived from Gens and maintained
by GerbilSoft. Project goals include clean source code, combined
features from various developments of Gens, and improved platform
portability.

%package        doc
Summary:        Documentation Manual for Gens/GS
Group:		Documentation
BuildArch:      noarch

%description doc
This package contains the documentation manual for Gens/GS

%prep
%setup -q -n %{name}-r7
%patch0 -p1
%patch1 -p2
#Erase all use of external libs:
sed -i '/extlib/d' configure.ac
sed -i 's/extlib//' src/Makefile.am
#Use shared minizip:
sed -i '/minizip/d' src/%{orgname}/Makefile.am
sed -i 's/"minizip\/unzip.h"/<minizip\/unzip.h>/' src/%orgname/util/file/decompressor/md_zip.c
#Remove all bundled code
rm -f -r src/extlib
#Rename to gens-gs to avoid conflicts:
sed -i 's/INIT(gens,/INIT(gens-gs,/' configure.ac
sed -i 's/gens.desktop/gens-gs.desktop/' xdg/Makefile.am
mv xdg/%{orgname}.desktop xdg/%name.desktop
#Obsolete macro in configure.ac
sed -i 's/AC_PROG_LIBTOOL/LT_INIT([disable-static])/' configure.ac

%build
%autoreconf
%configure --without-7z \
           --enable-mp3=no \
           --with-pic \
           --disable-static \
           --build=i586-alt-linux \
           --docdir='%_defaultdocdir/%name' \
           LIBS="-ldl -lX11 -lminizip"
%make_build

%install
%makeinstall_std
#Use imagemagick to create a 128x128 icon from 128x96 image
mkdir -p %buildroot%_iconsdir/hicolor/128x128/apps
convert images/%{orgname}_small.png -background none -gravity center -extent 128x128! %buildroot%_iconsdir/hicolor/128x128/apps/%{name}.png
#Copy icons into hicolor
for size in 16 32 48; do
    dim="${size}x${size}"
    install -p -D -m 0644 images/%{orgname}gs_$dim.png \
    %buildroot%_iconsdir/hicolor/$dim/apps/%{name}.png
done
#modify icon field in desktop to use hicolor icons
sed -i '/Icon=*/cIcon=%{name}' xdg/%name.desktop
#rename binary to gens-gs
mv %buildroot%_bindir/%orgname %buildroot%_bindir/%name
sed -i 's/Exec=gens/Exec=gens-gs/' xdg/%name.desktop
#install modified desktop file
desktop-file-install \
  --remove-key=Encoding \
  --dir %buildroot%_desktopdir \
  xdg/%name.desktop
#remove any .la files that may have generated:
rm -f %buildroot%_libdir/mdp/*.la

%files
%doc README.txt NEWS.txt COPYING.txt
%_bindir/%name
%_bindir/mdp_test
%_libdir/mdp/
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%files doc
%_defaultdocdir/%name

%changelog
* Thu Nov 12 2015 Andrey Cherepanov <cas@altlinux.org> 2.16.7-alt1
- Initial build in Sisyphus (thanks Fedora for spec)

