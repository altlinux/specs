%define _unpackaged_files_terminate_build 1
%define abiversion 0

Name:    yascreen
Version: 1.99
Release: alt1
Summary: Yet Another Screen Library (lib(n)curses alternative)
License: LGPL-3.0
Group: Terminals
Url: https://github.com/bbonev/yascreen

Source: %name-%version.tar

BuildRequires: go-md2man 

%description
lib(n)curses alternative oriented towards modern terminals.

Suitable for developing terminal applications or daemons with
telnet access and terminal support.

Main features

 * small footprint
 * does not have external dependencies
 * allows both internal and external event loop
 * allows stdin/stdout or external input/output (can work over socket)
 * supports basic set of telnet sequences, making it suitable for built-in
   terminal interfaces for daemons
 * supports a limited set of input keystroke sequences
 * fully Unicode compatible (parts of this depend on wcwidth in libc)
 * supports utf8 verification of input
 * relies only on a limited subset of ANSI/xterm ESC sequences, making it
   compatible with mostly all modern terminals (inspired by linenoise)
 * there is no curses API and ancient terminal compatibility, hence less bloat
 * clean API with opaque private data, usable from C/C++

%package -n lib%name%abiversion
Summary:  Shared library for %name
Group: Development/C

%description -n lib%name%abiversion
libs files for %name

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C

%description -n lib%name-devel
Files for development with %name.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std NO_VERSIONED=0 PREFIX=%prefix/ LIBDIR=%_lib/
%__rm %buildroot%_libdir/*.a

%files -n lib%name-devel
%_libdir/*.so
%_pkgconfigdir/%name.pc
%_man3dir/%name.3*
%_includedir/%name.h

%files -n lib%name%abiversion
%_libdir/*.so.%abiversion
%_libdir/*.so.%abiversion.*


%changelog
* Thu Feb 22 2024 Pavel Shilov <zerospirit@altlinux.org> 1.99-alt1
- initial build for Sisyphus
