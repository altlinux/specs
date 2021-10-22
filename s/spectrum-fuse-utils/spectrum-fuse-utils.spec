%define        cname spectrum-fuse

Name:          spectrum-fuse-utils
Version:       1.5.8
Release:       alt0.2
Summary:       Utils for the the Free Unix Spectrum Emulator
License:       GPLv2
Group:         Emulators
Url:           http://fuse-emulator.sourceforge.net/
Vcs:           git://git.code.sf.net/p/fuse-emulator/fuse
Packager:      ZX Spectrum Development Team <spectrum@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires: libalsa-devel
BuildRequires: pkgconfig(libspectrum) >= 1.4.5
# libgcrypt: the ability to digitally sign RZX files (note that Fuse requires version 1.1.42 or later).
BuildRequires: libgcrypt-devel
# libjsw: allow joystick input to be used (not required for joystick emulation).
BuildRequires: libjsw-devel
# libxml2: the ability to load and save Fuse's current configuration.
BuildRequires: libxml2-devel
# libpng: the ability to save screenshots.
BuildRequires: libpng-devel
# zlib: support for compressed RZX files.
BuildRequires: zlib-devel
# bzip2: support for certain compressed files.
BuildRequires: bzip2-devel
# libaudiofile: support for loading from .wav files.
BuildRequires: libaudiofile-devel
BuildRequires: glib2-devel
BuildRequires: libXext-devel
BuildRequires: libxml2-devel
BuildRequires: zlib-devel
BuildRequires: libgtk+3-devel
BuildRequires: gtk-update-icon-cache
BuildRequires: flex

Requires:      spectrum-fuse = %version


%description
Fuse is a Sinclair ZX Spectrum emulator. It supports several models
(including the 128), with quite faithful emulation of the display
and sound. The package contains utilities for the Emulator.

%prep
%setup
%ifarch %e2k
# LCC crashes with -O3 by default
sed -i "/scaler_AdvMame3x/i __attribute__((optimize(2)))" ui/scaler/scalers.c
%endif
find -name "Makefile.am" -exec sed -e "s/fuse_/spectrum_fuse_utils_/" -e "s/= fuse/= spectrum-fuse-utils/" -i {} \;
sed -e "s/\[fuse]/[spectrum-fuse]/g" -i configure.ac

%build
%autoreconf
%configure \
      --disable-ui-joystick \
      --enable-joystick \
      --with-gtk \
      --enable-desktop-integration \
      --disable-static
%make_build

%install
DESTDIR=%buildroot make install
find %buildroot -name "*.1" -o -name "*.scr" -o -name "*.bmp" -o -name "*.rom" | while read f; do rm -f "$f"; done

%files
%doc README AUTHORS COPYING ChangeLog THANKS
%_bindir/%name
%_datadir/%cname
%_desktopdir/*
%_datadir/mime/*
%_iconsdir/hicolor/*/apps/fuse.png


%changelog
* Fri Oct 22 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.5.8-alt0.2
- Fixed build for Elbrus.

* Fri Dec 11 2020 Pavel Skrylev <majioa@altlinux.org> 1.5.8-alt0.1
- ^ 1.5.7 -> 1.5.8[gamma]
- + support for zlib, bzip2, libaudiofile

* Thu Dec 06 2018 Pavel Skrylev <majioa@altlinux.org> 1.5.7-alt1
- Initial build bumped to 1.5.7.
