%define rname alt-app-starter

Name: %rname
Version: 1.1.2
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: The tool to run programs as another user
License: GPLv2

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kdesu-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kpty-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: plasma5-workspace-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
Requires: qt5-translations

%description
Alt-App-Starter is the tool to quick run programs as another user

%prep
%setup -n %rname-%version

%build
%K5build 
lrelease-qt5 translations/alt-app-starter_ru.ts

%install
%K5install

# translations
mkdir -p %buildroot/%_qt5_translationdir/
install -m 0644 translations/*.qm %buildroot/%_qt5_translationdir/

%find_lang --with-qt --all-name %rname

%files -f %rname.lang
%doc COPYING*
%_K5bin/*
%_K5xdgapp/*.desktop

%changelog
* Fri Jan 24 2020 Pavel Moseev <mars@altlinux.org>  1.1.2-alt1
- fix user interface translation

* Thu Jan 23 2020 Pavel Moseev <mars@altlinux.org>  1.1.1-alt1
- fix application title icon (#37870)
- fix behavior of alt-app-starter utility after starting selected app. (#37871)
- removed unused interface elements (#37873)

* Mon Jan 13 2020 Pavel Moseev <mars@altlinux.org>  1.1.0-alt1
- First version. Initial build

