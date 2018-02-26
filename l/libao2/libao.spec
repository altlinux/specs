%define oname libao

Name: %{oname}2
Version: 0.8.8
Release: alt5
Serial: 1
Summary: Cross Platform Audio Output Library
License: GPL
Group: System/Libraries
Url: http://www.xiph.org/ao/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: %oname

Source0: http://downloads.xiph.org/releases/ao/%oname-%version.tar.gz
Patch0: libao-0.8.8-alt-oss.patch

BuildRequires: gcc-c++ libalsa-devel libpulseaudio-devel

%description
Libao is a cross platform audio output library.
It currently supports ALSA and PULSE.

%package pulse
Summary: PulseAudio output plugin for libao
Group: System/Libraries
Requires: %oname-pulse %name = %version-%release

%description pulse
This is package contains PulseAudio output plugin for libao

%prep
%setup -q -n %oname-%version
%patch0 -p1

%build
%autoreconf
%configure \
	--enable-pulse \
	--enable-alsa09 \
	--disable-alsa \
	--disable-broken-oss \
	--disable-oss \
	--disable-esd \
	--disable-arts \
	--disable-nas
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%dir %_libdir/ao
%dir %_libdir/ao/plugins-2
%_libdir/ao/plugins-2/libalsa09.so

%files pulse
%dir %_libdir/ao
%dir %_libdir/ao/plugins-2
%_libdir/ao/plugins-2/libpulse.so

%changelog
* Fri Mar 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.8.8-alt5
- don't packaged devel subpackage

* Fri Feb 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.8.8-alt4
- added serial

* Tue Jul 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt3
- enabled pulse plugin

* Tue Dec 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt2
- disabled arts, esd, nas, oss plugins

* Tue Jul 10 2007 Igor Zubkov <icesik@altlinux.org> 0.8.8-alt1.13239
- 0.8.6 -> 0.8.8 (from svn r13239)

* Wed Jun 27 2007 Igor Zubkov <icesik@altlinux.org> 0.8.6-alt11
- remove libao-pulse from requires of libao-full (closes #11922)

* Thu May 24 2007 Igor Zubkov <icesik@altlinux.org> 0.8.6-alt10
- enable nas support (closes #11860)

* Mon Mar 26 2007 Igor Zubkov <icesik@altlinux.org> 0.8.6-alt9
- disable nas support

* Tue Sep 05 2006 Igor Zubkov <icesik@altlinux.ru> 0.8.6-alt8
- s/libao-polyp/libao-pulse/

* Sun Jun 25 2006 Igor Zubkov <icesik@altlinux.ru> 0.8.6-alt7
- spec clean up
- add libao-polyp to libao-full package Requires

* Fri Mar 31 2006 Igor Zubkov <icesik@altlinux.ru> 0.8.6-alt6
- add libao-oss and libao-alsa Requires to libao (#8633)

* Thu Mar 23 2006 Igor Zubkov <icesik@altlinux.ru> 0.8.6-alt5
- disable polypaudio support

* Wed Mar 22 2006 Igor Zubkov <icesik@altlinux.ru> 0.8.6-alt4
- enable nas support
- buildreq

* Sun Dec 25 2005 Igor Zubkov <icesik@altlinux.ru> 0.8.6-alt3
- added polypaudio support
- #8633
- disable nas support

* Wed Sep 21 2005 Igor Zubkov <icesik@altlinux.ru> 0.8.6-alt2
- change %%make to %%make_build and %%make_install
- change default_driver from oss to alsa09 (#7421)
- mark config /etc/libao.conf as noreplace
- spec clean up

* Sun Mar 20 2005 Andrey Astafiev <andrei@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Sun Mar 28 2004 Andrey Astafiev <andrei@altlinux.ru> 0.8.5-alt2
- Added BuildRequires to glib2-devel.

* Mon Mar 22 2004 Andrey Astafiev <andrei@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Tue Feb 10 2004 Andrey Astafiev <andrei@altlinux.ru> 0.8.4-alt3
- Fixed build with new alsa.

* Wed Dec 03 2003 Alexey Tourbin <at@altlinux.ru> 0.8.4-alt2
- Do not package .la files.
- Do not package %name-devel-static by default.

* Fri Nov 21 2003 Andrey Astafiev <andrei@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Mon Sep 15 2003 Andrey Astafiev <andrei@altlinux.ru> 0.8.3-alt3
- Removed possibility to build with old alsa.

* Wed Nov 13 2002 Andrey Astafiev <andrei@altlinux.ru> 0.8.3-alt2
- rebuilt with gcc3.2.

* Mon Jul 22 2002 Andrey Astafiev <andrei@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Thu May 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.8.2-alt3
- alsa2 by default now.

* Fri Jan 4 2002 Andrey Astafiev <andrei@altlinux.ru> 0.8.2-alt2
- added option for building with alsa or alsa2.

* Thu Jan 3 2002 Andrey Astafiev <andrei@altlinux.ru> 0.8.2-alt1
- 0.8.2
- some updates.

* Tue Jan 1 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt4
- really built with alsa and arts support (see buildreq).
- /etc/libao.conf created.
- all *.la moved in devel package, html documentation separated.
- russian summary added for all packages.
- other spec cleanups.

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.8.0-alt2
- Relocated documentation, a bit more specfile cleanup.

* Thu Sep 27 2001 Andrey Astafiev <andrei@altlinux.ru> 0.8.0-alt1
- spec cleanup.

* Sat Sep 22 2001 Michael Shigorin <mike@lic145.kiev.ua>
- built for ALTLinux.

* Sun Sep 03 2000 Jack Moffitt <jack@icecast.org>
- initial spec file created.
