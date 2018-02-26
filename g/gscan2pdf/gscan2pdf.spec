%def_without test

Name: gscan2pdf
Version: 1.0.4
Release: alt1

Summary: A GUI to ease the process of producing a multipage PDF from a scan
Group: Office
License: GPL

Url: http://gscan2pdf.sourceforge.net/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name/%version/%name-%version.tar

BuildArch: noarch

# perl(Gtk2/Ex/PodViewer.pm) at line 3501 (depth 4) inside eval SKIP
Requires: perl(Gtk2/Ex/PodViewer.pm) xdg-utils unpaper

# Automatically added by buildreq on Wed Feb 16 2011 (-bi)
BuildRequires: perl-Archive-Tar perl-Config-General perl-Goo-Canvas perl-Gtk2-Ex-Simple-List perl-Gtk2-ImageView perl-Locale-gettext perl-Log-Log4perl perl-PDF-API2 perl-Proc-ProcessTable perl-Readonly perl-Set-IntSpan perl-Test-Pod perl-XML-Simple perl-threads

BuildPreReq: perl-Magick perl-Sane >= 0.05

# ImageMagick
Requires: %_bindir/convert

Requires: perl-Magick

# %_bindir/cjb2
Requires: djvu-utils

# tiffcp
Requires: libtiff-utils

# OCR:
Requires: cuneiform

%description
At maturity, the GUI will have similar features to that of the Windows Imaging
program, but with the express objective of writing a PDF, including metadata.

Scanning is handled with SANE via scanimage. PDF conversion is done by libtiff.

%prep
%setup
#__subst "s|use Gtk2 -init;|use Gtk2; INIT { Gtk2->init; }|g" bin/%name
# djvu %_bindir/cjb2
%__subst "s|requires djvulibre-bin|djvu-utils|g" bin/%name

%build
%perl_vendor_build
#__subst "s|^test .*||g" Makefile
%make_build

# used Gtk2
#check
#make test

%install
%makeinstall_std INSTALLSITELIB=%perl_vendor_privlib INSTALLSITESCRIPT=%_bindir
find %buildroot -name perllocal.pod | xargs rm -f
find %buildroot -name .packlist | xargs rm -f

%find_lang %name

%files -f %name.lang
%doc History
%_bindir/gscan2pdf
%_bindir/scanadf-perl
%_bindir/scanimage-perl
%_desktopdir/%name.desktop
%_datadir/%name/
%_pixmapsdir/*
%perl_vendor_privlib/Gscan2pdf/
%perl_vendor_privlib/Gscan2pdf.pm

%changelog
* Thu Apr 12 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- new version 1.0.4 (with rpmrb script)

* Tue Apr 10 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Thu Mar 29 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Tue Feb 07 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Wed Feb 16 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.32-alt1
- new version 0.9.32 (with rpmrb script)
- add requires to libtiff-utils and ImageMagick, fix djvu-utils package name (closes: #24860)
- add cuneiform requires

* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.31-alt1
- new version (ALT bug 23475), fix build

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.23-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gscan2pdf
  * postclean-05-filetriggers for spec file

* Sat Mar 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.23-alt1
- new version 0.9.23 (with rpmrb script)

* Sun Jan 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.20-alt1
- new version 0.9.20
- cleanup spec, remove LICENCE file

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.19-alt1
- new version 0.9.19 (with rpmrb script)

* Sat Nov 17 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.18-alt1
- new version 0.9.18 (with rpmrb script)
- update buildreq

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.17-alt1
- new version 0.9.17 (with rpmrb script)

* Sun Sep 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.16-alt2
- fix update/clean menus

* Sun Aug 26 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.16-alt1
- new version 0.9.16 (with rpmrb script)
- add perl-Magick to buildreq

* Thu Jul 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.14-alt1
- new version 0.9.14 (with rpmrb script)

* Sat Jun 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.12-alt1
- new version 0.9.12 (with rpmrb script)

* Wed May 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt1
- new version 0.9.9 (with rpmrb script)

* Tue Apr 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- initial build for ALT Linux Sisyphus

* Thu Apr 05 2007 Jeffrey Ratcliffe <ra28145@users.sourceforge.net>
  - Fixed bug calling help
  - Fixed error message caused by update_options sub being called twice.
  - Streamlined image creation (speedup)
  - Adjusted widget justification in scan dialog
  - Suppressed rounded messages from scanadf frontend
  - Remembers scan area
  - Ghosts zoom and rotate buttons if no page selected
  - Fixed bug where custom scan area not hidden when A4 or Letter selected
  - Help update
