%define nameL luisbocanegra.smart.video.wallpaper.reborn
%define nameLC plasma_applet_luisbocanegra.smart.video.wallpaper.reborn

Name: kde-plasma-addon-smart-video-wallpaper-reborn
Version: 2.1.0
Release: alt1

Summary: Plasma 6 wallpaper plugin to play videos on your Desktop/Lock Screen
License: GPL-2.0
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2139746
Vcs: https://github.com/luisbocanegra/plasma-smart-video-wallpaper-reborn

Source0: %name-%version.tar
Source1: ru.po

BuildArch: noarch

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules gcc-c++ pkgconfig(Qt6Qml)
BuildRequires: qt6-multimedia-devel plasma6-lib-devel kf6-kpackage-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kwindowsystem-devel gettext-tools

Requires: ffmpeg

%description
%summary

%prep
%setup

cp -r %SOURCE1 package/translate/

%build
%K6cmake
%K6make

for locale in el_GR es nl pt_BR ru; do
 msgfmt package/translate/${locale}.po -o package/translate/${locale}.mo
done


%install
%K6install

for locale in el_GR es nl pt_BR ru; do
 install -Dm 0644 package/translate/${locale}.mo %buildroot%_datadir/locale/${locale}/LC_MESSAGES/%nameLC.mo
done

%files
%_datadir/metainfo/%nameL.appdata.xml
%exclude %_datadir/plasma/wallpapers/%nameL/translate
%_datadir/locale/*/LC_MESSAGES/%nameLC.mo
%_datadir/plasma/wallpapers/%nameL/*
%doc README.md

%changelog
* Sun Mar 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux.
