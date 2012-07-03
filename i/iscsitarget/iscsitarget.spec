Summary: iSCSI kernel module and utilities
Name: iscsitarget
%define module_name %name
Version: 1.4.20.2
Release: alt1
License: %gpl2only
Group: System/Configuration/Networking
Source: %name-%version.tar
Patch: %name-%version-alt.patch
URL: http://%name.sourceforge.net/
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires: kernel-build-tools rpm-build-licenses

# Automatically added by buildreq on Fri Jun 08 2007
BuildRequires: libssl-devel

%description
The %name package provides server kernel modules for the iSCSI
protocol, as well as utilities to configure the kernel modules. iSCSI
is a protocol that conveys SCSI protocol related command and data over
networks, especially over IP.


%package utils
Group: System/Configuration/Networking
Summary: iSCSI utilities

%description utils
iSCSI is a protocol that conveys SCSI protocol related command and data
over networks, especially over IP.
This package provides utils to create an iSCSI storage.


%package -n kernel-source-%module_name
Summary: Linux %module_name modules sources
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%module_name
This package contains sources for %module_name kernel module.


%prep
%setup
%patch -p1


%build
export CFLAGS="%optflags"
%make_build -C usr
bzip2 --best --keep --force ChangeLog


%install
%make_install DESTDIR=%buildroot install-usr install-man install-initd install-etc

rm -rf kernel-source-%module_name-%version
install -d -m 0755 kernel-source-%module_name-%version/{include,kernel}
install -m 0644 Makefile kernel-source-%module_name-%version/Makefile
install -m 0644 include/* kernel-source-%module_name-%version/include/
install -m 0644 kernel/* kernel-source-%module_name-%version/kernel/
install -d -m 0755 %buildroot%_usrsrc/kernel/sources
tar -c kernel-source-%module_name-%version | bzip2 -9c > \
    %buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%version.tar.bz2


%post utils
%post_service iscsi-target

%preun utils
%preun_service iscsi-target

%files utils
%doc ChangeLog.* README* etc/initiators.* etc/ietd.conf
%_initdir/*
%config %_sysconfdir/iet/ietd.conf
%config %_sysconfdir/iet/initiators.*
%config %_sysconfdir/iet/targets.*
%_sbindir/*
%_man5dir/*
%_man8dir/*


%files -n kernel-source-%module_name
%_usrsrc/kernel/sources/*.tar.bz2


%changelog
* Thu Apr 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.20.2-alt1
- 1.4.20.2

* Thu Apr 09 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.17-alt2
- Add configs

* Fri Apr 03 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.4.17-alt1
- 0.4.17
- Add Makefile to source

* Sun Oct 26 2008 Led <led@altlinux.ru> 0.4.16-alt2
- fixed build with glibc = 2.8 (used patches from Mandriva)

* Sun Sep 28 2008 Led <led@altlinux.ru> 0.4.16-alt1
- 0.4.16
- fixed License
- updated %name-0.4.16-alt.patch

* Mon Jun 11 2007 Led <led@altlinux.ru> 0.4.15-alt0.1
- 0.4.15
- remade spec
- removed ietd-0.4.14-makefile.patch
- added %name-0.4.15-alt.patch

* Wed Dec 20 2006 Yury A. Romanov (damned) <damned@altlinux.ru> 0.4.14-alt3
- Some minor fixes

* Wed Nov 08 2006 Yury A. Romanov (damned) <damned@altlinux.ru> 0.4.14-alt2
- Correct build for Sisyphus.
- Rename of kernel module package

* Mon Oct 30 2006 Yury A. Romanov (damned) <damned@altlinux.ru> 0.4.14-alt1
- New version

* Thu Oct 05 2006 Yury A. Romanov (damned) <damned@altlinux.ru> 0.4.13-alt1
- Initial Build
