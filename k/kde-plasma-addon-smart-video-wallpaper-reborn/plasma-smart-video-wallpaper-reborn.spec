%define nameL luisbocanegra.smart.video.wallpaper.reborn
%define nameLC plasma_wallpaper_luisbocanegra.smart.video.wallpaper.reborn

Name: kde-plasma-addon-smart-video-wallpaper-reborn
Version: 2.4.0
Release: alt1.1

Summary: Plasma 6 wallpaper plugin to play videos on your Desktop
License: GPL-2.0
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2139746
Vcs: https://github.com/luisbocanegra/plasma-smart-video-wallpaper-reborn

Source0: %name-%version.tar
Source1: ru.po

Patch: metadata-2.4.0-alt-fixes.patch

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
cp -r -f %SOURCE1 package/translate/
%patch -p0

%build
%K6cmake
%K6make

%install
%K6install

for locale in el_GR es nl pt_BR ru; do
 msgfmt package/translate/${locale}.po -o package/translate/${locale}.mo
 install -Dm 0644 package/translate/${locale}.mo %buildroot%_datadir/locale/${locale}/LC_MESSAGES/%nameLC.mo
done

%find_lang %nameLC --with-kde --all-name

%files -f %nameLC.lang
%_datadir/metainfo/%nameL.appdata.xml
%exclude %_datadir/plasma/wallpapers/%nameL/translate
%_datadir/plasma/wallpapers/%nameL/*
%doc README.md

%changelog
* Sun Nov 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.4.0-alt1.1
- spec cleanup

* Sat Nov 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.4.0-alt1
- 2.3.2 -> 2.4.0

* Sat Jun 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.3.2-alt1
- 2.3.1 -> 2.3.2

* Sun Jun 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.3.1-alt1
- 2.3.0 -> 2.3.1

* Thu May 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.3.0-alt1
- 2.2.0 -> 2.3.0
- Changes:
    + better Desktop Effects settings UI/UX
    + skip crossfade on manual switch and use a smoother easing type
    + port dbus calls to org.kde.plasma.workspace.dbus
    + port lock screen dbus method polling to ActiveChanged signal

* Fri Apr 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.0-alt1
- 2.1.0 -> 2.2.0

* Sun Apr 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.1.0-alt3
- Corrected russian translate (thnx katze_942@).

* Sat Apr 05 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.1.0-alt2
- Fixed upstream code for localizations to work.
- Created and added russian translate.

* Sun Mar 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux.
