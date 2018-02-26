Name: flowscan
Version: 1.006
Release: alt1.1
License: GPL
Group: Monitoring
Summary: FlowScan - Network Traffic Flow Visualization and Reporting Tool
Url: http://www.caida.org/tools/utilities/flowscan/
Source: FlowScan-%version.tar.gz
Source1: %name.init
Source2: sysconfig.%name
Patch: %name.diff
Patch1: %name-105-106.patch
Packager: Boris Savelev <boris@altlinux.org>
Requires: flow-capture

# Automatically added by buildreq on Fri Dec 05 2008
BuildRequires: pdksh perl-Boulder perl-Cflow perl-ConfigReader perl-HTML-Table perl-Net-Patricia
BuildRequires: perl-devel rcs rrd-perl rrd-utils

%description
FlowScan analyzes and reports on Internet Protocol (IP) flow data exported by routers.
Consisting of Perl scripts and modules, FlowScan binds together
(1) a flow collection engine (a patched version of cflowd),
(2) a high performance database (Round Robin Database - RRD), and
(3) a visualization tool (RRDtool).
FlowScan produces graph images that provide a continuous, near real-time view of the network border traffic.

%prep
%setup -q -n FlowScan-%version
%patch -p1
%patch1 -p0

# fix up config files
subst "s|FlowFileGlob flows.*|FlowFileGlob %_var/log/flow-capture/ft-v05\.*|" cf/flowscan.cf
subst "s|OutputDir graphs|OutputDir %_var/lib/%name|" cf/CampusIO.cf
subst "s|^Napster|#Napster|" cf/CampusIO.cf
subst "s|OutputDir graphs|OutputDir %_var/lib/%name|" cf/SubNetIO.cf

%build
./configure \
	--sysconfdir=%_sysconfdir/flowscan \
	--localstatedir=%_sysconfdir/flowscan
%perl_vendor_build

%install
%perl_vendor_install

# fix up graph makefile
subst "s|event2vrule = /usr/local/bin/event2vrule|event2vrule = %_datadir/%name/event2vrule|" graphs.mf

mkdir -p %buildroot{%_datadir,%_sysconfdir,%_var/lib}/%name
install -D -p -m 755 %SOURCE1 %buildroot%_initdir/flowscan
install -D -p -m 755 flowscan %buildroot%_bindir/%name
install -m 755 util/locker %buildroot%_datadir/%name
install -m 755 util/add_ds.pl %buildroot%_datadir/%name
install -m 755 util/add_txrx %buildroot%_datadir/%name
install -m 755 util/event2vrule %buildroot%_datadir/%name
install -m 755 util/ip2hostname %buildroot%_datadir/%name
install -m 644 cf/* %buildroot%_sysconfdir/%name/
install -D -p -m 700 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m 644 graphs.mf %buildroot%_var/lib/%name/Makefile

mkdir -p %buildroot%_var/log/flow-capture/saved
touch %buildroot%_var/log/flow-capture/saved/.gzip_lock

mkdir -p %buildroot%_var/run/%name

%files
%doc CampusIO.html CampusIO.README Changes COPYING README SubNetIO.README TODO INSTALL
%doc %perl_vendor_privlib/*.pod
%config(noreplace) %_sysconfdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
%_bindir/*
%perl_vendor_privlib/*.pm
%perl_vendor_archlib/auto/FlowScan
%_datadir/%name
%attr(2775,root,_flow) %dir %_var/lib/%name
%_var/lib/%name/Makefile
%attr(2775,root,_flow) %dir %_var/log/flow-capture/saved
%_var/log/flow-capture/saved/.gzip_lock
%attr(2770,root,_flow) %dir %_var/run/%name

%changelog
* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 1.006-alt1.1
- rebuilt with perl 5.12

* Fri Dec 05 2008 Boris Savelev <boris@altlinux.org> 1.006-alt1
- initial build

* Mon Feb 23 2007 Carsten Schoene <cs@linux-administrator.com>
- initial package build of version 1.006

