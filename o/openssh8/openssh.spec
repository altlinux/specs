%define pkgname openssh
%define _pamdir /etc/pam.d

%{expand:%%define _sysconfdir %_sysconfdir/ssh}
%{expand:%%define _libexecdir %_libexecdir/ssh}

Summary: The OpenSSH implementation of SSH protocol
Name: %{pkgname}8
Version: 8.0p1
Release: alt1
License: BSD
Group: System/Base
URL: https://www.openssh.com/portable.html
Source0: %name-%version.tar.xz
Obsoletes: ssh, ssh-clients
Provides: %pkgname = %version
Provides: %pkgname-clients = %version
Provides: %pkgname-common = %version

BuildRequires: libssl-devel
BuildRequires: pam-devel pam_userpass-devel rpm-macros-pam0
BuildRequires: perl
BuildRequires: zlib-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
SSH (Secure Shell) is a program for logging into a remote machine and
for executing commands on a remote machine. It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing
it up to date in terms of security and features, as well as removing
all patented algorithms to separate libraries (OpenSSL).

This package includes the core OpenSSH files and the client programs
necessary to make encrypted connections to SSH servers.

%package server
Summary: The OpenSSH server daemon.
Group: System/Base
Requires: pam_userpass, pam_mktemp
Obsoletes: ssh-server
Provides: %pkgname-server-control

%description server
SSH (Secure Shell) is a program for logging into a remote machine and
for executing commands on a remote machine. It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing
it up to date in terms of security and features, as well as removing
all patented algorithms to separate libraries (OpenSSL).

This package contains the Secure Shell daemon (sshd), which allows SSH
clients to connect to your host.

%package doc
Summary: Optional documentation for %pkgname
Group: System/Base
BuildArch: noarch

%description doc
%summary


%prep
%setup -q

%build
export LDFLAGS="-s"
# export LIBS="-lcrypt -lpam -lpam_misc -lpam_userpass"

# Explicitly disable weak ciphers
# ECDSA also should not be trusted, but people may need it in a client
export CFLAGS="	-fPIC \
		-DOPENSSL_NO_DES \
		-DOPENSSL_NO_RIPEMD -DOPENSSL_NO_RC4 -DOPENSSL_NO_CAST \
		"
#export CFLAGS="	-fPIC \
#		-DOPENSSL_NO_ECC \
#		-DOPENSSL_NO_DES \
#		-DOPENSSL_NO_RIPEMD -DOPENSSL_NO_RC4 -DOPENSSL_NO_CAST \
#		-DKEX_ECDH_METHODS -DHOSTKEY_ECDSA_CERT_METHODS -DHOSTKEY_ECDSA_METHODS \
#		-UOPENSSL_HAS_ECC \
#		"

%autoreconf
%configure \
	--with-default-path=/bin:/sbin:/usr/bin:/usr/sbin \
	--with-ipaddr-display \
	--with-mantype=doc \
	--without-md5-passwords \
	--without-rpath \
	--without-shadow \
	--without-tcp-wrappers \
	--with-privsep-path=/var/empty \
	--with-privsep-user=sshd \
	--with-ssl-engine \
	;
%__make

%install
rm -rf %buildroot
mkdir -pm755 %buildroot/etc/ssh
# create ghosts
touch %buildroot/etc/ssh/ssh_host_{rsa,ed25519}_key{,.pub}
%__make DESTDIR=%buildroot install
install -d %buildroot/etc/pam.d
install -d %buildroot/etc/rc.d/init.d
install -m 700 %pkgname-sshd.rc %buildroot/etc/rc.d/init.d/sshd
install -m 644 %pkgname-sshd.pam %buildroot%_pamdir/sshd
install -m 644 %pkgname-ssh_config %buildroot/etc/ssh/ssh_config
install -m 600 %pkgname-sshd_config %buildroot/etc/ssh/sshd_config

mkdir -pm755 %buildroot/etc/control.d/facilities
install -m 600 %pkgname-sftp.control \
	%buildroot/etc/control.d/facilities/sftp

rm -f	%buildroot%_bindir/slogin \
	%buildroot%_man1dir/slogin.1*

%clean
rm -rf %{buildroot} %{_builddir}/%{name}-%{version}


%post
id sshd > /dev/null || useradd -d / -s /bin/false -r sshd
test -c /dev/random && ssh-keygen -A
# unconditionally turn on daemon startup:
# when it is running, you may stop it remotely
# when it is not running, you can't do anything
chkconfig --add sshd
chkconfig --level 2345 sshd on


%files
%defattr(-,root,root)
%attr(0755,root,wheel) %dir /etc/ssh
%attr(0755,root,wheel) %dir %_libexecdir
%attr(0755,root,wheel) %_bindir/ssh
%attr(0755,root,wheel) %_bindir/ssh-add
%attr(0755,root,wheel) %_bindir/ssh-agent
%attr(0755,root,wheel) %_bindir/ssh-keyscan
%attr(0755,root,wheel) %_bindir/scp
%attr(0755,root,wheel) %_bindir/sftp
%attr(0755,root,wheel) %_bindir/ssh-keygen
%attr(0700,root,wheel) %_libexecdir/ssh-keysign
%attr(0644,root,wheel) %_mandir/man1/ssh.1*
%attr(0644,root,wheel) %_mandir/man1/ssh-add.1*
%attr(0644,root,wheel) %_mandir/man1/ssh-agent.1*
%attr(0644,root,wheel) %_mandir/man1/ssh-keygen.1*
%attr(0644,root,wheel) %_mandir/man1/ssh-keyscan.1*
%attr(0644,root,wheel) %_mandir/man1/sftp.1*
%attr(0644,root,wheel) %_mandir/man1/scp.1*
%attr(0644,root,wheel) %_mandir/man5/ssh_config.5*
%attr(0644,root,wheel) %_mandir/man8/ssh-keysign.8*
%attr(0644,root,wheel) %config(noreplace) %verify(not size md5 mtime) /etc/ssh/ssh_config

%files doc
%doc CREDITS LICENCE README

%files server
%defattr(-,root,wheel)
%attr(0700,root,wheel) %_sbindir/sshd
%attr(0755,root,wheel) %_libexecdir/sftp-server
%attr(0700,root,wheel) %_libexecdir/ssh-pkcs11-helper
%attr(0644,root,wheel) %_mandir/man5/moduli.5*
%attr(0644,root,wheel) %_mandir/man5/sshd_config.5*
%attr(0644,root,wheel) %_mandir/man8/sshd.8*
%attr(0644,root,wheel) %_mandir/man8/sftp-server.8*
%attr(0644,root,wheel) %_mandir/man8/ssh-pkcs11-helper.8*
%attr(0640,root,wheel) %config(noreplace) %verify(not size md5 mtime) /etc/ssh/sshd_config
%attr(0600,root,wheel) %config(noreplace) %ghost /etc/ssh/ssh_host*key
%attr(0644,root,wheel) %config(noreplace) %ghost /etc/ssh/ssh_host*key.pub
%attr(0600,root,wheel) %config(noreplace) /etc/ssh/moduli
%attr(0644,root,wheel) %config(noreplace) /etc/pam.d/sshd
%attr(0700,root,wheel) %config /etc/rc.d/init.d/sshd
%attr(0700,root,wheel) /etc/control.d/facilities/sftp


%changelog
* Thu Jun 20 2019 Gremlin from Kremlin <gremlin@altlinux.org> 8.0p1-alt1
- import 8.0p1 from upstream
- disable weak algorithms: CAST, Lucifer (DES), RC4, RIPEMD
- add CFB mode for 256 bit Blowfish and {256,192,128} bit Rijndael

