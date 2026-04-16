Name: qlipper
Version: 6.1.0
Release: alt1

Summary: Lightweight clipboard history
License: GPL-3.0-or-later
Group: Graphical desktop/Other

URL: https://github.com/pvanek/qlipper
VCS: https://github.com/pvanek/qlipper.git

Source0: %name-%version.tar
#Source1: qlipper_ru.ts
Source2: qlipper-startup.desktop
Patch: %name-%version-%release.patch
#Patch0: qlipper-5.1.1-cmake-ru.patch
#Patch1: qlipper-5.1.1-desktop-ru.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: qt6-tools-devel
BuildRequires: kf6-kguiaddons-devel

%description
Lightweight clipboard history applet.

%prep
%setup
%autopatch -p1

%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.h' |
	xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-validate %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_sysconfdir/xdg/autostart
install -pm644 %SOURCE2 %buildroot%_sysconfdir/xdg/autostart/

%find_lang %name --with-qt --without-mo

%files -f %name.lang
%doc COPYING
%doc README
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/128x128/apps/qlipper.png
%_sysconfdir/xdg/autostart/qlipper-startup.desktop
%dir %_datadir/%name
%dir %_datadir/%name/translations

%changelog
* Thu Apr 16 2026 Anton Midyukov <antohami@altlinux.org> 6.1.0-alt1
- New version 6.1.0.

* Sun Dec 21 2025 Anton Midyukov <antohami@altlinux.org> 6.0.0-alt1
- New version 6.0.0.

* Wed Jun 04 2025 Anton Midyukov <antohami@altlinux.org> 5.1.2-alt3.20241029.1
- new snapshot
- build with qt6

* Wed May 04 2022 Anton Midyukov <antohami@altlinux.org> 5.1.2-alt2
- autostart in LXQt only (Closes: 42674)
- clean Packager

* Tue Aug 13 2019 Anton Midyukov <antohami@altlinux.org> 5.1.2-alt1
- new version 5.1.2

* Fri Jun 21 2019 Michael Shigorin <mike@altlinux.org> 5.1.1-alt5
- E2K: strip UTF-8 BOM for lcc < 1.24
- Drop remainders of %%ubt use
- Minor spec cleanup

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt4
- NMU: remove %%ubt from release

* Sat Jun 16 2018 Anton Midyukov <antohami@altlinux.org> 5.1.1-alt3
- Rebuilt for aarch64

* Thu Mar 22 2018 Anton Midyukov <antohami@altlinux.org> 5.1.1-alt2
- Added autostart

* Tue Mar 06 2018 Anton Midyukov <antohami@altlinux.org> 5.1.1-alt1
- Initial build for ALT (thanks Rosa Team for russian translation)
