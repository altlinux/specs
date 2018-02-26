%define oname ptlib

Name: libpt
Version: 2.8.4
Release: alt2
Summary: Portable Tools Libary
License: MPL
Group: System/Libraries
Url: http://www.opalvoip.org/

Provides: ptlib libpw
Obsoletes: libpw

Source: %oname-%version.tar
Patch: %oname-%version-%release.patch

BuildRequires: flex gcc-c++ libSDL-devel libalsa-devel libavc1394-devel libdv-devel libexpat-devel
BuildRequires: libldap-devel libpulseaudio-devel libraw1394-devel libv4l-devel

%description
PTLib (Portable Tools Library) is a moderately large class library that has it's
genesis many years ago as PWLib (portable Windows Library), a method to product
applications to run on both Microsoft Windows and Unix systems. It has also been
ported to other systems such as Mac OSX, VxWorks and other embedded systems.

Since then the system has grown to include many classes that assist in writing
complete multi-platform applications. Classes for I/O portability, multi-
threading portability, aid in producing unix daemons and NT services portably
and all sorts of internet protocols were added over the years. So it became a
Portable Tools Library and was renamed to PTLib.

All this over and above basic "container" classes such as arrays, linear lists,
sorted lists (RB Tree) and dictionaries (hash tables) which were all created
before STL was standardized. Future versions of PTLib will see many of these
classes replaced or supplemented by STL.

%package devel
Summary: Portable Tools Libary development files
Group: Development/C
Requires: %name = %version-%release
Provides: libpw-devel
Obsoletes: libpw-devel

%description devel
Header files and libraries for developing applications that use %oname

%package plugins
Summary: Main plugins for %oname
Group: System/Libraries
Requires: %name = %version-%release
Provides: libpw-plugins
Obsoletes: libpw-plugins

%description plugins
This package contains the oss, alsa and v4l2 plugins for ptlib

%prep
%setup -q -n %oname-%version
%patch -p1

cd plugins
autoconf -f
cd ..

%build
%configure \
	--enable-v4l2 \
	--enable-plugins \
	--enable-alsa \
	--enable-pulse \
	--disable-oss \
	--disable-avc \
	--disable-v4l
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc *.txt
%_libdir/lib*.so.*

%files devel
%_bindir/%oname-config
%_includedir/pt*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/%oname

%files plugins
%dir %_libdir/%oname-%version
%dir %_libdir/%oname-%version/devices
%dir %_libdir/%oname-%version/devices/sound
%dir %_libdir/%oname-%version/devices/videoinput
%_libdir/%oname-%version/devices/sound/*_pwplugin.so
%_libdir/%oname-%version/devices/videoinput/*_pwplugin.so

%changelog
* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.8.4-alt2
- resurrect

* Tue Mar 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.8.4-alt1
- 2.8.4

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.6.7-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Mon May 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.6.7-alt1
- 2.6.7

* Tue Sep 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Tue Sep 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.4-alt3
- rebuild with libldap2.4

* Fri Jul 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.4-alt2
- backported pulse plugin from trunk

* Tue Jul 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Tue Jun 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.3-alt2
- 2.6.3 release

* Wed May 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Sun Apr 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Jan 13 2009 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- new version 2.4.4 (with rpmrb script)

* Tue Nov 18 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)

* Thu Oct 16 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- rename package to libpt (ptlib)
- update buildreq
- rewrote spec

* Wed Oct 10 2007 Vitaly Lipatov <lav@altlinux.ru> 1:1.10.10-alt1
- new version 1.10.10 (with rpmrb script)

* Tue Sep 18 2007 Vitaly Lipatov <lav@altlinux.ru> 1:1.10.9-alt1
- new version 1.10.9 (with rpmrb script)

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 1:1.10.7-alt2
- fix plugins linking (fix alsa problem)

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 1:1.10.7-alt1
- new version 1.10.7 (with rpmrb script)

* Sun Mar 11 2007 Vitaly Lipatov <lav@altlinux.ru> 1:1.10.5-alt1
- new version 1.10.5 (with rpmrb script)

* Sat Feb 17 2007 Vitaly Lipatov <lav@altlinux.ru> 1:1.10.4-alt1
- stable version (1.10.4)
- add serial:1

* Thu Oct 12 2006 Vitaly Lipatov <lav@altlinux.ru> 1.11.2-alt0.1cvs20061011
- new snapshot

* Sun Jul 23 2006 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt0.1cvs20060723
- new snapshot

* Wed Jun 07 2006 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt0.1cvs20060603
- new snapshot

* Wed May 24 2006 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt0.1cvs20060521
- new snapshot

* Tue May 16 2006 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt0.1cvs20060515
- new snapshot

* Thu Apr 13 2006 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt0.1cvs20060413
- new snapshot

* Tue Feb 28 2006 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt0.1cvs20060228
- new snapshot
- cleanup spec

* Sat Feb 25 2006 Yuri N. Sedunov <aris@altlinux.ru> 1.11.0-alt0.1
- current cvs snapshot

* Tue Feb 14 2006 Vitaly Lipatov <lav@altlinux.ru> 1.9.3-alt1
- new version

* Sat Jan 21 2006 Vitaly Lipatov <lav@altlinux.ru> 1.9.2-alt1
- new version (release)

* Sat Jan 07 2006 Vitaly Lipatov <lav@altlinux.ru> 1.9.2-alt0.1cvs20060107
- new version (actually snapshot)

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1.1
- rebuild with libraw1394.so.5

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version (from FC3)

* Sun Feb 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.8.3-alt1
- new version
- update patches and spec from MDK (enable plugins)
- enable rtti (fix bug #5806)
- use a macro for ldconfig
- remove defattr from files section

* Fri May 21 2004 Vitaly Lipatov <lav@altlinux.ru> 1.6.5-alt1
- new version

* Fri Jan 02 2004 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version
- build with gcc3.3
- adopted some fixes from Mandrake

* Tue Apr 01 2003 Vitaly Lipatov <lav@altlinux.ru> 1.4.7-alt2
- workaround for new bison
- rebuild with new libexpat

* Tue Mar 25 2003 Vitaly Lipatov <lav@altlinux.ru> 1.4.7-alt1
- new version

* Wed Dec 04 2002 Vitaly Lipatov <lav@altlinux.ru> 1.3.11-alt3
- rename package to libpw

* Mon Dec 02 2002 Vitaly Lipatov <lav@altlinux.ru> 1.3.11-alt2
- remove packname from spec
- rename package to libpwlib

* Sun Nov 24 2002 Vitaly Lipatov <lav@altlinux.ru> 1.3.11-alt1
- spec cleanup, summary and description are translated in russian
- move ptlib from /usr/include to /usr/include/libpwlib
- all pwlib entry changed to libpwlib
- new version

* Tue Oct 08 2002 AEN <aen@altlinux.ru> 1.3.3-alt1
- new version

* Wed Mar 13 2002 AEN <aen@logic.ru> 1.2.12-alt1
- new version

* Wed Oct 10 2001 AEN <aen@logic.ru> 1.1.36-alt1
- new version

* Tue Jul 3 2001 AEN <aen@logic.ru> 1.1.33-alt1
- rebuilt for Sisyphus
- new names

* Sat Jun 23 2001 Stefan van der Eijk <stefan@eijk.nu> 1.1.33-1mdk
- 1.1.33

*  Sun Jun  3 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.1.19-5mdk
- Add patch to fix build on newer gccs.

* Fri Mar 23 2001 David BAUDENS <baudens@mandrakesoft.com> 1.1.19-4mdk
- PPC: build with gcc
- Requires: %%version-%%release and not only %%version

* Mon Jan 22 2001 David BAUDENS <baudens@mandrakesoft.com> 1.1.19-3mdk
- Fix build on PPC
- Bzip2 sources

* Sun Jan 21 2001 David BAUDENS <baudens@mandrakesoft.com> 1.1.19-2mdk
- Fix %%changelog to allow automatic rebuild
- Add description for SRPM package

* Mon Jan 15 2001 Frederic Lepied <flepied@mandrakesoft.com> 1.1.19-1mdk
- first Linux-Mandrake version

# Dadou - 1.1.19-2mdk - Don't uncomment lines below or you'll break automatic
#                       rebuild
#* %%date PLD Team <pld-list@pld.org.pl>
#All persons listed below can be reached at <cvs_login>@pld.org.pl

#$Log: pwlib.spec,v $
#Revision 1.11  2001/01/11 21:42:36  waszi
#- fixed sed invocation

#Revision 1.10  2001/01/11 14:36:57  jajcus
#- some typos

#Revision 1.9  2001/01/10 14:53:33  jajcus
#- %%{debug} switch handling fixed

#Revision 1.8  2001/01/10 14:48:15  jajcus
#- Release: alt1
#- library names changed (we don't need sytem type and such in library name)
#- *.mak files changed so apps compilations won't try to build pwlib
#- %%{debug} macro used together with pwlib's building system
#- only dynamically-linked version of asnparser is built

#Revision 1.7  2001/01/08 09:50:13  kloczek
#- release 2.

#Revision 1.6  2001/01/06 11:08:13  jajcus
#- these are not X11 libraries

#Revision 1.5  2001/01/04 19:50:01  kloczek
#- small simplifications in %install.

#Revision 1.4  2001/01/04 19:31:42  jajcus
#- prefix changed to /usr, as the sources don't contain any GUI code

#Revision 1.3  2001/01/04 12:48:11  jajcus
#- while installing update *.mak files

#Revision 1.2  2001/01/04 10:40:49  jajcus
#- *.mak files are needed in -devel package

#Revision 1.1  2001/01/04 09:46:14  jajcus
#- initial spec
