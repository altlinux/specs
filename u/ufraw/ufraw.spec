%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: ufraw
Version: 0.18
Release: alt3

Summary: UFRaw is a graphical utility for opening and converting RAW files from digital photo cameras
License: GPLv2+
Group: Graphics

Url: http://ufraw.sourceforge.net/
Source0: http://downloads.sourceforge.net/ufraw/ufraw-%version.tar.gz
# Default path to curves and color profiles
Patch1: ufraw-0.16-defaults.patch
# Fix crash when loading dark frame
Patch2: ufraw-0.18-darkframe.patch

BuildPreReq: liblcms-devel >= 1.14
BuildPreReq: liblensfun-devel >= 0.2.3
# Automatically added by buildreq on Thu Mar 24 2011
BuildRequires: bzlib-devel gcc-c++ libexiv2-devel libgimp-devel libgomp-devel libgtkimageview-devel libjpeg-devel liblcms-devel liblensfun-devel libpng-devel libtiff-devel perl-podlators zlib-devel

# helps to expel broken 0.2.3-alt3 build...
Requires: liblensfun >= 0.2.3-alt4

%package -n gimp-plugin-ufraw
Summary: GIMP plugin for opening and converting RAW files from digital photo cameras (part of UFRaw project)
Group: Graphics
Conflicts: rawphoto
Requires: gimp
Obsoletes: gimp2-plugin-ufraw

%description
UFRaw is a graphical utility for opening and converting RAW files from digital
photo cameras.

%description -n gimp-plugin-ufraw
GIMP plugin for opening and converting RAW files from digital photo cameras
(part of UFRaw project).

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%configure --with-lensfun --enable-contrast --enable-openmp --enable-hotpixels
%make_build

%install
%makeinstall_std

install -d %buildroot%_datadir/ufraw
install -pD -m644 ufraw.desktop %buildroot%_desktopdir/ufraw.desktop
install -pD -m644 icons/ufraw.png %buildroot%_liconsdir/ufraw.png

%find_lang ufraw

%files -f ufraw.lang
%_bindir/*
%_datadir/ufraw
%_man1dir/*
%_desktopdir/*
%_liconsdir/*
%_pixmapsdir/*
%doc MANIFEST README

%files -n gimp-plugin-ufraw
%gimpplugindir/plug-ins/*

%changelog
* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt3
- rebuilt against libexiv2.so.11

* Thu Mar 24 2011 Victor Forsiuk <force@altlinux.org> 0.18-alt2
- Fix BuildRequires.
- Fix crash when loading dark frame (patch from Fedora).

* Mon Feb 21 2011 Victor Forsiuk <force@altlinux.org> 0.18-alt1
- 0.18

* Mon Aug 16 2010 Victor Forsiuk <force@altlinux.org> 0.17-alt1
- 0.17

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 0.16-alt3
- Rebuild with libexiv2.so.9.

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 0.16-alt2
- Rebuild with libexiv2.so.6.

* Tue Oct 20 2009 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- 0.16

* Tue Jul 21 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt3
- Rebuild with libexiv2.so.5.

* Tue Jun 09 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt2
- Fix gcc4.4 build.

* Fri Feb 20 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- 0.15
- Build with OpenMP support.

* Mon Oct 20 2008 Victor Forsyuk <force@altlinux.org> 0.14.1-alt1
- 0.14.1

* Thu Oct 16 2008 Victor Forsyuk <force@altlinux.org> 0.14-alt1
- 0.14
- Build with lensfun support.

* Fri Jun 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.13-alt2.1
- Automated rebuild due to libexiv2.so.2 -> libexiv2.so.4 soname change.

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 0.13-alt2
- Rebuild with new libexiv2.

* Tue Nov 13 2007 Victor Forsyuk <force@altlinux.org> 0.13-alt1
- 0.13

* Tue Sep 04 2007 Victor Forsyuk <force@altlinux.org> 0.12.1-alt1
- 0.12.1

* Tue Jul 31 2007 Victor Forsyuk <force@altlinux.org> 0.12-alt1
- 0.12

* Tue Apr 10 2007 Victor Forsyuk <force@altlinux.org> 0.11-alt1
- 0.11

* Thu Nov 23 2006 Victor Forsyuk <force@altlinux.org> 0.10-alt1
- 0.10
- Build with EXIF read support (using exiv2 library).
- Use SMP build.

* Mon Mar 06 2006 Dmitry Marochko <mothlike@altlinux.ru> 0.7-alt1
- New version
  + Much more accurate white balance temperature setting.
  + White balance presets per camera model.
  + Show the channel multipliers in the UI.
  + Apply base curve before gamma curve.
  + Fix a few general bugs.
  + Fix camera specific bugs for Sony F828, Sigma Foveon, Nikon D2H, D1X.
- Patch removed due incompatibility

* Fri Nov 25 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.6-alt1
- New version
  + Enabled AHD (Adaptive Homogeneity-Directed) interpolation.
  + Added base curve, which simulates Nikon tone curve behavior. (The old correction curve is still there.)
  + Automatically apply the embedded custom curve only if the camera was setup to use this curve.
  + Support the D1X rectangular pixels.
  + Fix EXIF support with libtiff 3.7.4.
  + Some bug fixes.
- Patch from Sergei Epiphanov kept back

* Sun Oct 02 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.5-alt2
- Patch removed
- Version 0.5
- Read support for Nikon Tone Curve (NTC/NCV) files.
- Added a curve editor.
- Added control on the base curve (see the user guide for more information).
- Support the new DCRaw color matrices for better color rendering.
- More controls can be set from the command-line.
- Preliminary EXIF support.
- New UFRaw ID files contain all the conversion parameters and allow for batch conversion.
- New ufraw-batch replaces ufraw --batch.
- Numerous other changes.
- Notice that the new Adaptive Homogeneity-Directed interpolation is still not enabled.

* Sun Sep 11 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.5-alt1.20050906cvs
- New CVS version
- ufraw(1) manual added
- Increased stability
- Build with new dcraw version included
- Enhance curves

* Mon Aug 08 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.5-alt1.20050808cvs
- CVS version 0.5
- Major changes from Sergei Epiphanov:
  + Package splitted to binary and GIMP plugin parts
  + Patch to enhance functionality

* Wed Aug 03 2005 Dmitry Marochko <mothlike@altlinux.ru> 0.4-alt1
- Initial Sisyphus build
- Version 0.4
