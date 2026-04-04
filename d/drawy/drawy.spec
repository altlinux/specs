%define oname org.kde.drawy
%define apiversion 1.0.0
%define soname 0

Name: drawy
Version: 20260405
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
BuildRequires: kf6-syntax-highlighting-devel

%description
Drawy is a work-in-progress infinite whiteboard tool written in Qt/C++,
which aims to be a native-desktop alternative to the amazing web-based Excalidraw.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%{name}gui%soname = %EVR
Requires: lib%{name}widgets%soname = %EVR
Requires: libstandardformplugin%soname = %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n lib%{name}gui%soname
Group: System/Libraries
Summary: %name library
%description -n lib%{name}gui%soname
%name library.

%package -n lib%{name}widgets%soname
Group: System/Libraries
Summary: %name library
%description -n lib%{name}widgets%soname
%name library.

%package -n libstandardformplugin%soname
Group: System/Libraries
Summary: %name library
%description -n libstandardformplugin%soname
%name library.

%prep
%setup
#seted lib devel path
subst 's|DrawyCore|include/DrawyCore|' src/gui/CMakeLists.txt

%build
%K6cmake
%K6make

%install
%K6install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc *.md LICENSES
%_bindir/%name
%_libdir/qt?/plugins/drawypluginforms/*.so
%_datadir/applications/%oname.desktop
%_iconsdir/hicolor/*/*/*.png
%_datadir/metainfo/%oname.metainfo.xml
%_datadir/qlogging-categories?/%name.categories

%files devel
%_libdir/kf?/devel/*.so
%_includedir/DrawyCore

%files -n lib%{name}gui%soname
%_libdir/lib%{name}gui.so.%soname
%_libdir/lib%{name}gui.so.%apiversion

%files -n lib%{name}widgets%soname
%_libdir/lib%{name}widgets.so.%soname
%_libdir/lib%{name}widgets.so.%apiversion

%files -n libstandardformplugin%soname
%_libdir/libstandardformplugin.so.%soname
%_libdir/libstandardformplugin.so.%apiversion

%changelog
* Sun Apr 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260405-alt1
- updated to git.38e5b3c856

* Sun Mar 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260327-alt1
- updated to git.4909273ea6

* Sun Mar 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260321-alt1
- updated to git.0127c29998

* Sun Mar 15 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260315-alt1
- updated to git.b2a2567c74

* Tue Mar 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260309-alt1
- updated to git.6d6ebd1b1d

* Sun Mar 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 20260228-alt1
- updated to git.170e895b33

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
