Name: VisualBoyAdvance
Version: 1.7.2
Release: alt3.3

Summary: This is a GB/GBC/GBA emulator for Linux

License: GPL
Group: Emulators
Source: %name-src-%version.tar.gz
Patch1: visualboyadvance-1.7.2-glibc2.10.patch
URL: http://vba.ngemu.com

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Sun Feb 22 2004
BuildRequires: xorg-libs esound flex gcc4.3 gcc4.3-c++ libSDL-devel libpng-devel nasm zlib-devel
ExclusiveArch: %ix86

%description
This is a GameBoy, GameBoyColor and GameBoyAdvance emulator for Linux
(and win32/BeOS).

%prep
%setup -q
%patch1 -p0

%build
export CC=gcc-4.3 CXX=g++-4.3
#set_automake_version 1.10
#set_autoconf_version 2.5
%configure 
#cd src
%make_build
# cd 
%install
%make_install

install -D -pm 755 src/sdl/%name %buildroot%_bindir/%name    
install -D -pm 755 src/sdl/TestEmu %buildroot%_bindir/TestEmu

%files
%doc README COPYING ChangeLog AUTHORS NEWS README-win.txt src/%name.cfg
%_bindir/*

%changelog
* Thu Aug 18 2011 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt3.3
- update requires

* Tue Aug 17 2010 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt3.2
- fix build

* Tue May 27 2008 Ilya Mashkin <oddity at altlinux dot ru> 1.7.2-alt3.1
- spec cleanup

* Wed May 02 2007 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt3
- rebuild 

* Tue Jun 15 2004 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt2
- update spec for 1.7.2

* Sun Jun 05 2004 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt1
- Update version to 1.7.2. Many fixes.

* Sun Feb 22 2004 Ilya Mashkin <oddity@altlinux.ru> 1.7.1-alt1
- Update version to 1.7.1. Many changes.

* Tue Nov 18 2003 Ilya Mashkin <oddity@altlinux.ru> 1.6a-alt0.1
- Initial build 
