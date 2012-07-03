Name: pam_pwdfile
Version: 0.99
Release: alt0.1

Summary: A PAM module that allows users to authenticate on htpasswd-type files separate from /etc/passwd.

Url: http://cpbotha.net/pam_pwdfile.html
License: GPL / BSD
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://cpbotha.net/files/pam_pwdfile/%name-%version.tar.bz2

Requires: pam

# Automatically added by buildreq on Fri Oct 13 2006
BuildRequires: libpam-devel linux-libc-headers

%description
This pam module can be used for the authentication service only, in cases
where one wants to use a different set of passwords than those in the main
system password database.  E.g. in our case we have an imap server running,
and prefer to keep the imap passwords different from the system passwords
for security reasons.

%prep
%setup -q
cp -f contrib/Makefile.standalone Makefile

%build
# fixes against undefined symbol: __stack_chk_fail_local
make "CFLAGS=-fPIC -O2 -c -g -Wall -Wformat-security -fno-stack-protector"

%install
make PAM_LIB_DIR="%buildroot/lib/security" install

%files
/%_lib/security/*
%doc README changelog

%changelog
* Fri Oct 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt0.1
- initial build for ALT Linux Sisyphus
