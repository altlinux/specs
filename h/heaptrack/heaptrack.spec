%define _unpackaged_files_terminate_build 1

Name: heaptrack
Version: 1.2.80
Release: alt1.git.1691cdd
Group: Development/Other
Summary: A heap memory profiler for Linux 
Url: https://www.kde.org
License: LGPL-2.1

%K5init altplace man

# https://github.com/KDE/heaptrack.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libunwind-devel zlib-devel libzstd-devel
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel
BuildRequires: libdwarf-devel
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kitemmodels-devel kf5-threadweaver-devel kf5-kconfigwidgets-devel kf5-kio-devel
BuildRequires: kf5-kdiagram-devel

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

%build
%K5build

%install
%K5install

%files
%doc COPYING
%doc README.md screenshots
%_bindir/*
%_libdir/%name

%files devel
%_includedir/*

%files gui
%_K5bin/*
%_K5xdgapp/*.desktop
%_K5icon/*/*/*/*%{name}.*
%_datadir/metainfo/*.appdata.xml

%changelog
* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.80-alt1.git.1691cdd
- Initial build for ALT
