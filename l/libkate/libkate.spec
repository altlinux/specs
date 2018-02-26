Name: libkate
Version: 0.4.1
Release: alt1.1
Summary: kate is a karaoke and text codec for embedding in ogg
License: BSD-style
Group: Video
URL: http://code.google.com/p/libkate/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: flex libogg-devel liboggz libpng-devel

%description
Kate is a codec for karaoke and text encapsulation for Ogg. Most of the time,
this would be multiplexed with audio/video to carry subtitles, song lyrics
(with or without karaoke data), etc, but doesn't have to be. A possible use
of a lone Kate stream would be an e-book. Moreover, the motion feature gives
Kate a powerful means to describe arbitrary curves, so hand drawing of shapes
can be achieved. This was originally meant for karaoke use, but can be used
for any purpose. Motions can be attached to various semantics, like position,
color, etc, so scrolling or fading text can be defined.

%package devel
Summary: %name Library and Header Files
Group: Development/C

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%package utils
Summary: Kate codec utilities
Group: Video
Requires: %name = %version-%release

%description utils
Basic utilities for encoding, decoding and manipulating subtitles.

%package -n KateDJ
Summary: simple UI for kate
Group: Video
Requires: %name-utils = %version-%release liboggz
BuildArch: noarch

%description -n KateDJ
KateDJ is a simple UI driven program that can extract Kate
streams from Ogg files, and merge them back in. It can be
used to make alterations to Kate streams easily, or to add
new Kate streams to an Ogg file.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS THANKS
%_libdir/*.so.*

%files devel
%_includedir/kate
%_libdir/*.so
%_pkgconfigdir/*.pc

%files utils
%doc README
%_bindir/kat*
%_man1dir/kat*.1*

%files -n KateDJ
%_bindir/KateDJ
%_prefix/lib/python*/site-packages/kdj
%_man1dir/KateDJ.1*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild with Python-2.7

* Tue Aug 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.3.8-alt1
- 0.3.8

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 0.3.7-alt1.1
- Rebuilt with python 2.6

* Tue Nov 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.7-alt1
- 0.3.7

* Thu Oct 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Sat Aug 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Sun Dec 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.7-alt1
- 0.2.7

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Oct 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Wed Oct 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.3-alt1
- initial build
