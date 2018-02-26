%define _user _q3
%define _group _q3
%define _home %_localstatedir/%name

%define revision 1114

%if %_arch == x86_64
%define __arch x86_64
%else
%define __arch i386
%endif

Name: quake3
Version: 1.34
Release: alt9.svn%revision

Summary: Quake 3: Arena by ID Software
License: GPL
Group: Games/Arcade
Url: http://ioquake3.org

Source: quake3-%version.tar.bz2
Source1: quake3-client.desktop
Source2: quake3-client-smp.desktop
Source3: quake3.png

Packager: Pavlov Konstantin <thresh@altlinux.ru>

Requires: %name-server = %version-%release
Requires: %name-client-smp = %version-%release
Requires: %name-client-up = %version-%release

BuildRequires: nasm gcc
BuildRequires: libSDL-devel libopenal-devel
BuildRequires: libXt-devel libGL-devel

%description
Quake 3: Arena by ID Software.

%description -l ru_RU.KOI8-R
Quake 3: Arena by ID Software.
Превосходная 3D-стрелялка.

%package common
Group: Games/Arcade
Summary: Common files for Quake 3: Arena

%description common
Quake 3: Arena by ID Software.
This package contains common files.

%description common -l ru_RU.KOI8-R
Quake 3: Arena by ID Software.
Этот пакет содержит общие файлы, используемые в других пакетах quake3.

%package client-up
Group: Games/Arcade
Summary: Uniprocessor quake3 client
Requires: %name-common = %version-%release
Provides: %name-client = %version-%release

%description client-up
Uniprocessor Quake 3: Arena client.

%description client-up -l ru_RU.KOI8-R
Клиент для игры Quake 3: Arena by ID Software. Однопроцессорная версия.

%package client-smp
Group: Games/Arcade
Summary: Multiprocessor quake3 client
Requires: %name-common = %version-%release
Provides: %name-client = %version-%release

%description client-smp
Multiprocessor Quake 3: Arena client.

%description client-smp -l ru_RU.KOI8-R
Клиент для игры Quake 3: Arena by ID Software. Многопроцессорная версия.

%package server
Group: Games/Arcade
Summary: Quake 3: Arena dedicated server package
Requires: %name-common = %version-%release

%description server
Quake 3: Arena by ID Software.
Dedicated server.

%description server -l ru_RU.KOI8-R
Quake 3: Arena by ID Software.
Выделенный сервер.

%prep
%setup -q

%build
%make_build release

%install
mkdir -p %buildroot%_bindir

install -p -D -m644 %SOURCE1 %buildroot%_datadir/applications/%name-client.desktop
install -p -D -m644 %SOURCE2 %buildroot%_datadir/applications/%name-client-smp.desktop

cat << __EOF__ > %buildroot%_bindir/quake3
#!/bin/sh

%_libdir/games/quake3/ioquake3.%__arch +set sv_pure 0 +set vm_cgame 0 +set vm_game 0 +set vm_ui 0 $@
__EOF__

cat << __EOF__ > %buildroot%_bindir/quake3-smp
#!/bin/sh

%_libdir/games/quake3/ioquake3-smp.%__arch +set sv_pure 0 +set vm_cgame 0 +set vm_game 0 +set vm_ui 0 $@
__EOF__

chmod +x %buildroot%_bindir/quake3
chmod +x %buildroot%_bindir/quake3-smp
ln -sf %_libdir/games/quake3/ioq3ded.%__arch %buildroot%_bindir/q3ded

install -D -p -m 0644 %{SOURCE3} %buildroot%_miconsdir/quake3.png

mkdir -p %buildroot%_libdir/games/quake3/baseq3/
make copyfiles COPYDIR="%buildroot%_libdir/games/quake3"

cat > README.ALT <<EOF
In order to actually play the game, you will need pak-files from original game CD (pak0.pk3) plus pak-
files from latest quake3 point release! Put them into %_libdir/games/quake3/baseq3/!
EOF

# initscript for dedicated server
install -pDm0755 %name.init %buildroot%_initdir/%name
install -pDm0755 %name-ctf.init %buildroot%_initdir/%name-ctf
install -pDm0644 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -pDm0644 %name-ctf.sysconfig %buildroot%_sysconfdir/sysconfig/%name-ctf

install -dm1700 %buildroot%_home

%pre server
/usr/sbin/groupadd -r -f %_group ||:
/usr/sbin/useradd -g %_group -c 'The quake3 user' \
        -d %_home -s /dev/null -r %_user >/dev/null 2>&1 ||:

%post common
echo "In order to actually play the game, you'll need pak-files from original game CD (pak0.pk3) plus pak-files from latest quake3 point release! Put them into %_libdir/games/quake3/baseq3/ ! "

%post server
%post_service %name
%post_service %name-ctf

%preun server
%preun_service %name
%preun_service %name-ctf

%files
%doc BUGS ChangeLog NOTTODO README TODO id-readme.txt md4-readme.txt README.ALT

%files common
%dir %_libdir/games/%name
%dir %_libdir/games/%name/baseq3
%dir %_libdir/games/%name/missionpack
%_libdir/games/%name/baseq3/cgame%__arch.so
%_libdir/games/%name/baseq3/qagame%__arch.so
%_libdir/games/%name/baseq3/ui%__arch.so
%_libdir/games/%name/missionpack/cgame%__arch.so
%_libdir/games/%name/missionpack/qagame%__arch.so
%_libdir/games/%name/missionpack/ui%__arch.so
%_miconsdir/*.png

%files client-up
%_bindir/%name
%_libdir/games/quake3/ioquake3.%__arch
%_datadir/applications/quake3-client.desktop

%files client-smp
%_bindir/%name-smp
%_libdir/games/quake3/ioquake3-smp.%__arch
%_datadir/applications/quake3-client-smp.desktop

%files server
%_bindir/q3ded
%_libdir/games/quake3/ioq3ded.%__arch
%config(noreplace) %_sysconfdir/sysconfig/*
%dir %attr(1770,root,%_group) %_home
%_initdir/*

%changelog
* Sun Apr 10 2011 Lenar Shakirov <snejok@altlinux.ru> 1.34-alt9.svn1114
- Fixed build: BuildReqs: libmesa-devel -> libGL-devel
- Desktop file fixed and cleaned: thanks to repocop!

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.34-alt8.svn1114.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for quake3-client-smp
  * pixmap-in-deprecated-location for quake3
  * update_menus for quake3-client-up
  * postclean-05-filetriggers for spec file

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt8.svn1114
- Fix #16247, thanks vvk@.

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt7.svn1114
- Fix #14027.

* Tue Dec 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt6.svn1114
- Merged vvk@'s initscripts for server side.

* Mon Jul 16 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt5.svn1114
- 1114 revision.
- Fixed launching.

* Tue Apr 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt4.svn1062
- Modified smp-desktop file to be able to launch SMP version.

* Tue Apr 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt3.svn1062
- 1062 revision.

* Thu Feb 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt3.svn1046
- Added requires: client-*, server to quake3 package.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt2.svn1046
- 1046 svn revision.
- Fixed symlinks.

* Mon Jan 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt2.svn1037
- 1037 svn revision.
- Gearified package.
- Added freedesktop menu files.
- Fixed Requires for common package.
- Fixed Provides for -client-smp package.
- Rewrote descriptions and summaries.
- Make common package own directories in %%_libdir/games/.
- Minor spec cleanup.
- Removed xorg-x11-devel from BuildRequires,
  Added libXt-devel and libmesa-devel to BuildRequires instead.
- Added icon.
- Added README.ALT concerning running the program.
- Removed gcc3.4 build-dependancy.
- Fixed URL.
- Rewrote install section using quake3 own Makefile directives.
- Moved binaries to %%_libdir/games/quake3.

* Wed Nov 01 2006 Igor Zubkov <icesik@altlinux.org> 1.34-alt1.svn956
- new version (#10073)
- rename quake3-client to quake3-client-up (#7811)
- add provides quake3-client to quake3-client-up and quake3-client-smp (#7811)
- add docs (#7810)
- use gcc 3.4 for build

* Tue Oct 31 2006 Alexey Shabalin <shaba@altlinux.ru> 1.34-alt0.1svn956
- svn 956
- fix spec for build x86_64
- move clients and server to %_bindir
- fix menu files

* Thu Oct 19 2006 Afanasov Dmitry <ender@atrus.ru> svn916-alt1
- svn rebuild

* Fri Aug 26 2005 Igor Zubkov <icesik@altlinux.ru> 1.32b-alt1
- Initial build for Sisyphus

