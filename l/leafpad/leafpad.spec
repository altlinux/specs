Name: leafpad
Version: 0.8.18.1
Release: alt1

Summary: GTK+2 based notepad clone

License: GPL
Group: Editors
Url: http://tarot.freeshell.org/leafpad/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://savannah.nongnu.org/download/%name/%name-%version.tar

Patch1: leafpad-ru-update.patch

Requires(post,postun): desktop-file-utils
BuildPreReq: desktop-file-utils

# Automatically added by buildreq on Sat Jun 02 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel pkg-config
BuildRequires: intltool libgtk+2-devel

%description
Leafpad is a simple GTK+ based text editor. The user interface is
similar to "notepad", and it aims to be lighter than GEdit and KWrite
and to be as useful as them.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README
%_bindir/%name
%_pixmapsdir/*
%_iconsdir/hicolor/*/*/*g
%_desktopdir/*

%changelog
* Sat Jun 02 2012 Vitaly Lipatov <lav@altlinux.ru> 0.8.18.1-alt1
- new version 0.8.18.1 (with rpmrb script)

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.17-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for leafpad

* Thu Jan 14 2010 Vitaly Lipatov <lav@altlinux.ru> 0.8.17-alt1
- new version 0.8.17 (with rpmrb script)

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.16-alt1
- new version 0.8.16 (with rpmrb script)
- remove post/postun scripts

* Wed Aug 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.14-alt2
- update russian translation (thanks to cas@)

* Wed Apr 23 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.14-alt1
- new version 0.8.14 (with rpmrb script)

* Sun Oct 21 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.12-alt1
- new version 0.8.12 (with rpmrb script)

* Thu Jul 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.11-alt1
- new version 0.8.11 (with rpmrb script)
- update buildreqs
- add icons

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.9-alt1
- new version (0.8.9)
- remove desktop/pixmaps dir macroses
- cleanup spec, remove menu file
- update buildreqs

* Wed Jan 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt1
- new version

* Wed Oct 26 2005 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- new version

* Wed Aug 03 2005 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt1
- new version

* Sat May 28 2005 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- fix buildrequires
- new version

* Mon Apr 04 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7.9-alt1
- new version

* Thu Feb 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7.8-alt1
- first build for ALT Linux Sisyphus
- spec from PLD Team <feedback@pld-linux.org>
