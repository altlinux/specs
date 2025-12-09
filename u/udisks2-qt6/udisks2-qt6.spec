%define sover 1

%def_disable clang

Name: udisks2-qt6
Version: 6.0.1
Release: alt1

Summary: Qt6 binding for udisks2

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/udisks2-qt6
VCS: https://github.com/linuxdeepin/udisks2-qt6

# Source-url: https://github.com/linuxdeepin/udisks2-qt6/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-6.0.0-alt-dqt6.patch

%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: cmake dqt6-base-devel

%description
This package provides a Qt6 binding for udisks2.


%package -n lib%name-common
Summary: Common files for %name
Group: Documentation
BuildArch: noarch

%description -n lib%name-common
This package provides a common files for %name.

%package -n lib%name-%sover
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name-%sover
This package provides a Qt6 binding for udisks2.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/KDE and QT

%description -n lib%name-devel
Header files and libraries for %name.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export LC_ALL=C.UTF-8
%DQ6build

%install
%DQ6install

%files -n lib%name-common
%doc LICENSE.txt README.md debian/changelog

%files -n lib%name-%sover
%_libdir/lib%name.so.%{sover}*
%_libdir/lib%name.so.6.0.0

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name/

%changelog
* Tue Dec 09 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.1-alt1
- New version 6.0.1.
- Packaged the docs.

* Thu Jan 23 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.0-alt1
- Initial build for ALT Sisyphus (for deepin-device-formatter).
