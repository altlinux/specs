Name: clamtk
Version: 4.40
Release: alt1

Summary: Easy to use front-end for ClamAV

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: Perl
Group: File tools
Url: http://clamtk.sourceforge.net/

BuildArch: noarch

Source: http://prdownloads.sf.net/%name/%name-%version.tar
Patch: %name-gtk.patch

Requires: clamav >= 0.83
Requires(post,postun): desktop-file-utils

# Automatically added by buildreq on Sun Feb 07 2010 (-bi)
BuildRequires: perl-Date-Calc perl-File-Find-Rule perl-Gtk2 perl-Locale-gettext perl-Net-DNS perl-libwww vixie-cron

%description
ClamTk is a front-end, point and click gui for ClamAV on Linux systems.
It supports easy signature-updates. It is meant to be lightweight and easy to use.

%prep
%setup
#%patch
# we place it in standard place
%__subst "s|.*/usr/lib.*||g" %name

%install
install -D -m755 %name %buildroot%_bindir/%name
mkdir -p %buildroot%perl_vendor_privlib/ClamTk
cp lib/*.pm %buildroot%perl_vendor_privlib/ClamTk/

install -D -m0644 images/%name.png %buildroot%_pixmapsdir/%name.png
install -D -m0644 clamtk.1.gz %buildroot%_man1dir/clamtk.1.gz
install -D -m0644 clamtk.desktop %buildroot%_desktopdir/clamtk.desktop

for n in po/*.mo; do
	install -D -m0644 $n %buildroot%_datadir/locale/`basename $n .mo`/LC_MESSAGES/clamtk.mo
done

%find_lang %name

%files -f %name.lang
%doc README DISCLAIMER CHANGES LICENSE
%_bindir/%name
%perl_vendor_privlib/ClamTk/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_man1dir/*

%changelog
* Sun May 27 2012 Vitaly Lipatov <lav@altlinux.ru> 4.40-alt1
- new version 4.40 (with rpmrb script)

* Sun Feb 07 2010 Vitaly Lipatov <lav@altlinux.ru> 4.23-alt1
- new version (4.23) import in git

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 4.11-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for clamtk
  * postclean-05-filetriggers for spec file

* Wed Apr 08 2009 Vitaly Lipatov <lav@altlinux.ru> 4.11-alt1
- new version 4.11 (with rpmrb script) (ALT bug #19532)

* Sun Nov 02 2008 Vitaly Lipatov <lav@altlinux.ru> 4.02-alt1
- new version 4.02
- update russian translation
- set noarch

* Thu Jul 03 2008 Vitaly Lipatov <lav@altlinux.ru> 3.10-alt1
- new version 3.10 (with rpmrb script)
- cleanup spec

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 3.06-alt1
- new version 3.06 (with rpmrb script)

* Thu Sep 13 2007 Vitaly Lipatov <lav@altlinux.ru> 3.02-alt1
- new version 3.02 (with rpmrb script)

* Sun Jul 29 2007 Vitaly Lipatov <lav@altlinux.ru> 2.99-alt1
- new version 2.99 (with rpmrb script)
- fix ru.po encoding

* Sat Jun 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.32-alt1
- new version 2.32 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.31-alt1
- new version 2.31 (with rpmrb script)

* Tue Mar 13 2007 Vitaly Lipatov <lav@altlinux.ru> 2.30-alt1
- new version 2.30 (with rpmrb script)

* Wed Jan 17 2007 Vitaly Lipatov <lav@altlinux.ru> 2.27-alt0.1
- new version 2.27 (with rpmrb script)
- update icon name in spec

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.26-alt0.1
- new version 2.26 (with rpmrb script)

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 2.24-alt0.1
- new version 2.24 (with rpmrb script)

* Sat Jul 29 2006 Vitaly Lipatov <lav@altlinux.ru> 2.22-alt0.1
- new version 2.22, rewrite spec, update buildreqs
- add localization (thanks Dave for motivate me to russian translation)

* Fri Jul 28 2006 Vitaly Lipatov <lav@altlinux.ru> 2.21-alt0.1
- new version 2.21 (with rpmrb script)

* Sun Jun 18 2006 Vitaly Lipatov <lav@altlinux.ru> 2.20-alt0.1
- new version 2.20 (with rpmrb script)
- update buildreq

* Tue May 16 2006 Vitaly Lipatov <lav@altlinux.ru> 2.19-alt0.1
- new version 2.19 (with rpmrb script)

* Wed Mar 22 2006 Vitaly Lipatov <lav@altlinux.ru> 2.16-alt0.1
- new version 2.16
- cleanup spec

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 2.15-alt0.1
- new version

* Sat Jan 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.14-alt1
- new version

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 2.13-alt1
- new version

* Mon Dec 26 2005 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt1
- new version

* Tue Nov 29 2005 Vitaly Lipatov <lav@altlinux.ru> 2.10-alt1
- new version

* Sat Nov 26 2005 Vitaly Lipatov <lav@altlinux.ru> 2.09-alt1
- new version

* Tue Sep 06 2005 Vitaly Lipatov <lav@altlinux.ru> 2.06-alt1
- new version

* Fri Jul 15 2005 Vitaly Lipatov <lav@altlinux.ru> 2.03-alt0.1
- first build for ALT Linux Sisyphus

* Tue Feb 28 2005 Dave M <dave.nerd@gmail.com> - 1.0.6
- Updated to release 1.0.6
- Added perl-DateManip rpm to Requires list.

* Tue Feb 26 2005 Dave M <dave.nerd@gmail.com> - 1.0.5
- Updated to release 1.0.5

* Tue Feb 21 2005 Dave M <dave.nerd@gmail.com> - 1.0.4
- Updated to release 1.0.4
- Tweaked spec file, and added Packager line.

* Tue Feb 20 2005 Dave M <dave.nerd@gmail.com> - 1.0.3
- Updated to release 1.0.3

* Tue Feb 19 2005 Dave M <dave.nerd@gmail.com> - 1.0.2
- Updated to release 1.0.2

* Tue Feb 13 2005 Dave M <dave.nerd@gmail.com> - 1.0.1
- Updated to release 1.0.1

* Tue Feb 12 2005 Dave M <dave.nerd@gmail.com> - 1.0
- Updated to release 1.0
- Added files LICENSE, CHANGES and TODO to doc

* Tue Feb 11 2005 Dave M <dave.nerd@gmail.com> - 1.0-rc2
- Updated to release 1.0-rc2

* Tue Feb 10 2005 Dave M <dave.nerd@gmail.com> - 1.0-rc1
- Updated to release 1.0-rc1

* Tue Feb 08 2005 Dave M <dave.nerd@gmail.com> - 0.9.9.9-1
- Updated to release 0.9.9.9.
- Removed unnecessary clamav-milter dependency.

* Tue Feb 04 2005 Dave M <dave.nerd@gmail.com> - 0.9.9.8
- Initial release 0.9.9.8.
