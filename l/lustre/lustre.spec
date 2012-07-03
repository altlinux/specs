%def_enable utils
%def_enable liblustre
%def_disable tests
%def_enable doc
%def_disable cray_xt3
%def_disable bgl
%def_disable uoss
%def_disable posix_osd
%def_enable server
%def_enable client
%def_disable libcfs_cdebug
%def_disable libcfs_trace
%def_disable libcfs_assert
%def_enable affinity
%def_enable backoff
%def_disable panic_dumplog
%def_enable pinger
%def_enable checksum
%def_enable liblustre_recovery
%def_enable quota
%def_disable health_write
%def_enable lru_resize
%def_enable adaptive_timeouts
%def_enable liblustre_acl
%def_enable readline
%def_disable efence
%def_enable libwrap
%def_enable libpthread
%def_enable sysio_init
%def_enable urandom
%def_enable usocklnd
%def_disable mindf
%def_enable fail_alloc
%def_enable snmp
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

Name: lustre
Version: 1.8.4
Release: alt6

Summary: Lustre File System
License: GPLv2
Group: Networking/Other
Url: http://clusterfs.com/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kernel
BuildRequires: libe2fs-devel perl-devel zlib-devel
%{?_enable_readline:BuildRequires: libncurses-devel libreadline-devel}
%{?_enable_efence:BuildRequires: libefence-devel}
%{?_enable_snmp:BuildRequires: libnet-snmp-devel libnl-devel libsensors3-devel}

%description
Userspace tools and files for the Lustre file system.

%package snmp
Summary: Lustre SNMP MIB and plugin 
Group: System/Servers
Requires: %name = %version-%release
Requires: net-snmp-mibs

%description snmp
Lustre SNMP MIB and plugin

%package -n liblustre-devel
Summary: Files for development with Lustre libs
Group: Development/C
Provides: liblustre-devel-static = %version-%release

%description -n liblustre-devel
Files for development with Lustre libs.


%package -n kernel-source-%name
Summary: Lustre sources for kernel development
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
Lustre sources for kernel development.


%if_enabled tests
%package tests
Summary: Lustre testing framework
Group: Development/Kernel
Requires: %name = %version

%description tests
This package contains a set of test binaries and scripts that are
intended to be used by the Lustre testing framework.
%endif


%prep
%setup

%build
%configure \
    --disable-modules \
    %{subst_enable utils} \
    %{subst_enable liblustre} \
    %{subst_enable tests} \
    %{subst_enable doc} \
    %{subst_enable_to cray_xt3 cray-xt3} \
    %{subst_enable bgl} \
    %{subst_enable uoss} \
    %{subst_enable_to posix_osd posix-osd} \
    %{subst_enable server} \
    %{subst_enable client} \
    %{subst_enable libcfs_cdebug libcfs-cdebug} \
    %{subst_enable libcfs_trace libcfs-trace} \
    %{subst_enable libcfs_assert libcfs-assert} \
    %{subst_enable affinity} \
    %{subst_enable backoff} \
    %{subst_enable panic_dumplog} \
    %{subst_enable pinger} \
    %{subst_enable checksum} \
    %{subst_enable liblustre_recovery liblustre-recovery} \
    %{subst_enable quota} \
    %{subst_enable health_write health-write} \
    %{subst_enable lru_resize lru-resize} \
    %{subst_enable adaptive_timeouts adaptive-timeouts} \
    %{subst_enable_to tests liblustre-tests} \
    %{subst_enable liblustre_acl liblustre-acl} \
    %{subst_enable_to tests mpitests} \
    %{subst_enable readline} \
    %{subst_enable efence} \
    %{subst_enable libwrap} \
    %{subst_enable libpthread} \
    %{subst_enable sysio_init sysio-init} \
    %{subst_enable urandom} \
    %{subst_enable usocklnd} \
    %{subst_enable mindf} \
    %{subst_enable fail_alloc fail-alloc} \
    %{subst_enable snmp}
%make_build distdir=kernel-source-%name-%version distdir all
bzip2 --best --keep --force {lnet,%name}/ChangeLog


%install
%make_install DESTDIR=%buildroot install
rm -f %buildroot{%_datadir/%name/*.patch,%_bindir/config.sh}
mv %buildroot%_includedir/{linux,%name/}
cp -a ldiskfs/ldiskfs/ldiskfs kernel-source-%name-%version/ldiskfs/ldiskfs
install -d -m 0755 %buildroot%kernel_src
tar -cj kernel-source-%name-%version > %buildroot%kernel_src/kernel-source-%name-%version.tar.bz2
install -d -m 0755 %buildroot%_docdir/%name-%version/{lnet,%name}
install -m 0755 lnet/ChangeLog.* %buildroot%_docdir/%name-%version/lnet/
install -m 0755 %name/{BUGS,ChangeLog.*} %buildroot%_docdir/%name-%version/%name/
install -m 0755 README %buildroot%_docdir/%name-%version/

%if_enabled snmp
mkdir -p %buildroot%_datadir/snmp/mibs
mv %buildroot%_datadir/lustre/snmp/mibs/* %buildroot%_datadir/snmp/mibs/
rm -rf %buildroot%_datadir/lustre/snmp
%endif

%files
%_docdir/%name-%version
/sbin/*
%_sbindir/*
%_bindir/*
%dir %_libdir/lustre
%_datadir/%name
%_man1dir/*
%_man7dir/*
%_man8dir/*


%files -n liblustre-devel
%_includedir/*
%_libdir/*.a
%_man3dir/*

%if_enabled snmp
%files snmp
%_libdir/lustre/snmp
%_datadir/snmp/mibs/Lustre-MIB.txt
%endif

%files -n kernel-source-%name
%kernel_src/*


%if_enabled tests
%files tests
%endif

%changelog
* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.4-alt6
- Fixed build with new e2fsprogs

* Thu May 05 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.4-alt5
- fixed build witn net-snmp, again

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.4-alt4
- Rebuilt for debuginfo

* Mon Dec 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.4-alt3
- Rebuilt with net-snmp 5.6

* Tue Oct 05 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.4-alt2
- fix kernel compatibility issue for v2.6.32

* Fri Oct  1 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Mon Apr 26 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.1.1-alt3
- workaround glibc detected overflow in `lfs getstripe'
- fix segfault in loadgen

* Thu Mar 18 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.1.1-alt2
- build snmp module

* Thu Nov 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.1.1-alt1
- 1.8.1.1

* Tue Jul 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0.1-alt1.2
- Fixed "always overflow destination buffer"

* Sun Jul 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0.1-alt1.1
- Build for Sisyphus

* Fri Jun 26 2009 Led <led@altlinux.ru> 1.8.0.1-alt1
- 1.8.0.1

* Mon Jun 22 2009 Led <led@altlinux.ru> 1.8.0-alt2
- fixes in kernel part

* Fri Jun 19 2009 Led <led@altlinux.ru> 1.8.0-alt1
- 1.8.0
- updated BuildRequires

* Fri Jun 19 2009 Led <led@altlinux.ru> 1.6.7.2-alt1
- 1.6.7.2

* Sun Apr 19 2009 Led <led@altlinux.ru> 1.6.7.1-alt1
- 1.6.7.1

* Mon Nov 10 2008 Led <led@altlinux.ru> 1.6.6-alt2
- removed %_bindir/config.sh

* Tue Nov 04 2008 Led <led@altlinux.ru> 1.6.6-alt1
- 1.6.6

* Tue Oct 14 2008 Led <led@altlinux.ru> 1.6.5.1-alt2
- remove default '-g' compile key

* Tue Oct 14 2008 Led <led@altlinux.ru> 1.6.5.1-alt1
- initial build
