Name: libtimidity
Version: 0.1.0
Release: alt4
Summary: MIDI to WAVE converter library
License: LGPL
Group: System/Libraries
Url: http://libtimidity.sourceforge.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: timidity-instruments

Source0: %name-%version.tar.bz2
Patch0: libtimidity-0.1.0-alt-timidity.patch

BuildRequires: libao-devel

%description
libTiMidity is MIDI to WAVE converter library. It based on the
TiMidity decoder from SDL_sound library. Purpose to create this
library is to avoid unnecessary dependences. SDL_sound requires
SDL and some other libraries, that not needed to process MIDI
files. In addition libTiMidity provides more suitable API to work
with MIDI songs, it enables to specify full path to the timidity
configuration file, and have function to retrieve meta data from
MIDI song.

%package devel
Summary: The development libraries and header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
These are the development libraries and header files for %name

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS CHANGES NEWS README README.timidity TODO
%_libdir/*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Aug 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt4
- rebuild with debuginfo

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt3
- rebuild

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Nov 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt0.M41.1
- build for branch 4.1

* Tue Nov 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt1
- initial release

