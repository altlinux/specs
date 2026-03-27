%define nameL luisbocanegra.smart.video.wallpaper.reborn
%define nameLC plasma_wallpaper_luisbocanegra.smart.video.wallpaper.reborn

Name: plasma-addon-smart-video-wallpaper-reborn
Version: 2.12.0
Release: alt1

Summary: Plasma 6 wallpaper plugin to play videos on your Desktop
License: GPL-2.0
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2139746
Vcs: https://github.com/luisbocanegra/plasma-smart-video-wallpaper-reborn

Source: %name-%version.tar

BuildArch: noarch

Provides: kde-plasma-addon-smart-video-wallpaper-reborn = %EVR
Obsoletes: kde-plasma-addon-smart-video-wallpaper-reborn < %EVR

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules gcc-c++ pkgconfig(Qt6Qml)
BuildRequires: qt6-multimedia-devel plasma6-lib-devel kf6-kpackage-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kwindowsystem-devel gettext-tools
BuildRequires: kf6-ki18n-devel

Requires: ffmpeg

%description
%summary

%prep
%setup

%build
%K6cmake
%K6make

%install
%K6install

for locale in el_GR es nl pt_BR ru zh_CN; do
 msgfmt translate/${locale}.po -o translate/${locale}.mo
 install -Dm 0644 translate/${locale}.mo %buildroot%_datadir/locale/${locale}/LC_MESSAGES/%nameLC.mo
done

%find_lang %nameLC --with-kde --all-name

%files -f %nameLC.lang
%_datadir/metainfo/%nameL.appdata.xml
%_datadir/plasma/wallpapers/%nameL/*
%doc README.md

%changelog
* Sat Mar 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.12.0-alt1
- 2.11.0 -> 2.12.0

* Tue Mar 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.11.0-alt1
- 2.10.0 -> 2.11.0

* Fri Feb 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.10.0-alt1
- 2.9.0 -> 2.10.0

* Wed Jan 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.9.0-alt1
- 2.8.1 -> 2.9.0

* Tue Dec 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.8.1-alt1
- 2.8.0 -> 2.8.1

* Thu Dec 11 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.8.0-alt1
- 2.7.1 -> 2.8.0

* Thu Dec 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.7.1-alt1
- 2.7.0 -> 2.7.1

* Sat Nov 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.7.0-alt1
- 2.6.0 -> 2.7.0

* Sun Nov 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.6.0-alt1
- 2.5.1 -> 2.6.0
- fix: restore *.patch for localizations to work

* Sat Nov 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.5.1-alt1
- 2.4.0 -> 2.5.1

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
