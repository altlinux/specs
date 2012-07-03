# Spec file for Dillo

Name: dillo
Version: 0.8.6
Release: alt7

Summary: a small GTK+ web browser
Summary(ru_RU.UTF-8): компактный веб-браузер, написанный на GTK+
Group: Networking/WWW
License: %gpl2plus
Url: http://www.dillo.org

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

# Patch for i18n:  http://teki.jpn.ph/pc/software/index-e.shtml
Source0: %name-%version.tar.bz2
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Source4: %name.desktop

Patch0: %name-0.8.6-i18n-misc-20070916.diff.bz2
Patch1: %name-0.8.6-alt-as_needed.patch
Patch2: %name-0.8.6-alt-dillorc.patch
Patch3: %name-0.8.6-alt-automake_fix.patch
Patch4: %name-0.8.6-alt-CVE_2009_2294.patch
Patch5: %name-0.8.6-alt-gold.patch

AutoReqProv: yes
BuildPreReq: rpm-build-licenses
BuildPreReq: gcc-c++ gtk+-devel libfltk-devel libjpeg-devel libpng-devel
BuildPreReq: libssl-devel libXft-devel linux-libc-headers
BuildPreReq: glib-devel zlib-devel

%description
Dillo  is a small GTK+ based  (GNOME is NOT required!) web browser.
Dillo aims to be a multi-platform browser alternative that's small,
stable, developer-friendly, usable, fast, and extensible.

This build incorporated  an Dillo internationalization (i18n) patch
from   http://teki.jpn.ph/pc/software/index-e.shtml   and  provides
support for viewing pages  in different charsets, automatic charset
recognition, tabbed browsing,  GUI tool for configuration and a lot
of other improvements over original Dillo.

%description -l ru_RU.UTF-8
Dillo - основанный на GTK+ (но не требующий GNOME) небольшой
веб-браузер. Dillo стремиться быть альтернативным браузером,
кросс-платформенным, небольшим, стабильным, быстрым, простым
в использовании и легко расширяемым.

Данная сборка  включает в себя патч  для интернационализации Dillo
(Dillo i18n patch,   http://teki.jpn.ph/pc/software/index-e.shtml)
и обеспечивает поддержку просмотра страниц в различных кодировках,
автоматическое  распознавание кодировки страниц, табы, графическую
утилиту настройки  и много прочих улучшений по сравнению с простым
Dillo.

%prep
%setup -q
%patch4
%patch0 -p1
%patch1
%patch2
%patch3
%patch5

%build
%autoreconf
%configure --sysconfdir=%_sysconfdir/%name \
	    --enable-meta-refresh \
	    --disable-dlgui \
	    --enable-ipv6
#	    --disable-anti-alias
#	    --enable-rtfl
%make_build

%install
%makeinstall

mkdir -p -- %buildroot%_sysconfdir/%name
mv -- %buildroot%_sysconfdir/dillorc %buildroot/%_sysconfdir/%name/
mv -- %buildroot%_sysconfdir/dpidrc %buildroot/%_sysconfdir/%name/
%__subst 's@dpi_dir=.*$@dpi_dir=%_libdir/%name/dpi@' %buildroot/%_sysconfdir/%name/dpidrc


mkdir -p -- %buildroot%_miconsdir %buildroot%_liconsdir %buildroot%_niconsdir
install -m0644 -- %SOURCE1 %buildroot%_miconsdir/%name.png
install -m0644 -- %SOURCE2 %buildroot%_niconsdir/%name.png
install -m0644 -- %SOURCE3 %buildroot%_liconsdir/%name.png

mkdir -p -- %buildroot%_desktopdir
install -m 0644 -- %SOURCE4 %buildroot%_desktopdir/%name.desktop

rm -f -- doc/Makefile*

%find_lang %name

%files -f %name.lang
%_bindir/dillo
%_bindir/dillocfg
%_bindir/dpid
%_bindir/dpidc
%_libdir/dillo*
%exclude %_bindir/bm-update

%doc AUTHORS ChangeLog COPYING INSTALL NEWS README doc/

%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/dillorc
%config(noreplace) %_sysconfdir/%name/dpidrc

%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*
%_desktopdir/%name.desktop

%changelog
* Sat May 26 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt7
- Fix build with --no-copy-dt-needed-entries

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.8.6-alt6.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sun Jul 05 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt6
- Security fix (CVE-2009-2294) (Closes: 20680)

* Sat Nov 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt5
- Fix build with automake_1.9
- Remove obsolete update_menus/clean_menus calls

* Sun Jul 20 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt4
- Fix repocop issues on icon's dirs and desktop file

* Mon Feb 25 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt3
- Updating Dillo i18n patch to v. 20070916

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt2
- Fix typos in package description.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.6-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Wed Jul 19 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt1
- Revives from orphaned
- New version 0.8.6
- Build with i18n-misc patch
- Localization for dillorc
- Adding desktop file and icon

* Wed Aug 27 2003 Alexey Tourbin <at@altlinux.ru> 0.7.3-alt1
- 0.7.3
- old toolbar icons kept, I don't like new ones
- new icons for menufile(5) from http://www.dillo.org/Icons/
- dillorc: changed default geometry 640x550 -> 720x600

* Tue Jul 08 2003 Alexey Tourbin <at@altlinux.ru> 0.7.2-alt2
- most of the CVS changes applied (0.7.3 to be)
- pld-gzip_fallback.patch updated
- optimization: -Os (the binary claims to be as small as 265Kb)

* Mon May 12 2003 Alexey Tourbin <at@altlinux.ru> 0.7.2-alt1
- 0.7.2
- patches updated; pld-gzip_fallback.patch disabled
- fixed libpng3 build

* Mon Feb 24 2003 Alexey Tourbin <at@altlinux.ru> 0.7.0-alt2
- menu entry added; large png icon added (PLD)
- double-free/endless loop in pld-gzip_fallback.patch fixed

* Mon Feb 20 2003 Alexey Tourbin <at@altlinux.ru> 0.7.0-alt1
- initial revision, various patches integrated
