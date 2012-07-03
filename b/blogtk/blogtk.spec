Name: blogtk
Version: 2.0
Release: alt1.1

Summary: Standalone blog entry poster
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://launchpad.net/blogtk/2.0/2.0/+download/%name-%version.tar

Url: http://blogtk.jayreding.com
License: Apache License
Group: Networking/Other

BuildArch: noarch

%py_requires libglade

%description
BloGTK is a weblog client that allows you to post to your weblog from Linux
without the need for a separate browser window. BloGTK allows you to connect
with many weblog systems such as Blogger, Movable Type, WordPress, and more.

%prep
%setup
chmod 644 data/*
%__subst 's|Exec=blogtk2|Exec=%name|' data/%name.desktop

# (Abel) eliminate runtime pygtk warnings
find -type f -name '*.py' -print0 | xargs -r -0 %__subst 's/gtk\.TRUE/True/g; s/gtk\.FALSE/False/g;'

%install
mkdir -p %buildroot%_datadir
cp -r share/blogtk2 %buildroot%_datadir

mkdir -p %buildroot/%_pixmapsdir
cp data/blogtk-icon.png %buildroot/%_pixmapsdir

mkdir -p %buildroot/%_desktopdir
cp data/blogtk.desktop %buildroot/%_desktopdir/

mkdir -p %buildroot/%_bindir
cp bin/blogtk2 %buildroot/%_bindir/%name

%files
%doc README ChangeLog AUTHORS
%_bindir/%name
%_datadir/blogtk2/
%_pixmapsdir/*
%_desktopdir/*
#%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1
- Rebuild with Python-2.7

* Sun Dec 05 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva!)

* Mon Jan 18 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.0-3mdv2010.1
+ Revision: 493194
- add missing BR (spotted by QA)

* Sun Jan 17 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.0-2mdv2010.1
+ Revision: 492773
- bump release (to ease upgrades in the future)

* Mon Dec 28 2009 Ahmad Samir <ahmadsamir@mandriva.org> 2.0-1mdv2010.1
+ Revision: 482960
- Update to 2.0
- Change URL and Source (now hosted on launchpad)
- Change License
- Clean spec

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1-9mdv2010.0
+ Revision: 413174
- rebuild

* Thu Dec 11 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-8mdv2009.1
+ Revision: 312912
- lowercase ImageMagick

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.1-8mdv2009.0
+ Revision: 218438
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 08 2007 Adam Williamson <awilliamson@mandriva.org> 1.1-7mdv2008.0
+ Revision: 82340
- rebuild for 2008
- fd.o icons
- correct errors in .desktop file
- drop legacy menu and icons
- drop patch, do it with a perl substitution instead
- spec clean

* Tue Oct 31 2006 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2006-10-31 22:48:20 (74823)
- add BuildRequires: desktop-file-utils

* Tue Oct 31 2006 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2006-10-31 22:45:29 (74822)
Import blogtk

* Thu Sep 28 2006 Lenny Cartier <lenny@mandriva.com> 1.1-5mdv2007.1
- fix xdg menu

- XDG

* Fri Nov 11 2005 Abel Cheung <deaddog@mandriva.org> 1.1-3mdk
- Eliminate pygtk runtime warnings

* Wed Aug 10 2005 Austin Acton <austin@mandriva.org> 1.1-2mdk
- requires gnome-python

* Fri Feb 04 2005 Austin Acton <austin@mandrake.org> 1.1-1mdk
- initial package

