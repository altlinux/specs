Name: pam_mount 
Version: 2.11
Release: alt4

Summary: Pluggable Authentication Module that can mount volumes for a user session 
License: GPLv2+ and LGPLv2+
Group: System/Libraries

BuildRequires:  glib2-devel, pam-devel, openssl-devel, libHX-devel libxml2-devel libavahi-devel libcryptsetup-devel

Source0: %name-%version.tar

%description
This module is aimed at environments with central file servers that
a user wishes to mount on login and unmount on logout, such as
(semi-)diskless stations where many users can logon and where statically
mounting the entire /home from a server is a security risk, or listing
all possible volumes in /etc/fstab is not feasible.

%prep
%setup 

%build
%autoreconf
%configure --with-slibdir=%buildroot/%_lib --with-ssbindir=%buildroot/sbin
%make_build

%install
%makeinstall

%files
%doc doc/*.txt
%config(noreplace) %_sysconfdir/security/%name.conf.xml
/%{_lib}/security/*
/usr/sbin/*
#/usr/bin/*
/sbin/*
%{_mandir}/man?/*

%changelog
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


