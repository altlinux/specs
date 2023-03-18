# SPDX-License-Identifier: GPL-2.0-only
# Based on openssh.spec from openssh and openssh-gostcrypto by glebfm.
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: openquantumsafe-openssh
Version: 8.9p1.202208
Release: alt2

Summary: OQS-OpenSSH is a fork of OpenSSH that adds quantum-safe algorithms
License: SSH-OpenSSH and ALT-Public-Domain and BSD-3-Clause and Beerware
Group: Networking/Remote access
Url: https://openquantumsafe.org/applications/ssh.html
Vcs: https://github.com/open-quantum-safe/openssh
Source: %name-%version.tar

%define confdir %_sysconfdir/openssh
%define _chrootdir /var/empty
%define docdir %_docdir/%name-%version
%def_with pam_userpass
%def_with libedit
%def_with libaudit
%def_with kerberos5
%def_with selinux
%def_with openssl
%def_without security_key_builtin
%def_with zlib

%{expand: %%global _libexecdir %_libexecdir/openssh}
%define _pamdir /etc/pam.d

Conflicts: openssh
Requires: %name-clients = %EVR
Requires: %name-server  = %EVR

BuildRequires: liboqs-devel >= 0.7.2
BuildRequires: libssl-devel
BuildRequires: pam_userpass-devel
%{?_with_zlib:BuildRequires: zlib-devel}
%{?_with_libedit:BuildRequires: libedit-devel}
%{?_with_libaudit:BuildRequires: libaudit-devel}
%{?_with_kerberos5:BuildRequires: libkrb5-devel}
%{?_with_selinux:BuildRequires: libselinux-devel}
# To generate algorithms
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-yaml

%package common
Summary: OQS-OpenSSH common files
Group: Networking/Remote access
Provides: openssh-common = %EVR
Conflicts: openssh-common
Conflicts: %name < %EVR

%package clients
Summary: OQS-OpenSSH Secure Shell protocol clients
Group: Networking/Remote access
Provides: openssh-clients = %EVR
Conflicts: openssh-clients
Requires: %name-common = %EVR

%package keysign
Summary: OQS-OpenSSH helper program for hostbased authentication
Group: Networking/Remote access
Provides: openssh-keysign = %EVR
Conflicts: openssh-keysign
Requires: %name-clients = %EVR

%package server
Summary: OQS-OpenSSH Secure Shell protocol daemon
Group: System/Servers
Provides: openssh-server = %EVR
Conflicts: openssh-server
Requires(pre,post): %name-server-control = %EVR
Requires: %_chrootdir, syslogd-daemon
# Because of /etc/syslog.d/ feature.
Conflicts: syslogd < 1.4.1-alt11

%package server-control
Summary: Control rules for the OQS-OpenSSH server configuration
License: GPLv2+
Group: System/Servers
BuildArch: noarch
Provides: openssh-server-control = %EVR
Conflicts: openssh-server-control
Requires: %name-common = %EVR

%package askpass-common
Summary: OQS-OpenSSH common passphrase dialog infrastructure
Group: Networking/Remote access
BuildArch: noarch
Provides: openssh-askpass-common = %EVR
Conflicts: openssh-askpass-common
Requires: %name-common = %EVR
Provides: %_libexecdir

%global preamble OQS-OpenSSH is a fork of OpenSSH that adds quantum-safe cryptography to\
enable its use and evaluation in the SSH protocol.\
\
Both liboqs and this fork are part of the Open Quantum Safe (OQS) project,\
which aims to develop and prototype quantum-safe cryptography.\
\
IT IS AT AN EXPERIMENTAL STAGE, and has not received the same level of\
auditing and analysis that OpenSSH has received. See README for details.\
\
WE DO NOT RECOMMEND RELYING ON THIS FORK TO PROTECT SENSITIVE DATA.

%description
%preamble

%description common
%preamble

This package includes common files necessary for both the OpenSSH
client and server.

%description clients
%preamble

This package includes the clients necessary to make encrypted connections
to SSH servers.

%description keysign
ssh-keysign is used by ssh(1) to access the local host keys and generate
the digital signature required during hostbased authentication with SSH
protocol version 2.  ssh-keysign is not intended to be invoked by the
user, but from ssh(1).  See ssh(1) and sshd(8) for more information about
hostbased authentication.

%description server
%preamble

This package contains the secure shell daemon.  The sshd is the server
part of the secure shell protocol and allows ssh clients to connect to
your host.

%description server-control
This package contains control rules for OpenSSH server configuration.
See control(8) for details.

%description askpass-common
%preamble

This package contains OpenSSH passphrase dialog infrastructure.
These dialogs are intended to be called from the ssh-add program and
not invoked directly.

%prep
%setup
# https://github.com/open-quantum-safe/openssh/wiki/Using-liboqs-supported-algorithms-in-the-fork
python3 oqs-template/generate.py

%build
%autoreconf

export ac_cv_path_LOGIN_PROGRAM_FALLBACK=/bin/login
export ac_cv_path_NROFF=/usr/bin/nroff
export ac_cv_path_PATH_PASSWD_PROG=/usr/bin/passwd
export ac_cv_path_PROG_LASTLOG=/usr/bin/lastlog
export ac_cv_path_xauth_path=/usr/bin/xauth

%configure \
	--sysconfdir=%confdir \
	--without-rpath \
	--disable-strip \
	--with-mantype=doc \
	--with-pam \
	--with-ipaddr-display \
	--with-privsep-user=sshd \
	--with-privsep-path=%_chrootdir \
	--with-default-path=/bin:/usr/bin:/usr/local/bin \
	--with-superuser-path=/sbin:/usr/sbin:/usr/local/sbin:/bin:/usr/bin:/usr/local/bin \
	%{subst_with kerberos5} \
	%{subst_with libedit} \
	%{subst_with openssl} \
	%{subst_with selinux} \
	%{?_with_libaudit:--with-audit=linux} \
	%{?_with_security_key_builtin:--with-security-key-builtin} \
	--with-liboqs-dir=%_prefix \
	%nil
%make_build

%install
%makeinstall_std

mkdir -p %buildroot{%_libexecdir,%_sysconfdir{,/X11}/profile.d,%systemd_unitdir}
mkdir -p %buildroot%confdir/authorized_keys{,2}
install -pD -m600 alt/sshd.pamd \
	%buildroot%_pamdir/sshd
install -pD -m755 alt/sshd.init \
	%buildroot%_initdir/sshd
install -pD -m600 alt/sshd.sysconfig \
	%buildroot%_sysconfdir/sysconfig/sshd
install -p -m755 alt/rescp \
	%buildroot%_bindir/
install -p -m755 alt/ssh-agent.sh \
	%buildroot%_sysconfdir/X11/profile.d/
install -pD -m755 alt/sftp.control \
        %buildroot%_sysconfdir/control.d/facilities/sftp
install -pD -m755 alt/sshd-allow-groups.control \
        %buildroot%_sysconfdir/control.d/facilities/sshd-allow-groups
install -pD -m755 alt/sshd-password-auth.control \
        %buildroot%_sysconfdir/control.d/facilities/sshd-password-auth

install -pD -m644 alt/sshd.service \
	%buildroot%systemd_unitdir/sshd.service

sed -i 's,@LIBEXECDIR@,%_libexecdir,g' \
        %buildroot%_sysconfdir/control.d/facilities/sftp

install -p -m755 contrib/ssh-copy-id %buildroot%_bindir/
install -p -m644 contrib/ssh-copy-id.1 %buildroot%_man1dir/

chmod 711 %buildroot%_sbindir/*

install -p -m755 alt/ssh-askpass.{sh,csh} \
	%buildroot%_sysconfdir/profile.d/

mkdir -p %buildroot%docdir
install -pm644 CREDITS LICENCE README* PROTOCOL* alt/[CR]* alt/faq.html \
	%buildroot%docdir/

%check
./ssh -V
# Query all available algorithms
for q in `./ssh -Q help`; do
	./ssh -Q $q | sed "s/^/ $q : /" >&2
done | sort -V

%pre clients
/usr/sbin/groupadd -r -f sshagent

%pre server
/usr/sbin/groupadd -r -f sshd
/usr/sbin/useradd -r -g sshd -d %_chrootdir -s /dev/null -n sshd >/dev/null 2>&1 ||:
%pre_control sftp sshd-allow-groups sshd-password-auth

%post server
%post_control -s enabled sftp
%post_control -s disabled sshd-allow-groups
%post_control -s default sshd-password-auth
if [ $1 -ge 2 ]; then
	/sbin/service sshd condreload ||:
else
	/sbin/chkconfig --add sshd ||:
fi

%preun server
if [ $1 = 0 ]; then
	/sbin/chkconfig --del sshd ||:
fi

%files

%files common
%_bindir/scp
%_bindir/ssh-keygen
%_man1dir/scp.*
%_man1dir/ssh-keygen.*
%docdir/

%files clients
%attr(751,root,root) %dir %confdir
%config(noreplace) %confdir/ssh_config
%config(noreplace) %_sysconfdir/X11/profile.d/*
%_bindir/rescp
%_bindir/sftp
%_bindir/ssh
%_bindir/ssh-add
%attr(2711,root,sshagent) %_bindir/ssh-agent
%_bindir/ssh-copy-id
%_bindir/ssh-keyscan
%attr(751,root,root) %dir %_libexecdir
%_libexecdir/ssh-pkcs11-helper
%_libexecdir/ssh-sk-helper
%_man1dir/sftp.*
%_man1dir/ssh.*
%_man1dir/ssh-add.*
%_man1dir/ssh-agent.*
%_man1dir/ssh-copy-id.*
%_man1dir/ssh-keyscan.*
%_man5dir/ssh_config.*
%_man8dir/ssh-pkcs11-helper.*
%_man8dir/ssh-sk-helper.*

%files keysign
%attr(751,root,root) %dir %_libexecdir
%_libexecdir/ssh-keysign
%_man8dir/ssh-keysign.*

%files server
%attr(751,root,root) %dir %confdir
%attr(600,root,root) %config %confdir/moduli
%attr(600,root,root) %config(noreplace) %verify(not size md5 mtime) %confdir/sshd_config
%attr(600,root,root) %config(noreplace) %_pamdir/sshd
%attr(600,root,root) %config(noreplace) %_sysconfdir/sysconfig/sshd
%attr(755,root,root) %config %_initdir/sshd
%attr(751,root,root) %dir %confdir/authorized_keys*
%systemd_unitdir/*
%_sbindir/*
%attr(751,root,root) %dir %_libexecdir
%_libexecdir/sftp-server
%_man5dir/moduli.*
%_man5dir/sshd_config.*
%_man8dir/sshd.*
%_man8dir/sftp-server.*

%files server-control
%attr(755,root,root) %_controldir/*

%files askpass-common
%_sysconfdir/profile.d/ssh-askpass.*
%attr(751,root,root) %dir %_libexecdir

%changelog
* Sat Mar 18 2023 Vitaly Chikunov <vt@altlinux.org> 8.9p1.202208-alt2
- Apply security fixes and sandbox filter from upstream.

* Thu Aug 11 2022 Vitaly Chikunov <vt@altlinux.org> 8.9p1.202208-alt1
- OpenSSH source code synced with 8.9p1.
- Remove Rainbow-I, SIKE (broken algorithms).
- Re-enable Falcon (SIG).

* Mon Jul 04 2022 Vitaly Chikunov <vt@altlinux.org> 8.6p1.202201-alt2
- Disable Falcon (SIG) due to problems with liboqs on armh.

* Sun Jan 09 2022 Vitaly Chikunov <vt@altlinux.org> 8.6p1.202201-alt1
- Updated to OQS-OpenSSH-snapshot-2022-01 (2022-01-06).

* Tue Sep 28 2021 Vitaly Chikunov <vt@altlinux.org> 8.6p1.202108-alt3
- Backported upstream fix for CVE-2021-41617 (AuthorizedKeysCommand).

* Sun Aug 29 2021 Vitaly Chikunov <vt@altlinux.org> 8.6p1.202108-alt2
- Dilithium algorithms re-enabled.

* Sun Aug 22 2021 Vitaly Chikunov <vt@altlinux.org> 8.6p1.202108-alt1
- Update to OQS-OpenSSH-snapshot-2021-08 (2021-08-11).
- Dilithium algorithms temporary disabled.

* Wed Jun 23 2021 Vitaly Chikunov <vt@altlinux.org> 7.9p1.202008-alt2
- Build on all arches (add x86 and ppc64le).
- Make server-control and askpass-common noarch.

* Sun Feb 28 2021 Vitaly Chikunov <vt@altlinux.org> 7.9p1.202008-alt1
- First import of OQS-OpenSSH-snapshot-2020-08.
