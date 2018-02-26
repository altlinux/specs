%define _name hargyllcms

Name: argyllcms
Version: 1.4.0
Release: alt1

Summary: ICC compatible color management system
Group: Graphics
License: GPLv3 and MIT

URL: http://gitorious.org/%_name
Source: http://people.freedesktop.org/~hughsient/releases/%_name-%version.tar.xz

BuildRequires: libusb-devel libtiff-devel libjpeg-devel libX11-devel libXext-devel
BuildRequires: libXxf86vm-devel libXinerama-devel libXScrnSaver-devel libXrandr-devel

%description
The Argyll color management system supports accurate ICC profile
creation for scanners, CMYK printers, film recorders and calibration and
profiling of displays.

Spectral sample data is supported, allowing a selection of illuminants
observer types, and paper fluorescent whitener additive compensation.
Profiles can also incorporate source specific gamut mappings for
perceptual and saturation intents. Gamut mapping and profile linking
uses the CIECAM02 appearance model, a unique gamut mapping algorithm,
and a wide selection of rendering intents. It also includes code for the
fastest portable 8 bit raster color conversion engine available
anywhere, as well as support for fast, fully accurate 16 bit conversion.
Device color gamuts can also be viewed and compared using a VRML viewer.

%package doc
Summary: Argyll CMS documentation
Group: Graphics
BuildArch: noarch
Conflicts: %name < %version

%description doc
The Argyll color management system supports accurate ICC profile
creation for scanners, CMYK printers, film recorders and calibration and
profiling of displays.

This package contains the Argyll color management system documentation.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static

# SMP-incompatible build
%make

%check
%make check

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_libdir/libargyll.so.*
%_libdir/libargyllicc.so.*
%_libdir/libargyllusb.so.*
%exclude %_libdir/libargyll.so
%exclude %_libdir/libargyllicc.so
%exclude %_libdir/libargyllusb.so
%_datadir/color/argyll/
/lib/udev/rules.d/55-Argyll.rules
%doc README *.txt

%files doc
%doc doc/*.html doc/*.jpg doc/*.txt

%exclude %_datadir/doc

%changelog
* Sun May 13 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Thu Apr 05 2012 Yuri N. Sedunov <aris@altlinux.org> 1.3.7-alt1
- 1.3.7

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.3.6-alt1
- 1.3.6

* Sat Jan 28 2012 Yuri N. Sedunov <aris@altlinux.org> 1.3.5-alt1
- 1.3.5
- used hargylcms from Richard Hughes as a source.

* Sat Sep 11 2010 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1
- remove upstremed patches

* Sun Jan 31 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0
- fixed "always buffer overflow" bug (patch4). Tnx to Valery Inozemtsev (shrek@)

* Tue Dec 15 2009 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt2
- system icclib used

* Tue Dec 08 2009 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- Fedora package adapted for Sisyphus

