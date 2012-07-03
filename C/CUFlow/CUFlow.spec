Name: CUFlow
Version: 1.7
Release: alt1
Summary: A module for FlowScan and an accompanying graphing cgi
License: GPL2
Group: Monitoring
Url: http://www.columbia.edu/acis/networks/advanced/CUFlow/
Packager: Boris Savelev <boris@altlinux.org>
Source: http://www.columbia.edu/acis/networks/advanced/CUFlow/%name-%version.tgz
Patch: %name.pm.patch
Patch1: CUGrapher.pl.patch
Patch2: %name.cf.patch

# Automatically added by buildreq on Fri Dec 05 2008
BuildRequires: perl-CGI perl-Cflow perl-Net-Patricia rrd-perl
BuildRequires: rpm-macros-webserver-common

%description
CGI script and config for FlowScan

%package -n flowscan-%name
Summary: A module for FlowScan and an accompanying graphing cgi
Group: Development/Perl
Requires: flowscan

%description -n flowscan-%name
CUFlow.pm is a FlowScan
module designed to combine the features of CampusIO and SubNetIO as we
needed them and also hopefully process data more quickly.  CUFlow
allows you to differentiate traffic by protocol, service, TOS, router,
and network and then generate TopN reports over 5 minutes periods and
over an extended period of time.  CUGrapher is the companion graphing
tool and is designed as a CGI which generates images on the fly based
on user input with data supplied by CUFlow.

%prep
%setup -q -n %name-%version
%patch -p0
%patch1 -p0
%patch2 -p0

%install
install -m 644 -D %name.pm %buildroot%perl_vendor_privlib/%name.pm
install -m 644 -D %name.cf %buildroot%_sysconfdir/flowscan/%name.cf
install -m 755 -D CUGrapher.pl %buildroot%webserver_htdocsdir/flowscan/index.cgi
mkdir -p %buildroot%webserver_htdocsdir/flowscan/scoreboard

%files -n flowscan-%name
%doc COPYING README.txt
%config(noreplace) %attr(0640,root,_flow) %_sysconfdir/flowscan/%name.cf
%perl_vendor_privlib/%name.pm
%attr(2775,root,_flow) %dir %webserver_htdocsdir/flowscan/scoreboard
%attr(2775,root,_flow) %dir %webserver_htdocsdir/flowscan
%attr(0755,root,root) %webserver_htdocsdir/flowscan/index.cgi

%changelog
* Fri Dec 05 2008 Boris Savelev <boris@altlinux.org> 1.7-alt1
- initial build
