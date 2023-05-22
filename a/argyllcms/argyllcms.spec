Name: argyllcms
Version: 2.3.1
Release: alt1

Summary: ICC compatible color management system

License: AGPL-3.0
Group: Graphics
Url: https://www.argyllcms.com/

# Source-url: https://www.argyllcms.com/Argyll_V%{version}_src.zip
Source: %name-%version.tar

Patch1: argyllcms-datadir.patch

BuildRequires: jam
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xdmcp)

# owner for %_datadir/color
Requires: icc-profiles

%description
The Argyll color management system supports accurate ICC profile creation for
scanners, CMYK printers, film recorders and calibration and profiling of
displays.

Spectral sample data is supported, allowing a selection of illuminants observer
types, and paper fluorescent whitener additive compensation. Profiles can also
incorporate source specific gamut mappings for perceptual and saturation
intents. Gamut mapping and profile linking uses the CIECAM02 appearance model,
a unique gamut mapping algorithm, and a wide selection of rendering intents. It
also includes code for the fastest portable 8 bit raster color conversion
engine available anywhere, as well as support for fast, fully accurate 16 bit
conversion. Device color gamuts can also be viewed and compared using a VRML
viewer.

%prep
%setup
%patch1 -p1

%build
export CCOPTFLAG="%optflags"
export LINKFLAGS=""
jam -q -dx -fJambase %_smp_mflags

%install
jam -q -dx -fJambase %_smp_mflags \
  -sDESTDIR=%buildroot \
  -sPREFIX=%prefix \
  -sREFSUBDIR=%_datadir/color/argyll \
  install

rm -rv %buildroot%_bindir/License.txt

%files
%doc doc/License.txt
%doc Readme.txt
%_bindir/*
%_datadir/color/argyll/

%changelog
* Thu Apr 20 2023 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- initial build for ALT Sisyphus (thanks, Cauldron!)
