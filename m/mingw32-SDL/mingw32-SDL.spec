Name: mingw32-SDL
Version: 1.2.13
Release: alt1
Summary: MinGW Windows port of SDL cross-platform multimedia library

License: LGPLv2+
Group: System/Libraries
Url: http://www.libsdl.org/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://www.libsdl.org/release/SDL-%version.tar.gz

BuildArch: noarch

# Patches from native version.
Patch: SDL-1.2.10-byteorder.patch
Patch17: SDL-1.2.13-libdir.patch
Patch21: SDL-1.2.12-multilib.patch
Patch23: SDL-1.2.11-dynamic-esd.patch
Patch24: SDL-1.2.12-x11dyn64.patch
Patch25: SDL-1.2.12-disable_yasm.patch
Patch26: SDL-1.2.13-dynamic-pulse.patch
Patch27: SDL-1.2.13-pulse-rework.patch
Patch28: SDL-1.2.13-audiodriver.patch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-iconv

Requires: pkgconfig

# Not required at the moment, but SDL does contain plenty of C++ code,
# I just haven't worked out how to enable it.
#BuildRequires:  mingw32-gcc-c++

# If we have nasm in the future, then this would enable future
# optimizations on x86-based architectures.
#%ifarch %ix86
#BuildRequires: nasm
#%endif

# kraxel pointed out that the headers need <iconv.h>, hence:
Requires: mingw32-iconv

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

%prep
%setup -q -n SDL-%version
%patch0 -p1 -b .byteorder
%patch17 -p1 -b .libdir
%patch21 -p1 -b .multilib
%patch23 -p1 -b .dynamic-esd
%patch24 -p1 -b .x11dyn64
%patch25 -p1 -b .disable_yasm
%patch26 -p1 -b .dynamic-pulse
%patch27 -p1 -b .pulse-rework
%patch28 -p1 -b .audiodriver

%build
%_mingw32_configure \
  --disable-video-svga --disable-video-ggi --disable-video-aalib \
  --disable-debug \
  --enable-sdl-dlopen \
  --enable-dlopen \
  --enable-arts-shared \
  --enable-esd-shared \
  --enable-pulseaudio-shared \
  --enable-alsa \
  --disable-rpath

%make_build

%install
%makeinstall_std
# Remove static libraries but DON'T remove *.dll.a files.
rm %buildroot%_mingw32_libdir/libSDL.a

# Actually libSDLmain.a seems to be required.  It just contains
# a single object file called SDL_win32_main.o.
#rm %buildroot%_mingw32_libdir/libSDLmain.a

# Delete man pages since they duplicate what is already available
# in base Fedora package.
rm %buildroot%_mingw32_mandir/man3/*.3*

%files
%doc COPYING
%_mingw32_bindir/SDL.dll
%_mingw32_bindir/sdl-config
%_mingw32_libdir/libSDL.dll.a
%_mingw32_libdir/libSDL.la
%_mingw32_libdir/libSDLmain.a
%_mingw32_libdir/pkgconfig/sdl.pc
%_mingw32_datadir/aclocal/sdl.m4
%_mingw32_includedir/SDL

%changelog
* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 1.2.13-alt1
- initial build for Sisyphus

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 29 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.13-7
- Add runtime Requires mingw32-iconv (kraxel).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.13-5
- Rebuild for mingw32-gcc 4.4

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.13-4
- Verify we are still up to date with Fedora release.
- Include COPYING in documentation.
- Build with dlfcn.
- List all BRs.
- No need to package the man pages, don't duplicate what's in the
  base Fedora package already.
- Requires pkgconfig.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.13-2
- Initial RPM release.
