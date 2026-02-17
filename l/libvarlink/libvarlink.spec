%define _unpackaged_files_terminate_build 1
%define abiversion 0

Name:           libvarlink
Version:        24.0.1
Release:        alt1
Group:          System/Libraries
Summary:        Varlink C Library
License:        Apache-2.0 and BSD-3-Clause
URL:            https://github.com/varlink/libvarlink
Source:         %name-%version.tar
Patch:          meson.build.patch

BuildRequires:  gcc meson ninja-build

%description
Varlink is an interface description format and protocol for creating APIs.

A varlink interface combines the classic UNIX command line options,
STDIN/OUT/ERROR text formats, man pages, service metadata and provides the
equivalent over a single file descriptor, a.k.a. "FD3".

Varlink is plain-text, type-safe, discoverable, self-documenting and remotable.

%package     -n %name%abiversion
Group:          System/Libraries
Summary:        A C implementation of Varlink, a protocol for creating APIs
Provides:       %name = %version-%release

%description -n %name%abiversion
Varlink is an interface description format and protocol for creating APIs.

A varlink interface combines the classic UNIX command line options,
STDIN/OUT/ERROR text formats, man pages, service metadata and provides the
equivalent over a single file descriptor, a.k.a. "FD3".

Varlink is plain-text, type-safe, discoverable, self-documenting and remotable.

%package        devel
Group:          Development/C
Summary:        Development files for %name
Requires:       %name = %version-%release

%description    devel
Varlink is an interface description format and protocol for creating APIs.

The %name-devel package contains libraries and header files for
developing applications that use %name.

%package     -n varlink-util
Group:          Development/Other
Summary:        Varlink command line tools
Provides:       %name-util = %version-%release

%description -n varlink-util
The %name-util package contains varlink command line tools and with bash
command-line completion and vim editor support.


%prep
%setup
%patch -p1

%build
%meson
%meson_build

%check
export LC_CTYPE=C.utf8
%meson_test

%install
%meson_install

%files -n %name%abiversion
%doc LICENSE
%_libdir/libvarlink.so.*

%files -n varlink-util
%_bindir/varlink
%_datadir/bash-completion/completions/varlink
%_datadir/vim/vimfiles/after/*

%files devel
%_includedir/varlink.h
%_libdir/libvarlink.so
%_pkgconfigdir/libvarlink.pc

%changelog
* Wed Feb 18 2026 Evgeny Sinelnikov <sin@altlinux.org> 24.0.1-alt1
- Initial build for Sisyphus

