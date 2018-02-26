Name:           rsibreak
Version:        0.11
Release:        alt1
Summary:        A small utility which bothers you at certain intervals
Group:          Graphical desktop/KDE
License:        GPLv2+
URL:            http://www.rsibreak.org
Source0:        %{name}-%{version}.tar.bz2
Packager:	Dmitry M. Maslennikov <rlz at altlinux dot org>

BuildRequires:  gcc-c++
BuildRequires:  kde4libs-devel > 4.4

%description
RSIBreak is a small utility which bothers you at certain intervals. The
interval and duration of two different timers can be configured. You can
use the breaks to stretch out or do the dishes. The aim of this utility
is to let you know when it is time to have a break from your computer.
This can help people to prevent Repetive Strain Injury.

%prep
%setup -q

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %name
%K4find_lang plasma_applet_%name
cat plasma_applet_%name.lang >> %name.lang


%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS TODO
%_K4bindir/%name
%_K4xdg_apps/%name.desktop
%_K4apps/%name
%_K4apps/desktoptheme/default/widgets/%name.svg
%_K4start/%name.desktop
%_K4dbus_interfaces/org.%name.rsiwidget.xml
%_K4lib/plasma_*_%name.so
%_K4srv/plasma-*-%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/hicolor/*/actions/*.png
%_K4doc/*/%name

%changelog
* Fri Jan 13 2012 Andrey Cherepanov <cas@altlinux.org> 0.11-alt1
- New version 0.11
- Rewrite on KDE4

* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1.1.qa1
- Disable aRts support
- Adapt to new KDE3 placement

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for rsibreak

* Mon Apr 07 2008 Dmitry M. Maslennikov <rlz at altlinux.ru> 0.8.0-alt1
- initial build
