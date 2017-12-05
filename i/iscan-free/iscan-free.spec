Name: iscan-free
Version: 2.20.0
Release: alt5

Summary: Free Image Scan Version with epkowa Driver for Epson Scanners

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://www.avasys.jp/english/linux_e/index.html
License: GPL v2 or later; LGPL v2.1 or later
Group: Graphics

# How to make Source:
# Get the matching source from the iscan package (iscan_2.10.0-1.tar.bz2)
# Unpack it:
# tar -xjvf iscan_2.10.0-1.tar.bz2
# Remove only the really non-free files:
# rm iscan-2.10.0/non-free/libesmod-i386*.so iscan-2.10.0/non-free/EAPL.*.txt
# The remaining file filter.hh and the Makefiles are free software.
# The proprietary binary-only i386-only libesmod library is needed only
# to make the %_bindir/iscan frontend and the EAPL.*.txt license files
# apply only to this libesmod library.
# By using "configure --disable-frontend" it builds without the frontend
# (i.e. without the non-free libesmod library).
# Pack the remaining free sources:
# tar -cjvf iscan-free_2.10.0-1.tar.bz2 iscan-2.10.0/*

Source: iscan-free-2.20.0.tar
# A README regarding the changes of the free version:
Source1: README

Patch1: libltdl.patch
# Patch10 changes the "sane-epkowa" man page so that those models are removed
# which require a non-free binary-only i386-only plugin. To determine those models use
# egrep '^:model|^:comment' doc/epkowa.desc | grep -B1 'non-free' | grep '^:model'
Patch10: adapt-man-for-free.patch

# Either iscan-free or iscan can be installed.
# If iscan replaces iscan-free, proprietary software becomes installed.
# If iscan-free replaces iscan, some scanner models do no longer work (see README).
# Therefore real "Conflicts" (and not "Obsoletes" which does a silent replacement):
Conflicts: iscan

# manually removed: dpkg, gcc-fortran
# Automatically added by buildreq on Fri Apr 01 2011
BuildRequires: gcc-c++ libgtk+2-devel libjpeg-devel libltdl7-devel libpng-devel libsane-devel libtiff-devel libusb-compat-devel

# %_localstatedir
BuildRequires: rpm-macros-intro-conflicts

%description
This version of the Image Scan for Linux software contains only free
software. The proprietary binary-only i386-only "libesint*" driver
libraries are available in the separate package
iscan-proprietary-drivers.

The "esfw*.bin" firmware files are available in the separate package
iscan-firmware.

The proprietary binary-only i386-only "libesmod" library is removed
from this package. It is required by the "%_bindir/iscan" front-end.
This package is built without the front-end.

This package contains only the epkowa back-end for SANE, which compiles
and runs natively even on non-i386 platforms. For documentation, see
"man sane-epkowa".

Drawbacks:

The free version of the epkowa back-end cannot work for those scanners
that require proprietary binary-only i386-only libraries, available in
the separate package iscan-proprietary-drivers. At the moment, those
scanners are the following models:

Perfection 1250 / GT-7200U, Perfection 1250 PHOTO, Perfection 1260 /
GT-7300U, Perfection 1260 PHOTO, Perfection 2480 PHOTO / GT-F500,
Perfection 2580 PHOTO / GT-F550, Perfection 3170 PHOTO / GT-9400UF,
Perfection 3490 PHOTO / GT-F520, Perfection 3590 PHOTO / GT-F570,
Perfection 4180 PHOTO / GT-F600, Perfection 4490 PHOTO / GT-X750,
Perfection V10 / GT-S600, Perfection V100 PHOTO / GT-F650, Perfection
V200 PHOTO / GT-F670, Perfection V350 PHOTO / GT-F700, Stylus CX4300,
Stylus CX4400, Stylus CX5500, Stylus CX5600, Stylus DX4400.

Those models do not work with the free iscan version. They require the
original iscan package and the iscan-proprietary-drivers package, which
are only available for i386-compatible platforms.

Some scanners require proprietary firmware files that are available in
the package iscan-firmware. At the moment, those scanners are the
following models:

Perfection 2480 PHOTO / GT-F500, Perfection 2580 PHOTO / GT-F550,
Perfection 3170 PHOTO / GT-9400UF, Perfection 3490 PHOTO / GT-F520,
Perfection 3590 PHOTO / GT-F570, Perfection 4180 PHOTO / GT-F600,
Perfection 4490 PHOTO / GT-X750, Perfection V10 / GT-S600, Perfection
V100 PHOTO / GT-F650, Perfection V200 PHOTO / GT-F670, Perfection V350
PHOTO / GT-F700.

The front-end %_bindir/iscan was removed because it requires the
proprietary binary-only i386-only "libesmod" library. This should cause
no problem because the back-end epkowa runs now natively even on
non-i386 platforms so that all the usual front-ends (like scanimage,
xscanimage, xsane, and kooka) can be used even on non-i386 platforms.

Authors:
--------
    Noriyuki Sasaki
    Peter J. Schretlen
    Olaf Meeuwissen
    Narihiro Matsukuma
    Ross Boylan
    Tobias Kramer
    Dirk O. Siebnich

%prep
%setup
%__subst "s|non-free||" Makefile.*
# Get the README regarding the changes of the free version:
cp %SOURCE1 .
#%patch1
# Patch3 replaces fixed HZ compile-time value by sysconf(_SC_CLK_TCK) runtime value:
#%patch3
# Patch4 applies fixes for GCC 4.3:
#%patch4
# Remove those models from the man page which require a non-free plugin:
#%patch10
# Distinguish the no longer supported models in the description file
# but do not remove them because otherwise they would be no longer shown in YaST
# when the package iscan-free is installed because the 'triggerin' section
# replaces the description file and from this file YaST will re-build its database
# using %_libdir/YaST2/bin/create_scanner_database which tests if a comment
# contains 'requires DFSG non-free' and if yes it sets the package name
# in the YaST database to iscan (otherwise to iscan-free) so that YaST can
# test and install the right package even for the no longer supported models:
grep -q 'requires DFSG non-free' doc/epkowa.desc || exit 1
%__subst '/requires DFSG non-free/s/^:comment[[:space:]][[:space:]]*"/:comment "unsupported by the iscan-free package<br>/' doc/epkowa.desc
%__subst 's/requires DFSG non-free/requires DFSG non-free plugin in the iscan-proprietary-drivers package:/' doc/epkowa.desc

%build
#rm -f m4/libtool.m4
#autoreconf
# By using disable-frontend it builds without the frontend (i.e. without the non-free stuff):
%configure  --enable-jpeg \
            --enable-png \
            --enable-tiff \
            --disable-static \
            --disable-frontend
#            --enable-gimp
%__make

%install
%makeinstall_std
# Install the backend's config file:
install -d %buildroot%_sysconfdir/sane.d/
install -m 644 backend/epkowa.conf %buildroot%_sysconfdir/sane.d/
# Install the backend's description file:
install -d %buildroot%_datadir/iscan/
# Change the manufacturer name to the same as in SANE's epson.desc file.
grep -q '^:mfg[[:space:]][[:space:]]*"EPSON"' doc/epkowa.desc || exit 1
sed -e 's|^:mfg[[:space:]][[:space:]]*"EPSON".*|:mfg "Epson"|' doc/epkowa.desc >%buildroot%_datadir/iscan/epkowa.desc
mv %buildroot%_libdir/iscan/* %buildroot%_datadir/iscan/
# Remove the installed man page for the "iscan" frontend because it is not included in this package:
rm -f %buildroot%_man1dir/iscan.1

rm -f %buildroot%_libdir/sane/libsane-epkowa.la
rm -f %buildroot%_datadir/iscan/fix-udev-rules

%files
%_sbindir/iscan-registry
%doc COPYING AUTHORS NEWS README KNOWN-PROBLEMS SUPPORTED-DEVICES
%dir %_sysconfdir/sane.d
%config %_sysconfdir/sane.d/epkowa.conf
%dir %_libdir/sane
%_libdir/sane/libsane-epkowa.so*
%_datadir/iscan/
%_man5dir/sane-epkowa.5.*


%changelog
* Tue Dec 05 2017 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt5
- fix /var/lib/lib/iscan (add rpm-macros-intro-conflicts)

* Fri Jul 01 2016 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt4
- drop dpkg require

* Mon Feb 08 2016 Lenar Shakirov <snejok@altlinux.ru> 2.20.0-alt3
- man packaging fixed

* Fri Apr 01 2011 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt2
- update buildreqs

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- separate build 2.20.0

* Wed Apr 16 2008 schwab@suse.de
- Add some forward compatibility with libtool.
* Thu Apr 10 2008 jsmeix@suse.de
- Updated to version 2.10.0-1 (results package version 2.10.0.1):
  There are many more supported models (for details see
  the NEWS file and see the epkowa.desc to find out which
  models require a proprietary 32-bit-only i386-only module
  so that they are are not supported by this package but
  require the 32-bit-only i386-only iscan package).
* Tue Oct 16 2007 jsmeix@suse.de
- Changed fixes-for-GCC43.patch as suggested by Olaf Meeuwissen
  so that it also works for GCC before 4.3.
  With the previous fixes-for-GCC43.patch GCC before 4.3 showed:
  "pisa_tool.h:59: multiple definition of 'double similarity..."
  and for GCC 4.3 the error was "pisa_tool.h:69: error: explicit
  template specialization cannot have a storage class".
* Thu Oct 11 2007 jsmeix@suse.de
- fixes-for-GCC43.patch applies fixes for GCC 4.3,
  see http://en.opensuse.org/GCC_4.3_Transition
* Thu Aug 02 2007 jsmeix@suse.de
- Updated to version 2.8.0-1 (results package version 2.8.0.1)
  only to keep iscan-free in compliance with our iscan package.
  There are no more supported scanners in iscan-free
  (the Perfection V200 PHOTO / GT-F670 requires iscan and the
  proprietary module iscan-plugin-gt-f670).
* Wed Jul 11 2007 jsmeix@suse.de
- Updated to version 2.7.0-1 (results package version 2.7.0.1):
  There are several more supported scanners.
- fix-friend-declaration.diff no longer needed (fixed in source).
* Mon Jan 29 2007 jsmeix@suse.de
- Package 'sane' was renamed to 'sane-backends'.
  Adapted it so that it works with 'sane-backends'
* Sat Oct 28 2006 meissner@suse.de
- buildrequires libgphoto2-devel
* Tue Oct 10 2006 jsmeix@suse.de
- Updated to version 2.3.0-1 (results package version 2.3.0.1):
  There are several more supported scanners.
* Thu Sep 21 2006 jsmeix@suse.de
- Updated to version 2.2.0-1 (results package version 2.2.0.1):
  There are several more supported scanners.
- fix-buffer-overflow.patch is no longer needed (fixed in source).
* Tue Jul 04 2006 jsmeix@suse.de
- replace-HZ-by-sysconf_SC_CLK_TCK.patch replaces the fixed HZ
  compile-time value (no longer supported by new glibc)
  by the more correct sysconf(_SC_CLK_TCK) runtime value.
* Wed Jun 28 2006 jsmeix@suse.de
- fix-buffer-overflow.patch fixes a too small char array
  which causes a buffer overflow if SANE_DEBUG_EPKOWA is set.
* Mon Jun 26 2006 jsmeix@suse.de
- Updated to version 2.1.0-1 (results package version 2.1.0.1):
  The disable-nonfree.patch is no longer needed because the
  new "configure --disable-frontend" option builds it without
  the %_bindir/iscan frontend which is the only part which still
  would require proprietary binary-only i386-only software.
  All proprietary binary-only i386-only stuff was removed from the
  sources (i.e. the libesmod library and the EAPL license files).
* Mon Jun 12 2006 ro@suse.de
- remove unused gnome-vfs and oaf from BuildRequires
* Wed Feb 01 2006 jsmeix@suse.de
- Distinguish the no longer supported models in the description
  file but do not remove them because otherwise they would be
  no longer shown in YaST (i.e. no longer any user information
  that those models would work with the iscan package).
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Jan 13 2006 jsmeix@suse.de
- Re-enabled the patches which remove the no longer
  supported models from the "sane-epkowa" man page
  and from the "epkowa.desc" description file.
* Fri Jan 13 2006 jsmeix@suse.de
- Updated to version 1.18.0-1 (results package version 1.18.0.1).
* Tue Nov 22 2005 jsmeix@suse.de
- Added -fno-strict-aliasing to the CXXFLAGS to avoid problems
  in jpegstream.cc (lines 180, 195).
* Mon Oct 10 2005 jsmeix@suse.de
- Added missing forward declarations of friend functions.
* Wed Oct 05 2005 jsmeix@suse.de
- Updated to version 1.17.0-1 (results package version 1.17.0.1).
* Tue Sep 27 2005 jsmeix@suse.de
- Made a free version by removing all non-free stuff.
  For an overview see the README or the package description.
  In particular there is no longer the GIMP plugin link
  to the frontend %_bindir/iscan because it was removed.
* Mon Aug 08 2005 jsmeix@suse.de
- Added GIMP plugin link (see "man iscan"
  and %_docdir/packages/iscan/README).
* Mon Aug 01 2005 jsmeix@suse.de
- Added the USB usermap file to the iscan package to have the
  USB manufacturer and model IDs available for scanner detection.
* Tue Jul 26 2005 jsmeix@suse.de
- Updated to version 1.15.0-2 (results package version 1.15.0.2).
- Removed obsolete fixes for GCC4 (gcc4.diff).
- Added epkowa.desc to the iscan package.
- Copy epkowa.desc via "triggerin" to the sane package location.
* Fri Jul 01 2005 jsmeix@suse.de
- Use RPM_OPT_FLAGS
* Fri Apr 22 2005 jsmeix@suse.de
- Updated to version 1.14.0-3 (results package version 1.14.0.3).
- Added fixes for GCC4 (gcc4.diff).
- Removed obsolete patch for epkowa.conf (see Jan 25 2005).
* Tue Mar 22 2005 jsmeix@suse.de
- Added PreReq.
* Mon Mar 07 2005 ro@suse.de
- block provides for libsane.so.1 (in sane package only)
* Thu Feb 17 2005 jsmeix@suse.de
- Update to version 1.13.1-1 (results package version 1.13.1.1).
* Tue Feb 15 2005 jsmeix@suse.de
- Using '%%triggerin -- sane' to add the 'epkowa' backend to
%_sysconfdir/sane.d/dll.conf so that now sane can be re-installed
  from scratch without the need to re-install iscan too.
* Wed Jan 26 2005 jsmeix@suse.de
- Replaced '/usr/lib' by %%{_libdir} to be prepared for 64-bit
  but at the moment it cannot be built on non-i386 platforms
  because of the proprietary binary-only i-386-only libesmod.so
* Tue Jan 25 2005 jsmeix@suse.de
- Changed the wrong "usb ..." entry in epkowa.conf so that the
  epkowa backend can autodetect its known USB scanners.
- If the package was removed then remove the epkowa lines
  in %_sysconfdir/sane.d/dll.conf
* Wed Jan 19 2005 jsmeix@suse.de
- Update to version 1.13.0-3 (results package version 1.13.0.3).
- Removed the redundant requirement for resmgr.
- Simplified the RPM post install script to add the epkowa
  backend disabled (with leading '#') to %_sysconfdir/sane.d/dll.conf
* Mon Jul 19 2004 jsmeix@suse.de
- Added libieee1284 because sane has now libieee1284 support
  and therefore ican links itself to libieee1284 libraries too.
- To be safe added an explicite requirement for resmgr
  because libusb requires resmgr.
* Thu Jun 24 2004 jsmeix@suse.de
- initial version
