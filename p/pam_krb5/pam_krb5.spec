Summary: A Pluggable Authentication Module for Kerberos 5.
Name: pam_krb5
Version: 3.13
Release: alt1.1
Source0: pam_krb5-%version.tar.bz2
License: BSD or LGPLv2+
Group: System/Base
BuildPrereq: byacc, flex, libkrb5-devel, libpam-devel
URL: http://www.eyrie.org/~eagle/software/pam-krb5/
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
BuildRequires: perl-podlators
%description 
This is pam_krb5, a pluggable authentication module that can be used with
Linux-PAM and Kerberos 5. This module supports password checking, ticket
creation, and optional TGT verification and conversion to Kerberos IV tickets.
The included pam_krb5afs module also gets AFS tokens if so configured.

%prep
%setup -q -n pam_krb5-%version

%build
./autogen
%add_optflags -fPIC
%configure --libdir=/%_lib LDFLAGS='-lpam' \
	--with-default-use-shmem=sshd --with-default-external=sshd
make

%install
make install DESTDIR=%buildroot

%find_lang %name

%files -f %name.lang
/%_lib/security/pam_krb5.so
%_mandir/man5/*
%doc README* LICENSE NEWS

%changelog
* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 3.13-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Apr 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.13-alt1
- Migrate to 3.13 original modification from
  git://git.eyrie.org/kerberos/pam-krb5.git

* Mon Oct 30 2006 Michail Yakushin <silicium@altlinux.ru> 2.2.9-alt1
- package from fc5
