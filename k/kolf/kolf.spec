%define rname kolf

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Games/Arcade
Summary: Miniature golf
Url: http://www.kde.org
License: BSD-3-Clause

Provides:  kde5-kolf = %EVR
Obsoletes: kde5-kolf < %EVR
Provides:  kde5-kolf-common = %EVR
Obsoletes: kde5-kolf-common < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: qt6-phonon-devel
BuildRequires: kf6-kio-devel kf6-kdoctools-devel kf6-ki18n-devel kf6-ktextwidgets-devel
BuildRequires: kde6-libkdegames-devel

%description
Kolf is a miniature golf game with 2d top-down view.
Courses are dynamic, and up to 10 people can play at once in competition.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kolf
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6bin/kolf
%_K6icon/*/*/apps/kolf.*
%_K6xdgapp/org.kde.kolf.desktop
%_K6data/kolf/
%_datadir/metainfo/*.xml

%changelog
* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build
