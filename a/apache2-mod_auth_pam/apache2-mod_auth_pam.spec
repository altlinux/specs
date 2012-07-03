%define apache 2.0
%define oname mod_auth_pam
Summary: PAM authentication module for Apache
Name: apache2-mod_auth_pam
Version: 1.1.1
Release: alt3
License: GPL
Group: System/Servers
Packager: Boris Savelev <boris@altlinux.org>
Url: http://pam.sourceforge.net/mod_auth_pam/
Source: %oname-%apache-%version.tar.gz
Source1: auth_pam.load
Source2: auth_pam.usage
Source3: httpd2
Source4: auth_sys_group.load

Patch0: libapache2-mod-auth-pam.002.pam_rhosts_user_variables.diff

# Automatically added by buildreq on Mon Sep 29 2008
BuildRequires: apache2-devel libpam-devel

%description
The PAM authentication module implements Basic authentication on top of the
Pluggable Authentication Module library. Thereby it supports standard unix
passwd, shadow, NIS, SMB auth and radius authentication transparently and
easily interchangeable, wherever the HTTP protocol allows it.
Build for apache2.

%prep
%setup -q -n %oname
%patch0 -p1
subst 's|APXS=apxs|#APXS=apxs|g' Makefile
subst 's|pam_servicename = "httpd"|pam_servicename = "httpd2"|g' %oname.c

%build
# apache-2
export APXS=%_sbindir/apxs2
%make_build

%install
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
mkdir -p %buildroot%_sysconfdir/pam.d
install -m 644 .libs/*.so %buildroot%apache2_moduledir
install -m 644 %SOURCE1 %buildroot%apache2_mods_available
install -m 644 %SOURCE4 %buildroot%apache2_mods_available
install -m 644 %SOURCE2 %_builddir/%oname
install -m 644 %SOURCE3 %buildroot%_sysconfdir/pam.d

%files
%doc README INSTALL auth_pam.usage
%apache2_mods_available/*.load
%apache2_moduledir/*.so
%_sysconfdir/pam.d/httpd2

%changelog
* Mon Aug 24 2009 Boris Savelev <boris@altlinux.org> 1.1.1-alt3
- add patch from debian
- split loader for modules to auth_pam and auth_sys_group
- update usage in docs

* Wed Jul 01 2009 Boris Savelev <boris@altlinux.org> 1.1.1-alt2
- fix load config (closes:#20635)

* Mon Sep 29 2008 Boris Savelev <boris@altlinux.org> 1.1.1-alt1
- initial build for Sisyphus
