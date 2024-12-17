%define _unpackaged_files_terminate_build 1
%define abiversion 7
%def_enable check

Name: crengine-ng
Version: 0.9.12
Release: alt1

Summary: Cross-platform library designed to implement text viewers and e-book readers
License: GPL-2.0-or-later
Group: Development/C++
Url: https://gitlab.com/coolreader-ng/crengine-ng
VCS: https://gitlab.com/coolreader-ng/crengine-ng.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: bzlib-devel
BuildRequires: cmake
BuildRequires: fontconfig-devel
BuildRequires: gcc-c++
BuildRequires: libbrotli-devel
BuildRequires: libexpat-devel
BuildRequires: libfreetype-devel
BuildRequires: libfribidi-devel
BuildRequires: libjpeg-devel
BuildRequires: libpcre2-devel
BuildRequires: libunibreak-devel
BuildRequires: libutf8proc-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel

%description
%summary.

%package -n lib%name%abiversion
Summary: %summary
Group: System/Libraries

%description -n lib%name%abiversion
Crengine-ng is cross-platform library designed to implement
text viewers and e-book readers.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C++
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel
Files for development with %name.

%prep
%setup

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CXX_STANDARD=17 \
  -DCRE_BUILD_STATIC=OFF \
  %nil
%cmake_build

%install
%cmake_install

%files -n lib%name%abiversion
%_datadir/crengine-ng
%_libdir/libcrengine-ng.so.%abiversion
%_libdir/libcrengine-ng.so.%version

%files -n lib%name-devel
%doc AUTHORS ChangeLog crengine/docs/WolfFormat.txt README.md
%_cmakedir/crengine-ng
%_libdir/libcrengine-ng.so
%_includedir/crengine-ng
%_pkgconfigdir/crengine-ng.pc

%changelog
* Mon Dec 16 2024 Constantin Sunzow <protvin@altlinux.org> 0.9.12-alt1
- Initial build.
