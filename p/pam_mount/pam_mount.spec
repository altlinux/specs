Name: pam_mount
Version: 2.16
Release: alt1.1

Summary: Pluggable Authentication Module that can mount volumes for a user session 
License: GPLv2+ and LGPLv2+
Group: System/Libraries

BuildRequires: glib2-devel pam-devel openssl-devel libHX-devel libxml2-devel libavahi-devel
BuildRequires: libcryptsetup-devel libmount-devel libpcre-devel

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

%description
This module is aimed at environments with central file servers that
a user wishes to mount on login and unmount on logout, such as
(semi-)diskless stations where many users can logon and where statically
mounting the entire /home from a server is a security risk, or listing
all possible volumes in /etc/fstab is not feasible.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-slibdir=/%_lib \
	--with-ssbindir=/sbin
%make_build

%install
%make DESTDIR=%buildroot install
mv %buildroot%_libdir/lib*.so.* %buildroot/%_lib/

%files
%doc doc/*.txt
%config(noreplace) %_sysconfdir/security/%name.conf.xml
/%_lib/security/*
%_sbindir/*
/sbin/*
/%_lib/*.so.*
%_mandir/man?/*

%changelog
* Tue Jan 30 2018 Alexey Shabalin <shaba@altlinux.ru> 2.16-alt1.1
- rebuild with libcryptsetup.so.12

* Wed Oct 18 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.16-alt1
- 2.16

* Thu Apr 04 2013 Andrey Cherepanov <cas@altlinux.org> 2.11-alt5
- Use full path to /usr/sbin/pmvarrun to prevent warning in su/sudo

* Mon Nov 07 2011 Alexey Shabalin <shaba@altlinux.ru> 2.11-alt4
- rebuild with cryptsetup-1.4.0

* Wed Oct 05 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.11-alt3.1
- 2.11

* Wed Dec 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.22-alt3.1
- rebuild with openssl 1.0

* Mon Aug 10 2009 Mikhail Efremov <sem@altlinux.org> 1.22-alt3
- Try to resolve names and use FQDN.
- use 'options' for DNS-SD volumes.

* Tue Apr 21 2009 Andriy Stepanov <stanv@altlinux.ru> 1.22-alt2
- Add avahi support.

* Mon Apr 20 2009 Andriy Stepanov <stanv@altlinux.ru> 1.22-alt1
- New version

* Sat Jan 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.15-alt1
- First build for Sisyphus 


