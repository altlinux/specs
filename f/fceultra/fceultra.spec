Name: fceultra
Version: 0.98.13
Release: alt2.1
Summary: A portable NES/Famicom emulator.

License: GPL
Group: Emulators

Url: http://fceultra.sourceforge.net

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: fceu-%version.src.tar.bz2
Patch0: fceultra-0.98.13-alt-str-buff-overflw.patch
Patch1: fceultra-0.98.13-alt-DSO.patch
# Automatically added by buildreq on Sun Jan 08 2006
BuildRequires: esound gcc-c++ libSDL-devel  zlib-devel
Exclusivearch: i586

%description
FCE Ultra is a portable NES/Famicom emulator based on Bero's original
FCE source code. Large portions of it have been rewritten, resulting
in a much stabler and very compatible emulator.

%prep
%setup -q -n fceu
%patch0 -p2
%patch1 -p2
#perl -pi -e's/-mcpu=i686/\$(RPM_OPT_FLAGS)/' Makefile*
%__subst 's,-mcpu=i686,\\$(RPM_OPT_FLAGS),' Makefile*
#__subst 's,\.la,\.so,' configure

%build
export CC=gcc CXX=g++
./configure --with-opengl
make
mv src/fceu src/fceu-sdl

%install
rm -rf %buildroot
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man6dir

install -p src/fceu-sdl %buildroot%_bindir
install -p Documentation/fceu-sdl.6 %buildroot%_man6dir


%files

%doc Documentation
%_bindir/fceu-sdl
%_man6dir/fceu-sdl.6*

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.98.13-alt2.1
- Fixed build

* Sun May 01 2011 Ilya Mashkin <oddity@altlinux.ru> 0.98.13-alt2
- fix build

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 0.98.13-alt1.1
- fix build (only for i586)

* Sun Jan 08 2006 Ilya Mashkin <oddity at altlinux.ru> 0.98.13-alt1
- Initial Christmas build for ALT Linux

* Fri Feb 18 2005 Winston Chang <winston@stdout.org>
- Updated to 0.98.13.

* Wed Dec  3 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Updated to 0.97.5.

* Fri Jun 13 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 
- Initial build.


