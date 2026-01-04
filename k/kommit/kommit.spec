Name: kommit
Version: 1.8.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Git gui client for KDE
Url: https://invent.kde.org/sdk/kommit
License: GPLv3

Source: %name-%version.tar.gz
ExcludeArch: i586 armh


BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
Buildrequires: kf6-kdoctools kf6-kdoctools-devel kf6-kiconthemes-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-ktexteditor-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kparts-devel kf6-ktexteditor-devel
BuildRequires: kf6-kxmlgui-devel kf6-syntax-highlighting-devel
BuildRequires: libgit2-devel
BuildRequires: qt6-charts-devel
BuildRequires: qt6-svg-devel
BuildRequires: dolphin-devel

##gettext 
Requires: kf6-syntax-highlighting libkf6kiowidgets libkf6kiogui libkf6kiocore libgit2 libqt6-charts

%description
%summary.

%prep
%setup -n %name-%version
# fix category
%__subst 's|Categories=Development|Categories=Development;RevisionControl;|' src/data/*.desktop

%build
%K6build -DBUILD_WITH_QT6=ON -DCMAKE_BUILD_TYPE=MinSizeRel

%install
%K6install
%find_lang %name --with-kde --all-name


%files -f %name.lang
%_bindir/*
%_libdir/*
%_K6plug/dolphin/vcs/*.so
%_datadir/qlogging-categories6/*.*categories
%_desktopdir/*
%_K6icon/*/*/apps/*
%_datadir/metainfo/*.xml

%changelog
* Sun Jan 04 2026 Alexei Mezin <alexvm@altlinux.org> 1.8.1-alt1
- New version
  - switch to QT6
  - enable Dolphin plugin

* Sat Nov 16 2024 Alexei Mezin <alexvm@altlinux.org> 1.6.0-alt1
- New version
- Drop Dolphin5 integration

* Fri Jan 05 2024 Alexei Mezin <alexvm@altlinux.org> 1.3.1-alt1.2
- Add correct category to desktop files

* Fri Jan 05 2024 Alexei Mezin <alexvm@altlinux.org> 1.3.1-alt1.1
- Exclude 32bit arch: i586 and armh

* Fri Jan 05 2024 Alexei Mezin <alexvm@altlinux.org> 1.3.1-alt1
- Initial build


