Name: SDL2
Version: 2.0.2
Release: alt1

Summary: Simple DirectMedia Layer
License: zlib
Group: System/Libraries

Url: http://www.libsdl.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: http://www.libsdl.org/release/%name-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: libGL-devel
BuildRequires: libGLES-devel
BuildRequires: libICE-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXcursor-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libalsa-devel
BuildRequires: libaudio-devel
BuildRequires: libdbus-devel
BuildRequires: libesd-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libudev-devel

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
%__rm -rf %buildroot%_libdir/*.a %buildroot%_libdir/*.la

%files -n lib%name
%doc BUGS.txt COPYING.txt CREDITS.txt INSTALL.txt README*.txt TODO.txt WhatsNew.txt
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%_bindir/sdl2-config
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/lib%name.so
%_pkgconfigdir/sdl2.pc
%_aclocaldir/sdl2.m4

%changelog
* Sun Mar 09 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Tue Feb 25 2014 Fr. Br. George <george@altlinux.ru> 2.0.1-alt2.1
- Rebuild with pkgconfig fix by new rpm

* Wed Feb 05 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1.M70T.1
- Build for branch t7

* Fri Nov 01 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt2
- Fix post-install unowned files

* Wed Oct 30 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux

