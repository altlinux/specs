Name: tircproxy
Version: 0.4.5
Release: alt3

Summary: (transparent) IRC proxy with DCC support.
Source: tircproxy-0.4.5.tar.gz
License: GPL
Group: Networking/IRC
Packager: Andrey Khavryuchenko <akhavr@altlinux.ru>
Url: http://bre.klaki.net/programs/tircproxy/
BuildRequires: OpenSP sgml-tools
Source1: tircproxy.service
Source2: tircproxy.conf.example

%changelog
%description
Tircproxy is a program designed to help IRC users who are not directly 
connected to the internet, but are behind a firewall based on Linux or 
some other Unix variant.

This is an IRC proxy server.  Features:
  + Supports DCC CHAT, SEND, RESUME and TSEND protocols.
  + Supports both transparent and dedicated operation.
  + Supports "anonymization" to hide users' identities.
  + Supports flexible authentication for access.
  + Can be run either standalone or via inetd.
  + Allows the admin to send "MOTD" style messages and/or
    broadcasts to the user(s).
  + Can block trojans such as 'script.ini', 'dmsetup.exe', etc.
  + Access controlled by /etc/hosts.allow and /etc/hosts.deny.
  + Can cooperate with some identds for non-root operation, or
    (if root) can change UID/GID according to client's IP addr.
  + Extensive documentation

%prep
%setup -c -q
%build
cd tircproxy-0.4
./configure
make
strip tircproxy
cd docs
make tircproxy.html
cd ..

%install
cd tircproxy-0.4
rm -f $RPM_BUILD_ROOT/usr/sbin/tircproxy
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man8
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/tircproxy

install -m 644 tircproxy.8 $RPM_BUILD_ROOT/usr/share/man/man8/tircproxy.8
install -s -m 755 tircproxy $RPM_BUILD_ROOT/usr/sbin/tircproxy
install -m 755 %SOURCE1 $RPM_BUILD_ROOT/etc/rc.d/init.d/tircproxy
install -m 644 %SOURCE2 $RPM_BUILD_ROOT/etc/tircproxy/

%files
/usr/sbin/tircproxy
/usr/share/man/man8/tircproxy.8.gz
/etc/rc.d/init.d/tircproxy
/etc/tircproxy/
%doc tircproxy-0.4/CHANGELOG.txt tircproxy-0.4/BUGS.txt 
%doc tircproxy-0.4/README 
%doc tircproxy-0.4/tircproxy-%{version}.lsm tircproxy-0.4/trojans.html 
%doc tircproxy-0.4/quizzes.txt tircproxy-0.4/docs/*.sgml 
%doc tircproxy-0.4/docs/Makefile tircproxy-0.4/docs/*.html

%changelog
* Wed Feb 2 2005 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.5-alt3
- Fixed manual page location

* Tue Feb 1 2005  Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.5-alt2
- Fixed BuildRequires

* Mon Jan 31 2005 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.5-alt1
- Initial build
