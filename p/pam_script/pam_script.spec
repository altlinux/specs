%define oname pam-script
Name: pam_script
Version: 1.1.8
Release: alt1

Summary: This PAM module can invoke scripts within the PAM stack

#Url: http://pam-script.sourceforge.net/
Url: https://github.com/jeroennijhof/pam_script
License: GPL
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: http://prdownloads.sf.net/%oname/%oname/%oname-%version/%oname-%version.tar
# Source-url: https://github.com/jeroennijhof/pam_script/archive/%version.tar.gz
Source: %oname-%version.tar

Requires: pam

# Automatically added by buildreq on Thu Sep 30 2010
BuildRequires: glibc-devel-static libpam-devel

%description
PAM script module will allow you to execute scripts during authorization,
password changes and sessions. This is very handy if your current
security application has no pam support but is accessable with perl or
other scripts.

%prep
%setup -n %oname-%version

%build
# it is strange we need it
mkdir config
%autoreconf
%configure	--prefix=%prefix \
		--libdir=%_pam_modules_dir \
		--sysconfdir=%_sysconfdir/pam-script \
		--mandir=%_mandir

%install
%makeinstall_std
make DESTDIR=%buildroot install-man7
make DESTDIR=%buildroot install-examples
rm -f %buildroot/%_sysconfdir/pam-script/tally
rm -f %buildroot/%_sysconfdir/pam-script/logscript

%files
%doc AUTHORS NEWS README etc/logscript etc/tally
%_sysconfdir/pam-script/
%_pam_modules_dir/%name.so
%_man7dir/*

%changelog
* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt1
- new version 1.1.8 (with rpmrb script)

* Fri Aug 21 2015 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt1
- new version 1.1.7 (with rpmrb script)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Sep 30 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- initial build for ALT Linux Sisyphus
