Name: fping
Version: 2.4b2
Release: alt4
%define srcname %name-%{version}_to

Summary: %name - A tool to quickly ping N number of hosts to determine their reachability
Summary(ru_RU.UTF-8): аналог ping для использования в скриптах.
License: GPL
Group: Security/Networking
Url: http://www.fping.com

Source0: http://www.fping.com/download/%name.tar.gz
Source1: fping.control
Patch: %name-2.4-alt-cleanup.patch

%description
fping is a ping(1) like program which uses the Internet Control Message
Protocol (ICMP) echo request to determine if a host is up. fping is
different from ping in that you can specify any number of hosts on the
command line, or specify a file containing the lists of hosts to ping.
Instead of trying one host until it timeouts or replies, fping will send out
a ping packet and move on to the next host in a round-robin fashion. If a
host replies, it is noted and removed from the list of hosts to check. If a
host does not respond within a certain time limit and/or retry limit it will
be considered unreachable.

%description -l ru_RU.UTF-8
fping это аналог известной утилиты ping(1) использующей протокол ICMP для
определения доступности удаленного хоста. fping создан для использования
в perl и shell скриптах. Поддерживает возможность сканирования диапазона
адресов.

%prep
%setup -q -n %srcname

%patch -p1

%build
%configure

%make_build

# in original tarball all files executable :(
chmod -x README INSTALL ChangeLog

%install
%make_install install DESTDIR=%buildroot

install -pD -m755 %SOURCE1 "%buildroot%_controldir/fping"

%pre
%pre_control fping

%post
%post_control -s public fping

%files
%_sbindir/*
%config %_controldir/*
%_man8dir/*
%doc README INSTALL ChangeLog

%changelog
* Sun Apr 06 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.4b2-alt4
- add control(8) support (#11891). Default state is restricted.

* Sun Apr 08 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.4b2-alt3
- rebuild with latest Sisyphus

* Sat Nov 16 2002 Igor Homyakov <homyakov at altlinux dot ru> 2.4b2-alt2
- spec cleanup (grammatic mistakes, wrong URL: )

* Tue Sep 03 2002 Igor Homyakov <homyakov at altlinux dot ru> 2.4b2-alt1
- little code cleanup
- first build for ALT Linux
