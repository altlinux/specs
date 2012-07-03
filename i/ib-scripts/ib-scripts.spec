name: ib-scripts
version:1.0.0
release:alt1
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
mkdir -p %buildroot%_sysconfdir/udev/rules.d/
cp etc/udev/rules.d/90-ib.rules %buildroot%_sysconfdir/udev/rules.d/

mkdir -p %buildroot%_sysconfdir/modprobe.d/
cp etc/modprobe.d/* %buildroot%_sysconfdir/modprobe.d/

mkdir -p %buildroot%_sysconfdir/rc.d/init.d/
cp etc/init.d/* %buildroot%_sysconfdir/rc.d/init.d/

%post 
%post_service ib

%preun 
%preun_service ib

%files 
%_sysconfdir/udev/rules.d/*
%attr(0755,root,root) %_sysconfdir/rc.d/init.d/*
%_sysconfdir/modprobe.d/*

%changelog
* Tue Feb 26 2008 Michail Yakushin <silicium@altlinux.ru> 1.0.0-alt1
- moved from kernel-image-hpc 

