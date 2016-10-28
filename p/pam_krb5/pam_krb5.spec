Summary: A Pluggable Authentication Module for Kerberos 5.
Name: pam_krb5
Version: 4.7
Release: alt1
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
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
%setup -q -n %name-%version
%patch -p1

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
* Fri Oct 28 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.7-alt1
- Upgrade to new 4.x release

* Fri Sep 30 2016 Evgeny Sinelnikov <sin@altlinux.ru> 3.15-alt1
- Update to latest 3.x release

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.13-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 3.13-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Apr 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.13-alt1
- Migrate to 3.13 original modification from
  git://git.eyrie.org/kerberos/pam-krb5.git

* Mon Oct 30 2006 Michail Yakushin <silicium@altlinux.ru> 2.2.9-alt1
- package from fc5
