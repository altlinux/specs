Name: alterator-fbi-se-config
Version: 0.1
Release: alt1

Summary: Separate config and service override for alterator-fbi
License: GPL-3.0-or-later
Group: System/Configuration/Other

URL: https://www.altlinux.org/Alterator

BuildArch: noarch

AutoReqProv: no

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/ahttpd
cat > %buildroot%_sysconfdir/ahttpd/ahttpd-se.conf << EOF
#main server settings
#format:parameter	value

server-listen	*
server-port	8080
server-user	_ahttpd
server-group	_ahttpd
server-pidfile	/var/run/ahttpd.pid

log-file	/var/log/ahttpd/access.log
log-mode	errors

tls-key-file	/var/lib/ssl/private/ahttpd.key
tls-cert-file	/var/lib/ssl/certs/ahttpd.cert

framework-uri	/acc
login-uri	/login
logout-uri	/logout

loginchain	root:officer
prelogin-only	officer
EOF

mkdir -p %buildroot%_unitdir/ahttpd.service.d
cat > %buildroot%_unitdir/ahttpd.service.d/selinux.conf << EOF
[Service]
ExecStart=
ExecStart=/usr/sbin/ahttpd -c %_sysconfdir/ahttpd/ahttpd-se.conf
EOF

%files
%config(noreplace) %_sysconfdir/ahttpd/ahttpd-se.conf
%_unitdir/ahttpd.service.d/selinux.conf

%changelog
* Tue Sep 08 2026 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
