Summary: specialized packet sniffer designed for displaying and logging HTTP traffic
Name: httpry
Version: 0.1.7
Release: alt1
License: GPLv2
Group: Networking/WWW
Url: http://dumpsterventures.com/jason/httpry/
Source: %name-%version.tar

BuildRequires: libpcap-devel perl-DBD-mysql

%def_disable daemon

%description
httpry is a tool designed for displaying and logging HTTP traffic. It is not
intended to perform analysis itself, but instead to capture, parse and/or
log the traffic for later analysis. It can be run in real-time displaying
the live traffic on the wire, or as a daemon process that logs to an output
file. It is written to be as lightweight and flexible as possible, so that
it can be easily adaptable to different applications. It does not display
the raw HTTP data transferred, but instead focuses on parsing and displaying
the request/response line along with associated header fields.

%package scripts
Summary: Plugins for %name
Group: Networking/WWW
Requires: perl-DBD-mysql
%description scripts
A number of Perl scripts are included with the project to provide a basic
log parsing framework.

Read perl-tools for detail information.

%if_enabled daemon
%package daemon
Summary: Iniscript for %name
Group: Networking/WWW
%description daemon
Plugins for %name
%endif

%prep
%setup
sed -i '/DEFAULT_PLUGIN_DIR/s/plugins/\/usr\/share\/perl5\/httpry/' scripts/parse_log.pl

%build
%make_build

%install
install -D -m 0755 %name %buildroot%_sbindir/%name
install -D -m 0755 scripts/parse_log.pl %buildroot%_bindir/parse_log
install -D -m 0644 %name.1 %buildroot%_mandir/man1/%name.1
%if_enabled daemon
install -D -m 0755 rc.%name %buildroot%_initdir/%name
%endif
mkdir -p %buildroot%perl_vendor_privlib/%name
cp -r scripts/plugins/* %buildroot%perl_vendor_privlib/%name

%if_enabled daemon
%post
%post_service %name
%preun
%preun_service %name
%endif

%files
%doc doc
%_sbindir/*
%_mandir/man1/*

%if_enabled daemon
%files daemon
%_initdir/*
%endif

%files scripts
%_bindir/*
%perl_vendor_privlib/%name

%changelog
* Sun Nov 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.7-alt1
- New version

* Thu Sep 15 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.6-alt1
- Build for ALT

* Wed Jan 21 2009 Shawn Ashlee <shawn.ashlee@rackspace.com>
- updated to latest sources

* Fri Sep 05 2008 Shawn Ashlee <shawn.ashlee@rackspace.com>
- initial build
