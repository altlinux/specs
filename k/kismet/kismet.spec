%define _unpackaged_files_terminate_build 1

%define cfgdir		%_sysconfdir/%name

Name: kismet
Version: 2014.02.R1
Release: alt1

Summary: Kismet wireless tools
License: GPLv2+
Group: Security/Networking

Url: http://www.kismetwireless.net/

# https://github.com/kismetwireless/kismet.git
Source: %name-%version.tar

BuildRequires: control gcc-c++ libcap-devel libncurses-devel libnl-devel
BuildRequires: libpcap-devel libpcre-devel libssl-devel setproctitle-devel
BuildRequires: libbluez-devel

Requires: kismet-client = %version-%release
Requires: kismet-server = %version-%release
Requires: kismet-drone = %version-%release
Requires: kismet-plugins = %version-%release

%description
Kismet is an 802.11 layer2 wireless network detector, sniffer, and
intrusion detection system. Kismet will work with any wireless card
which supports raw monitoring (rfmon) mode, and can sniff 802.11b,
802.11a, and 802.11g traffic.

Kismet identifies networks by passively collecting packets and detecting
standard named networks, detecting (and given time, decloaking) hidden
networks, and infering the presence of nonbeaconing networks via data
traffic.

This package is a virtual package requiring all the kismet files to be
installed. You may want to install it in the first time using kismet.

%package common
Summary: Common files for both client/server of kismet
Group: Security/Networking

%description common
Kismet is an 802.11 layer2 wireless network detector, sniffer, and
intrusion detection system. Kismet will work with any wireless card
which supports raw monitoring (rfmon) mode, and can sniff 802.11b,
802.11a, and 802.11g traffic.

This package contains common files for client/server of kismet.

%package client
Summary: Client user interface for kismet
Group: Security/Networking
Requires: kismet-common = %version-%release

%description client
Kismet is an 802.11 layer2 wireless network detector, sniffer, and
intrusion detection system. Kismet will work with any wireless card
which supports raw monitoring (rfmon) mode, and can sniff 802.11b,
802.11a, and 802.11g traffic.

This package contains user interface for kismet.

%package server
Summary: Server side of kismet project
Group: Security/Networking
Requires: kismet-common = %version-%release

%description server
Kismet is an 802.11 layer2 wireless network detector, sniffer, and
intrusion detection system. Kismet will work with any wireless card
which supports raw monitoring (rfmon) mode, and can sniff 802.11b,
802.11a, and 802.11g traffic.

This package contains server side of kismet project.

%package drone
Summary: Drone part of kismet project
Group: Security/Networking

%description drone
Kismet is an 802.11 layer2 wireless network detector, sniffer, and
intrusion detection system. Kismet will work with any wireless card
which supports raw monitoring (rfmon) mode, and can sniff 802.11b,
802.11a, and 802.11g traffic.

This package contains drone part of kismet project.

%package plugins
Summary: Plugins for kismet
Group: Security/Networking
Requires: %name-common = %version-%release

%description plugins
Kismet is an 802.11 layer2 wireless network detector, sniffer, and
intrusion detection system. Kismet will work with any wireless card
which supports raw monitoring (rfmon) mode, and can sniff 802.11b,
802.11a, and 802.11g traffic.

This package contains plugins shipped by the kismet package.


%prep
%setup

sed -i \
	-e '\!^ouifile=/etc/manuf!d' \
	-e '\!^ouifile=/usr/share/wireshark/wireshark/manuf!d' \
    		conf/kismet.conf.in conf/kismet_drone.conf

bzip2 CHANGELOG

%add_optflags -I%_includedir/pcre -fPIC

%autoreconf

%build
export ac_cv_lib_uClibcpp_main=no	# we do not want to build against uClibc++, even when available
%configure \
	--sysconfdir=%cfgdir \
	--with-pcreheaders=%_includedir/pcre

%make_build dep
%make_build HOME="$HOME"

for i in plugin-{alertsyslog,btscan,spectools,syslog}; do
	%make_build -C $i KIS_SRC_DIR=`pwd`
done

%install
%makeinstall_std \
	INSTUSR="$(id -un)" INSTGRP="$(id -gn)" MANGRP="$(id -gn)"

for i in plugin-{alertsyslog,btscan,spectools,syslog}; do
	%make install -C $i \
		INSTUSR="$(id -un)" INSTGRP="$(id -gn)" \
		KIS_SRC_DIR=`pwd` DESTDIR=`pwd`/_tmp
	install -pD -m644 $i/README %buildroot%_docdir/%name-plugins-%version/$i/README
done

mkdir -p %buildroot%_libdir/kismet{,_client}
install -pD -m755 _tmp/%_libdir/kismet/* %buildroot%_libdir/kismet/
install -pD -m755 _tmp/%_libdir/kismet_client/* %buildroot%_libdir/kismet_client/

install -pD -m755 %name-capture.control %buildroot%_controldir/%name-capture
install -pD -m755 kismet_capture %buildroot%_bindir/

rm -f %buildroot%_bindir/%name


%pre server
/usr/sbin/groupadd -r -f netadmin
%pre_control %name-capture

%post server
%post_control -s netadmin %name-capture


%files

%files common
%dir %cfgdir
%dir %_libdir/kismet/
%dir %_libdir/kismet_client/
%_datadir/kismet
%_man1dir/kismet.1*
%doc CHANGELOG* README* docs/ extra/old/

%files client
%_bindir/kismet_client

%files server
%config %_controldir/%name-capture
%_bindir/kismet_server
%attr(700,root,root) %verify(not mode,group) %_bindir/kismet_capture
%config(noreplace) %cfgdir/kismet.conf
%_man5dir/kismet.conf*

%files drone
%_bindir/kismet_drone
%_man1dir/kismet_drone*
%_man5dir/kismet_drone*
%config(noreplace) %cfgdir/kismet_drone.conf

%files plugins
%_libdir/kismet/*.so
%_libdir/kismet_client/*.so
%_docdir/%name-plugins-%version/

%changelog
* Tue Jan 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2014.02.R1-alt1
- Updated to upstream version 2014.02.R1.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2010.07.R1-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 2010.07.R1-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Jul 17 2010 Andrey Rahmatullin <wrar@altlinux.org> 2010.07.R1-alt1
- 2010-07-R1

* Tue Jan 12 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2010.01.R1-alt1
- 2010-01-R1
- package plugin README file

* Fri Dec 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2009.11.R1-alt1
- 2009-11-R1

* Sun Aug 23 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2009.06.R1-alt1
- 2009-06-R1 Newcore (closes: #15590)
- drop initscript and all related stuff, server should be run by user
  now (closes: #21186)
- implement control(8) support for kismet_capture (raorn@)
- package bundled plugins into -plugins subpackage
- leave only proper path to the wireshark manuf file in the default
  config (RH)

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 2008.05.R1-alt3
- fix build in current environment

* Sat Feb 21 2009 Ilya Mashkin <oddity@altlinux.ru> 2008.05.R1-alt2
- fix build
- update requires (fix #18831)
- fix init script (fix #18832)

* Mon Jun 02 2008 Pavlov Konstantin <thresh@altlinux.ru> 2008.05.R1-alt1
- 2008-05-R1 release.

* Fri Oct 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.10.R1-alt1
- 2007.10.R1 version.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.01.R1b-alt4
- Added fix for enable building on x86_64.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.01.R1b-alt3
- Specfile fixes here and there.
- Removed wget and diffutils from build requres.
- Replaced linux-libc-headers with glibc-kernheaders.
- Introduced gpsmap package.
- Packed some scripts from extra/ to kismet-common package.

* Sat Jan 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.01.R1b-alt2
- Added daemonization patch.
- Fixed kismet init script to work with daemonization.

* Sat Jan 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.01.R1b-alt1
- 2007-01-R1b version.

* Sat Jan 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 2006.04.R1-alt2
- Merged patches into source tree.
- Removed unneeded SOURCE1.

* Fri Nov 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 2006.04.R1-alt1
- Added init-script.
- Changed pid dir.
- Removed *.conf files from common package.

* Mon Aug 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 2006.04.R1-alt0.2
- Initial packaging for ALT Linux.
- main package is virtual, that requires:
  + kismet-server, the server side of kismet.
  + kismet-client, the client user interface of kismet.
  + kismet-drone, the remote drone for kismet.
- The spec file is based on Mandriva/FC's one, good man who made it is
  + Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>

