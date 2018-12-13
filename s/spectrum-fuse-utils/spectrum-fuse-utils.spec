%define cname spectrum-fuse
Name: spectrum-fuse-utils
Version: 1.5.7
Release: alt1

Summary: Utils for the the Free Unix Spectrum Emulator

License: GPLv2
Group: Emulators
Url: http://fuse-emulator.sourceforge.net/

Packager: ZX Spectrum Development Team <spectrum@packages.altlinux.org>

Source: %name-%version.tar

Requires: spectrum-fuse = %version

BuildRequires: libspectrum-devel >= 1.4.1
# Automatically added by buildreq on Mon Dec 10 2018
BuildRequires: flex glib2-devel gtk-update-icon-cache libXext-devel libspectrum-devel libxml2-devel ruby zlib-devel


%description
Fuse is a Sinclair ZX Spectrum emulator. It supports several models
(including the 128), with quite faithful emulation of the display
and sound. The package contains utilities for the Emulator.

%prep
%setup -q -n %name-%version
find -name "Makefile.am" -exec sed -e "s/fuse_/spectrum_fuse_utils_/" -e "s/= fuse/= spectrum-fuse-utils/" -i {} \;
sed -e "s/\[fuse]/[spectrum-fuse]/g" -i configure.ac

%build
%autoreconf
%configure --with-internal-glib --disable-static
%make_build

%install
%makeinstall
find %buildroot -name "*.1" -o -name "*.scr" -o -name "*.bmp" -o -name "*.rom" | while read f; do rm -f "$f"; done

%files
%doc README AUTHORS COPYING ChangeLog THANKS
%_bindir/%name
%_datadir/%cname

%changelog
* Thu Dec 06 2018 Pavel Skrylev <majioa@altlinux.org> 1.5.7-alt1
- Initial build bumped to 1.5.7.
