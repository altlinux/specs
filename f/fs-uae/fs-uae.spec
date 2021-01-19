Name:       fs-uae
Version:    3.0.5
Release:    alt1
License:    GPLv2
URL:        https://fs-uae.net
Group:      Emulators
Summary:    An Amiga emulator based on UAE/WinUAE, with a focus on emulating games
Source:     %name-%version.tar.gz

# Automatically added by buildreq on Mon Jan 18 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libX11-devel libXext-devel libXfixes-devel libglvnd-devel libstdc++-devel pkg-config python-modules python2-base sh4 tzdata xorg-proto-devel zlib-devel
BuildRequires: gcc-c++ glib2-devel glibc-devel-static libSDL-devel libSDL2-devel libXi-devel libXv-devel libmpeg2-devel libopenal-devel libpng-devel zip

%description
FS-UAE is an Amiga emulator for Windows, Linux and Mac OS X based on
UAE/WinUAE, with a focus on emulating games.

Features include emulation of Amiga 500, 1200, 4000, CD32 and CDTV,
perfectly smooth scrolling on 50Hz displays, support for floppy images in
ADF and IPF formats, CD-ROM images in ISO or BIN/CUE format, mounting folders
on your computer as Amiga hard drives, support for Picasso 96 drivers for
high-color and high-resolution Workbench displays, and more...

A unique feature is support for cross-platform online play. You can now play
Amiga games against (or with) friends over the Internet.

%ifarch %ix86 x86_64
%def_enable jit
%else
%def_disable jit
%endif

%prep
%setup
%configure %subst_enable jit

%build
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc *[A-Z]
%_bindir/*
%_desktopdir/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_datadir/mime/*

%changelog
* Mon Jan 18 2021 Fr. Br. George <george@altlinux.ru> 3.0.5-alt1
- Initial build for ALT

