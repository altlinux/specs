%def_enable pulse

Name: libao
Version: 1.2.2
Release: alt3
Epoch: 1

Summary: Cross Platform Audio Output Library
License: GPL
Group: System/Libraries

Url: http://www.xiph.org/ao/
# https://git.xiph.org/libao.git
Source0: %name-%version.tar
Patch0: libao-1.0.0-alt-oss.patch

BuildRequires: libalsa-devel
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}

Provides: %name-alsa = %version-%release
Obsoletes: %name-alsa < %version-%release

%description
Libao is a cross platform audio output library.
It currently supports ALSA and PULSE.

%package pulse
Summary: PulseAudio output plugin for libao
Group: System/Libraries
Requires: %name = %version-%release

%description pulse
This is package contains PulseAudio output plugin for libao

%package devel
Summary: Development files for %name
Group: Development/C
PreReq: %name = %version-%release

%description devel
The %name-devel package contains the header files and documentation
needed to develop applications with %name

%prep
%setup
%patch -p1
sed -i 's,-O20,%optflags_optimization,g' configure*

%build
%autoreconf
%configure \
	--enable-pulse \
	--enable-alsa \
	--disable-alsa-mmap \
	--disable-broken-oss \
	--disable-oss \
	--disable-esd \
	--disable-arts \
	--disable-nas
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir
cat <<__EOF__ >%buildroot%_sysconfdir/%name.conf
# possible values for "default_driver" are: alsa, pulse
default_driver=alsa
__EOF__

%files
%config(noreplace) %_sysconfdir/%name.conf
%_libdir/*.so.*
%dir %_libdir/ao
%dir %_libdir/ao/plugins-4
%_libdir/ao/plugins-4/libalsa.so
%_man5dir/*

%if_enabled pulse
%files pulse
%_libdir/ao/plugins-4/libpulse.so
%endif

%files devel
%doc AUTHORS CHANGES TODO doc/*.{html,css,c}
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*

%changelog
* Fri Dec 01 2017 Michael Shigorin <mike@altlinux.org> 1:1.2.2-alt3
- generalized optflags fixup (ldv@)

* Fri Dec 01 2017 Michael Shigorin <mike@altlinux.org> 1:1.2.2-alt2
- introduce pulse knob (on by default)
- E2K: "-O20" is a bit too much!
  + see also https://github.com/kripken/emscripten/issues/264
- minor spec cleanup

* Sun Nov 05 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:1.2.2-alt1
- 1.2.2
- fixed pulse plugin (ALT#33125)

* Mon Mar 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt2
- patch from upstream: libao-1.0.0 pulseaudio fix

* Fri Mar 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt1
- 1.0.0

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
