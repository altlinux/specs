Name: smokeping
Version: 2.9.0
Release: alt2

Summary: Latency logging and graphing and alerting system

License: GPL-2.0-or-later
Group: Monitoring
Url: https://github.com/oetiker/SmokePing

# Source-url: https://github.com/oetiker/SmokePing/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name.service
Source3: smokeping_cgi_wrapper

BuildArch: noarch

%add_perl_lib_path %perl_vendorlib
%add_findreq_skiplist %perl_vendorlib/Smokeping/probes/TacacsPlus.pm
# Net::SNPP is optional (for SNPP alerts) and not in ALT repos
%filter_from_requires /perl(Net.SNPP/d

BuildRequires: autoconf automake groff-base
BuildRequires: perl(Config/Grammar.pm)
BuildRequires: perl(RRDs.pm)
BuildRequires: perl(FCGI.pm)
BuildRequires: perl(CGI.pm)
BuildRequires: perl(CGI/Fast.pm)
BuildRequires: perl(Socket6.pm)
BuildRequires: perl(IO/Socket/SSL.pm)
BuildRequires: perl(Digest/HMAC_MD5.pm)
BuildRequires: perl(Net/Telnet.pm)
BuildRequires: perl(Net/OpenSSH.pm)
BuildRequires: perl(Net/SNMP.pm)
BuildRequires: perl(Net/LDAP.pm)
BuildRequires: perl(Net/DNS.pm)
BuildRequires: perl(IO/Pty.pm)
BuildRequires: perl(LWP.pm)
BuildRequires: perl(Authen/Radius.pm)
BuildRequires: perl(Path/Tiny.pm)
BuildRequires: perl(SNMP_util.pm)
BuildRequires: perl-podlators

Requires: fping

%description
SmokePing is a latency logging and graphing and alerting system.
It consists of a daemon process which organizes the latency
measurements and a CGI which presents the graphs with interesting
smoke-like effects. SmokePing uses RRDtool for data storage and
graph drawing.

%prep
%setup
echo %version > VERSION

%build
./bootstrap
%configure --sysconfdir=%_sysconfdir/%name --enable-pkgonly
%make_build SUBDIRS="lib bin doc etc htdocs"

%install
%makeinstall_std SUBDIRS="lib bin doc etc htdocs"

# Move Perl modules to proper location
mkdir -p %buildroot%perl_vendorlib
mv %buildroot%_prefix/lib/Smokeping* %buildroot%perl_vendorlib/
# Remove bundled SNMP modules, use perl-SNMP_Session instead
rm %buildroot%_prefix/lib/BER.pm %buildroot%_prefix/lib/SNMP_Session.pm %buildroot%_prefix/lib/SNMP_util.pm

# Move htdocs to proper web location
mkdir -p %buildroot%_datadir/%name
mv %buildroot%_prefix/htdocs/* %buildroot%_datadir/%name/

# Fix paths in default config
sed -i \
    -e 's|imgcache = /usr/cache|imgcache = /var/cache/smokeping|' \
    -e 's|datadir  = /usr/data|datadir  = /var/lib/smokeping|' \
    -e 's|piddir  = /usr/var|piddir  = /run/smokeping|' \
    -e 's|smokemail = /usr/etc/smokemail.dist|smokemail = /etc/smokeping/smokemail|' \
    -e 's|tmail = /usr/etc/tmail.dist|tmail = /etc/smokeping/tmail|' \
    -e 's|template = /usr/etc/basepage.html.dist|template = /etc/smokeping/basepage.html|' \
    -e 's|secrets=/usr/etc/smokeping_secrets.dist|secrets=/etc/smokeping/smokeping_secrets|' \
    -e 's|sendmail = /path/to/sendmail|sendmail = /usr/sbin/sendmail|' \
    %buildroot%_sysconfdir/%name/config.dist

# Rename .dist config files
for f in basepage.html config smokemail smokeping_secrets tmail; do
    [ -f %buildroot%_sysconfdir/%name/$f.dist ] && mv %buildroot%_sysconfdir/%name/$f.dist %buildroot%_sysconfdir/%name/$f
done

# Remove examples from config dir
rm -rf %buildroot%_sysconfdir/%name/examples

# Create data directories
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_cachedir/%name

# Install systemd unit
install -Dpm644 %SOURCE1 %buildroot%_unitdir/%name.service

# Install CGI wrapper
install -Dpm755 %SOURCE3 %buildroot%_bindir/smokeping_cgi_wrapper

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md CHANGES CONTRIBUTORS COPYRIGHT LICENSE TODO
%_bindir/smokeinfo
%_bindir/smokeping
%_bindir/smokeping_cgi
%_bindir/smokeping_cgi_wrapper
%_bindir/tSmoke
%perl_vendorlib/Smokeping/
%perl_vendorlib/Smokeping.pm
%_datadir/%name/
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%dir %_localstatedir/%name
%dir %_cachedir/%name
%_unitdir/%name.service
%_man1dir/*
%_man3dir/*
%_man5dir/*
%_man7dir/*

%changelog
* Mon Mar 30 2026 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt2
- add RuntimeDirectory=smokeping to systemd unit (fixes startup in LXC)
- remove tmpfiles.d config (redundant with RuntimeDirectory)

* Fri Feb 06 2026 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt1
- initial build for ALT Sisyphus
