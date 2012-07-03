# Spec file for ftpproxy

Name: ftpproxy
Version: 1.2.3
Release: alt4

Summary: FTP proxy with optional access and command control

License: %gpl2plus
Group: System/Servers
URL: http://www.ftpproxy.org

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source:  %name-%version.tar
Source1: %name.conf
Source2: %name.xinetd
Source3: %name.logrotate
Patch0:  %name-1.2.3-alt-fix_config_path.patch
Patch1:  %name-1.2.3-alt-Werror.patch
Patch2:  %name-1.2.3-alt-fix_repocop_tmp_warn.patch
Patch3:  %name-1.2.3-alt-config_line_length.patch

BuildRequires(pre): rpm-build-licenses
Requires(pre): shadow-utils
Requires:  xinetd

%description
ftp.proxy  is an application level gateway for FTP. It sits between a
client and a server forwarding command and  data streams supporting a
subset of the file transfer protocol as described in RFC 959.
Beside this basic function which makes the program useful on firewall
or masqueraders it offers fixing the FTP server (e.g. for connections
into a protected LAN) and proxy authentication.

%define confdir		%_sysconfdir/%name
%define scriptdir	%_datadir/%name
%define logdir		 %_logdir/%name

%define username	_ftpproxy

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0

# Replacing license file with reference
mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENSE) LICENSE

%build
subst 's/-ggdb/-Werror -pipe/' src/Makefile
%make_build

%install
install -pD -m0755 -- src/ftp.proxy %buildroot/%_sbindir/ftp.proxy
install -pD -m0644 -- doc/ftp.proxy.1 %buildroot/%_man1dir/ftp.proxy.1
install -pD -m0644 -- %SOURCE1 %buildroot/%confdir/%name.conf
install -pD -m0644 -- samples/proxy-user.conf %buildroot/%confdir/proxy-user.conf
install -pD -m0640 -- %SOURCE2 %buildroot/%_sysconfdir/xinetd.d/%name
install -pD -m0755 -- samples/operator.ctp %buildroot/%scriptdir/ctp.awk
install -pD -m0644 -- %SOURCE3 %buildroot/%_sysconfdir/logrotate.d/%name

mkdir -p -- %buildroot/%logdir/

subst 's#@user@#%{username}#g'		%buildroot/%_sysconfdir/xinetd.d/%name
subst 's#@bindir@#%{_sbindir}#g'	%buildroot/%_sysconfdir/xinetd.d/%name
subst 's#@confdir@#%{confdir}#g'	%buildroot/%_sysconfdir/xinetd.d/%name
subst 's#@appname@#%{name}#g'		%buildroot/%_sysconfdir/xinetd.d/%name

subst 's#@scriptdir@#%{scriptdir}#g'	%buildroot/%confdir/%name.conf
subst 's#@logdir@#%{logdir}#g'	%buildroot/%confdir/%name.conf \
					%buildroot/%_sysconfdir/logrotate.d/%name

%pre
%_sbindir/groupadd -r -f %username 2>/dev/null ||:
%_sbindir/useradd  -r -g %username -c 'ftpproxy service' \
	-d /var/empty -s /dev/null %username 2>/dev/null ||:

%files
%doc HISTORY INSTALL samples
%doc --no-dereference LICENSE

%_sbindir/ftp.proxy
%scriptdir/*

%_man1dir/ftp.proxy*

%attr(0750,root,%username) %dir %confdir
%attr(1770,root,%username) %dir %logdir

%config(noreplace) %confdir/*.conf
%config(noreplace) %_sysconfdir/xinetd.d/%name
%config %_sysconfdir/logrotate.d/%name

%changelog
* Fri Jun 01 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.3-alt4
- Fix build with GCC 4.6

* Mon Feb 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.3-alt3
- Allow config file lines with arbitrary length
- Spec file cleanup

* Mon May 25 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.3-alt2
- Fix build with GCC 4.4
- Fix repocop warning about /tmp/ usage in sample script

* Sat Mar 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.3-alt1
- Initial build for ALT Linux Sisyphus

