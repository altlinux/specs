Name: apt-scripts
Version: 0.1.2
Release: alt2

Summary: Lua scripts for APT
License: GPL
Group: System/Configuration/Packaging

Source0: %name-%version.tar.gz

BuildRequires: apt
BuildArch: noarch

%description
apt-cache list-extras
	This script will list all installed packages which are
	not availabe in any online repository.
apt-cache list-nodeps
	This script will list all installed packages which are
	not required by any other installed package.
apt-cache list-unreleased
	This script will list all installed packages which have
	version newer than in repository.

%prep
%setup -q

%install
for f in *.lua; do install -pD -m755 $f %buildroot/usr/share/apt/scripts/$f; done
for f in *.conf; do install -pD -m644 $f %buildroot/etc/apt/apt.conf.d/$f; done

cat *.conf >.apt.conf
apt-cache -c .apt.conf -o Dir::Bin::scripts=%buildroot/usr/share/apt/scripts list-extras
apt-cache -c .apt.conf -o Dir::Bin::scripts=%buildroot/usr/share/apt/scripts list-nodeps
apt-cache -c .apt.conf -o Dir::Bin::scripts=%buildroot/usr/share/apt/scripts list-unreleased
apt-cache -c .apt.conf script ./list-extras.lua
apt-cache -c .apt.conf script ./list-nodeps.lua
apt-cache -c .apt.conf script ./list-unreleased.lua

mkdir -p %buildroot/etc/buildreqs/files/ignore.d
ls *.conf |sed 's:^:^/etc/apt/apt.conf.d/:;s:[.]:[.]:g' >%buildroot/etc/buildreqs/files/ignore.d/%name

%files
/usr/share/apt
%config /etc/apt/apt.conf.d/*
%config /etc/buildreqs/files/ignore.d/%name

%changelog 
* Fri Dec 23 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1.2-alt2
- fixed list-extras and list-unreleased scripts (closes: #32938)

* Wed Jan  2 2013 Terechkov Evgenii <evg@altlinux.org> 0.1.2-alt1
- list-unreleased
 
* Sat Mar 01 2008 Alexey Tourbin <at@altlinux.ru> 0.1.1-alt3
- rebuild for new dependencies

* Sat Jun 17 2006 Alexey Tourbin <at@altlinux.ru> 0.1.1-alt2
- added /etc/buildreqs/files/ignore.d/%name (*.conf files)

* Sun May 21 2006 Alexey Tourbin <at@altlinux.ru> 0.1.1-alt1
- added 'apt-cache list-nodeps'

* Tue May 16 2006 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- initial revision, only 'apt-cache list-extras' for now
