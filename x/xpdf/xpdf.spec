%define urwdir /usr/share/fonts/type1/urw
%define srcurl ftp://ftp.foolabs.com/pub/xpdf
%def_without protections

Name: xpdf
Version: 3.03
Release: alt1

Summary: Portable Document Format (PDF) suite
License: GPLv2 or GPLv3
Group: Office

URL: http://www.foolabs.com/xpdf/
Source0: %srcurl/xpdf-%version.tar.gz

Source2: %srcurl/xpdf-cyrillic-2003-jun-28.tar.gz
Source3: %srcurl/xpdf-greek-2003-jun-28.tar.gz
Source4: %srcurl/xpdf-hebrew-2003-feb-16.tar.gz
Source5: %srcurl/xpdf-latin2-2002-oct-22.tar.gz
Source6: %srcurl/xpdf-turkish-2002-apr-10.tar.gz
Source7: %srcurl/xpdf-chinese-simplified-2004-jan-16.tar.gz
Source8: %srcurl/xpdf-chinese-traditional-2004-jan-16.tar.gz
Source9: %srcurl/xpdf-japanese-2004-jul-27.tar.gz
Source10: %srcurl/xpdf-korean-2005-jul-07.tar.gz
Source11: %srcurl/xpdf-thai-2002-jan-16.tar.gz
Source100: xpdf-16x16.png
Source101: xpdf-32x32.png
Source102: xpdf-48x48.png
Source103: xpdf.desktop

Patch2: xpdf-3.03-xpdfrc.patch

Patch5: xpdf-2.02-ext.patch
Patch6: xpdf-3.00-core.patch

Patch15: xpdf-3.00-papersize.patch
Patch16: xpdf-3.03-crash.patch
Patch17: xpdf-3.00-64bit.patch

Patch22: xpdf-3.02-additionalzoom.patch

Patch24: xpdf-3.02-fontlist.patch

# Debian patches:
Patch30: xpdf-3.03-permissions.patch
Patch31: xpdf-3.02-debian-add_accelerators.patch
# Proper stream encoding on 64bit platforms
Patch34: xpdf-debian-fix-444648.patch

Requires: fonts-type1-urw
Requires: urlview

# Finally: we choose openmotif
#BuildPreReq: openmotif-devel

# xpdf moans when xpdfrc points to thai files that does not installed.
# instead of editing xpdfrc when (un)installing xpdf-thai, we eliminate
# this package and move thai files to main xpdf package
Obsoletes: xpdf-thai

# Automatically added by buildreq on Fri Oct 01 2010
BuildRequires: gcc4.3-c++ imake libXp-devel libXpm-devel libfreetype-devel libopenmotif-devel xorg-cf-files

# xpdf now - virtual fileless package that depends on both splitted
# subpackages for compatability with previous versions
Requires: xpdf-reader = %version-%release
###Requires: xpdf-utils = %version-%release
#!!! As of xpdf-3.02-alt6 xpdf-utils nuked (obsoleted by poppler)
#!!! So now 'xpdf' package no more needed but we will not touch it

%description
Xpdf is a suite of tools for Portable Document Format (PDF) files.
PDF files are sometimes called Acrobat files, after Adobe Acrobat
(Adobe's PDF viewer).

This package is intended for compatibility with previous versions of this
package only. You can safely remove it from your system.

%package common
Summary: Portable Document Format (PDF) suite -- common files
Group: Office
BuildArch: noarch

%description common
Xpdf is an X Window System based viewer for Portable Document Format (PDF)
files. PDF files are sometimes called Acrobat files, after Adobe Acrobat
(Adobe's PDF viewer).

This package contains common files needed by the other xpdf packages.

%package reader
Summary: Portable Document Format (PDF) suite -- viewer for X11
Group: Office
Requires: %name-common = %version-%release

%description reader
Xpdf is an X Window System based viewer for Portable Document Format (PDF)
files. PDF files are sometimes called Acrobat files, after Adobe Acrobat
(Adobe's PDF viewer).

This package contains xpdf itself, a PDF viewer for X11. xpdf is designed to
be small and efficient. xpdf supports encrypted PDF files. Standard X fonts,
Truetype fonts and Type 1 fonts are supported.

This package also contains pdftoppm, a utility for converting PDF files to
Portable Pixmap formats (PBM, PGM, PPM).

See also the xpdf-utils package for conversion utilities and the other xpdf-*
packages for additional language support.

%package chinese-simplified
Summary: ISO-2022-CN, EUC-CN and GBK encoding support for xpdf
Group: Office
Requires: %name-common = %version-%release
BuildArch: noarch

%description chinese-simplified
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.) 
This package provides support files needed to use the Xpdf tools with
Chinese-simplified PDF files.

%package chinese-traditional
Summary: Big5 and Big5ascii encoding support for xpdf
Group: Office
Requires: %name-common = %version-%release
BuildArch: noarch

%description chinese-traditional
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.) 
This package provides support files needed to use the Xpdf tools with
Chinese-traditional PDF files.

%package japanese
Summary: ISO-2022-JP, EUC-JP and Shift-JIS encoding support for xpdf
Group: Office
Requires: %name-common = %version-%release
BuildArch: noarch

%description japanese
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.) 
This package provides support files needed to use the Xpdf tools with
Japanese PDF files.

%package korean
Summary: ISO-2022-KR (KSX1001) encoding support for xpdf
Group: Office
Requires: %name-common = %version-%release
BuildArch: noarch

%description korean
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.) 
This package provides support files needed to use the Xpdf tools with
Korean PDF files.

%prep
%setup -q -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11

%patch2 -p1

%patch5 -p1
%patch6 -p1

%patch15 -p1
%patch16 -p1
%patch17 -p1

%patch22 -p1

%patch24 -p1

%patch30 -p1
%patch31 -p1

%patch34 -p1

%build
# Not sure about --enable-multithreaded and --enable-wordlist options
# Now they are enabled (as in PLD), but this is subject to reevaluation.
# --enable-a4-paper removed. Why? See xpdf-3.00-papersize.patch.

export CXXFLAGS="%optflags %optflags_nocpp"
export CXX="g++-4.3"
%configure \
	--without-t1-library \
	--enable-opi \
		--enable-multithreaded \
		--enable-wordlist \
	--enable-freetype2 \
	--with-freetype2-includes=%_includedir/freetype2

make urwdir=%urwdir

subst 's@/usr/local/etc/@%_sysconfdir/@' doc/*.1 doc/*.5
subst 's@/usr/local/share/ghostscript/fonts@%urwdir@' doc/sample-xpdfrc doc/*.1 doc/*.5
subst 's@^#displayFontT1@displayFontT1@' doc/sample-xpdfrc

for i in cyrillic greek hebrew latin2 turkish \
         chinese-simplified chinese-traditional japanese korean thai; do
	subst 's@/usr/local/share/xpdf@%_datadir/xpdf@' \
		xpdf-$i/add-to-xpdfrc \
		xpdf-$i/README
	echo >> doc/sample-xpdfrc
	cat xpdf-$i/add-to-xpdfrc >> doc/sample-xpdfrc
	rm xpdf-$i/add-to-xpdfrc
done

# xpdf no longer supports X fonts
subst 's/^displayCIDFontX/#displayCIDFontX/g' doc/sample-xpdfrc

%install
%makeinstall_std
for i in cyrillic greek hebrew latin2 turkish \
         chinese-simplified chinese-traditional japanese korean thai; do
	mkdir -p %buildroot%_datadir/xpdf/$i
	cp -a xpdf-$i/* %buildroot%_datadir/xpdf/$i/
done


install -pD -m644 %_sourcedir/xpdf.desktop %buildroot%_desktopdir/xpdf.desktop
# mdk icons
install -pD -m644 %_sourcedir/xpdf-16x16.png %buildroot%_miconsdir/xpdf.png
install -pD -m644 %_sourcedir/xpdf-32x32.png %buildroot%_niconsdir/xpdf.png
install -pD -m644 %_sourcedir/xpdf-48x48.png %buildroot%_liconsdir/xpdf.png

%files

%files common
%doc CHANGES README
%config(noreplace) %_sysconfdir/xpdfrc
%_man5dir/*
%dir %_datadir/xpdf
%_datadir/xpdf/cyrillic
%_datadir/xpdf/greek
%_datadir/xpdf/hebrew
%_datadir/xpdf/latin2
%_datadir/xpdf/thai
%_datadir/xpdf/turkish

%files reader
%_bindir/xpdf
%exclude %_bindir/pdf*
%_desktopdir/*
%_man1dir/xpdf*
%exclude %_man1dir/pdf*
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png

%files chinese-simplified
%_datadir/xpdf/chinese-simplified

%files chinese-traditional
%_datadir/xpdf/chinese-traditional

%files japanese
%_datadir/xpdf/japanese

%files korean
%_datadir/xpdf/korean

%changelog
* Sun Aug 28 2011 Victor Forsiuk <force@altlinux.org> 3.03-alt1
- 3.03

* Wed Mar 30 2011 Victor Forsiuk <force@altlinux.org> 3.02-alt11
- Build without t1lib to close denial of service vulnerability. This fix should
  address CVE-2011-0764. See also http://www.kb.cert.org/vuls/id/376500.

* Thu Oct 14 2010 Victor Forsiuk <force@altlinux.org> 3.02-alt10
- Security fixes: CVE-2010-3702, CVE-2010-3704.

* Mon Oct 04 2010 Victor Forsiuk <force@altlinux.org> 3.02-alt9
- Re-apply patch for removing pdf restrictions check. Closes bug: #9923.
- Better .desktop file.

* Fri Oct 01 2010 Victor Forsiuk <force@altlinux.org> 3.02-alt8
- Compile with g++-4.3 due to scrolling speed regression with gcc 4.4.x.

* Sun Nov 15 2009 Victor Forsyuk <force@altlinux.org> 3.02-alt7
- Apply xpdf-3.02pl4 security patch to fix:
  CVE-2009-3603, CVE-2009-3604, CVE-2009-3605, CVE-2009-3606,
  CVE-2009-3608, CVE-2009-3609.

* Tue Jul 07 2009 Victor Forsyuk <force@altlinux.org> 3.02-alt6
- Drop the xpdf-utils subpackage. Let poppler provides those utilities.

* Wed Apr 22 2009 Victor Forsyuk <force@altlinux.org> 3.02-alt5
- Apply xpdf-3.02pl3 security patch to fix:
  CVE-2009-0146, CVE-2009-0147, CVE-2009-0166, CVE-2009-0799,
  CVE-2009-0800, CVE-2009-1179, CVE-2009-1180, CVE-2009-1181,
  CVE-2009-1182, CVE-2009-1183, CVE-2009-1187, CVE-2009-1188.
- Remove obsolete install time scripts.
- Build language support packages as noarch.
- Apply bunch of debian and RH patches.

* Mon Apr 14 2008 Victor Forsyuk <force@altlinux.org> 3.02-alt4
- Desktop file mime entry fix.

* Mon Nov 12 2007 Victor Forsyuk <force@altlinux.org> 3.02-alt3
- Security fixes:
  - CVE-2007-4352
  - CVE-2007-5392
  - CVE-2007-5393

* Wed Aug 08 2007 Victor Forsyuk <force@altlinux.org> 3.02-alt2
- Security fix, see CVE-2007-3387.

* Mon Mar 05 2007 Victor Forsyuk <force@altlinux.org> 3.02-alt1
- New version.

* Tue May 23 2006 Victor Forsyuk <force@altlinux.ru> 3.01-alt6
- Fix build with gcc4.
- Switch from Debian-style menu to .desktop file.
- Fix BTS#9300.

* Fri Mar 03 2006 Victor Forsyuk <force@altlinux.ru> 3.01-alt5
- Fix program icon locations.

* Sat Feb 18 2006 Victor Forsyuk <force@altlinux.ru> 3.01-alt4
- Security patch to fix CVE-2006-0301.

* Fri Jan 13 2006 Victor Forsyuk <force@altlinux.ru> 3.01-alt3
- Security fix (CVE-2005-3191). Apply both recent security patches
  from Fedora package.

* Wed Dec 07 2005 Victor Forsyuk <force@altlinux.ru> 3.01-alt2pl1
- Security fix (CAN-2005-3193).
- Updated japanese and korean support packages.
- Fix allocation size for 64bit architecture.
- Fix to don't use freetype internals.
- Apply upstream patch to fix resize/redraw.

* Fri Aug 19 2005 Victor Forsyuk <force@altlinux.ru> 3.01-alt1
- 3.01
- Reworked remove_protections patch.

* Mon Aug 15 2005 Victor Forsyuk <force@altlinux.ru> 3.00-alt6pl3
- Add patch to fix xpdf DoS, CAN-2005-2097.
- Updated buildreqs.

* Wed Jan 19 2005 Victor Forsyuk <force@altlinux.ru> 3.00-alt5pl3
- Add patch to address CAN-2005-0064.
- Add patch to set 'match' as default psPaperSize.
- Fix bug #5659 (patch from Debian).

* Wed Dec 22 2004 Victor Forsyuk <force@altlinux.ru> 3.00-alt4pl2
- Add patch to address CAN-2004-1125 vulnerability.

* Tue Nov 16 2004 Victor Forsyuk <force@altlinux.ru> 3.00-alt3
- Fix build with new (post-2.1.5) freetype2.

* Thu Oct 21 2004 Stanislav Ievlev <inger@altlinux.org> 3.00-alt2
- bump release number for sisyphus

* Mon Oct 18 2004 Stanislav Ievlev <inger@altlinux.org> 3.00-alt1.1
- sec fix

* Thu May 06 2004 Victor Forsyuk <force@altlinux.ru> 3.00-alt1
- New version.
- Updated language support packages.
- Enable multithread and wordlist configure options.
- Added mimetypes to menu and change menu section.

* Wed Oct 22 2003 Victor Forsyuk <force@altlinux.ru> 2.03-alt1
- New version.
- Updated cyrillic and greek support packages.
- Added patch (PLD) for disabling print and copy protection.
- Added patch (RHL) for secure temp file creation.
- Added patch (RHL) to fix huge memory leak.
- Final decision: build with openmotif :))
- Better subpackages split (Debian-like).

* Mon Oct 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.02pl1-alt1.1
- Rebuilt with libt1.so.5

* Thu Jun 19 2003 Victor Forsyuk <force@altlinux.ru> 2.02pl1-alt1
- security update

* Sun Feb 02 2003 Victor Forsyuk <force@altlinux.ru> 2.01-alt3
- move thai language support to main xpdf package
- openmotif cause warning messages on stderror when exiting xpdf
  and we have patch to avoid SEGV with lesstif, so switch back
  to lesstif.

* Wed Jan 08 2003 Victor Forsyuk <force@altlinux.ru> 2.01-alt2
- added official security patch (pdfto* can be used as filters)
- added nonumericlocale patch to avoid SEGV caused by LC_NUMERIC with ',' as
  decimal point
- added "-fno-exceptions -fno-rtti" to CXXFLAGS
- switch from xpdf-handle-url to url_handler.sh (provided by urlview package)

* Tue Dec 17 2002 Victor Forsyuk <force@altlinux.ru> 2.01-alt1
- new version
- switch from lesstif to openmotif: fixes BTS #0001657 and #0001737

* Wed Nov 06 2002 Victor Forsyuk <force@altlinux.ru> 2.00-alt1
- new version
- use freetype2 unconditionally
- add build requirement for t1lib-devel
- purge eliminated configure parameters
- move out asian languages support (huge!) to separate packages
- install xpdf-url-handler script to be used as urlCommand

* Mon Oct 28 2002 AEN <aen@altlinux.ru> 1.01-alt1
- new spec from MDK
- new version

* Mon Oct 29 2001 AEN <aen@logic.ru> 0.93-alt2
- built with freetype2

* Mon Oct 29 2001 AEN <aen@logic.ru> 0.93-alt1
- new version

* Thu Dec 07 2000 AEN <aen@logic.ru>
- new version
- build for RE
* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 0.91-7mdk
- Rebuild with gcc-2.96 & glibc-2.2

* Mon Oct 09 2000 Daouda Lo <daouda@mandrakesoft.com> 0.91-6mdk
- build with generic optflags (ghibo )

* Mon Oct 09 2000 Daouda Lo <daouda@mandrakesoft.com> 0.91-5mdk
- icons

* Sat Oct 07 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.91-4mdk
- fixed 0.91-t1urw patch.

* Sat Oct 07 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.91-3mdk
- re-adapted patch 0.90-t1urw to version 0.91 (it allows to use
  Type1 URW fonts for standard PDF 14 fonts for better quality).

* Fri Oct 06 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.91-2mdk
- fixed a typo in %post and %postun scripts.
- added icons.
- added rgb, patch from RedHat.
- enabled opi.

* Tue Aug 15 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.91-1mdk
- s|0.90|0.91| aka decrypt me babe.
- remove the font patch.

* Wed Aug 09 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.90-11mdk
- BM
- spechelper

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.90-10mdk
- automatically added BuildRequires

* Fri Apr 21 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.90-9mdk
- removed xpdf.desktop also from the %install stage.

* Sat Apr 01 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.90-8mdk
- updated for t1lib 1.0.1.
- added things for new menu entry.
- removed xpdf.desktop.

* Thu Mar 02 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.90-7mdk
- increased default antialias font level from low to high. Files look
  nicer.

* Tue Feb 08 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 0.90-6mdk
- Correct the URL in the spec file
- remove egcs as build require

* Thu Jan 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.90-5mdk
- Fix build as non-root.

* Sat Dec 18 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- fixed a bug for Times-Italic and Helvetica-BoldOblique name in URW fonts.

* Tue Dec 07 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix for gcc-2.95.

* Fri Nov 11 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- built for Oxygen.

* Mon Sep 27 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- added patch to use aliased Type 1 URW fonts by default for standard
  14 PDF fonts.
- added Preston Brown <pbrown@redhat.com>'s zapf patch.

* Wed Aug 11 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- update to version 0.90.
- strip binaries.
- added t1lib dependencies.

* Thu May  6 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- converted wmconfig to desktop entry

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Nov 30 1998 Preston Brown <pbrown@redhat.com>
- updated to 0.80

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- patched to compile with new, stricter egcs

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.7a

* Thu Nov 20 1997 Otto Hammersmith <otto@redhat.com>
- added changelog
- added wmconfig
