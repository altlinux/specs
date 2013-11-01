Name: SDL2
Version: 2.0.1
Release: alt2

Summary: Simple DirectMedia Layer
License: zlib
Group: System/Libraries

Url: http://www.libsdl.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: http://www.libsdl.org/release/%name-2.0.1.tar.gz

BuildRequires: gcc-c++ libEGL-devel libGL-devel libICE-devel libXScrnSaver-devel libXcursor-devel libXi-devel libXinerama-devel libXrandr-devel libXxf86vm-devel libalsa-devel libdbus-devel libesd-devel libpulseaudio-devel

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package -n lib%name
Summary: Simple DirectMedia Layer
Group: System/Libraries

%description -n lib%name
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package -n lib%name-devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

This is the libraries, include files and other resources you can use
to develop SDL applications.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%__rm -rf %buildroot%_libdir/*.a
%__rm -rf %buildroot%_libdir/*.la

%files -n lib%name
%doc BUGS.txt COPYING.txt CREDITS.txt INSTALL.txt README*.txt TODO.txt WhatsNew.txt
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%_bindir/sdl2-config
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/lib%name.so
%_pkgconfigdir/sdl2.pc
%_datadir/aclocal/sdl2.m4

%changelog
* Fri Nov 01 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt2
- Fix post-install unowned files

* Wed Oct 30 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux

