%define snapshot 681

Name: libvterm
Version: 0+bzr%snapshot
Release: alt1

Summary: an abstract C99 library which implements a VT220 or xterm-like terminal emulator

License: MIT
Group: System/Libraries
Url: http://www.leonerd.org.uk/code/libvterm/

# git://git.altlinux.org/gears/l/libvterm.git
Source: %name-%version-%release.tar
Source1: %name.watch

%package devel
Summary: Development files needed for %name
Group: Development/C

%package tools
Summary: %name tools
Group: Terminals

%define common_descr \
An abstract C99 library which implements a VT220 or xterm-like terminal\
emulator. It doesn't use any particular graphics toolkit or output system,\
instead it invokes callback function pointers that its embedding program should\
provide it to draw on its behalf. It avoids calling malloc() during normal\
running state, allowing it to be used in embedded kernel situations.

%description
%common_descr

%description devel
%common_descr

This package contains development files needed for %name.

%description tools
%common_descr

This package contains %name tools.

%prep
%setup

%build
%make_build PREFIX=%_prefix LIBDIR=%_libdir CFLAGS="%optflags"

%install
%makeinstall_std  PREFIX=%_prefix LIBDIR=%_libdir
rm -- %buildroot%_libdir/%name.a

%check
make test

%files
%doc LICENSE
%_libdir/%name.so.0
%_libdir/%name.so.0.0.0

%files devel
%_includedir/*.h
%_libdir/%name.so
%_pkgconfigdir/vterm.pc

%files tools
%_bindir/*

%changelog
* Wed May 03 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0+bzr681-alt1
- Initial build for Sisyphus.

