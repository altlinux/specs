# spec file for package smtptrapd
#

Name: smtptrapd
Version: 1.4
Release: alt1

Summary: a SMTP daemon that always returns a 4xx soft error

#%%gpl2plus
License: GPLv2+
Group: System/Servers
Url: http://smtptrapd.inodes.org/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar.bz2
Source1: %name.init
Source2: %name.sysconfig
Patch0:  %name-1.4-alt-pidfile.patch

%description
The smtptrapd program is a multi-threaded daemon that provides 
a RFC 2821 compliant SMTP service that always returns a 4xx 
soft error to the RCPT TO verb. 

%prep
%setup -n %name-%version
%patch0

%build
%make_build

%install
mkdir -p -- %buildroot/%_sbindir
install -m 0755 -- %name %buildroot/%_sbindir/%name

mkdir -p -- %buildroot/%_initdir
install -m 0755 -- %SOURCE1 %buildroot%_initdir/%name

mkdir -p -- %buildroot/%_sysconfdir/sysconfig
install -m 0640 -- %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/%name

%config(noreplace) 	    %_sysconfdir/sysconfig/%name
%config			    %_initdir/%name

%changelog
* Wed Jan 09 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.4-alt1
- Initial build for ALT Linux Sisyphus

* Sat Jan 05 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.4-alt0
- Initial build
