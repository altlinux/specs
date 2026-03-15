%define _unpackaged_files_terminate_build 1

%def_without check

Name: mkcal
Version: 0.7.31
Release: alt1

Summary: SQlite storage backend for KCalendarCore
License: LGPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/sailfishos/mkcal

Source: %name-%version.tar

# sync with version 0.7.27+dfsg-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt5)
BuildRequires: kf5-kcalcore-devel
BuildRequires: pkgconfig(sqlite3)

%if_with check
BuildRequires: ctest
BuildRequires: /usr/bin/xvfb-run
BuildRequires: tzdata
%endif

%description
Extends KDE calendar core library and provides an SQlite backend.
This package contains the Qt5 build of the libmkcal library.

%package -n lib%{name}
Summary: %{name} shared library
Group: System/Libraries

%description -n lib%{name}
Extends KDE calendar core library and provides an SQlite backend.
This package contains the Qt5 build of the libmkcal library.

%package -n lib%{name}-devel
Summary: %{name} development files
Group: Development/Other
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
%{name} development files.

%prep
%setup
%patch -p1

%build
%cmake \
       -DBUILD_PLUGINS=OFF
%cmake_build

%install
%cmake_install

%check
xvfb-run -a %ctest -j1 -VV

%files -n lib%{name}
%_libdir/lib%{name}-qt5.so.0*

%files -n lib%{name}-devel
%_bindir/mkcaltool
%dir %_includedir/%{name}-qt5
%_includedir/%{name}-qt5/*
%_libdir/lib%{name}-qt5.so
%_pkgconfigdir/libmkcal-qt5.pc

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.31-alt1
- new version 0.7.31 (with rpmrb script)

* Sat Dec 20 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.30-alt1
- New version 0.7.30.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.29-alt1
- New version 0.7.29.

* Sun Jul 20 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.27-alt1
- Initial build for Sisyphus
