Name: libcelt
Version: 0.10.0
Release: alt1
Serial: 1
Summary: The CELT Low-Latency Audio Compression Codec
Group: System/Libraries
License: BSD
URL: http://www.xiph.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libogg-devel

%description
CELT is a fully open, non-proprietary, patent- and royalty-free,
low-latency compressed audio format for voice and music.

The libcelt package contains runtime libraries for use in programs
that support Ogg CELT.

%package devel
Summary: Files for CELT application development
Group: Development/C
Requires: %name = %version-%release

%description devel
The libcelt-devel package contains the header files and documentation
needed to develop applications with Ogg CELT

%package utils
Summary: CELT codec utilities
Group: Sound
Requires: %name = %version-%release

%description utils
Basic utilities for encoding, decoding and manipulating Ogg CELT streams

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

#%check
#%make -k check

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS README
%_libdir/lib*.so.*

%files devel
%_includedir/celt
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%files utils
%_bindir/celt*

%changelog
* Wed Dec 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.10.0-alt1
- 0.10.0

* Wed Nov 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.9.1-alt1
- 0.9.1

* Wed Oct 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.8.1-alt1
- 0.8.1

* Sun Jan 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.7.1-alt1
- 0.7.1

* Thu Oct 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.7.0-alt2
- 0.7.0

* Thu Jul 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.1-alt1
- initial release

