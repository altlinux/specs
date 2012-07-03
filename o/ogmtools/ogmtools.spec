Name: ogmtools
Version: 1.5
Release: alt2

Summary: Tools for Ogg media streams
License: GPL
Group: Sound
Url: http://www.bunkus.org/videotools/ogmtools

Source0: %url/%name-%version.tar.bz2

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: vorbis-tools
#Requires: /usr/bin/mencoder
Requires: MPlayer
Requires: normalize

# Automatically added by buildreq on Sat Sep 19 2009
BuildRequires: gcc-c++ libdvdread-devel libvorbis-devel

%description
These tools allow information about (ogminfo) or extraction from
(ogmdemux) or creation of (ogmmerge) or the splitting of (ogmsplit) OGG
media streams. OGM is used for "OGG media streams".

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*
%doc README ChangeLog TODO

%changelog
* Sat Sep 19 2009 Igor Zubkov <icesik@altlinux.org> 1.5-alt2
- rebuild

* Thu Nov 16 2006 Igor Zubkov <icesik@altlinux.org> 1.5-alt1
- 1.4.1 -> 1.5
- buildreq
- add packager tag

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.1-alt1.1.1
- Rebuilt with libstdc++.so.6.

* Tue Oct 05 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.1-alt1.1
- Rebuilt with libdvdread.so.3.

* Wed Aug 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Fri Nov 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2-alt1
- 1.2

* Wed Oct 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1-alt1
- 1.1

* Tue Jun 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Apr 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Mon Mar 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Fri Feb 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.973-alt1
- First build for Sisyphus.

