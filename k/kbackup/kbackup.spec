%define rname kbackup

Name: %rname
Version: 26.04.2
Release: alt2

Group: Graphical desktop/KDE
Summary: Backup program with an easy-to-use interface
License: GPL-2.0-or-later
Url: https://invent.kde.org/utilities/kbackup

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kstatusnotifieritem-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: pkgconfig(libarchive)

%description
Kbackup is a program that lets you back up any directories or files. It
uses an easy to use directory tree to select the things to back up and
lets you save your settings in "profile" files. These are simple textfiles containing definitions for directories and files to be included or
excluded from the backup process.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_K6bin/*%{rname}*
%_K6xdgapp/*%{rname}*
%_K6icon/hicolor/*/*/*%{rname}*
%_K6icon/hicolor/*/*/*kbp*
%_K6data/metainfo/*%{rname}*
%_K6xdgmime/*%{rname}*

%changelog
* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt2
- update packaging

* Fri Jun 05 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.2-alt1
- New version 26.04.2.

* Thu May 07 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.1-alt1
- New version 26.04.1.

* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.0-alt1
- New version 26.04.0.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.3-alt1
- New version 25.12.3.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.2-alt1
- Initial build of kf6-based KBackup for Sisyphus
