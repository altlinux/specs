%define oname org.kde.drawy

Name: drawy
Version: 20260218
Release: alt1

Summary: Drawy is a work-in-progress infinite whiteboard tool
License: GPL-3.0-or-later
Group: Graphics

Url: https://apps.kde.org/drawy
Vcs: https://invent.kde.org/graphics/drawy

ExcludeArch: i586

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules qt6-base-devel
BuildRequires: kf6-kcrash-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kwidgetsaddons-devel libzstd-devel
BuildRequires: qt6-tools-devel kf6-kconfig-devel qt6-declarative-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kxmlgui-devel kf6-ki18n-devel
BuildRequires: kf6-kcolorscheme-devel kf6-kiconthemes-devel

%description
Drawy is a work-in-progress infinite whiteboard tool written in Qt/C++,
which aims to be a native-desktop alternative to the amazing web-based Excalidraw.

%prep
%setup

%build
%K6cmake
%K6make

%install
%K6install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc *.md LICENSES
%_bindir/%name
%_libdir/*.so.*
%_datadir/applications/%oname.desktop
%_iconsdir/hicolor/*/*/*.png
%_datadir/metainfo/%oname.metainfo.xml
%_datadir/qlogging-categories?/%name.categories

%changelog
* Sun Feb 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260218-alt1
- updated to git.58006b218f

* Sun Feb 15 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260214-alt1
- updated to git.abdd884d8f

* Sun Feb 08 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260207-alt1
- updated to git.48340e15c4

* Wed Feb 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260203-alt1
- updated to git.10c401f7c8

* Tue Jan 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260119-alt1
- update to git.8319f1d6

* Sat Jan 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260116-alt1
- update to git.de18a497

* Wed Jan 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260113-alt1
- update to git.c2ab5a6c

* Mon Jan 12 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260111-alt1
- update to git.83e0f4e5

* Sat Jan 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260110-alt1
- Initial build for ALT Linux.
