%define _unpackaged_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: libnick
Version: 2025.10.0
Release: alt1

Summary: A cross-platform base for native Nickvision applications
License: GPL-3.0
Group: Development/C++

URL: https://github.com/NickvisionApps/libnick
VCS: https://github.com/NickvisionApps/libnick
Source: %name-%version.tar

BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: libcpr-devel
BuildRequires: libmaddy-devel
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(sqlcipher)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(libidn2)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(libselinux)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(mit-krb5-gssapi)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(libtasn1)
BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(libnghttp2)
BuildRequires: pkgconfig(libngtcp2)
BuildRequires: pkgconfig(libnghttp3)

%description
A cross-platform base for native Nickvision applications.

libnick provides Nickvision apps with a common set of cross-platform APIs
for managing system and desktop app functionality such as network management,
taskbar icons, translations, app updates, and more.

%package devel
Summary: Headers for %name
Group: Development/C++

%description devel
%summary.

%package devel-static
Summary: Static libraries for %name
Group: Development/C++
Requires: %name-devel = %EVR

%description devel-static
%summary.

%prep
%setup

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -Wno-dev
%cmake_build

%install
%cmake_install

%files devel
%_includedir/%name
%_cmakedir/%name
%_pkgconfigdir/%name.pc

%files devel-static
# Required for packages that use this library
%_libdir/lib%name.a

%changelog
* Wed Dec 10 2025 David Sultaniiazov <x1z53@altlinux.org> 2025.10.0-alt1
- Initial build.
