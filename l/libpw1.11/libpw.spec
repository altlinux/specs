Packager: Denis Smirnov <mithraen@altlinux.ru>

%define _name pwlib

Name: libpw1.11
Version: 1.11.2
Release: alt0.9cvs20061011.1

Summary: Portable Windows Libary
Summary(ru_RU.KOI8-R): Переносимая Windows-библиотека

License: GPL
Group: System/Libraries
#Url: http://www.openh323.org/
Url: http://snapshots.gnomemeeting.net/

#Source: http://www.openh323.org/bin/pwlib-%version.tar.bz2
Source: http://snapshots.ekiga.net/cvs/%_name-cvs.tar.bz2
#Source: http://www.ekiga.org/downloads/beta2/sources/pwlib-%version.tar.bz2

%def_without dc
%def_without avc

# Automatically added by buildreq on Sat Jan 21 2006
BuildRequires: aalib-devel flex gcc-c++ libSDL_sound-devel libalsa-devel libexpat-devel libldap-devel libsasl2-devel libssl-devel libstdc++-devel xorg-proto-devel

BuildPreReq: bison
BuildPreReq: libexpat-devel > 1.95.6-alt1

Conflicts: libpw-devel
Conflicts: libpw

%description
PWLib is a moderately large class library that has its genesis many
years ago asa method to product applications to run on both Microsoft
Windows and Unix X-Window systems. It also was to have a Macintosh
port as well but this never eventeated. Unfortunately this package
contains no GUI code.

%description -l ru_RU.KOI8-R
PWLib -- это достаточно большая библиотека классов, которая возникла
много лет назад на основе метода asa выпускать приложения, выполняющиеся
как на Microsoft Windows, так и на Unix-системах X-Window. Также она
должна была быть портирована на Macintosh, но этого пока не случилось.
К сожалению, данный пакет не содержит кода графического интерфейса
пользователя.

%package devel
Summary: Portable Windows Libary development files
Summary(ru_RU.KOI8-R): Файлы для разработки с переносимой оконной библиотекой
Group: Development/C
Requires: %name = %version-%release
Obsoletes: libpwlib-devel

Conflicts: libpt-devel
Conflicts: libpw-devel

%description devel
Header files and libraries for developing applications that use pwlib.

%description devel -l ru_RU.KOI8-R
Заголовочные файлы и библиотеки для разработки программ, использующих pwlib.

%package plugins
Summary: Main plugins for pwlib
Group: System/Libraries
Requires: %name = %version-%release

Conflicts: libpw-plugins

%description plugins
This package contains the oss, alsa and v4l plugins for pwlib

%if_with dc
%package plugins-dc
Summary: Dc plugin for pwlib
Group: System/Libraries
Requires: %name = %version-%release

Conflicts: libpw-plugins-dc

%description plugins-dc
This package contains the dc plugin for pwlib
%endif

%if_with avc
%package plugins-avc
Summary: AVC plugin for pwlib
Group: System/Libraries
Requires: %name = %version-%release

Conflicts: libpw-plugins-avc

%description plugins-avc
This package contains the AVC plugin for pwlib
%endif

%prep
%setup -q -n %_name
sed -i "s|LIBRARIES = |LIBRARIES=|" ./configure

%build
# Fature since gcc3.4
%add_optflags -fno-unit-at-a-time
%configure \
	--enable-plugins --enable-rtti \
	--enable-alsa --enable-oss
# enable only? (see configure --help)
#	--enable-openh323 --enable-opal
%make_build
# optshared OPTCCFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall_std

#fix doc perms
chmod a+r *.txt

cd %buildroot%_datadir/%_name/make
#fix PWLIBDIR
sed -i 's|\(PWLIBDIR.*\)=.*|\1= %_datadir/%_name|' ./ptbuildopts.mak
#remove unpackaged files
rm -f *.{pat,in,lib64,libname,%_namedir,includesdir}
# do not packing esd plugin
rm -f %buildroot/%_libdir/pwlib/devices/sound/esd_pwplugin.so

# install ptlib-config
install -d %buildroot%_bindir
ln -snf %_datadir/%_name/make/ptlib-config %buildroot%_bindir/ptlib-config

%files
%doc *.txt
%_libdir/lib*.so.*

%files devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_datadir/%_name/

%files plugins
%dir %_libdir/pwlib/
%dir %_libdir/%_name/devices/
%dir %_libdir/%_name/devices/sound/
%dir %_libdir/%_name/devices/videoinput/
%_libdir/%_name/devices/sound/alsa_pwplugin.so
%_libdir/%_name/devices/sound/oss_pwplugin.so
%_libdir/%_name/devices/videoinput/v4l_pwplugin.so

%if_with dc
%files plugins-dc
%_libdir/%_name/devices/videoinput/dc_pwplugin.so
%endif

%if_with avc
%files plugins-avc
%_libdir/%_name/devices/videoinput/avc_pwplugin.so
%endif

%changelog
* Wed May 25 2011 Denis Smirnov <mithraen@altlinux.ru> 1.11.2-alt0.9cvs20061011.1
- rebuild

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.11.2-alt0.9cvs20061011
- auto rebuild

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.11.2-alt0.8cvs20061011
- auto rebuild

* Mon Oct 04 2010 Denis Smirnov <mithraen@altlinux.ru> 1.11.2-alt0.7cvs20061011
- fix build with new openssl

* Sat Sep 19 2009 Denis Smirnov <mithraen@altlinux.ru> 1.11.2-alt0.6cvs20061011
- build without video support

* Fri Dec 19 2008 Denis Smirnov <mithraen@altlinux.ru> 1.11.2-alt0.5cvs20061011
- add coinflict %name-devel -> libpw-devel

* Sat Dec 13 2008 Denis Smirnov <mithraen@altlinux.ru> 1.11.2-alt0.4cvs20061011
- add conflict %name-devel -> libpt-devel
- add conflicts %name-plugins-* -> libpw-plugins-*

* Mon Nov 17 2008 Denis Smirnov <mithraen@altlinux.ru> 1.11.2-alt0.3cvs20061011
- post/postun ldconfig
- cleanup spec

* Mon Mar 05 2007 Denis Smirnov <mithraen@altlinux.ru> 1.11.2-alt0.2cvs20061011
- package libpw 1.11 cvs with different name

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
- move ptlib from %_includedir to %_includedir/libpwlib
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
#- %%debug switch handling fixed

#Revision 1.8  2001/01/10 14:48:15  jajcus
#- Release: alt0.1
#- library names changed (we don't need sytem type and such in library name)
#- *.mak files changed so apps compilations won't try to build pwlib
#- %%debug macro used together with pwlib's building system
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
