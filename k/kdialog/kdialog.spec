%define rname kdialog

Name: %rname
Version: 24.08.1
Release: alt1
%K6init no_altplace

Group: Graphical desktop/KDE
Summary: Utility to display GUI dialog boxes from shell scripts
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-kdialog = %EVR
Obsoletes: kde5-kdialog < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-ktextwidgets-devel kf6-knotifications-devel kf6-kiconthemes-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel
BuildRequires: libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel
BuildRequires: libXxf86misc-devel libXxf86vm-devel libxkbfile-devel

%description
kdialog allows you to display dialog boxes from shell scripts.
The syntax is very much inspired from the "dialog" command
(which shows text mode dialogs).

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kdialog*
%_K6xdgapp/*kdialog*.desktop
#%_K6dbus_iface/org.kde.kdialog.ProgressDialog.xml
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

