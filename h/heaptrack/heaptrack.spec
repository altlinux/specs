%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: heaptrack
Version: 1.5.0
Release: alt1

Summary: A heap memory profiler for Linux 

License: LGPL-2.1
Group: Development/Other
Url: https://www.kde.org
VCS: https://github.com/KDE/heaptrack.git

%K5init altplace man

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: gcc-c++ cmake extra-cmake-modules ctest
BuildRequires: libunwind-devel zlib-devel libzstd-devel
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel
BuildRequires: libdwarf-devel
BuildRequires: qt5-base-devel
BuildRequires: kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kitemmodels-devel kf5-threadweaver-devel kf5-kconfigwidgets-devel kf5-kio-devel kf5-kdiagram-devel kf5-kiconthemes-devel
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

rm -f screenshots/.directory

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%K5build

%install
%K5install
%find_lang --with-kde %name

%files -f %name.lang
%doc LICENSES README.md screenshots
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
* Wed Nov 01 2023 Mikhail Tergoev <fidel@altlinux.org> 1.5.0-alt1
- Updated to upstream version 1.5.0.

* Thu Jan 13 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt1
- Updated to upstream version 1.3.0.

* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.80-alt1.git.1691cdd
- Initial build for ALT
