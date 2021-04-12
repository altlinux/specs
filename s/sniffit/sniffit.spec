Summary: Program for demonstrating the unsafeness of TCP
Summary(es):	A network protocol analyzer
Summary(pl):	Program do nasłuchu połączeń TCP/UDP/ICMP
Summary(pt_BR):	Um analisador de protocolos de rede
Name: sniffit
Version: 0.5
Release: alt1
License: BSD-3-Clause
Group: Monitoring
Source: %name-%version.tar.gz
Patch: sniffit_0.3.7.beta-11.diff
Url: http://www.securitylab.ru/software/233919.php

# Automatically added by buildreq on Sun Mar 25 2012
# optimized out: libtinfo-devel
BuildRequires: libncurses-devel libpcap-devel

%description
Sniffit is a packet sniffer for TCP/UDP/ICMP packets. Sniffit is able
to give you very detailed technical info on these packets (SEQ, ACK,
TTL, Window, ...) but also packet contence in different formats (hex
or plain text, ...).

%description -l es
Sniffit is a robust non-commercial network protocol analyzer or packet
sniffer. A packet sniffer basically listens to network traffic and
produces analysis based on the traffic and/or translates packets into
some level of human readable form.

%description -l pl
Sniffit jest programem do podsłuchu pakietów TCP/UDP/ICMP. Sniffit
jest w stanie podać Ci bardzo wiele informacji o tych pakietach (SEQ,
ACK, TTL, Okno, ...) a także ich zawartość w różnych formatach
(szesnastkowo lub w czystej postaci, ...).

%description -l pt_BR
Sniffit é um analisador de redes. Ele monitora o tráfego de rede e
produz uma análise compreensível por humanos.

%prep
%setup
#patch -p1

%build
%autoreconf
%configure --sbindir=%_bindir
%make_build OBJ_OPT="-g" EXE_OPT="-lpcap -g"

%install
%makeinstall_std
#install -D sniffit $RPM_BUILD_ROOT%_bindir/sniffit
#install -D sniffit.5 $RPM_BUILD_ROOT%_man5dir/sniffit.5
#install -D sniffit.8 $RPM_BUILD_ROOT%_man8dir/sniffit.8

%files
%doc docs examples
%doc *.md
%_mandir/man?/*
%_bindir/*

%changelog
* Mon Apr 12 2021 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Autobuild version bump to 0.5

* Mon Mar 26 2012 Fr. Br. George <george@altlinux.ru> 0.3.7-alt4
- Drop all old patches in favour of Debian one

* Tue Feb 16 2010 Fr. Br. George <george@altlinux.ru> 0.3.7-alt3
- Fix *64 build

* Sat Sep 27 2008 Fr. Br. George <george@altlinux.ru> 0.3.7-alt2
- Fix build

* Fri Jul 08 2005 Fr. Br. George <george@altlinux.ru> 0.3.7-alt1
- Adapted TLD Port

