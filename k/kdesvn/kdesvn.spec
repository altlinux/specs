Name:           kdesvn
Version:        2.0.0
Release:        alt1
Summary:        A subversion client for KDE4 with KIO integration

Group:          Development/Tools
License:        GPLv2+
URL:            https://projects.kde.org/projects/extragear/sdk/kdesvn
# git clone git://anongit.kde.org/kdesvn
Source0:        %name-%{version}.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: gcc-c++
BuildRequires: subversion-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-ktextwidgets-devel

%description
KDESvn is a frontend to the subversion vcs. In difference to most other
tools it uses the subversion C-Api direct via a c++ wrapper made by
Rapid SVN and doesn't parse the output of the subversion client. So it
is a real client itself instead of a frontend to the command line tool.

It is designed for the K-Desktop environment and uses all of the goodies
it has. It is planned for future that based on the native client some
plugins for konqueror and/or kate will made.

%prep
%setup -q

%build
%K5init no_altplace
%K5build

%install
%K5install
%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING GPL.txt TODO
%_K5bin/kdesvn*
%_qt5_plugindir/*.so
%_qt5_plugindir/kf5/kded/*.so
%_K5srv/*
%_datadir/kconf_update/*
%_K5cfg/*.kcfg
%_K5dbus_iface/*
%_K5dbus_srv/*
%_K5icon/hicolor/*/*/*.png
%_K5icon/hicolor/*/*/*.svgz
%_K5xdgapp/*.desktop
%_K5xmlgui/%name
%_datadir/%name

%changelog
* Fri Jan 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version for KF5

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- New version

* Tue Oct 06 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt2
- Fix localization build

* Wed Mar 19 2014 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- First build KDE4 version for ALT Linux (ALT #29251)
