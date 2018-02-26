Name: hunspell
Summary: Hunspell is a spell checker and morphological analyzer
Version: 1.3.1
Release: alt1
License: LGPL
Group: Text tools
URL: http://hunspell.sourceforge.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: lib%name = %version-%release

Source: http://downloads.sourceforge.net/%name/%name-%version.tar.gz

Patch0: hunspell-1.2.7-alt-ncursesw.patch
Patch1: hunspell-1.2.14-alt-dict-path.patch
Patch2: hunspell-1.3.1-alt-soname.patch

# Automatically added by buildreq on Tue Jul 24 2007
BuildRequires: gcc-c++ libncursesw-devel libreadline-devel

%description
Hunspell is a spell checker and morphological analyzer program designed for
languages with rich morphology and complex word compounding or character
encoding. Hunspell interfaces: Ispell-like terminal interface using
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

%package -n lib%name
Summary: Hunspell is a spell checker and morphological analyzer library
Group: System/Libraries

%description -n lib%name
Hunspell is a spell checker and morphological analyzer library designed for
languages with rich morphology and complex word compounding or character encoding.

%package -n lib%name-devel
Summary: Files for developing with hunspell
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Includes and definitions for developing with hunspell

%package utils
Summary: Morphological utilities provided with hunspell
Group: Text tools
Requires: lib%name = %version-%release

%description utils
Morphological utilities and dictionary formatr converters provided with
hunspell.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

subst '/AM_GNU_GETTEXT_VERSION/d' configure.ac

%build
%autoreconf
%configure \
	--disable-static \
	--with-ui \
	--with-readline
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/myspell

%find_lang %name

%files -f %name.lang
%doc AUTHORS AUTHORS.myspell license.hunspell license.myspell NEWS THANKS
%_bindir/%name
%_man1dir/%name.1*
%_man4dir/%name.4*

%files -n lib%name
%_libdir/*.so.*
%_datadir/myspell

%files -n lib%name-devel
%_includedir/%name
%_bindir/*munch
%_bindir/h*zip
%_libdir/*.so
%_pkgconfigdir/hunspell.pc
%_man1dir/h*zip.1*
%_man3dir/%name.3*

%files utils
%_bindir/analyze
%_bindir/affixcompress
%_bindir/chmorph
%_bindir/ispellaff2myspell
%_bindir/makealias
%_bindir/wordforms
%_bindir/wordlist2hunspell

%changelog
* Mon Feb 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Sun Jan 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.2.14-alt1
- 1.2.14

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt2
- rebuild

* Thu Sep 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.12-alt1
- 1.2.12
- new subpackage: hunspell-utils with morpholgical analyzer
  and dictionary format converters (Kirill Maslinsky)

* Mon May 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.10-alt1
- 1.2.10

* Wed Feb 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.7-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sat Nov 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.7-alt2
- fixed dictionaries path

* Wed Sep 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sat Aug 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1.10-alt1
- 1.1.10

* Tue Jul 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1.8.2-alt1
- initial build
