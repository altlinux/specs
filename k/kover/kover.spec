Name: kover
Summary: WYSIWYG CD cover printer with CDDB support
Version: 6
Release: alt2.1
Source: %name-%version.tar.bz2
Source1: %name.desktop
Patch0: %name-fix-mimetypes.patch
Patch1: %name-4-gcc44.patch
Url: http://lisas.de/kover
Group: Archiving/Other
License: GPLv2+

BuildPreReq: rpm-macros-kde-common-devel

# Automatically added by buildreq on Tue May 11 2010
BuildRequires: gcc-c++ kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcddb-devel libxkbfile-devel

BuildRequires: libcdio-devel >= 0.90

%description
Kover is an easy to use WYSIWYG CD cover printer with CDDB support.

%prep
%setup
mkdir -p build

%build
%cmake
%cmake_build

%install
#install -D %SOURCE1 %buildroot/%_desktopdir/kde4/%name.desktop

%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS README NEWS THANKS ChangeLog
%_bindir/kover
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/locolor/*/apps/*.png
%_iconsdir/kover*
%_Kapps/%name
%_man1dir/*
%_K4xdg_mime/%name.xml
%_desktopdir/kde4/%name.desktop

%changelog
* Fri Jan 12 2018 Fr. Br. George <george@altlinux.ru> 6-alt2.1
- Rebuild for libcdio-2.0.0

* Mon Sep 14 2015 Fr. Br. George <george@altlinux.ru> 6-alt2
- Rebuild for new libcdio

* Mon Apr 14 2014 Fr. Br. George <george@altlinux.ru> 6-alt1
- Autobuild version bump to 6
- Fix build (switch to cmake)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue May 11 2010 Fr. Br. George <george@altlinux.ru> 4-alt1
- New version

* Tue Nov 17 2009 Fr. Br. George <george@altlinux.ru> 3-alt4
- libcdio soname change

* Thu Aug 27 2009 Fr. Br. George <george@altlinux.ru> 3-alt3
- Release bump to comply task 11609

* Tue Oct 28 2008 Fr. Br. George <george@altlinux.ru> 3-alt2
- GCC4.3 build fix

* Thu May 22 2008 Fr. Br. George <george@altlinux.ru> 3-alt1
- Initial build from MDV

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 3-4mdv2008.1
+ Revision: 141734
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 20 2007 Nicolas Lécureuil <neoclust@mandriva.org> 3-3mdv2008.0
+ Revision: 91460
- Fix File list
- Move kover in tools
- Install existing mimetype x-kover

* Sat Jul 14 2007 Adam Williamson <awilliamson@mandriva.com> 3-1mdv2008.0
+ Revision: 52158
- rebuild for 2008
- clean file list
- update MIME database and icon cache in %%post
- drop old menu file
- install menu entry to the right place and correct it
- buildrequires libcdio and libcddb (app now uses these)
- specify license as GPLv2 or later
- drop sourced icons (not needed)
- drop patch (no longer needed, larger values are now default upstream)
- new release 3
- Import kover

- Rebuild to generate category

* Mon May 08 2006 Laurent MONTEL <lmontel@mandriva.com> 2.9.6-4
- Rebuild to generate category

- Add patch2 : Fix ticket #20442
- clean spec
- use mkrel

* Fri Jul 08 2005 Laurent MONTEL <lmontel@mandriva.com> 2.9.6-2mdk
- Rebuild

* Fri Nov 12 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.9.6-1mdk
- 2.9.6
- cleanups

* Tue Oct 26 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.9.5-4mdk
- fix deps and build on lib64 platforms

* Thu Aug 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.5-3mdk
- Remove explicite dependance on kdebase

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.5-2mdk
- Rebuild

* Mon May 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.5-1mdk
- 2.9.5

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.3-1mdk
- 2.9.3

* Fri Jul 18 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.1-5mdk
- Rebuild

* Fri Apr 25 2003 Marcel Pol <mpol@gmx.net> 2.9.1-4mdk
- buildrequires

* Mon Mar 03 2003 Marcel Pol <mpol@gmx.net> 2.9.1-3mdk
- fix buildrequires

* Sat Mar 01 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.1-2mdk
- Rebuild

* Fri Feb 21 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.9.1-1mdk
- 2.9.1

* Wed Oct 16 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.8.7-1mdk
- 2.8.7

* Sat Aug 17 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.8.6-3mdk
- Rebuild against gcc-3.2

* Sat Jul 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.8.6-2mdk
- Rebuild against gcc-3.2

* Wed Jul 24 2002  Lenny Cartier <lenny@mandrakesoft.com> 2.8.6-1mdk
- 2.8.6

* Tue Jul 09 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.8.5-3mdk
- patch1: libtool tag

* Sat Jun 01 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.8.5-2mdk
- Rebuild

* Sat May 25 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.8.5-1mdk
- new version

* Fri Jan 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.3-2mdk
- Fix spec file

* Tue Nov 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.3-1mdk
- Update code (0.8.3)

* Tue Oct 23 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.8-2mdk
- fixes by Claudio Panichi <sorcla@tiscalinet.it> :
	- Added missing files
	- Added menu entry
	- Fixed permissions on source file

* Wed Oct 17 2001 Claudio Panichi <sorcla@tiscalinet.it> 0.8-1mdk
- First personal RPM for Linux Mandrake =:o)
