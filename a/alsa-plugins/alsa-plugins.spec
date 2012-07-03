Name: alsa-plugins
Version: 1.0.24
Release: alt2
Serial: 1

Summary: Advanced Linux Sound Architecture (ALSA) plugins
License: LGPL
Group: System/Libraries

Url: http://www.alsa-project.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libalsa-devel libavcodec-devel libdbus-devel
BuildRequires: libpulseaudio-devel libsamplerate-devel libspeex-devel

Summary(ru_RU.UTF-8): Плагины ALSA
Summary(uk_UA.UTF-8): Плаг╕ни ALSA

%description
Advanced Linux Sound Architecture (ALSA) plugins.

%description -l ru_RU.UTF-8
Этот пакет содержит плагины ALSA.

%description -l uk_UA.UTF-8
Цей пакунок м╕стить плаг╕ни ALSA.

%package pulse
Summary: ALSA pulseaudio plugin
Group: Sound
Requires: libalsa >= 1.0.21a pulseaudio-daemon

%description pulse
ALSA pulseaudio plugin

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/alsa
cat << __EOF__ >> %buildroot%_datadir/alsa/pulse.conf
pcm.!default { type pulse }
ctl.!default { type pulse }
pcm.pulse { type pulse }
ctl.pulse { type pulse }
__EOF__

%files
%doc doc/*.txt doc/README-*
%_libdir/alsa-lib/*.so
%exclude %_libdir/alsa-lib/*pulse*.so

%files pulse
%_libdir/alsa-lib/*pulse*.so
%_datadir/alsa/pulse.conf

%changelog
* Fri Sep 09 2011 Michael Shigorin <mike@altlinux.org> 1:1.0.24-alt2
- rebuilt against libva
- merged spec with my old 1.0.22-alt1

* Wed Feb 16 2011 Michael Shigorin <mike@altlinux.org> 1:1.0.24-alt1
- 1.0.24

* Sun Apr 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.23-alt1
- 1.0.23

* Thu Dec 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.22-alt1
- 1.0.22

* Tue Sep 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.21-alt1
- 1.0.21
- new subpackage %name-pulse (closes: #21534)

* Tue Jul 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt4
- rebuild with libavutil.so.50

* Mon Jul 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt3
- disabled jack plugin

* Sun May 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt2
- rebuild

* Thu May 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt1
- 1.0.20

* Thu Feb 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.19-alt2
- rebuild with libavcodec.so.52

* Mon Jan 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.19-alt1
- 1.0.19

* Wed Oct 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.18-alt1
- 1.0.18

* Wed Jul 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt1
- 1.0.17

* Thu May 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.16-alt1
- 1.0.16

* Sun Jan 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.15-alt1
- 1.0.15
- spec cleanup
- update build dependencies

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.0.14-alt1
- 1.0.14
- fixed install
- set _unpackaged_files_terminate_build

* Mon Oct 16 2006 Michael Shigorin <mike@altlinux.org> 1.0.13-alt1
- 1.0.13

* Tue Sep 05 2006 Igor Zubkov <icesik@altlinux.ru> 1.0.12-alt2
- NMU
- add PulseAudio support (polypaudio removed)

* Sun Sep 03 2006 Michael Shigorin <mike@altlinux.org> 1.0.12-alt1
- 1.0.12
- changed BuildPreReq: kernel-headers-std to linux-libc-headers
- fixed README-polyp being renamed

* Wed May 31 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt5
- rebuilt against libpolyp-0.9

* Sat Apr 29 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt4
- accepted changes by icesik@
- minor cleanup

* Fri Apr 28 2006 Igor Zubkov <icesik@altlinux.ru> 1.0.11-alt3
- NMU
- real fix #9447
- buildreq
- add packager tag
- add docs

* Thu Apr 27 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt2
- fix #9447 (polypaudio support), thanks icesik@
- remove (unpackaged) *.la

* Wed Apr 19 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt1
- 1.0.11

* Wed Apr 05 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt0.4
- 1.0.11rc4
- minor spec cleanup

* Wed Nov 16 2005 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- 1.0.10

* Thu Jun 23 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1
- 1.0.9

* Thu Jun 09 2005 Michael Shigorin <mike@altlinux.ru> 1.0.9-alt0
- built for ALT Linux
