%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: maui-booth
Version: 1.1.3
Release: alt1.git.bf21c036

Summary: Convergent camera app based on Maui framework
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://invent.kde.org/maui/maui-booth

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: libmauikit-devel

Requires: libmauikit
Requires: libkf6prisonscanner
Requires: libqt6-multimediaquick
Requires: libmauikit-filebrowsing

%description
%summary.

%prep
%setup
sed -i "s|Categories=Qt;KDE;AudioVideo;|Categories=Qt;KDE;AudioVideo;Recorder;Player;|" org.kde.booth.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang booth

# unify executable names even if there are no file conflicts
mv -v %buildroot%_bindir/booth %buildroot%_bindir/org.kde.booth
sed -i "s|Exec=booth|Exec=org.kde.booth|" %buildroot%_desktopdir/org.kde.booth.desktop

%files -f booth.lang
%_bindir/org.kde.booth
%_desktopdir/org.kde.booth.desktop
%_iconsdir/hicolor/scalable/apps/booth.svg
%_datadir/metainfo/org.kde.booth.appdata.xml

%changelog
* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 1.1.3-alt1.git.bf21c036
- Initial build for Sisyphus
