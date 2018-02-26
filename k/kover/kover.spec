Name:		kover
Summary:	WYSIWYG CD cover printer with CDDB support
Version:	4
Release:	alt1
Source:		http://lisas.de/kover/%name-%version.tar.bz2
Source1:	%name.desktop
Patch0:		%name-fix-mimetypes.patch
Patch1:		%name-4-gcc44.patch
Url:		http://lisas.de/kover
Group:		Archiving/Other
Packager:.	Fr. Br. George <george@altlinux.ru>
License:	GPLv2+

BuildPreReq:	rpm-macros-kde-common-devel

# Automatically added by buildreq on Tue May 11 2010
BuildRequires: gcc-c++ kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcddb-devel libcdio-devel libxkbfile-devel

%description
Kover is an easy to use WYSIWYG CD cover printer with CDDB support.

%prep
%setup -q
%patch1 -p1
mkdir -p build

%build
cd build
cmake .. \
    -DCMAKE_SKIP_RPATH:BOOL=yes \
    -DCMAKE_BUILD_TYPE=MinSizeRel \
    -DCMAKE_C_FLAGS:STRING='-pipe -Wall -O2' \
    -DCMAKE_CXX_FLAGS:STRING='-pipe -Wall -O2' \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DLIB_DESTINATION=lib64 \
    %if "lib64" == "lib64" 
    -DLIB_SUFFIX="64"
    %else 
    -DLIB_SUFFIX=""
    %endif 

%make_build

%install
install -D %SOURCE1 %buildroot/%_desktopdir/kde4/%name.desktop

cd build
%makeinstall DESTDIR=%buildroot
cd -
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

* Thu Sep 20 2007 Nicolas LÃ©cureuil <neoclust@mandriva.org> 3-3mdv2008.0
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

* Mon Jun 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.9.6-5mdv2007.0
- Rebuild to generate category

* Mon May 08 2006 Laurent MONTEL <lmontel@mandriva.com> 2.9.6-4
- Rebuild to generate category

* Mon Jan 16 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.9.6-3mdk
- Add patch2 : Fix ticket #20442
- clean spec
- use mkrel

* Fri Jul 08 2005 Laurent MONTEL <lmontel@mandriva.com> 2.9.6-2mdk
- Rebuild

* Fri Nov 12 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 2.9.6-1mdk
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

* Thu Nov 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.3-1mdk
- Update code (0.8.3)

* Tue Oct 23 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.8-2mdk
- fixes by Claudio Panichi <sorcla@tiscalinet.it> :
	- Added missing files
	- Added menu entry
	- Fixed permissions on source file

* Wed Oct 17 2001 Claudio Panichi <sorcla@tiscalinet.it> 0.8-1mdk
- First personal RPM for Linux Mandrake =:o)
