Name: gbrainy
Version: 1.20
Release: alt1

Summary: A brain teaser game and trainer to have fun and to keep your brain trained

License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/gbrainy

Packager: Ilya Shpigor <elly@altlinux.org>

Source: http://www.softcatala.org/~jmas/gbrainy/%name-%version.tar.gz

# Automatically added by buildreq on Sun Oct 25 2009
BuildRequires: glib2-devel glibc-devel-static intltool libgnome-sharp libnss-mysql mono-addins mono-addins-devel mono-mcs mono-devel libgnome-sharp-devel librsvg-devel librsvg

%description
gbrainy is a brain teaser game and trainer written for GNOME using Mono,
C# and Cairo.

Its mission is to provide a platform for creating different kinds of
brain-teasers and brain trainer games for GNOME.

%prep
%setup %name-%version

%build
%configure
%make

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README
%_bindir/*
%dir %_libdir/%name/
%_libdir/%name/%name.exe
%_libdir/%name/%name.exe.config
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_man6dir/*
%_pixmapsdir/*
%_gamesdatadir/%name

%changelog
* Tue Dec 01 2009 Ilya Shpigor <elly@altlinux.org> 1.20-alt1
- new version 1.20

* Sun Oct 25 2009 Ilya Shpigor <elly@altlinux.org> 1.12-alt1
- initial build for ALT Linux Sisyphus

* Sat Aug 22 2009 Frederik Himpe <fhimpe@mandriva.org> 1.12-1mdv2010.0
+ Revision: 419737
- update to new version 1.12

* Sun Jun 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.11-1mdv2010.0
+ Revision: 385900
- update to new version 1.11

* Sat Mar 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1-2mdv2009.1
+ Revision: 354880
- BuildRequires mono-addins
- Update to new version 1.1

* Fri Dec 26 2008 Frederik Himpe <fhimpe@mandriva.org> 1.01-1mdv2009.1
+ Revision: 319318
- Fix BuildRequires
- update to new version 1.01

* Wed Sep 03 2008 Funda Wang <fundawang@mandriva.org> 1.00-2mdv2009.0
+ Revision: 279411
- fix file list

* Mon Sep 01 2008 Frederik Himpe <fhimpe@mandriva.org> 1.00-1mdv2009.0
+ Revision: 278651
- Fix BuildRequires
- Update to version 1.00, adding config file to file list

* Fri Aug 22 2008 Funda Wang <fundawang@mandriva.org> 0.70-2mdv2009.0
+ Revision: 275022
- rebuild
- fix br in order to backport

* Sat Jun 21 2008 Funda Wang <fundawang@mandriva.org> 0.70-1mdv2009.0
+ Revision: 227757
- update to new version 0.70

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Apr 15 2008 Funda Wang <fundawang@mandriva.org> 0.61-1mdv2009.0
+ Revision: 193655
- BR gnome-sharp2-devel
- New version 0.61

* Sat Mar 08 2008 Funda Wang <fundawang@mandriva.org> 0.60-1mdv2008.1
+ Revision: 182089
- New version 0.60

* Sun Feb 24 2008 Funda Wang <fundawang@mandriva.org> 0.5.3-1mdv2008.1
+ Revision: 174264
- New version 0.53

* Fri Feb 08 2008 Funda Wang <fundawang@mandriva.org> 0.5.2-1mdv2008.1
+ Revision: 164029
- New version 0.52

* Sun Jan 27 2008 Funda Wang <fundawang@mandriva.org> 0.5.1-1mdv2008.1
+ Revision: 158577
- add missing file
- New version 0.51

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 Funda Wang <fundawang@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 111010
- fix file list
- drop patch0
- New version 0.41

* Fri Nov 09 2007 Funda Wang <fundawang@mandriva.org> 3mdv2008.1-current
+ Revision: 107078
- rebuild for new lzma

* Sun Oct 28 2007 Funda Wang <fundawang@mandriva.org> 0.3-2mdv2008.1
+ Revision: 102721
- fix startup script (bug#35093)

* Fri Oct 26 2007 Funda Wang <fundawang@mandriva.org> 0.3-1mdv2008.1
+ Revision: 102284
- More BR
- add filelist
- Import gbrainy
- create gbrainy

