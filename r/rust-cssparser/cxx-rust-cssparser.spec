%define rname cxx-rust-cssparser
%define sover 1
%define libname libcxx-rust-cssparser%sover

Name: rust-cssparser
Version: 1.0.0
Release: alt1

Group: System/Libraries
Summary: C++ library for parsing CSS using the Rust cssparser crate
License: LGPL-2.1-only OR LGPL-3.0-only
Url: https://invent.kde.org/libraries/cxx-rust-cssparser

Source: %rname-%version.tar
Source1: vendor.tar

#BuildRequires(pre): rpm-build-rust
BuildRequires: cmake corrosion extra-cmake-modules gcc-c++ rust-cargo rustc

%description
A C++ library for parsing CSS that uses the Rust cssparser crate internally.

%package -n %libname
Group: System/Libraries
Summary: %name library
%description -n %libname
%name library

%package devel
Summary: Development files for %name
Group: Development/C++
#Requires: %name
%description devel
Headers and CMake metadata for developing applications with %name.

%prep
%setup -n %rname-%version -a1

%build
export CARGO_HOME="$PWD/rust/.cargo"
export CARGO_NET_OFFLINE=true
cargo install --locked --path rust/vendor/cxxbridge-cmd-1.0.194 --root "$PWD/cxxbridge"
export PATH="$PWD/cxxbridge/bin:$PATH"
%cmake \
    -DBUILD_DOCS:BOOL=OFF \
    -DBUILD_TESTING:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%doc LICENSES/*
%_bindir/cxx-rust-cssparser-parse

%files -n %libname
%_libdir/libcxx-rust-cssparser.so.%sover
%_libdir/libcxx-rust-cssparser.so.*

%files devel
%_includedir/cxx-rust-cssparser/
%_libdir/cmake/cxx-rust-cssparser/
%_libdir/lib*.so

%changelog
* Fri Jul 24 2026 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- initial build
