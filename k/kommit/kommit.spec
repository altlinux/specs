Name: kommit
Version: 1.6.0
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Git gui client for KDE
Url: https://invent.kde.org/sdk/kommit
License: GPLv3

Source: %name-%version.tar.gz
ExcludeArch: i586 armh


BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel
Buildrequires: kf5-kdoctools kf5-kdoctools-devel 
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-ktexteditor-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kparts-devel kf5-ktexteditor-devel
BuildRequires: kf5-kxmlgui-devel kf5-syntax-highlighting-devel
BuildRequires: libgit2-devel
BuildRequires: qt5-charts-devel
##gettext 
Requires: kf5-syntax-highlighting libkf5kiowidgets libkf5kiogui libkf5kiocore libgit2 libqt5-charts

%description
%summary.

%prep
%setup -n %name-%version
# fix category
%__subst 's|Categories=Development|Categories=Development;RevisionControl;|' src/data/*.desktop

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name


%files -f %name.lang
%_bindir/*
%_libdir/*
##%_K5plug/dolphin/vcs/*.so
%_datadir/qlogging-categories5/*.*categories
%_desktopdir/*
%_K5icon/*/*/apps/*
%_K5icon/*/*/actions/*
%_datadir/metainfo/*.xml

%changelog
* Sat Nov 16 2024 Alexei Mezin <alexvm@altlinux.org> 1.6.0-alt1
- New version
- Drop Dolphin5 integration

* Fri Jan 05 2024 Alexei Mezin <alexvm@altlinux.org> 1.3.1-alt1.2
- Add correct category to desktop files

* Fri Jan 05 2024 Alexei Mezin <alexvm@altlinux.org> 1.3.1-alt1.1
- Exclude 32bit arch: i586 and armh

* Fri Jan 05 2024 Alexei Mezin <alexvm@altlinux.org> 1.3.1-alt1
- Initial build


