Name: pam_ssh
Version: 1.97
Release: alt1.1

Summary: This PAM module provides single sign-on behavior for SSH

Url: http://pam-ssh.sourceforge.net/
License: BSD
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/pam-ssh/%name-%version.tar.bz2

Requires: pam

%set_verify_elf_method unresolved=strict

# Automatically added by buildreq on Sun Oct 18 2009
BuildRequires: libpam-devel libssl-devel openssh-clients

%description
This module provides single sign-on behavior. The user types a passphrase
when logging in and is allowed in if it decrypts the user's SSH private
key. An ssh-agent is started and keys are added. For the entire session,
the user types no more passwords.

%prep
%setup

%build
rm -f libtool
%autoreconf
%configure --with-pam-dir=%_pam_modules_dir
%make_build

%install
%makeinstall_std
rm -f %buildroot/%_lib/security/%name.la

%files
%doc AUTHORS NEWS README ChangeLog TODO
/%_lib/security/%name.so
%_man8dir/*

%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.97-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sun Oct 11 2009 Vitaly Lipatov <lav@altlinux.ru> 1.97-alt1
- initial build for ALT Linux Sisyphus
