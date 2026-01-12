%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mauikit-calendar
Version: 4.0.2
Release: alt1

Summary: Calendar support components for Maui applications
License: LGPL-3.0-only
Group: Development/KDE and QT
Url: https://invent.kde.org/maui/mauikit-calendar

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: libmauikit-devel
BuildRequires: akonadi-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: akonadi-calendar-devel
BuildRequires: kf6-kcalendarcore-devel
BuildRequires: kidentitymanagement-devel
BuildRequires: akonadi-contacts-devel
BuildRequires: kf6-kcontacts-devel
BuildRequires: kf6-ktexttemplate-devel
BuildRequires: akonadi-mime-devel
BuildRequires: kcalutils-devel

# no akonadi-calendar-devel
ExcludeArch: %ix86 riscv64

Requires: libmauikit
Requires: libqt6-qml
Requires: libqt6-quick
Requires: libqt6-quickcontrols2
Requires: libqt6-quicklayouts

%description
%summary.

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}
%summary. Library files for %name.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}-devel
%summary. Development files for %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang mauikitcalendar

%files -f mauikitcalendar.lang
%doc README.md
%dir %_libdir/qt6/qml/org/mauikit/calendar
%_libdir/qt6/qml/org/mauikit/calendar/*

%files -n lib%{name}
%_libdir/libMauiKitCalendar4.so.4
%_libdir/libMauiKitCalendar4.so.4.0.2

%files -n lib%{name}-devel
%dir %_includedir/MauiKit4/Calendar
%_includedir/MauiKit4/Calendar/calendar_export.h
%_includedir/MauiKit4/Calendar/calendar_version.h
%_includedir/MauiKit4/Calendar/moduleinfo.h
%dir %_libdir/cmake/MauiKitCalendar4
%_libdir/cmake/MauiKitCalendar4/MauiKitCalendar4Config.cmake
%_libdir/cmake/MauiKitCalendar4/MauiKitCalendar4ConfigVersion.cmake
%_libdir/cmake/MauiKitCalendar4/MauiKitCalendar4Targets-noconfig.cmake
%_libdir/cmake/MauiKitCalendar4/MauiKitCalendar4Targets.cmake
%_libdir/libMauiKitCalendar4.so

%changelog
* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 4.0.2-alt1
- Initial build for Sisyphus
