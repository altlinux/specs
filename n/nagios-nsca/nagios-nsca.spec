Name: nagios-nsca
Version: 2.9.2
Release: alt1

Summary: Nagios addon to send check results to a central monitoring server

Group: Monitoring
License: GPLv2
Url: https://sourceforge.net/projects/nagios/

Source: nsca-%version.tar

BuildRequires: libnsl2-devel libsocket libmcrypt-devel

Requires: nagios xinetd

%description
This program is designed to accept passive service check results from
clients that use the send_nsca utility and pass them along to the
Nagios process by using the external command
interface. The program can either be run as a standalone daemon or as
a service under inetd. If you have libmcrypt installed on your systems,
you can choose from multiple crypto algorithms (DES, 3DES, CAST, xTEA,
Twofish, LOKI97, RJINDAEL, SERPENT, GOST, SAFER/SAFER+, etc.) for
encrypting the traffic between the client and the server.
Encryption is important in this addon, as it prevents unauthorized users
from sending bogus check results to Nagios. Read the included SECURITY
document for more information.

This package provides the core agent running on the Nagios server

%package send
Summary: A program to send check results to a central Nagios server
Group: Monitoring

%description send
This program is designed to accept passive service check results from
clients that use the send_nsca utility (which is included in this package)
and pass them along to the Nagios process by using the external command
interface. The program can either be run as a standalone daemon or as
a service under inetd. If you have libmcrypt installed on your systems,
you can choose from multiple crypto algorithms (DES, 3DES, CAST, xTEA,
Twofish, LOKI97, RJINDAEL, SERPENT, GOST, SAFER/SAFER+, etc.) for
encrypting the traffic between the client and the server.
Encryption is important in this addon, as it prevents unauthorized users
from sending bogus check results to Nagios. Read the included SECURITY
document for more information.

This package provides the send_nsca utility running on the client.

%prep
%setup -n nsca-%version

%build
#%autoreconf
%configure
%make_build

%install
#%makeinstall_std
install -D -m 0644 sample-config/nsca.cfg %buildroot%_sysconfdir/nagios/nsca.cfg
install -D -m 0644 sample-config/send_nsca.cfg %buildroot%_sysconfdir/nagios/send_nsca.cfg
install -D -m 0644 sample-config/nsca.xinetd %buildroot%_sysconfdir/xined.d/nsca
install -D -m 0755 src/nsca %buildroot%_sbindir/nsca
install -D -m 0755 src/send_nsca %buildroot%_bindir/send_nsca

#%check
#%make_build check

%files
%_sysconfdir/xined.d/nsca
%_sbindir/nsca
%config(noreplace) %_sysconfdir/nagios/nsca.cfg
%doc Changelog LEGAL README SECURITY

%files send
%_bindir/send_nsca
%config(noreplace) %_sysconfdir/nagios/send_nsca.cfg
%doc Changelog LEGAL README SECURITY

%changelog
* Tue Jan 21 2020 Paul Wolneykien <manowar@altlinux.org> 2.9.2-alt1
- Initial release for Sisyphus.

* Tue Jan 21 2020 Paul Wolneykien <manowar@altlinux.org> 2.9.2-alt0
- Test release.
