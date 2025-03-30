%def_enable check

Name: libomemo-c
Version: 0.5.1
Release: alt1

Summary: OMEMO C Library
License: GPL-3.0
Group: System/Libraries
Url: https://github.com/dino/libomemo-c

Vcs: https://github.com/dino/libomemo-c.git

Source: %url/archive/v%version/%name-%version.tar.gz

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++
BuildRequires: pkgconfig(libprotobuf-c) protobuf-c-compiler
BuildRequires: libgcrypt-devel libssl-devel
%{?_enable_check:BuildRequires: ctest libcheck-devel}

%description
This is a fork of libsignal-protocol-c, an implementation of Signal's
ratcheting forward secrecy protocol that works in synchronous and
asynchronous messaging. The fork adds support for OMEMO as defined in
XEP-0384 versions 0.3.0 and later.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the libraries and headers needed for developing
applications with %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name.so.*
%doc README*

%files devel
%_includedir/omemo
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Sun Mar 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Sat Apr 08 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus



