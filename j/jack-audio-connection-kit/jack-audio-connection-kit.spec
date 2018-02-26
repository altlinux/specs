Summary: The Jack Audio Connection Kit
Name: jack-audio-connection-kit
Version: 1.9.7
Release: alt1.1
Epoch: 1
License: GPLv2 and GPLv2+ and LGPLv2+
Group: Sound
URL: http://www.jackaudio.org

Provides: jackd = %epoch:%version-%release
Obsoletes: jackd < %epoch:%version

Source0: http://www.grame.fr/~letz/jack-%version.tar.bz2
Source2: %name-script.pa
Source3: %name-limits.conf
Patch0: jack-realtime-compat.patch
Patch1: jack-1.9.7-alt-fix.patch

BuildRequires: doxygen gcc-c++ libalsa-devel libcelt-devel libdbus-devel libexpat-devel libffado-devel libfreebob-devel
BuildRequires: libncurses-devel libreadline-devel libsamplerate-devel libsndfile-devel python-modules-compiler
BuildRequires: python-modules-email python-modules-encodings python-modules-logging

%description
JACK is a low-latency audio server, written primarily for the Linux
operating system. It can connect a number of different applications to
an audio device, as well as allowing them to share audio between
themselves. Its clients can run in their own processes (i.e. as a
normal application), or can they can run within a JACK server (i.e. a
"plugin").

JACK is different from other audio server efforts in that it has been
designed from the ground up to be suitable for professional audio
work. This means that it focuses on two key areas: synchronous
execution of all clients, and low latency operation.

%package -n libjack
Summary: Shared libraries to run JACK
Group: System/Libraries

%description -n libjack
This package contains the shared libraries required for %name

%package -n libjack-devel
Summary: Development files for JACK
Group: Development/C++
Provides: jackit-devel = %epoch:%version-%release jackit-devel-doc = %epoch:%version-%release
Obsoletes: jackit-devel < %epoch:%version jackit-devel-doc < %epoch:%version

%description -n libjack-devel
This package includes the development libraries and header files
necessary for developing programs which will use JACK

%package utils
Summary: Utilities for JACK
Group: Sound
Requires: %name = %version-%release
Provides: jackit-utils = %epoch:%version-%release
Obsoletes: jackit-utils < %epoch:%version

%description utils
Utilities that control and interact with the JACK server-jackd

%prep
%setup -q -n jack-%version
%patch0 -p1
%patch1 -p1

%build
./waf configure --prefix=%_prefix --libdir=/%_lib --doxygen --firewire --freebob --alsa --dbus --classic
[ -n "$NPROCS" ] || NPROCS=%__nprocs; ./waf build -j$NPROCS

%install
./waf --destdir=%buildroot install
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/pulse/%name.pa
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/security/limits.d/99-%name.conf

mkdir -p %buildroot%_datadir/doc/%name
mv %buildroot%_datadir/jack-audio-connection-kit/reference/html/* %buildroot%_datadir/doc/%name/

%files
%_sysconfdir/pulse/%name.pa
%_sysconfdir/security/limits.d/99-%name.conf
%_bindir/jackd*
%_bindir/jack_load
%_bindir/jack_unload
%_bindir/jack_connect
%_bindir/jack_disconnect
%_bindir/jack_lsp
%_libdir/libjackserver.so.*
%dir %_libdir/jack
%_libdir/jack/*.so
%_datadir/dbus-1/services/org.jackaudio.service
%_man1dir/jackd*.1*
%_man1dir/jack_load.1*
%_man1dir/jack_unload.1*
%_man1dir/jack_connect.1*
%_man1dir/jack_disconnect.1*
%_man1dir/jack_lsp.1*

%files -n libjack
%_libdir/libjack.so.*

%files -n libjack-devel
%_includedir/jack
%_libdir/libjack.so
%_pkgconfigdir/*.pc
%_datadir/doc/%name

%files utils
%exclude %_bindir/jack_load
%exclude %_bindir/jack_unload
%exclude %_bindir/jack_connect
%exclude %_bindir/jack_disconnect
%exclude %_bindir/jack_lsp
%_bindir/jack_*
%exclude %_man1dir/jack_load.1*
%exclude %_man1dir/jack_unload.1*
%exclude %_man1dir/jack_connect.1*
%exclude %_man1dir/jack_disconnect.1*
%exclude %_man1dir/jack_lsp.1*
%_man1dir/jack_*.1*
%_man1dir/jackrec.1*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.9.7-alt1.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.9.7-alt1
- 1.9.7

* Tue Mar 15 2011 Alexey Tourbin <at@altlinux.ru> 1:1.9.6-alt3
- rebuilt for debuginfo

* Wed Oct 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.9.6-alt2
- rebuild with celt-0.8.1

* Mon Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.9.6-alt1
- 1.9.6

* Tue Sep 14 2010 Fr. Br. George <george@altlinux.ru> 0.118.0-alt2
- Merged from test 5.1 build

* Tue Sep 14 2010 Fr. Br. George <george@altlinux.ru> 0.118.0-alt0.M51.2
- Build for 5.1
- Rebuild with libffado
- Minor spec cleanup

* Thu Dec 24 2009 Alex Karpov <karpov@altlinux.ru> 0.118.0-alt1
- picked from orphaned
    + new version

* Sat Dec 13 2008 Yuri N. Sedunov <aris@altlinux.org> 0.116.1-alt1
- 0.116.1 release
- updated faq.html, NEWS
- updated buildreqs
- removed obsolete post{,un}_ldconfig calls

* Sun Sep 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.102.9-alt0.svn.r987
- svn snapshot revision r987.
- add freebob support.

* Mon Apr 04 2006 LAKostis <lakostis at altlinux.ru> 0.100.0-alt1
- 0.100.0
- cleanup buildreq.

* Tue Sep 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.99.0-alt1
- 0.99.0
- added faq from %%url/docs/faq.php to jackd subpackage.
- NEWS file created from announce on %%url/releases/%%version/notice.php
- new %name-devel-doc subpackage includes reference manual,
  and example-clients source code.

* Tue Sep 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.98.1-alt1.1
- russian manpage (thanks Alexandre Prokoudine).

* Wed May 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.98.1-alt1
- 0.98.1

* Wed Jan 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.94.0-alt1
- 0.94.0

* Sat Dec 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.92.0-alt1
- 0.92.0
- do not build libjack-devel-static subpackage by default.

* Wed Nov 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.90.1-alt1
- 0.90.1
- don't package .la files.

* Sun Nov 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.90.0-alt1
- 0.90.0

* Fri Aug 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.80.0-alt1
- 0.80.0

* Thu Aug 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.75.0-alt1
- 0.75.0

* Fri Jul 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.74.0-alt1
- 0.74.0
- fixed silly bug with chown running from %%_sysconfdir/profile.d/jack.{sh,csh}
- summary, descriptions by avp.

* Mon Jul 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.72.4-alt3
- only users from group audio can run jackstart.
- change %%jackit_tmpdir to /var/lib/jack/tmp.
- mount, set ownership and permissions for %%jackit_tmpdir in %%post.
- adjust ownership and permissions for mounted %%jackit_tmpdir on boot.
- summary, descriptions by avp.

* Fri Jul 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.72.4-alt2
- jack_time_t defined as a type, patch from cvs.

* Tue Jun 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.72.4-alt1
- 0.72.4

* Sat May 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.71.1-alt1
- 0.71.1
- compiled --with-default-tmpdir=/mnt/ramfs. (see /usr/share/doc/jackd-0.71.1/README)

* Tue May 06 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.70.4-alt1
- 0.70.4

* Fri Mar 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.61.0-alt1
- New version.
- Capabilities enabled (wait for special multimedia kernel).

* Wed Feb 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.50.0-alt1
- new version.

* Sun Nov 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.34.0-alt0.8
- Built with new libsndfile-1.0.1, libfltk-1.1.0rc7
- Capabilities disabled (unusual for our kernels).

* Tue Aug 13 2002 Grigory Milev <week@altlinux.ru> 0.34.0-alt0.7
- recompile with libfltk-1.1.0rc5

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 0.34.0-alt0.6
- fixed suid/sgid file permissions

* Wed Jun 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.34.0-alt0.5
- 0.34.0
- fixed requires for devel-static package.

* Thu May 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.7-alt0.5cvs20020523
- built current cvs snapshot.

* Mon Feb 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.7-alt0.5
- first build for Sisyphus.

