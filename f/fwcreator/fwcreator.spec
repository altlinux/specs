Name:		fwcreator
Version:	0.11.5
Release:	alt2
License:	GPL
Group:		Security/Networking
Source:		%{name}-%{version}.tar.bz2
#URL:		http://
BuildArch: 	noarch
#BuildRequires: 

Summary:	Firewall-script generator for iptables
Summary(ru_RU.CP1251):	Генератор shell-скрипта для организации файрвола на базе iptables
Summary(ru_UA.CP1251):	Генератор shell-скрипта для организации файрвола на базе iptables
Summary(uk_UA.CP1251):	Генератор shell-скрипту для створення файрволу засобами iptables

%description
Firewall-script generator for iptables
%description -l ru_RU.CP1251
Генератор shell-скрипта для создания файрвола. С его помощью вы
легко сможете настроить файрвол средней сложности пригодный для
использования на серверах небольших организаций. Получаемый 
скрипт использует программу управления пакетным фильтром ядра
iptables и строится по принципу "что не разрешено - запрещено"
%description -l ru_UA.CP1251
Генератор shell-скрипта для создания файрвола. С его помощью вы
легко сможете настроить файрвол средней сложности пригодный для
использования на серверах небольших организаций. Получаемый 
скрипт использует программу управления пакетным фильтром ядра
iptables и строится по принципу "что не разрешено - запрещено"
%description -l uk_UA.CP1251
Генератор shell-скрипту, який створює файрвол. За його допомогою ви
легко зможете налагодити файрвол середньої складності, придатний для
використання на серверах невеликих организацій. Скрипт який 
створюється використовує програму керування пакетним фільтром ядра
iptables і будується за принципом "що не дозволено - те заборонено"

%prep
%setup -q 

%build
#%make_build

%install
install -d $RPM_BUILD_ROOT%_bindir
install -m 755 %name $RPM_BUILD_ROOT%_bindir
install -d $RPM_BUILD_ROOT%_datadir/%name/shapes
install shapes/* $RPM_BUILD_ROOT%_datadir/%name/shapes

%files
%doc ChangeLog README* TODO COPYING samples KnownBugs
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Fri May 25 2007 Serge Polkovnikov <robin@altlinux.ru> 0.11.5-alt2
- Fixed spec-file Summary encoding
- Package group changed to Security/Networking

* Mon Dec 11 2006 Serge Polkovnikov <robin@altlinux.ru> 0.11.5-alt1
- Fixed nfs rules for use unprivileged ports (due moving mount.nfs
  to user space)
- Change American Army's rules for v2.7 (not tested)

* Tue Oct 17 2006 Serge Polkovnikov <robin@altlinux.ru> 0.11.4-alt2
- initial build for Sisyphus

* Tue Jun 21 2005 Serge Polkovnikov <p_serge@fromru.com> 0.11.4-alt1
- Added rules for network printers (port 515)
- Added rules for connect to VNC-servers (Virtual Network Computing)
- Fixed rules for dhcp (dhcp_output)
- Added rules for LineAge 2 servers
- Added rule for connecting to local NFS-server

* Tue Jan 31 2005 Serge Polkovnikov <p_serge@fromru.com> 0.11.3-alt1
- Added rules for M$SQL, JetDirect, RDP protocols
- Added rules for LIGA
- Fix rules for MySQL protocol
- Added $ANYPORTS constant for use in shapes

* Tue Dec 21 2004 Serge Polkovnikov <p_serge@fromru.com> 0.11.2-alt1
- Change name of some rules
- Fix misspells

* Mon Dec 09 2004 Serge Polkovnikov <p_serge@fromru.com> 0.11.1-alt1
- Redirect output to stdout if second parameter is absent 
- All files are converted to cp1251

* Mon Sep 28 2004 Serge Polkovnikov <p_serge@fromru.com> 0.11.0-alt1
- Replace command "iptables" to variable $IPTABLES in rule definition files
- Create shape-file "_iptables" where defined $IPTABLES 
- Append KnownBugs file to package

* Mon Sep 27 2004 Serge Polkovnikov <p_serge@fromru.com> 0.10.12-alt1
- Initial build

