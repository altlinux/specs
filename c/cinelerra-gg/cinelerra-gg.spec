%set_verify_elf_method unresolved=relaxed
Name: cinelerra-gg
Version: 2023.11
Release: alt1

Summary: Cinelerra is an Non-Linear Editor for Linux.
License: GPLv2
Group: Video

Url: https://www.cinelerra-gg.org/
VCS: git://git.cinelerra-gg.org/goodguy/cinelerra.git

Source: %name-%version.tar
Patch1: cinelerra-5.1-alt-fixes.patch 

BuildRequires(pre): rpm-build rpm-macros-make 
BuildRequires: gcc-c++ gcc
BuildRequires: nasm yasm cmake meson
BuildRequires: texinfo
BuildRequires: python3 perl perl-XML-XPath

#Various "devel" dependencies from build scripts
BuildRequires: libusb-devel libflac-devel 
BuildRequires: libjpeg-devel libdvdnav-devel libdvdread-devel 
BuildRequires: ncurses-devel libfftw3-devel 
BuildRequires: libSDL-devel libpng-devel 
BuildRequires: libXfixes-devel libXft-devel libXinerama-devel libXv-devel 
BuildRequires: festival-devel libdc1394-devel libiec61883-devel  
BuildRequires: libjbig-devel libvdpau-devel libva-devel gtk2-devel 
BuildRequires: libpulseaudio-devel  boost-devel
BuildRequires: ladspa_sdk libnuma-devel
BuildRequires: libfreetype-devel libalsa-devel 
BuildRequires: bzip2-devel liblzma-devel zlib-devel bzlib-devel

#LV2
BuildRequires: lilv-devel libsuil-devel libserd-devel libsord-devel 
BuildRequires: libsratom-devel lv2-devel

#Thirdparty without patches
BuildRequires: liblame-devel libturbojpeg-devel libogg-devel 
BuildRequires: libraw1394-devel libsndfile-devel libtheora-devel
BuildRequires: libvorbis-devel libopenjpeg2.0-devel libopus-devel
BuildRequires: libtwolame-devel libtiff-devel

ExclusiveArch: x86_64

%description
Cinelerra is an NLE - Non-Linear Editor - for Linux that provides a way
to compose audio and video media. Besides editing, it can be used as an
audio/video player, for recording audio or video to include broadcast
television programs, creating dvd/bluray media, and touching up old photos.
Because cinelerra has many features for uncompressed content, high resolution
processing, and compositing, using cinelerra can be quite complex. However,
with only a little bit of introduction, even novice will be able to create
simple artful videos.

Cinelerra-gg is licensed under the GNU General Public License (GNU GPL or GPL)
which is free software license giving users opportunity to run, share, and
modify the software. Any included libraries, such as Ffmpeg, are also under
the GPL license. Cinelerra-gg used the original cinelerra software (Heroine
Virtual) as its base, incorporated the work and modifications made by numerous
developers over the years (Community Version), added numerous enhancements
over the years, and is continously being improved. Currently new pre-built
versions for many distros are released monthly.

To expand functionality, it is recommended to install these packages:
dvdauthor, inkscape, udftools


%prep
%setup 
%patch1 -p0

%build
cd cinelerra-5.1

%autoreconf
%add_optflags -fpermissive 

#--disable means "use system libraries, don't build from thirdparty"!
%configure --disable-lv2 

%make_build

%install

cd cinelerra-5.1
%makeinstall_std
cd ..
%find_lang cin

%files -f cin.lang
%doc cinelerra-5.1/README


%_bindir/*
%_libdir/cin/
%_datadir/cin/
%_pixmapsdir/cin.svg
%_pixmapsdir/cin.xpm
%_desktopdir/cin.desktop


%changelog
* Tue Jan 09 2024 Alexey Shemyakin <alexeys@altlinux.org> 2023.11-alt1
- Initial build for ALT.

