%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: heaptrack
Version: 1.5.0
Release: alt3

Summary: A heap memory profiler for Linux 

License: LGPL-2.1
Group: Development/Other
Url: https://www.kde.org
VCS: https://github.com/KDE/heaptrack.git

%K6init man

Source: %name-%version.tar
Patch1: fix-gcc14-cmake-compat.patch
Patch2: 0001-Support-KChart6-for-KF6.patch
Patch3: 0002-Use-QString-for-KConfigGroup-names.patch
Patch4: 0003-Drop-unused-kitemmodels-dependency.patch
Patch5: 0004-Use-QPalette-instead-of-KColorScheme.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: gcc-c++ cmake extra-cmake-modules ctest
BuildRequires: libunwind-devel zlib-devel libzstd-devel
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel
BuildRequires: libdwarf-devel
BuildRequires: qt6-base-devel qt6-svg-devel qt6-declarative-devel
BuildRequires: kf6-kcoreaddons-devel kf6-ki18n-devel kf6-threadweaver-devel kf6-kconfigwidgets-devel kf6-kio-devel kde6-kdiagram-devel kf6-kiconthemes-devel
BuildRequires: librobin-map-devel
BuildRequires: elfutils-devel

%description
Heaptrack traces all memory allocations and annotates these events with stack traces.
Dedicated analysis tools then allow you to interpret the heap memory profile to:

- find hotspots that need to be optimized to reduce the **memory footprint** of your application
- find **memory leaks**, i.e. locations that allocate memory which is never deallocated
- find **allocation hotspots**, i.e. code locations that trigger a lot of memory allocation calls
- find **temporary allocations**, which are allocations that are directly followed by their deallocation

%package devel
Summary: Development files for %name
Group: Development/C

Requires: %name = %EVR

%description devel
Heaptrack traces all memory allocations and annotates these events with stack traces.
Dedicated analysis tools then allow you to interpret the heap memory profile to:

- find hotspots that need to be optimized to reduce the **memory footprint** of your application
- find **memory leaks**, i.e. locations that allocate memory which is never deallocated
- find **allocation hotspots**, i.e. code locations that trigger a lot of memory allocation calls
- find **temporary allocations**, which are allocations that are directly followed by their deallocation

This package contains development files for %name.

%package gui
Summary: GUI for %name
Group: Development/Tools

Requires: %name = %EVR

%description gui
Heaptrack traces all memory allocations and annotates these events with stack traces.
Dedicated analysis tools then allow you to interpret the heap memory profile to:

- find hotspots that need to be optimized to reduce the **memory footprint** of your application
- find **memory leaks**, i.e. locations that allocate memory which is never deallocated
- find **allocation hotspots**, i.e. code locations that trigger a lot of memory allocation calls
- find **temporary allocations**, which are allocations that are directly followed by their deallocation

This package contains GUI for %name.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

rm -f screenshots/.directory

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%K6build -DHEAPTRACK_USE_QT6:BOOL=ON

%install
%K6install
%find_lang --with-kde %name

%files -f %name.lang
%doc LICENSES README.md screenshots
%_bindir/%name
%_bindir/%{name}_print
%_libdir/%name

%files devel
%_includedir/*

%files gui
%_bindir/%{name}_gui
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/metainfo/*.appdata.xml

%changelog
* Thu Sep 17 2026 Mikhail Tergoev <fidel@altlinux.org> 1.5.0-alt3
- build GUI with Qt6/KF6 instead of Qt5/KF5 (ALT bug 59545)
- cherry-picked upstream fixes for KF6 (KChart6, KConfigGroup, QPalette)

* Mon Nov 11 2024 Mikhail Tergoev <fidel@altlinux.org> 1.5.0-alt2
- fixed build with gcc14

* Wed Nov 01 2023 Mikhail Tergoev <fidel@altlinux.org> 1.5.0-alt1
- Updated to upstream version 1.5.0.

* Thu Jan 13 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt1
- Updated to upstream version 1.3.0.

* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.80-alt1.git.1691cdd
- Initial build for ALT
