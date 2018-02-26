%def_with original
Name: kde4-menu-common
Version: 0.03
Release: alt1
License: BSD

URL: http://altlinux.org/
Source: %name-%version.tar
Packager: Igor Vlasenko <viy@altlinux.org>
BuildArch: noarch

#package -n kde4-menu-common
Summary: common KDE4 menus
Group: Graphical desktop/KDE
Requires: kde4-menu-resources
Conflicts: kde4libs <= 4.6.2-alt6
Conflicts: kde4base-runtime-core <= 4.6.2-alt1

%package -n kde4-menu-original
Summary: Original KDE4 menu.
Group: Graphical desktop/KDE
Requires: altlinux-menus
Requires: kde4-menu-resources
Requires: kde4-menu-common
Provides: kde4-freedesktop-menu = 0.02
Conflicts: kde4base-runtime-core <= 4.6.2-alt1

%description -n kde4-menu-original
Original KDE4 menu.

%description -n kde4-menu-common
Internal and private KDE4 menus
shared among various KDE4 menu implementations.

%prep
%setup

%build

%install

mkdir -p %buildroot
#find etc/kde*/xdg -name '*.menu' -exec sed -i -e 's,Directory>kde-,Directory>kde4/,' {} \;

mv etc %buildroot/

%files -n kde4-menu-common
%dir /etc/kde*/xdg/menus
%dir /etc/kde*/xdg/menus/applications-merged
/etc/kde*/xdg/menus/kde-information.menu

%if_with original
%files -n kde4-menu-original
/etc/kde*/xdg/menus/applications-merged/applications.menu
%else
%exclude /etc/kde*/xdg/menus/applications-merged/applications.menu
%endif

%changelog
* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added versioned provides for original menu

* Thu Apr 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- full build

* Wed Apr 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- bootstrap build
