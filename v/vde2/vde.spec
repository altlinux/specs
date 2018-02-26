%add_verify_elf_skiplist %_libdir/libvdehist.so*
%define _group vmusers

Name: vde2
Version: 2.3.1
Release: alt2

Summary: Virtual Distributed Ethernet
License: GPL
Group: Networking/Other
Url: http://vde.sourceforge.net/
Packager: Igor Vlasenko <viy@altlinux.ru>

Source0: http://prdownloads.sourceforge.net/%name/%name-%version.tar
Source1: README.altlinux
Source2: vde.init
Source3: vde-external.conf
Source4: vde-internal.conf

Patch: vde2-2.2.2-alt-PATH_MAX-1.patch
Patch1: vde2-2.3.1-alt-link.patch

%define major   .2
%define libname      lib%name%major
%def_disable static

Requires: %libname = %version-%release

BuildRequires: gcc-c++
BuildRequires: libssl-devel libpcap-devel

%description
VDE is a virtual network that can be spawned over a set of physical
computer over the Internet

VDE connects together:
  (1) real GNU-linux boxes (tuntap)
  (2) virtual machines: UML-User Mode Linux, qemu, bochs, MPS.

VDE can be used:
  (i) to create a general purpose tunnel (every protocol that runs
    on a Ethernet can be put into the tunnel)
  (ii) to connect a set of virtual machine to the Internet with no
    need of free access of tuntap
  (iii) to support mobility: a VDE can stay interconnected despite
    of the change of virtual cables, i.e. the change of IP addresses
    and interface in the real world

%package -n %libname
Summary: VDE libraries
Group: Networking/Other

%description -n %libname
Library files for VDE

%package -n libvde-devel
Summary: VDE libraries - header files
Group: Development/C
Requires: %libname = %version-%release

%description -n libvde-devel
header files for VDE Library files

%prep
%setup -q
cp %SOURCE1 .
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure %{subst_enable static} --enable-experimental
%make

%install
%makeinstall_std
find %buildroot -type f -name \*.la -delete

mkdir -p %buildroot%_initdir
install -m 0755 %SOURCE2 %buildroot%_initdir/%name
install -m 0644 %SOURCE3 %buildroot%_sysconfdir/%name/
install -m 0644 %SOURCE4 %buildroot%_sysconfdir/%name/
install -m 0770 -d %buildroot%_var/run/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/*
%_sbindir/*
%_mandir/man?/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_initdir/%name
%attr(750,root,%_group) %_var/run/%name
%doc README README.altlinux

%files -n %libname
%_libdir/*.so.*
%_libdir/vde2/
%_libexecdir/vdetap

%files -n libvde-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt2
- add libssl-devel to BR: for  VDE CryptCab
- add libpcap-devel to BR: for build pdump
- add --enable-experimental configure

* Fri Feb 25 2011 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Fri Oct 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt3
- Rebuilt for soname set-versions

* Tue Nov 24 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt2
- Fixed interpackage dependencies.
- Cleaned up specfile.

* Wed Oct 29 2008 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1
- new version

* Wed Jan 03 2007 Igor Vlasenko <viy@altlinux.ru> 2.1.6-alt1
- first build for Sisyphus

* Wed Jan  3 2007 Igor Vlasenko <viy@altlinux.org> 2.1.6-1.fc5.viy
- new version

* Tue Dec 26 2006 Igor Vlasenko <viy@altlinux.org> 1.5.11-1.fc5.viy
- rebuild for fc5

* Fri Aug 04 2006 Stew Benedict <sbenedict@mandriva.com> 1.5.11-1mdv2007.0
- 1.5.11, drop P0 - merged upstream

* Tue Jul 19 2005 Stew Benedict <sbenedict@mandriva.com> 1.5.9-1mdk
- first Mandriva release

