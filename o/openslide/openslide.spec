Name: openslide
Version: 3.4.0
Release: alt1

Summary: C library for reading virtual slides
License: LGPLv2
Group: System/Libraries

Url: http://openslide.org/
Source: https://github.com/%name/%name/releases/download/v%version/%name-%version.tar.xz
Source100: openslide.watch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(zlib)
BuildRequires: libpng-devel
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: libopenjpeg-devel
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(sqlite3)

BuildRequires: libturbojpeg-devel
BuildRequires: libjpeg-devel

%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.

%package -n lib%name
Summary: Shared library for %name
Group: System/Libraries

%description -n lib%name
This package contains shared libraries for applications that use %name.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Command line tools for %name
Group: Video

%description tools
This package contains command line tools for working
with virtual slides.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files -n lib%name
%doc README.txt lgpl-2.1.txt LICENSE.txt CHANGELOG.txt
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*.pc

%files tools
%_bindir/*
%_man1dir/*

%changelog
* Thu Jun 19 2014 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- initial build for ALT Linux Sisyphus (based on fedora package)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 26 2014 Benjamin Gilbert <bgilbert@backtick.net> - 3.4.0-1
- New release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 13 2013 Benjamin Gilbert <bgilbert@backtick.net> - 3.3.3-1
- New upstream release
   + Minor compatibility improvements for Aperio JP2K and Hamamatsu slides
- Update Source0 URL

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 3.3.2-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.3.2-3
- rebuild against new libjpeg

* Fri Dec 21 2012 Benjamin Gilbert <bgilbert@backtick.net> - 3.3.2-2
- Rebuild for jpeg8

* Sat Dec 01 2012 Benjamin Gilbert <bgilbert@backtick.net> - 3.3.2-1
- New upstream release
   + Fix seams in MIRAX 2.2 slides
   + Fix associated images in single-level Aperio slides
   + Improve performance on MIRAX and Hamamatsu VMU

* Sun Oct 14 2012 Benjamin Gilbert <bgilbert@backtick.net> - 3.3.1-1
- New upstream release
   + Parallelize concurrent openslide_read_region calls
   + Performance improvements for MIRAX and Hamamatsu VMS

* Sat Sep 22 2012 Benjamin Gilbert <bgilbert@backtick.net> - 3.3.0-1
- New upstream release
   + Support for Leica SCN format (requires libtiff 4)
   + Partial support for MIRAX 2.2
   + Standard properties for microns-per-pixel and objective power
   + Improved reporting of open errors
   + Command-line tool improvements
- Add versioned dependency on main package to subpackages

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 29 2012 Adam Goode <adam@spicenitz.org> - 3.2.6-1
- New upstream release
   + Support for downsampled MIRAX files
   + Improved MIRAX performance and bugfixes
   + Fix for openslide_read_region with large dimensions

* Thu Feb 09 2012 Rex Dieter <rdieter@fedoraproject.org> 3.2.5-2
- rebuild (openjpeg)

* Mon Jan 16 2012 Adam Goode <adam@spicenitz.org> - 3.2.5-1
- New upstream release
   + Support for MIRAX 1.03 files
   + openslide_read_region now works for large dimensions
   + quickhash-1 is disabled for unusual TIFFs where it is very slow

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.2.4-2
- Rebuild for new libpng

* Fri Aug 12 2011 Adam Goode <adam@spicenitz.org> - 3.2.4-1
- New upstream release, see http://github.com/openslide/openslide/blob/master/CHANGELOG.txt

* Fri Aug 12 2011 Adam Goode <adam@spicenitz.org> - 3.2.3-5
- Clean up the spec file a little

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Rex Dieter <rdieter@fedoraproject.org> - 3.2.3-3
- rebuild (openjpeg)

* Wed Sep 29 2010 jkeating - 3.2.3-2
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Adam Goode <adam@spicenitz.org> - 3.2.3-1
- New upstream release, see http://github.com/openslide/openslide/blob/master/CHANGELOG.txt

* Sat Jun 19 2010 Adam Goode <adam@spicenitz.org> - 3.2.2-2
- Restore missing clean section

* Wed Jun 16 2010 Adam Goode <adam@spicenitz.org> - 3.2.2-1
- New upstream release
   + Add openslide-write-png
   + Support for VMU files
   + New error handling system

* Tue Apr 27 2010 Adam Goode <adam@spicenitz.org> - 3.1.1-1
- New upstream release
   + Don't crash or leak memory on some invalid VMS files
   + Ignore extra layers in VMS files

* Thu Apr  1 2010 Adam Goode <adam@spicenitz.org> - 3.1.0-1
- New upstream release
   + Support newer Aperio files (compression 33005)
   + Be more robust in reading raw TIFF tiles
   + Reject invalid TIFF files earlier
   + Fix many memory leaks when probing for TIFF files

* Tue Mar  2 2010 Adam Goode <adam@spicenitz.org> - 3.0.3-1
- New upstream release
   + Fix nasty MIRAX seam problem

* Wed Feb 17 2010 Adam Goode <adam@spicenitz.org> - 3.0.2-1
- New upstream release
   + Allow building on RHEL

* Thu Feb  4 2010 Adam Goode <adam@spicenitz.org> - 3.0.1-1
- New upstream release
   + Fix rendering of the edges of TIFF files
   + Include CHANGELOG.txt

* Mon Feb  1 2010 Adam Goode <adam@spicenitz.org> - 3.0.0-1
- New upstream release
   + License change from GPLv2 to LGPLv2
   + Bug fixes
   + Support more MIRAX files
   + Improve perforamance of MIRAX
   + Add some command-line tools
   + Rework API documentation
   + Add some new properties
   + Remove some unimplemented functions from the header file

* Mon Dec 21 2009 Adam Goode <adam@spicenitz.org> - 2.3.1-1
- New upstream release
   + Support for generic tiled TIFF
   + Bug fixes
   + Try to be less chatty with TIFF output

* Thu Nov 12 2009 Adam Goode <adam@spicenitz.org> - 2.2.1-1
- New upstream release
   + Fix thread safety problems from 2.2.0

* Tue Sep 22 2009 Adam Goode <adam@spicenitz.org> - 2.2.0-3
- Use xz instead of gz

* Mon Sep 21 2009 Adam Goode <adam@spicenitz.org> - 2.2.0-2
- Be more explicit about include directory in files section

* Tue Sep 15 2009 Adam Goode <adam@spicenitz.org> - 2.2.0-1
- New upstream release
   + Thread safety (sometimes lockless)

* Thu Sep 10 2009 Adam Goode <adam@spicenitz.org> - 2.1.0-1
- New upstream release
   + MIRAX support
   + More Aperio support
   + Properties and associated images support
   + Bug fixes

* Wed Feb 25 2009 Adam Goode <adam@spicenitz.org> - 1.1.1-1
- New upstream release
- No more included OpenJPEG
- Much faster rendering and loading

* Tue Dec  9 2008 Adam Goode <adam@spicenitz.org> - 1.0.0-1
- First release
