Name:           rsibreak
Version:        0.12.3
Release:        alt1
Summary:        A small utility which bothers you at certain intervals
Group:          Graphical desktop/KDE
License:        GPLv2+
URL:            http://www.rsibreak.org
Source0:        %{name}-%{version}.tar.bz2
Packager:	Dmitry M. Maslennikov <rlz at altlinux dot org>

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kauth-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-purpose-devel
BuildRequires: kf5-solid-devel
BuildRequires: libkf5quickaddons

BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kidletime-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-sonnet-devel

BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-kdoctools

%description
RSIBreak is a small utility which bothers you at certain intervals. The
interval and duration of two different timers can be configured. You can
use the breaks to stretch out or do the dishes. The aim of this utility
is to let you know when it is time to have a break from your computer.
This can help people to prevent Repetive Strain Injury.

%prep
%setup -q

%build
%K5init no_altplace
%K5build

%install
%K5install
%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS TODO
%_K5bin/%name
%_K5xdgapp/%name.desktop
%_K5start/%{name}_autostart.desktop
%_K5dbus_iface/org.%name.rsiwidget.xml
%_K5notif/%name.notifyrc
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/hicolor/*/actions/*.png

%changelog
* Tue Jun 14 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.3-alt1
- New version
- Build with KF5

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
