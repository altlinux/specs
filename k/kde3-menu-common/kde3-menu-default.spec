%def_without kde3_menu_original
%def_with original
Name: kde3-menu-common
Version: 0.05
Release: alt2
License: BSD

URL: http://altlinux.org/
Source: %name-%version.tar
Packager: Igor Vlasenko <viy@altlinux.org>
BuildArch: noarch

#package -n kde3-menu-common
Summary: common KDE3 menus
Group: Graphical desktop/KDE
Requires: kde3-menu-resources
Conflicts: kdebase-libs <= 3.5.12-alt9
Conflicts: kdelibs <= 3.5.12-alt7
Conflicts: kdemultimedia-libs <= 3.5.12-alt3

%if_with kde3_menu_original
%package -n kde3-menu-original
Summary: Original KDE3 menu.
Group: Graphical desktop/KDE
Requires: altlinux-menus
Requires: kde3-menu-resources
Requires: kde3-menu-common
Provides: kde3-freedesktop-menu
Conflicts: kdebase-libs <= 3.5.12-alt9
Conflicts: kdelibs <= 3.5.12-alt7
Conflicts: kdemultimedia-libs <= 3.5.12-alt3
%endif #kde3_menu_original

%if_with kde3_menu_original
%description -n kde3-menu-original
Original KDE3 menu.
%endif #kde3_menu_original

%description -n kde3-menu-common
Internal and private KDE3 menus (kcontrol, screen savers, etc)
shared among various KDE3 menu implementations.

%prep
%setup

%build

%install

mkdir -p %buildroot
find etc/kde*/xdg -name '*.menu' -exec sed -i -e 's,Directory>kde-,Directory>kde3/,' {} \;

mv usr etc %buildroot/

%files -n kde3-menu-common
%dir /etc/kde*/xdg/menus
%dir /etc/kde*/xdg/menus/applications-merged
/etc/kde*/xdg/menus/applications-merged/kde-essential.menu
/etc/kde*/xdg/menus/kde-information.menu
/etc/kde*/xdg/menus/kde-settings.menu
/etc/kde*/xdg/menus/kde-screensavers.menu

%if_with original
%if_with kde3_menu_original
%files -n kde3-menu-original
%_datadir/desktop-directories/kde3/multimedia-music.directory
/etc/kde*/xdg/menus/applications-merged/applications.menu
/etc/kde*/xdg/menus/applications-merged/kde-multimedia-music.menu
%else
%exclude %_datadir/desktop-directories/kde3/multimedia-music.directory
%exclude /etc/kde*/xdg/menus/applications-merged/applications.menu
%exclude /etc/kde*/xdg/menus/applications-merged/kde-multimedia-music.menu
%endif
%endif #kde3_menu_original


%changelog
* Sat Jun 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- disabled kde3-menu-original

* Tue Apr 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added kde3-menu-common subpackage

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- removed overlaps with altlinux-menus

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- use kde3-menu-resources

* Fri Apr 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- Initial build
