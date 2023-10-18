Name: nativefiledialog-extended
Version: 1.1.0
Release: alt2
Summary: Native file dialog library with C and C++ bindings

License: Zlib
Group: Development/C
Url: https://github.com/btzy/nativefiledialog-extended

# Source0-url: https://github.com/btzy/nativefiledialog-extended/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgtk+3-devel
BuildRequires: libpcre2-devel
BuildRequires: libffi-devel
BuildRequires: bzlib-devel
BuildRequires: libbrotli-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libselinux-devel
BuildRequires: libfribidi-devel
BuildRequires: libthai-devel
BuildRequires: libdatrie-devel
BuildRequires: libexpat-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libXtst-devel
BuildRequires: libpixman-devel
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libepoxy-devel
BuildRequires: at-spi2-atk-devel
BuildRequires: libwaylandpp-devel

%description
A small C library with that portably invokes native file open, folder
select and file save dialogs. Write dialog code once and have it pop up
native dialogs on all supported platforms. Avoid linking large
dependencies like wxWidgets and Qt.

This library is based on Michael Labbe's Native File Dialog (
mlabbe/nativefiledialog).

%package -n lib%name
Summary: Native file dialog library with C and C++ bindings
Group: Development/Tools

%description -n lib%name
A small C library with that portably invokes native file open, folder
select and file save dialogs. Write dialog code once and have it pop up
native dialogs on all supported platforms. Avoid linking large
dependencies like wxWidgets and Qt.

This library is based on Michael Labbe's Native File Dialog (
mlabbe/nativefiledialog).

%package -n lib%name-devel
Summary: Development files for %name
Requires: lib%name = %version-%release
Group: Development/Tools

%description -n lib%name-devel
A small C library with that portably invokes native file open, folder
select and file save dialogs. Write dialog code once and have it pop up
native dialogs on all supported platforms. Avoid linking large
dependencies like wxWidgets and Qt.

This library is based on Michael Labbe's Native File Dialog (
mlabbe/nativefiledialog).

%prep
%setup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DNFD_BUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files -n lib%name
%doc README.md LICENSE
%_libdir/libnfd.so.*

%files -n lib%name-devel
%doc LICENSE
%_libdir/libnfd.so
%_includedir/nfd.*
%_libdir/cmake/nfd/
%_libdir/cmake/nfd/*.cmake

%changelog
* Wed Oct 18 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.1.0-alt2
- NMU: fixed FTBFS on LoongArch

* Tue Jul 18 2023 Mikhail Tergoev <fidel@altlinux.org> 1.1.0-alt1
- Initial build for ALT Sisyphus

