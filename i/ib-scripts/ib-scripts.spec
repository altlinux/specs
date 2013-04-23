name: ib-scripts
version:1.0.0
release:alt1.qa1
Summary:Scripts for runting infiniband 
Group:System/Kernel and hardware
License:GPL
Packager:Michail Yakushin <silicium@altlinux.ru>
Source: ib-scripts.tar
Provides: udev-rules-hpc
Obsoletes: udev-rules-hpc
requires(post,preun): /sbin/service
Buildarch: noarch
%description
Scripts for runing infiniband in HPC clusters

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_udevrulesdir/
cp etc/udev/rules.d/90-ib.rules %buildroot%_udevrulesdir/

mkdir -p %buildroot%_sysconfdir/modprobe.d/
cp etc/modprobe.d/* %buildroot%_sysconfdir/modprobe.d/

mkdir -p %buildroot%_sysconfdir/rc.d/init.d/
cp etc/init.d/* %buildroot%_sysconfdir/rc.d/init.d/

%post 
%post_service ib

%preun 
%preun_service ib

%files 
%_udevrulesdir/*
%attr(0755,root,root) %_sysconfdir/rc.d/init.d/*
%_sysconfdir/modprobe.d/*

%changelog
* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for ib-scripts

* Tue Feb 26 2008 Michail Yakushin <silicium@altlinux.ru> 1.0.0-alt1
- moved from kernel-image-hpc 

