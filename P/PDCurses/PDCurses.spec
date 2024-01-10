Name:           PDCurses
Version:        3.8
Release:        alt1
Summary:        An implementation of X/Open curses for multiple platforms
URL:            https://pdcurses.org
Source:         %name-%version.tar.gz
Group:          System/Libraries
License:        MIT

# Automatically added by buildreq on Wed Jan 10 2024
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel libgpg-error python3 python3-base python3-dev sh5 xorg-proto-devel
BuildRequires: libSDL2-devel libXaw-devel libXext-devel libXpm-devel

%description
PDCurses is an implementation of X/Open curses for multiple platforms.

%package -n libXCurses
Group:          System/Libraries
Summary:        A port of PDCurses for X11, aka XCurses
Provides:       pdcurses

%description -n libXCurses
This is a port of PDCurses for X11, aka XCurses.  It is designed to
allow existing curses programs to be re-compiled with PDCurses,
resulting in native X11 programs.

%package -n libXCurses-devel
Group:          Development/C
Summary:        A port of PDCurses for X11, aka XCurses, development files
Provides:       pdcurses-devel

%description -n libXCurses-devel
%summary

%package -n libXCurses-devel-static
Group:          Development/C
Summary:        A port of PDCurses for X11, aka XCurses, static development files
Provides:       pdcurses-devel-static
Requires:       libXCurses-devel = %EVR

%description -n libXCurses-devel-static
%summary

%package -n pdcurses_SDL2
Group:          System/Libraries
Summary:        This is a port of PDCurses for version 2.x of SDL

%description -n pdcurses_SDL2
%summary

%package -n pdcurses_SDL2-devel
Group:          Development/C
Summary:        A port of PDCurses for version 2.x of SDL, development files

%description -n pdcurses_SDL2-devel
%summary

%prep
%setup
rm x11/aclocal.m4

%build
export CC=gcc
cd x11
%configure --enable-widec --enable-xim --enable-force-utf8 --x-includes=%_includedir --x-libraries=%_libdir --prefix=%_prefix
%make_build

cd ../sdl2
%make_build
gcc -shared *.o -o pdcurses_SDL2.so -lSDL2

%install
cd x11
%makeinstall install
mv %buildroot%_libdir/libXCurses.so %buildroot%_libdir/libXCurses.so.0.0
ln -sr %buildroot%_libdir/libXCurses.so.0.0 %buildroot%_libdir/libXCurses.so.0
ln -sr %buildroot%_libdir/libXCurses.so.0.0 %buildroot%_libdir/libXCurses.so

cd ../sdl2
install -D pdcurses_SDL2.so %buildroot%_libdir/pdcurses_SDL2.so.0.0
ln -sr %buildroot%_libdir/pdcurses_SDL2.so.0.0 %buildroot%_libdir/pdcurses_SDL2.so.0
ln -sr %buildroot%_libdir/pdcurses_SDL2.so.0.0 %buildroot%_libdir/pdcurses_SDL2.so

%files -n libXCurses
%_libdir/lib*.so.*

%files -n libXCurses-devel
%doc demos x11/*.md
%_libdir/lib*.so
%_includedir/xcurses
%_bindir/xcurses*

%files -n libXCurses-devel-static
%_libdir/lib*.a

%files -n pdcurses_SDL2
%_libdir/pd*.so.*

%files -n pdcurses_SDL2-devel
%doc demos sdl2/*.md
%_libdir/pd*.so

%check
make -C x11 demos
make -C sdl2 demos

%changelog
* Wed Jan 10 2024 Fr. Br. George <george@altlinux.org> 3.8-alt1
- Initial build for ALT
