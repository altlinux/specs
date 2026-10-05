%define _unpackaged_files_terminate_build 1
%define abiversion 0

Name: libetebase
Version: 0.5.8
Release: alt1

Summary: C library for Etebase (EteSync end-to-end encrypted sync)

License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/etesync/libetebase

# Source-url: https://github.com/etesync/libetebase/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml
# install to the arch libdir (upstream hardcodes $(PREFIX)/lib)
# https://github.com/etesync/libetebase/pull/23
Patch: libetebase-libdir.patch
# install libetebase.so.VERSION with soname symlinks
# https://github.com/etesync/libetebase/pull/24
Patch1: libetebase-versioned-so.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: pkg-config libsodium-devel libssl-devel

%description
Etebase is an end-to-end encrypted backend as a service.
This package contains the C bindings of the Etebase client library,
used by EteSync clients.

%package -n %name%abiversion
Summary: C library for Etebase (EteSync end-to-end encrypted sync)
Group: System/Libraries

%description -n %name%abiversion
Etebase is an end-to-end encrypted backend as a service.
This package contains the shared library with the C bindings
of the Etebase client library.

%package devel
Summary: Development files for the Etebase C library
Group: Development/C
Requires: %name%abiversion = %EVR

%description devel
This package contains the header, pkg-config and CMake files
needed to build applications that use the Etebase C library.

%prep
%setup -a1
%patch -p1
%patch1 -p1
install -vD %SOURCE2 .cargo/config.toml

%build
# link with the system libsodium instead of building the bundled copy
export SODIUM_USE_PKG_CONFIG=1
%rust_build
%make_build pkgconfig PREFIX=%prefix LIBDIR=%_libdir

%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_libdir

%files -n %name%abiversion
%doc LICENSE README.md ChangeLog.md
%_libdir/libetebase.so.%abiversion
%_libdir/libetebase.so.%version

%files devel
%_libdir/libetebase.so
%_includedir/etebase/
%_pkgconfigdir/etebase.pc
%_libdir/cmake/Etebase/

%changelog
* Mon Oct 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.5.8-alt1
- initial build for Sisyphus (closes: #39984)
