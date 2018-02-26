
Name: altlinux-menus
Version: 0.5.1
Release: alt1

Summary: ALT Linux menu
License: GPL
Group: System/Base
Url: http://www.altlinux.ru

BuildArch: noarch

Source: %name-%version.tar.gz

%description
The package contains an implementation of the draft "Desktop Menu
Specification" from http://www.freedesktop.org/Standards/menu-spec/

%prep
%setup -q


%build


%install
mkdir -p -m0755 %buildroot/{%_desktopdir,%_datadir/desktop-directories,%_sysconfdir/xdg/menus/applications{,-altlinux}-merged}

# install menu spec
install -m0644 applications.menu %buildroot/%_sysconfdir/xdg/menus/applications.menu
install -m0644 applications-altlinux.menu %buildroot/%_sysconfdir/xdg/menus/applications-altlinux.menu
install -m0644 applications-merged.menu %buildroot/%_sysconfdir/xdg/menus/applications-merged/applications.menu
install -m0644 applications-merged.menu %buildroot/%_sysconfdir/xdg/menus/applications-altlinux-merged/applications-altlinux.menu
touch %buildroot/%_desktopdir/defaults.list

# install directories
for f in *.directory
do
    install -m0644 "$f" %buildroot/%_datadir/desktop-directories/
done
#install -m0644 altlinux-main.directory %buildroot/%_datadir/desktop-directories/altlinux-main.directory


%files
%config %_sysconfdir/xdg/menus/applications.menu
%config %_sysconfdir/xdg/menus/applications-altlinux.menu
%dir %_sysconfdir/xdg/menus/applications-merged
%dir %_sysconfdir/xdg/menus/applications-altlinux-merged
%ghost %_sysconfdir/xdg/menus/applications-merged/applications.menu
%ghost %_sysconfdir/xdg/menus/applications-altlinux-merged/applications-altlinux.menu
#
%_desktopdir/defaults.list
%_datadir/desktop-directories/altlinux-*.directory

%changelog
* Mon Aug 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- add %_desktopdir/defaults.list

* Fri Aug 21 2009 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- move menu to applications-altlinux.menu to easy merging
- update default layout

* Fri Jul 24 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- update default layout
- remove applications-alt.menu inclusion

* Mon Oct 01 2007 Sergey V Turchin <zerg at altlinux dot org> 0.3.0-alt2
- add ownership of %_sysconfdir/xdg/menus/applications-merged/applications.menu

* Wed Sep 06 2006 Sergey V Turchin <zerg at altlinux dot org> 0.3.0-alt1
- add altlinux-settings.directory

* Wed Feb 08 2006 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt2
- remove %_sysconfdir/xdg/menus/applications-merged/applications.menu

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- add empty file in applications-merged to be owner

* Tue Jan 31 2006 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt2
- add catalog %_sysconfdir/xdg/menus/applications-merged

* Tue Dec 06 2005 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1
- move /etc/xsg/menus/applicataions-alt.menu to menu package
- include /etc/xsg/menus/applicataions-alt.menu by default

* Fri Jun 17 2005 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt2
- remove ownership of /etc/xsg/menus and /usr/share/desktop-directories

* Thu Mar 31 2005 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1
- remove KDELegacyDirs
- add symlink to debian menu spec

* Tue Mar 22 2005 Sergey V Turchin <zerg at altlinux dot org> 0.0.1-alt1
- initial spec
