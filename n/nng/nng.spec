%define _unpackaged_files_terminate_build 1

%define sover 1

Name: nng
Version: 1.12.0
Release: alt1

Summary: Lightweight brokerless messaging
License: MIT
Group: System/Libraries
URL: https://nng.nanomsg.org
VCS: https://github.com/nanomsg/nng

# Source-url: %vcs/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Patch: nng-1.11-disable-htmldoc.patch
Patch1: nng-1.12.0-bump-version.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: asciidoctor

%description
NNG is a lightweight, broker-less library, offering a simple API to solve
common recurring messaging problems, such as publish/subscribe, RPC-style
request/reply, or service discovery.

%package -n lib%name%sover
Summary: Lightweight brokerless messaging
Group: System/Libraries

%description -n lib%name%sover
NNG is a lightweight, broker-less library, offering a simple API to solve
common recurring messaging problems, such as publish/subscribe, RPC-style
request/reply, or service discovery.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name%sover = %EVR

%description -n lib%name-devel
%summary.

%package tools
Summary: NNG extra tools
Group: Other

%description tools
%summary.

%prep
%setup
%autopatch -p1

%build
# Many tests require internet connection, so are disabled
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DNNG_TOOLS=ON \
    -DNNG_TESTS=OFF \
    -DNNG_ENABLE_DOC=ON
%cmake_build

%install
%cmake_install

# Fix mandirs
rm -rf %buildroot%_mandir/man3tls
mv %buildroot%_mandir/man3{compat,http,str,supp}/* %buildroot%_man3dir

%files -n lib%name%sover
%doc README.adoc LICENSE.txt
%_libdir/lib%name.so.%{version}*
%_libdir/lib%name.so.%sover

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name
%_cmakedir/%name
%_man3dir/*
%_man5dir/*
%_man7dir/*

%files tools
%_bindir/*
%_man1dir/*

%changelog
* Mon Jun 29 2026 Valery Zabrovsky <brow@altlinux.org> 1.12.0-alt1
- New version 1.12.0.

* Thu May 28 2026 Valery Zabrovsky <brow@altlinux.org> 1.11-alt1
- Initial build for ALT Sisyphus.
