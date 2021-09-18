%def_without qt
%define _pseudouser_user     _pcp
%define _pseudouser_group    _pcp
%define _pseudouser_home     %_sharedstatedir/pcp
%define _unpackaged_files_terminate_build 1


%define _localstatedir /var
%define _libexecdir /usr/libexec
%define _confdir  %_sysconfdir/pcp
%define _logsdir  %_localstatedir/log/pcp
%define _pmnsdir  %_sharedstatedir/pcp/pmns
%define _tempsdir %_sharedstatedir/pcp/tmp
%define _pmdasdir %_sharedstatedir/pcp/pmdas
%define _logconfdir %_sharedstatedir/pcp/config/pmlogconf

Name: pcp
Version: 5.2.0
Release: alt2
Summary: System-level performance monitoring and performance management
License: GPLv2+ and LGPLv2+ and CC-BY-SA-3.0
Group: Monitoring
URL: https://pcp.io

Source0: %name-%version.tar.gz
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: flex

BuildRequires: libavahi-devel
BuildRequires: liblzma-devel
BuildRequires: libnss-devel
BuildRequires: libreadline-devel
BuildRequires: librpm-devel
BuildRequires: libsasl2-devel
BuildRequires: libssl-devel
BuildRequires: libsystemd-devel
%if_with qt5
BuildRequires: qt5-base-devel qt5-svg-devel gcc-c++
%endif

BuildRequires: perl-devel
BuildRequires: python3-devel

BuildRequires: perl-autodie
BuildRequires: perl-Class-DBI
BuildRequires: perl-DateTime
BuildRequires: perl-File-Slurp
BuildRequires: perl-JSON
BuildRequires: perl-LWP-UserAgent-Determined
BuildRequires: perl-List-MoreUtils
BuildRequires: perl-RRD
BuildRequires: perl-TimeDate
BuildRequires: perl-Spreadsheet-WriteExcel
BuildRequires: perl-XML-LibXML
BuildRequires: perl-XML-TokeParser

BuildRequires: chrpath
BuildRequires: postfix
BuildRequires: man-db

Requires: libpcopilot = %EVR
Requires(post): pcp-conf

# PCP discovery service now provided by pmfind
Obsoletes: pcp-manager-debuginfo < 5.2.0
Obsoletes: pcp-manager < 5.2.0

%description
Performance Co-Pilot (PCP) provides a framework and services to support
system-level performance monitoring and performance management.

The PCP open source release provides a unifying abstraction for all of
the interesting performance data in a system, and allows client
applications to easily retrieve and process any subset of that data.

# pcp-conf
%package conf
License: LGPLv2+
Group: Monitoring
Summary: Performance Co-Pilot run-time configuration

%description conf
Performance Co-Pilot (PCP) run-time configuration

# libpcp
%package -n libpcopilot
License: LGPLv2+
Group: Monitoring
Summary: Performance Co-Pilot run-time libraries
Requires: pcp-conf = %EVR

%description -n libpcopilot
Performance Co-Pilot (PCP) run-time libraries

# libpcp-devel
%package -n libpcopilot-devel
License: GPLv2+ and LGPLv2+
Group: Development/Other
Summary: Performance Co-Pilot (PCP) development headers
Requires: libpcopilot = %EVR

%description -n libpcopilot-devel
Performance Co-Pilot (PCP) headers for development.

# pcp-devel
%package devel
License: GPLv2+ and LGPLv2+
Group: Development/Other
Summary: Performance Co-Pilot (PCP) development tools and documentation
Requires: pcp = %EVR
Requires: libpcopilot-devel = %EVR

%description devel
Performance Co-Pilot (PCP) documentation and tools for development.

# perl-PCP-common.
%package -n perl-PCP-common
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Perl common

%description -n perl-PCP-common
Performance Co-Pilot (PCP) Perl common

# perl-PCP-PMDA. This is the PCP agent perl binding.
%package -n perl-PCP-PMDA
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Perl bindings and documentation
Requires: perl-PCP-common

%description -n perl-PCP-PMDA
The PCP::PMDA Perl module contains the language bindings for
building Performance Metric Domain Agents (PMDAs) using Perl.
Each PMDA exports performance data for one specific domain, for
example the operating system kernel, Cisco routers, a database,
an application, etc.

# perl-PCP-MMV
%package -n perl-PCP-MMV
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Perl bindings for PCP Memory Mapped Values
Requires: perl-PCP-common

%description -n perl-PCP-MMV
The PCP::MMV module contains the Perl language bindings for
building scripts instrumented with the Performance Co-Pilot
(PCP) Memory Mapped Value (MMV) mechanism.
This mechanism allows arbitrary values to be exported from an
instrumented script into the PCP infrastructure for monitoring
and analysis with pmchart, pmie, pmlogger and other PCP tools.

# perl-PCP-LogImport
%package -n perl-PCP-LogImport
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Perl bindings for importing external data into PCP archives
Requires: perl-PCP-common

%description -n perl-PCP-LogImport
The PCP::LogImport module contains the Perl language bindings for
importing data in various 3rd party formats into PCP archives so
they can be replayed with standard PCP monitoring tools.

# perl-PCP-LogSummary
%package -n perl-PCP-LogSummary
BuildArch: noarch
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Perl bindings for post-processing output of pmlogsummary
Requires: perl-PCP-common

%description -n perl-PCP-LogSummary
The PCP::LogSummary module provides a Perl module for using the
statistical summary data produced by the Performance Co-Pilot
pmlogsummary utility.  This utility produces various averages,
minima, maxima, and other calculations based on the performance
data stored in a PCP archive.  The Perl interface is ideal for
exporting this data into third-party tools (e.g. spreadsheets).

# pcp-import-tools
%package import-tools
License: LGPLv2+
Group: Monitoring
Summary: Performance Co-Pilot tools for importing various format into PCP archive logs

%description import-tools
Performance Co-Pilot (PCP) front-end tools for importing various format
into standard PCP archive logs for replay with any PCP monitoring tool.

# pcp-export-tools
%package export-tools
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot tools for exporting PCP metrics to various format
Requires: python3-module-pcp = %EVR

%description export-tools
Performance Co-Pilot (PCP) front-end tools for exporting metric values
in various format.

# pcp-pmdas
%package pmdas
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) metrics for various services
Requires: perl-PCP-PMDA = %EVR
Requires: python3-module-pcp = %EVR
Requires: python3-module-psycopg2
Requires: python3-module-libvirt
Requires: python3-module-lxml
Requires: python3-module-rtslib
Requires: python3-module-requests

%description pmdas
This package contains the PCP performance metrics domain agent (PMDA)
to collect metrics from various services

%package zeroconf
BuildArch: noarch
License: GPLv2+
Group: Monitoring
Summary: Performance Co-Pilot (PCP) Zeroconf Package

%description zeroconf
This package contains configuration tweaks and files to increase metrics
gathering frequency, several extended pmlogger configurations, as well as
automated pmie diagnosis, alerting and self-healing for the localhost.

# python3-module-pcp. This is the PCP library bindings for python3.
%package -n python3-module-pcp
License: GPLv2+
Group: Development/Python3
Summary: Performance Co-Pilot (PCP) Python3 bindings and documentation

%description -n python3-module-pcp
This python PCP module contains the language bindings for
Performance Metric API (PMAPI) monitor tools and Performance
Metric Domain Agent (PMDA) collector tools written in Python3.

%if_with qt
# pcp-gui package for Qt tools
%package gui
License: GPLv2+ and LGPLv2+ and LGPLv2+ with exceptions
Summary: Visualization tools for the Performance Co-Pilot toolkit
URL: https://pcp.io

%description gui
Visualization tools for the Performance Co-Pilot toolkit.
The pcp-gui package primarily includes visualization tools for
monitoring systems using live and archived Performance Co-Pilot
(PCP) sources.
%endif

# pcp-doc package
%package doc
BuildArch: noarch
License: GPLv2+ and CC-BY-SA-3.0
Group: Monitoring
Summary: Documentation and tutorial for the Performance Co-Pilot

%description doc
Documentation and tutorial for the Performance Co-Pilot
Performance Co-Pilot (PCP) provides a framework and services to support
system-level performance monitoring and performance management.

The pcp-doc package provides useful information on using and
configuring the Performance Co-Pilot (PCP) toolkit for system
level performance management.  It includes tutorials, HOWTOs,
and other detailed documentation about the internals of core
PCP utilities and daemons, and the PCP graphical tools.

%prep
%setup -q
%patch0 -p1

%build

# Rename the libpcp library to libpcopilot in all files, 
# because the pcp library is already in the pgpool-II package
grep -rl '\(libpcp.*\|lpcp.*\|Extension\)' | xargs sed -i \
-e 's/libpcp/libpcopilot/g' \
-e 's/lpcp/lpcopilot/g' \
-e '/libraries/s/pcp/pcopilot/g'

# Rename file and folder names from libpcp to libpcopilot
find -type f,d -name 'libpcp*' | sort -r | sed 'p;s:\(.*\)libpcp:\1libpcopilot:' | xargs -n2 mv

mv src/include/pcp src/include/pcopilot
sed -i -e 's:include/pcp/:include/pcopilot/:g' configure.ac 
sed -i -e 's:SUBDIRS = pcp:SUBDIRS = pcopilot:' src/include/GNUmakefile
grep -rl '/include/pcp' | xargs sed -i \
-e '/PCP_INC_DIR/s:/include/pcp:/include/pcopilot:g' \
-e 's:/include/pcp/:/include/pcopilot/:g' \
-e '/-I/s:/include/pcp:/include/pcopilot:g' \
-e '/-I/s:$(TOPDIR)/src/include/pcp:$(TOPDIR)/src/include/pcopilot:g' \
-e 's:$(TOPDIR)/src/include/pcp/:$(TOPDIR)/src/include/pcopilot/:g' 

grep -rl '\($INCDIR/pcp/\|$includedir/pcp\)' | xargs sed -i \
-e 's:$INCDIR/pcp/:$INCDIR/pcopilot/:g' \
-e 's:$includedir/pcp:$includedir/pcopilot:g'

grep -rl '\(<pcp/\|"pcp/\|find_library\)' | xargs sed -i \
-e '/include/s/pcp/pcopilot/g' \
-e 's:@<pcp/pmapi.h>@:@<pcopilot/pmapi.h>@:g' \
-e '/find_library/s/pcp/pcopilot/g'

# Change path for ALTLinux
sed -i \
-e 's_/etc/apache2:/etc/httpd_/etc/httpd2_' \
-e 's_log/apache2_log/httpd2_' \
-e 's/FTPPATH:-$_logdir/FTPPATH:-\/var\/ftp/' src/pmdas/weblog/server.sh

%autoreconf

# due to @b78cbe17d and @8ab231919
sed -i \
-e '/undef HAVE_32BIT_LONG/d' \
-e '/undef HAVE_32BIT_PTR/d' \
-e '/undef HAVE_64BIT_LONG/d' \
-e '/undef HAVE_64BIT_PTR/d' \
-e '/undef PM_SIZEOF_SUSECONDS_T/d' \
-e '/undef PM_SIZEOF_TIME_T/d' \
src/include/pcopilot/config.h.in

%configure \
%if_with qt
	--with-qt=yes \
	--with-qt3d=yes \
%else
	--with-qt=no \
	--with-qt3d=no \
%endif
	--with-rcdir=%_initddir \
	--with-rundir=/run/pcp \
	--with-python3=yes \
	--with-selinux=no \
	--with-pmdapodman=no \
	--with-perfevent=no \
	--with-pmdabcc=no \
	--with-infiniband=no \
	--with-dstat-symlink=no \
	--with-pmdanutcracker=no \
	--with-pmdajson=no \
	--with-python=no \
	--with-webapps=no \
	--with-pmdasnmp=no \
	--with-user=%_pseudouser_user \
	--with-group=%_pseudouser_group 

%make_build default_pcp

%install
export NO_CHOWN=true DIST_ROOT=%buildroot
%make install_pcp
# strange source place(tests' dir) for runtime Perl module
install -D ./qa/slurm/Slurm/Hostlist.pm \
    %buildroot%perl_vendorarch/Slurm/Hostlist.pm
install ./qa/slurm/Slurm.pm %buildroot%perl_vendorarch/

chrpath -d \
    %buildroot%perl_vendor_autolib/PCP/LogImport/LogImport.so \
    %buildroot%perl_vendor_autolib/PCP/MMV/MMV.so \
    %buildroot%perl_vendor_autolib/PCP/PMDA/PMDA.so

install -m 644 src/pmdas/activemq/Queue.pm \
    %buildroot%perl_vendorarch/PCP/
PCP_GUI='pmchart|pmconfirm|pmdumptext|pmmessage|pmquery|pmsnap|pmtime'

# Fix stuff we do/don't want to ship
rm %buildroot%_libdir/*.a

rm %buildroot%_bindir/sheet2pcp

# remove {config,platform}sz.h as these are not multilib friendly.
rm %buildroot%_includedir/pcopilot/configsz.h
rm %buildroot%_includedir/pcopilot/platformsz.h

rm -r %buildroot%_sharedstatedir/pcp/config/pmchart/
rm -r %buildroot%_datadir/pcp-gui/pixmaps/

touch %buildroot/%_pmnsdir/root \
        %buildroot/%_pmnsdir/root.prev \
        %buildroot/%_pmnsdir/stdpmid
chmod 644 %buildroot/%_pmnsdir/root \
        %buildroot/%_pmnsdir/root.prev \
        %buildroot/%_pmnsdir/stdpmid

%pre
getent group %_pseudouser_group >/dev/null || groupadd -r %_pseudouser_group
getent passwd %_pseudouser_user >/dev/null || \
  useradd -c "Performance Co-Pilot" -g %_pseudouser_group -d %_pseudouser_home -M -r -s /sbin/nologin %_pseudouser_user

%post zeroconf
# increase default pmlogger recording frequency
sed -i 's/^\#\ PMLOGGER_INTERVAL.*/PMLOGGER_INTERVAL=10/g' \
    "%_sysconfdir/sysconfig/pmlogger"

%post_service pmcd
%post_service pmlogger
%post_service pmie
%post_service pmfind

%post
PCP_LOG_DIR=%_logsdir
PCP_PMNS_DIR=%_pmnsdir
# restore saved configs, if any
test -s "$PCP_LOG_DIR/configs.sh" && source "$PCP_LOG_DIR/configs.sh"
rm -f $PCP_LOG_DIR/configs.sh

touch "$PCP_PMNS_DIR/.NeedRebuild"
chmod 644 "$PCP_PMNS_DIR/.NeedRebuild"
%post_service pmproxy

cd $PCP_PMNS_DIR && ./Rebuild -s && rm -f .NeedRebuild

%files
%doc CHANGELOG COPYING INSTALL.md README.md

%_pmdasdir/jbd2/
%_pmdasdir/kvm/
%_pmdasdir/linux/
%_pmdasdir/mmv/
%_pmdasdir/pipe/
%_pmdasdir/pmcd/
%_pmdasdir/proc/
%_pmdasdir/root/
%_pmdasdir/xfs/
%_bindir/dbpmda
%_bindir/pcp
%_bindir/pcp2csv
%_bindir/pmafm
%_bindir/pmdate
%_bindir/pmdiff
%_bindir/pmdumplog
%_bindir/pmevent
%_bindir/pmfind
%_bindir/pmgenmap
%_bindir/pmie
%_bindir/pmie2col
%_bindir/pmieconf
%_bindir/pmiectl
%_bindir/pminfo
%_bindir/pmjson
%_bindir/pmlc
%_bindir/pmlogcheck
%_bindir/pmlogconf
%_bindir/pmlogctl
%_bindir/pmlogextract
%_bindir/pmlogger
%_bindir/pmloglabel
%_bindir/pmlogmv
%_bindir/pmlogpaste
%_bindir/pmlogsize
%_bindir/pmlogsummary
%_bindir/pmprobe
%_bindir/pmpython
%_bindir/pmsocks
%_bindir/pmstat
%_bindir/pmstore
%_bindir/pmtrace
%_bindir/pmval
%dir %_libexecdir/pcp
%dir %_libexecdir/pcp/bin
%_libexecdir/pcp/bin/chkhelp
%_libexecdir/pcp/bin/discover
%_libexecdir/pcp/bin/find-filter
%_libexecdir/pcp/bin/install-sh
%_libexecdir/pcp/bin/mkaf
%_libexecdir/pcp/bin/newhelp
%_libexecdir/pcp/bin/pcp-python
%_libexecdir/pcp/bin/pcp-summary
%_libexecdir/pcp/bin/pcp-vmstat
%_libexecdir/pcp/bin/pmcd
%_libexecdir/pcp/bin/pmcd_wait
%_libexecdir/pcp/bin/pmconfig
%_libexecdir/pcp/bin/pmcpp
%_libexecdir/pcp/bin/pmfind_check
%_libexecdir/pcp/bin/pmgetopt
%_libexecdir/pcp/bin/pmhostname
%_libexecdir/pcp/bin/pmie_check
%_libexecdir/pcp/bin/pmie_daily
%_libexecdir/pcp/bin/pmie_dump_stats
%_libexecdir/pcp/bin/pmie_email
%_libexecdir/pcp/bin/pmiestatus
%_libexecdir/pcp/bin/pmlock
%_libexecdir/pcp/bin/pmlogconf
#%_libexecdir/pcp/bin/pmlogconf-setup
%_libexecdir/pcp/bin/pmlogextract
%_libexecdir/pcp/bin/pmlogger
%_libexecdir/pcp/bin/pmlogger_check
%_libexecdir/pcp/bin/pmlogger_daily
%_libexecdir/pcp/bin/pmlogger_merge
%_libexecdir/pcp/bin/pmlogger_rewrite
%_libexecdir/pcp/bin/pmlogreduce
%_libexecdir/pcp/bin/pmlogrewrite
%_libexecdir/pcp/bin/pmnewlog
%_libexecdir/pcp/bin/pmnsadd
%_libexecdir/pcp/bin/pmnsdel
%_libexecdir/pcp/bin/pmnsmerge
%_libexecdir/pcp/bin/pmpause
%_libexecdir/pcp/bin/pmpost
%_libexecdir/pcp/bin/pmproxy
%_libexecdir/pcp/bin/pmsignal
%_libexecdir/pcp/bin/pmsleep
%_libexecdir/pcp/bin/pmwtf
%_libexecdir/pcp/bin/telnet-probe
# todo: move to subpackages
%dir %_libexecdir/pcp/lib
%dir %_libexecdir/pcp/pmdas
%_libexecdir/pcp/pmdas/activemq
%_libexecdir/pcp/pmdas/apache
%_libexecdir/pcp/pmdas/bash
%_libexecdir/pcp/pmdas/bind2
%_libexecdir/pcp/pmdas/bonding
%_libexecdir/pcp/pmdas/cifs
%_libexecdir/pcp/pmdas/cisco
%_libexecdir/pcp/pmdas/dbping
%_libexecdir/pcp/pmdas/dm
%_libexecdir/pcp/pmdas/docker
%_libexecdir/pcp/pmdas/ds389
%_libexecdir/pcp/pmdas/ds389log
%_libexecdir/pcp/pmdas/elasticsearch
%_libexecdir/pcp/pmdas/gfs2
%_libexecdir/pcp/pmdas/gluster
%_libexecdir/pcp/pmdas/gluster
%_libexecdir/pcp/pmdas/gpfs
%_libexecdir/pcp/pmdas/gpsd
%_libexecdir/pcp/pmdas/haproxy
%_libexecdir/pcp/pmdas/jbd2
%_libexecdir/pcp/pmdas/jbd2
%_libexecdir/pcp/pmdas/kvm
%_libexecdir/pcp/pmdas/kvm
%_libexecdir/pcp/pmdas/linux
%_libexecdir/pcp/pmdas/lmsensors
%_libexecdir/pcp/pmdas/logger
%_libexecdir/pcp/pmdas/lustre
%_libexecdir/pcp/pmdas/lustrecomm
%_libexecdir/pcp/pmdas/mailq
%_libexecdir/pcp/pmdas/memcache
%_libexecdir/pcp/pmdas/mic
%_libexecdir/pcp/pmdas/mmv
%_libexecdir/pcp/pmdas/mounts
%_libexecdir/pcp/pmdas/mssql
%_libexecdir/pcp/pmdas/named
%_libexecdir/pcp/pmdas/netcheck
%_libexecdir/pcp/pmdas/netfilter
%_libexecdir/pcp/pmdas/news
%_libexecdir/pcp/pmdas/nfsclient
%_libexecdir/pcp/pmdas/nginx
%_libexecdir/pcp/pmdas/nvidia
%_libexecdir/pcp/pmdas/openvswitch
%_libexecdir/pcp/pmdas/oracle
%_libexecdir/pcp/pmdas/pdns
%_libexecdir/pcp/pmdas/pipe
%_libexecdir/pcp/pmdas/pmcd
%_libexecdir/pcp/pmdas/postfix
%_libexecdir/pcp/pmdas/proc
%_libexecdir/pcp/pmdas/rabbitmq
%_libexecdir/pcp/pmdas/redis
%_libexecdir/pcp/pmdas/roomtemp
%_libexecdir/pcp/pmdas/root
%_libexecdir/pcp/pmdas/rpm
%_libexecdir/pcp/pmdas/rsyslog
%_libexecdir/pcp/pmdas/samba
%_libexecdir/pcp/pmdas/sample
%_libexecdir/pcp/pmdas/sendmail
%_libexecdir/pcp/pmdas/shping
%_libexecdir/pcp/pmdas/simple
%_libexecdir/pcp/pmdas/slurm
%_libexecdir/pcp/pmdas/smart
%_libexecdir/pcp/pmdas/summary
%_libexecdir/pcp/pmdas/systemd
%_libexecdir/pcp/pmdas/trace
%_libexecdir/pcp/pmdas/trivial
%_libexecdir/pcp/pmdas/txmon
%_libexecdir/pcp/pmdas/unbound
%_libexecdir/pcp/pmdas/weblog
%_libexecdir/pcp/pmdas/weblog
%_libexecdir/pcp/pmdas/xfs
%_libexecdir/pcp/pmdas/zimbra
%_libexecdir/pcp/pmdas/zswap
%_libexecdir/pcp/pmns
%_libexecdir/pcp/lib/bashproc.sh
%_libexecdir/pcp/lib/pmdaproc.sh
%_libexecdir/pcp/lib/rc-proc.sh
%_libexecdir/pcp/lib/rc-proc.sh.minimal
%_libexecdir/pcp/lib/utilproc.sh
%dir %_confdir/bind2
%config(noreplace) %_confdir/bind2/bind2.conf
%dir %_confdir/derived
%config(noreplace) %_confdir/derived/cpu-util.conf
%config(noreplace) %_confdir/derived/iostat.conf
%config(noreplace) %_confdir/derived/mssql.conf
%config(noreplace) %_confdir/derived/proc.conf
%dir %_confdir/haproxy
%config(noreplace) %_confdir/haproxy/haproxy.conf
%dir %_confdir/linux
%config(noreplace) %_confdir/linux/samplebandwidth.conf
%dir %_confdir/lustre
%config(noreplace) %_confdir/lustre/lustre.conf
%dir %_confdir/mounts
%config(noreplace) %_confdir/mounts/mounts.conf
%dir %_confdir/mssql
%config(noreplace) %_confdir/mssql/mssql.conf
%dir %_confdir/netcheck
%config(noreplace) %_confdir/netcheck/netcheck.conf
%dir %_confdir/nginx
%config(noreplace) %_confdir/nginx/nginx.conf
%dir %_confdir/oracle
%config(noreplace) %_confdir/oracle/sample.conf
%dir %_confdir/pipe
%config(noreplace) %_confdir/pipe/sample.conf
%dir %_confdir/pmafm
%config(noreplace) %_confdir/pmafm/pcp
%config(noreplace) %_confdir/pmafm/pcp-gui
%dir %_confdir/pmchart
%config(noreplace) %_confdir/pmchart/Apache
%config(noreplace) %_confdir/pmchart/Cisco
%config(noreplace) %_confdir/pmchart/Sample
%config(noreplace) %_confdir/pmchart/Sendmail
%config(noreplace) %_confdir/pmchart/Web.Alarms
%config(noreplace) %_confdir/pmchart/Web.Allservers
%config(noreplace) %_confdir/pmchart/Web.Perserver.Bytes
%config(noreplace) %_confdir/pmchart/Web.Perserver.Requests
%config(noreplace) %_confdir/pmchart/Web.Requests
%config(noreplace) %_confdir/pmchart/Web.Volume
%config(noreplace) %_confdir/pmchart/shping.CPUTime
%config(noreplace) %_confdir/pmchart/shping.RealTime
%dir %_confdir/pmie
%dir %_confdir/pmie/class.d
%config(noreplace) %_confdir/pmie/class.d/pmfind
%dir %_confdir/pmieconf
%dir %_confdir/pmieconf/cisco
%config(noreplace) %_confdir/pmieconf/cisco/in_util
%config(noreplace) %_confdir/pmieconf/cisco/out_util
%dir %_confdir/pmieconf/cpu
%config(noreplace) %_confdir/pmieconf/cpu/context_switch
%config(noreplace) %_confdir/pmieconf/cpu/load_average
%config(noreplace) %_confdir/pmieconf/cpu/low_util
%config(noreplace) %_confdir/pmieconf/cpu/system
%config(noreplace) %_confdir/pmieconf/cpu/util
%dir %_confdir/pmieconf/dm
%config(noreplace) %_confdir/pmieconf/dm/data_high_util
%config(noreplace) %_confdir/pmieconf/dm/metadata_high_util
%dir %_confdir/pmieconf/entropy
%config(noreplace) %_confdir/pmieconf/entropy/available
%dir %_confdir/pmieconf/filesys
%config(noreplace) %_confdir/pmieconf/filesys/filling
%dir %_confdir/pmieconf/global
%config(noreplace) %_confdir/pmieconf/global/parameters
%config(noreplace) %_confdir/pmieconf/global/pcp_actions
%dir %_confdir/pmieconf/memory
%config(noreplace) %_confdir/pmieconf/memory/exhausted
%config(noreplace) %_confdir/pmieconf/memory/swap_low
%dir %_confdir/pmieconf/network
%config(noreplace) %_confdir/pmieconf/network/tcplistenoverflows
%config(noreplace) %_confdir/pmieconf/network/tcpqfulldocookies
%config(noreplace) %_confdir/pmieconf/network/tcpqfulldrops
%dir %_confdir/pmieconf/percpu
%config(noreplace) %_confdir/pmieconf/percpu/many_util
%config(noreplace) %_confdir/pmieconf/percpu/some_util
%config(noreplace) %_confdir/pmieconf/percpu/system
%dir %_confdir/pmieconf/pernetif
%config(noreplace) %_confdir/pmieconf/pernetif/collisions
%config(noreplace) %_confdir/pmieconf/pernetif/errors
%config(noreplace) %_confdir/pmieconf/pernetif/packets
%config(noreplace) %_confdir/pmieconf/pernetif/util
%dir %_confdir/pmieconf/primary
%config(noreplace) %_confdir/pmieconf/primary/pmda_status
%dir %_confdir/pmieconf/shping
%config(noreplace) %_confdir/pmieconf/shping/response
%config(noreplace) %_confdir/pmieconf/shping/status
%dir %_confdir/pmieconf/zeroconf
%config(noreplace) %_confdir/pmieconf/zeroconf/all_threads
%dir %_confdir/pmlogconf
%dir %_confdir/pmlogconf/apache
%config(noreplace) %_confdir/pmlogconf/apache/processes
%config(noreplace) %_confdir/pmlogconf/apache/summary
%config(noreplace) %_confdir/pmlogconf/apache/uptime
%dir %_confdir/pmlogconf/cpu
%config(noreplace) %_confdir/pmlogconf/cpu/percpu
%config(noreplace) %_confdir/pmlogconf/cpu/summary
%dir %_confdir/pmlogconf/disk
%config(noreplace) %_confdir/pmlogconf/disk/percontroller
%config(noreplace) %_confdir/pmlogconf/disk/perdisk
%config(noreplace) %_confdir/pmlogconf/disk/perpartition
%config(noreplace) %_confdir/pmlogconf/disk/summary
%dir %_confdir/pmlogconf/elasticsearch
%config(noreplace) %_confdir/pmlogconf/elasticsearch/summary
%dir %_confdir/pmlogconf/filesystem
%config(noreplace) %_confdir/pmlogconf/filesystem/all
%config(noreplace) %_confdir/pmlogconf/filesystem/rpc-server
%config(noreplace) %_confdir/pmlogconf/filesystem/summary
%config(noreplace) %_confdir/pmlogconf/filesystem/xfs-all
%config(noreplace) %_confdir/pmlogconf/filesystem/xfs-io-linux
%dir %_confdir/pmlogconf/gfs2
%config(noreplace) %_confdir/pmlogconf/gfs2/gfs2-all
%config(noreplace) %_confdir/pmlogconf/gfs2/gfs2-base
%dir %_confdir/pmlogconf/kernel
%config(noreplace) %_confdir/pmlogconf/kernel/bufcache-activity
%config(noreplace) %_confdir/pmlogconf/kernel/bufcache-all
%config(noreplace) %_confdir/pmlogconf/kernel/inode-cache
%config(noreplace) %_confdir/pmlogconf/kernel/interrupts-irix
%config(noreplace) %_confdir/pmlogconf/kernel/load
%config(noreplace) %_confdir/pmlogconf/kernel/memory-irix
%config(noreplace) %_confdir/pmlogconf/kernel/memory-linux
%config(noreplace) %_confdir/pmlogconf/kernel/queues-irix
%config(noreplace) %_confdir/pmlogconf/kernel/read-write-data
%config(noreplace) %_confdir/pmlogconf/kernel/summary-linux
%config(noreplace) %_confdir/pmlogconf/kernel/summary-windows
%config(noreplace) %_confdir/pmlogconf/kernel/syscalls-irix
%config(noreplace) %_confdir/pmlogconf/kernel/syscalls-linux
%config(noreplace) %_confdir/pmlogconf/kernel/syscalls-percpu-irix
%config(noreplace) %_confdir/pmlogconf/kernel/vnodes
%dir %_confdir/pmlogconf/kvm
%config(noreplace) %_confdir/pmlogconf/kvm/kvm
%dir %_confdir/pmlogconf/libvirt
%config(noreplace) %_confdir/pmlogconf/libvirt/libvirt
%dir %_confdir/pmlogconf/mailq
%config(noreplace) %_confdir/pmlogconf/mailq/summary
%dir %_confdir/pmlogconf/memcache
%config(noreplace) %_confdir/pmlogconf/memcache/summary
%dir %_confdir/pmlogconf/memory
%config(noreplace) %_confdir/pmlogconf/memory/buddyinfo
%config(noreplace) %_confdir/pmlogconf/memory/ksminfo
%config(noreplace) %_confdir/pmlogconf/memory/meminfo
%config(noreplace) %_confdir/pmlogconf/memory/proc-linux
%config(noreplace) %_confdir/pmlogconf/memory/slabinfo
%config(noreplace) %_confdir/pmlogconf/memory/swap-activity
%config(noreplace) %_confdir/pmlogconf/memory/swap-all
%config(noreplace) %_confdir/pmlogconf/memory/swap-config
%config(noreplace) %_confdir/pmlogconf/memory/tlb-irix
%config(noreplace) %_confdir/pmlogconf/memory/vmstat
%config(noreplace) %_confdir/pmlogconf/memory/zoneinfo
%dir %_confdir/pmlogconf/mmv
%config(noreplace) %_confdir/pmlogconf/mmv/summary
%dir %_confdir/pmlogconf/mssql
%config(noreplace) %_confdir/pmlogconf/mssql/summary
%dir %_confdir/pmlogconf/netcheck
%config(noreplace) %_confdir/pmlogconf/netcheck/summary
%dir %_confdir/pmlogconf/netfilter
%config(noreplace) %_confdir/pmlogconf/netfilter/config
%config(noreplace) %_confdir/pmlogconf/netfilter/summary
%dir %_confdir/pmlogconf/networking
%config(noreplace) %_confdir/pmlogconf/networking/icmp6
%config(noreplace) %_confdir/pmlogconf/networking/interface-all
%config(noreplace) %_confdir/pmlogconf/networking/interface-summary
%config(noreplace) %_confdir/pmlogconf/networking/ip6
%config(noreplace) %_confdir/pmlogconf/networking/mbufs
%config(noreplace) %_confdir/pmlogconf/networking/multicast
%config(noreplace) %_confdir/pmlogconf/networking/nfs2-client
%config(noreplace) %_confdir/pmlogconf/networking/nfs2-server
%config(noreplace) %_confdir/pmlogconf/networking/nfs3-client
%config(noreplace) %_confdir/pmlogconf/networking/nfs3-server
%config(noreplace) %_confdir/pmlogconf/networking/nfs4-client
%config(noreplace) %_confdir/pmlogconf/networking/nfs4-server
%config(noreplace) %_confdir/pmlogconf/networking/other-protocols
%config(noreplace) %_confdir/pmlogconf/networking/rpc
%config(noreplace) %_confdir/pmlogconf/networking/socket-irix
%config(noreplace) %_confdir/pmlogconf/networking/socket-linux
%config(noreplace) %_confdir/pmlogconf/networking/softnet
%config(noreplace) %_confdir/pmlogconf/networking/streams
%config(noreplace) %_confdir/pmlogconf/networking/tcp-activity-irix
%config(noreplace) %_confdir/pmlogconf/networking/tcp-activity-linux
%config(noreplace) %_confdir/pmlogconf/networking/tcp-all
%config(noreplace) %_confdir/pmlogconf/networking/udp-all
%config(noreplace) %_confdir/pmlogconf/networking/udp-packets-irix
%config(noreplace) %_confdir/pmlogconf/networking/udp-packets-linux
%config(noreplace) %_confdir/pmlogconf/networking/udp6
%dir %_confdir/pmlogconf/nginx
%config(noreplace) %_confdir/pmlogconf/nginx/summary
%dir %_confdir/pmlogconf/openvswitch
%config(noreplace) %_confdir/pmlogconf/openvswitch/summary
%dir %_confdir/pmlogconf/oracle
%config(noreplace) %_confdir/pmlogconf/oracle/summary
%dir %_confdir/pmlogconf/platform
%config(noreplace) %_confdir/pmlogconf/platform/hinv
%config(noreplace) %_confdir/pmlogconf/platform/linux
%dir %_confdir/pmlogconf/rabbitmq
%config(noreplace) %_confdir/pmlogconf/rabbitmq/summary
%dir %_confdir/pmlogconf/sgi
%config(noreplace) %_confdir/pmlogconf/sgi/cpu-evctr
%config(noreplace) %_confdir/pmlogconf/sgi/craylink
%config(noreplace) %_confdir/pmlogconf/sgi/efs
%config(noreplace) %_confdir/pmlogconf/sgi/hub
%config(noreplace) %_confdir/pmlogconf/sgi/kaio
%config(noreplace) %_confdir/pmlogconf/sgi/node-memory
%config(noreplace) %_confdir/pmlogconf/sgi/numa
%config(noreplace) %_confdir/pmlogconf/sgi/numa-summary
%config(noreplace) %_confdir/pmlogconf/sgi/xbow
%config(noreplace) %_confdir/pmlogconf/sgi/xlv-activity
%config(noreplace) %_confdir/pmlogconf/sgi/xlv-stripe-io
%config(noreplace) %_confdir/pmlogconf/sgi/xvm-all
%config(noreplace) %_confdir/pmlogconf/sgi/xvm-ops
%config(noreplace) %_confdir/pmlogconf/sgi/xvm-stats
%dir %_confdir/pmlogconf/shping
%config(noreplace) %_confdir/pmlogconf/shping/summary
%dir %_confdir/pmlogconf/sqlserver
%config(noreplace) %_confdir/pmlogconf/sqlserver/summary
%dir %_confdir/pmlogconf/statsd
%config(noreplace) %_confdir/pmlogconf/statsd/statsd
%dir %_confdir/pmlogconf/storage
%config(noreplace) %_confdir/pmlogconf/storage/vdo
%config(noreplace) %_confdir/pmlogconf/storage/vdo-summary
%dir %_confdir/pmlogconf/tools
%config(noreplace) %_confdir/pmlogconf/tools/atop
%config(noreplace) %_confdir/pmlogconf/tools/atop-gpustats
%config(noreplace) %_confdir/pmlogconf/tools/atop-hotproc
%config(noreplace) %_confdir/pmlogconf/tools/atop-httpstats
%config(noreplace) %_confdir/pmlogconf/tools/atop-infiniband
%config(noreplace) %_confdir/pmlogconf/tools/atop-nfsclient
%config(noreplace) %_confdir/pmlogconf/tools/atop-perfevent
%config(noreplace) %_confdir/pmlogconf/tools/atop-proc
%config(noreplace) %_confdir/pmlogconf/tools/atop-summary
%config(noreplace) %_confdir/pmlogconf/tools/collectl
%config(noreplace) %_confdir/pmlogconf/tools/collectl-interrupts
%config(noreplace) %_confdir/pmlogconf/tools/collectl-summary
%config(noreplace) %_confdir/pmlogconf/tools/dmcache
%config(noreplace) %_confdir/pmlogconf/tools/dstat
%config(noreplace) %_confdir/pmlogconf/tools/dstat-summary
%config(noreplace) %_confdir/pmlogconf/tools/free
%config(noreplace) %_confdir/pmlogconf/tools/free-summary
%config(noreplace) %_confdir/pmlogconf/tools/hotproc
%config(noreplace) %_confdir/pmlogconf/tools/iostat
%config(noreplace) %_confdir/pmlogconf/tools/ip
%config(noreplace) %_confdir/pmlogconf/tools/ipcs
%config(noreplace) %_confdir/pmlogconf/tools/mpstat
%config(noreplace) %_confdir/pmlogconf/tools/mpstat-interrupts
%config(noreplace) %_confdir/pmlogconf/tools/mpstat-summary
%config(noreplace) %_confdir/pmlogconf/tools/numastat
%config(noreplace) %_confdir/pmlogconf/tools/pcp-summary
%config(noreplace) %_confdir/pmlogconf/tools/pidstat
%config(noreplace) %_confdir/pmlogconf/tools/pidstat-summary
%config(noreplace) %_confdir/pmlogconf/tools/pmclient
%config(noreplace) %_confdir/pmlogconf/tools/pmclient-summary
%config(noreplace) %_confdir/pmlogconf/tools/pmieconf
%config(noreplace) %_confdir/pmlogconf/tools/pmstat
%config(noreplace) %_confdir/pmlogconf/tools/sar
%config(noreplace) %_confdir/pmlogconf/tools/sar-summary
%config(noreplace) %_confdir/pmlogconf/tools/tapestat
%config(noreplace) %_confdir/pmlogconf/tools/uptime
%config(noreplace) %_confdir/pmlogconf/tools/vector
%config(noreplace) %_confdir/pmlogconf/tools/vector-summary
%config(noreplace) %_confdir/pmlogconf/tools/vmstat
%config(noreplace) %_confdir/pmlogconf/tools/vmstat-summary
%dir  %_confdir/pmlogconf/v1.0
%config(noreplace) %_confdir/pmlogconf/v1.0/C2
%config(noreplace) %_confdir/pmlogconf/v1.0/C3
%config(noreplace) %_confdir/pmlogconf/v1.0/D3
%config(noreplace) %_confdir/pmlogconf/v1.0/K0
%config(noreplace) %_confdir/pmlogconf/v1.0/S0
%config(noreplace) %_confdir/pmlogconf/v1.0/S1
%dir %_confdir/pmlogconf/zeroconf
%config(noreplace) %_confdir/pmlogconf/zeroconf/atop-proc
%config(noreplace) %_confdir/pmlogconf/zeroconf/interrupts
%config(noreplace) %_confdir/pmlogconf/zeroconf/nfsclient
%config(noreplace) %_confdir/pmlogconf/zeroconf/numastat
%config(noreplace) %_confdir/pmlogconf/zeroconf/pidstat
%config(noreplace) %_confdir/pmlogconf/zeroconf/pidstat-summary
%config(noreplace) %_confdir/pmlogconf/zeroconf/tapestat
%config(noreplace) %_confdir/pmlogconf/zeroconf/xfs-perdev
%dir %_confdir/pmlogconf/zimbra
%config(noreplace) %_confdir/pmlogconf/zimbra/all
%dir %_confdir/pmlogger
%dir %_confdir/pmlogger/class.d
%config(noreplace) %_confdir/pmlogger/class.d/pmfind
%config(noreplace) %_confdir/pmlogger/config.pmstat
%dir %_confdir/pmlogrewrite
%config(noreplace) %_confdir/pmlogrewrite/cgroup_units.conf
%config(noreplace) %_confdir/pmlogrewrite/jbd2_kernel_ulong.conf
%config(noreplace) %_confdir/pmlogrewrite/linux_disk_all_fixups.conf
%config(noreplace) %_confdir/pmlogrewrite/linux_kernel_fixups.conf
%config(noreplace) %_confdir/pmlogrewrite/linux_kernel_ulong.conf
%config(noreplace) %_confdir/pmlogrewrite/linux_proc_fs_nfsd_fixups.conf
%config(noreplace) %_confdir/pmlogrewrite/linux_proc_migrate.conf
%config(noreplace) %_confdir/pmlogrewrite/linux_proc_net_snmp_migrate.conf
%config(noreplace) %_confdir/pmlogrewrite/linux_proc_net_tcp_migrate.conf
%config(noreplace) %_confdir/pmlogrewrite/linux_xfs_migrate.conf
%config(noreplace) %_confdir/pmlogrewrite/nfsclient_migrate.conf
%config(noreplace) %_confdir/pmlogrewrite/pmcd_migrate.conf
%config(noreplace) %_confdir/pmlogrewrite/proc_discrete_strings.conf
%config(noreplace) %_confdir/pmlogrewrite/proc_jiffies.conf
%config(noreplace) %_confdir/pmlogrewrite/proc_kernel_ulong.conf
%config(noreplace) %_confdir/pmlogrewrite/proc_kernel_ulong_migrate.conf
%config(noreplace) %_confdir/pmlogrewrite/proc_scheduler.conf
%config(noreplace) %_confdir/pmlogrewrite/rpm_migrate.conf
%dir %_confdir/proc
%config(noreplace) %_confdir/proc/samplehotproc.conf
%dir %_confdir/rabbitmq
%config(noreplace) %_confdir/rabbitmq/rabbitmq.conf
%dir %_confdir/redis
%config(noreplace) %_confdir/redis/redis.conf
%dir %_confdir/shping
%config(noreplace) %_confdir/shping/sample.conf
%dir %_confdir/simple
%config(noreplace) %_confdir/simple/simple.conf
%dir %_confdir/summary
%config(noreplace) %_confdir/summary/expr.pmie
# end todo
%_logconfdir/statsd
%_logconfdir/apache
%_logconfdir/cpu
%_logconfdir/disk
%_logconfdir/elasticsearch
%_logconfdir/filesystem
%_logconfdir/gfs2
%_logconfdir/kernel
%_logconfdir/kvm
%_logconfdir/libvirt
%_logconfdir/mailq
%_logconfdir/memcache
%_logconfdir/memory
%_logconfdir/mmv
%_logconfdir/netfilter
%_logconfdir/networking
%_logconfdir/nginx
%_logconfdir/oracle
%_logconfdir/platform
%_logconfdir/sgi
%_logconfdir/shping
%_logconfdir/sqlserver
%_logconfdir/storage
%_logconfdir/tools
%_logconfdir/v1.0
%_logconfdir/zimbra
%_logconfdir/mssql
%_logconfdir/netcheck
%_logconfdir/openvswitch
%_logconfdir/rabbitmq

%dir %_confdir
%dir %_pmdasdir
%dir %_logconfdir
%dir %_datadir/pcp
%dir %_sharedstatedir/pcp
%dir %_sharedstatedir/pcp/config
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_tempsdir
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_tempsdir/pmie
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_tempsdir/pmlogger
%dir %attr(0700,root,root) %_tempsdir/pmcd

%dir %_datadir/pcp/lib
%_datadir/pcp/lib/ReplacePmnsSubtree
%_datadir/pcp/lib/bashproc.sh
%_datadir/pcp/lib/lockpmns
%_datadir/pcp/lib/pmdaproc.sh
%_datadir/pcp/lib/utilproc.sh
%_datadir/pcp/lib/rc-proc.sh
%_datadir/pcp/lib/rc-proc.sh.minimal
%_datadir/pcp/lib/unlockpmns

%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir
%attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir/pmcd
%attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir/pmlogger
%attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir/pmie
%attr(0775,%_pseudouser_user,%_pseudouser_group) %_logsdir/pmproxy
%_sharedstatedir/pcp/pmns
%_initddir/pcp
%_initddir/pmcd
%_initddir/pmlogger
%_initddir/pmie
%_initddir/pmproxy
%_unitdir/pmcd.service
%_unitdir/pmlogger.service
%_unitdir/pmie.service
%_unitdir/pmfind.service
%_unitdir/pmfind.timer
%_unitdir/pmproxy.service
%_unitdir/pmlogger_check.service
%_unitdir/pmlogger_check.timer
%_unitdir/pmlogger_daily.service
%_unitdir/pmlogger_daily.timer
%_unitdir/pmlogger_daily-poll.service
%_unitdir/pmlogger_daily-poll.timer
%_unitdir/pmie_check.service
%_unitdir/pmie_check.timer
%_unitdir/pmie_daily.service
%_unitdir/pmie_daily.timer
%config(noreplace) %_sysconfdir/sysconfig/pmie_timers
%config(noreplace) %_sysconfdir/sysconfig/pmlogger_timers
%config(noreplace) %_sysconfdir/sasl2/pmcd.conf
%config(noreplace) %_sysconfdir/sysconfig/pmlogger
%config(noreplace) %_sysconfdir/sysconfig/pmproxy
%config(noreplace) %_sysconfdir/sysconfig/pmcd
%config(noreplace) %_sysconfdir/sysconfig/pmfind
%config %_sysconfdir/pcp.env
%dir %_confdir/labels
%dir %_confdir/pmcd
%config(noreplace) %_confdir/pmcd/pmcd.conf
%config(noreplace) %_confdir/pmcd/pmcd.options
%config(noreplace) %_confdir/pmcd/rc.local
%dir %_confdir/pmproxy
%config(noreplace) %_confdir/pmproxy/pmproxy.options
%config(noreplace) %_confdir/pmproxy/pmproxy.conf
%dir %_confdir/pmie
%dir %_confdir/pmie/control.d
%config(noreplace) %_confdir/pmie/control
%config(noreplace) %_confdir/pmie/control.d/local
%dir %_confdir/pmlogger
%dir %_confdir/pmlogger/control.d
%config(noreplace) %_confdir/pmlogger/control
%config(noreplace) %_confdir/pmlogger/control.d/local
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_confdir/nssdb
%dir %_confdir/discover
%config(noreplace) %_confdir/discover/pcp-kube-pods.conf

%ghost %dir %attr(0775,%_pseudouser_user,%_pseudouser_group) /run/pcp
%_sharedstatedir/pcp/config/pmafm
%exclude %_sharedstatedir/pcp/config/pmafm/pcp-gui
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_sharedstatedir/pcp/config/pmie
#%_sharedstatedir/pcp/config/pmie/*
%_sharedstatedir/pcp/config/pmieconf
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_sharedstatedir/pcp/config/pmlogger
%_sharedstatedir/pcp/config/pmlogger/*
%_sharedstatedir/pcp/config/pmlogrewrite
%dir %attr(0775,%_pseudouser_user,%_pseudouser_group) %_sharedstatedir/pcp/config/pmda

%dir %_datadir/bash-completion/
%dir %_datadir/bash-completion/completions
%_datadir/bash-completion/completions/*
%dir %_datadir/zsh/
%dir %_datadir/zsh/site-functions/
%_datadir/zsh/site-functions/_pcp

%_bindir/pmiostat
%_bindir/pmrep
%_libexecdir/pcp/bin/pcp-atop
%_libexecdir/pcp/bin/pcp-atopsar
%_libexecdir/pcp/bin/pcp-dmcache
%_libexecdir/pcp/bin/pcp-dstat
%_libexecdir/pcp/bin/pcp-free
%_libexecdir/pcp/bin/pcp-iostat
%_libexecdir/pcp/bin/pcp-ipcs
%_libexecdir/pcp/bin/pcp-lvmcache
%_libexecdir/pcp/bin/pcp-mpstat
%_libexecdir/pcp/bin/pcp-numastat
%_libexecdir/pcp/bin/pcp-pidstat
%_libexecdir/pcp/bin/pcp-shping
%_libexecdir/pcp/bin/pcp-tapestat
%_libexecdir/pcp/bin/pcp-uptime
%_libexecdir/pcp/bin/pcp-verify
%dir %_confdir/dstat
%dir %_confdir/pmrep
%config(noreplace) %_confdir/dstat/*
%config(noreplace) %_confdir/pmrep/*

%files zeroconf
%_libexecdir/pcp/bin/pmlogger_daily_report
%_unitdir/pmlogger_daily_report.service
%_unitdir/pmlogger_daily_report.timer
%_unitdir/pmlogger_daily_report-poll.service
%_unitdir/pmlogger_daily_report-poll.timer
%_sharedstatedir/pcp/config/pmlogconf/zeroconf

%files conf
%dir %_includedir/pcopilot
%dir %_localstatedir/lib/pcp
%dir %_localstatedir/lib/pcp/config
%_includedir/pcopilot/builddefs
%_includedir/pcopilot/buildrules
%config %_sysconfdir/pcp.conf
%dir %_sharedstatedir/pcp/config/derived
%config %_sharedstatedir/pcp/config/derived/*

%files -n libpcopilot
%_libdir/libpcopilot.so.3
%_libdir/libpcopilot_gui.so.2
%_libdir/libpcopilot_mmv.so.1
%_libdir/libpcopilot_pmda.so.3
%_libdir/libpcopilot_trace.so.2
%_libdir/libpcopilot_import.so.1
%_libdir/libpcopilot_web.so.1

%files -n libpcopilot-devel
%_libdir/libpcopilot.so
%_libdir/libpcopilot_gui.so
%_libdir/libpcopilot_mmv.so
%_libdir/libpcopilot_pmda.so
%_libdir/libpcopilot_trace.so
%_libdir/libpcopilot_import.so
%_libdir/libpcopilot_web.so
%_libdir/pkgconfig/libpcopilot.pc
%_libdir/pkgconfig/libpcopilot_pmda.pc
%_libdir/pkgconfig/libpcopilot_import.pc
%_includedir/pcopilot/*.h

%files devel
%_bindir/genpmda
%_bindir/pmclient
%_bindir/pmclient_fg
%_bindir/pmdbg
%_bindir/pmerr
%_datadir/pcp/examples
# PMDAs that ship src and are not for production use
# straight out-of-the-box, for devel or QA use only.
%_pmdasdir/simple
%_pmdasdir/sample
%_pmdasdir/trivial
%_pmdasdir/txmon

%files import-tools
%_bindir/sar2pcp
%_bindir/iostat2pcp
%_bindir/mrtg2pcp
%_bindir/ganglia2pcp
%_bindir/collectl2pcp

%files pmdas
%_pmdasdir/activemq
%dir %perl_vendorarch/PCP
%dir %perl_vendor_autolib/PCP
%dir %perl_vendorarch/Slurm
%perl_vendor_archlib/PCP/*
%exclude %perl_vendorarch/PCP/PMDA.pm
%exclude %perl_vendorarch/PCP/MMV.pm
%exclude %perl_vendorarch/PCP/server.pl
%exclude %perl_vendorarch/PCP/LogImport.pm
%perl_vendorarch/Slurm/*
%perl_vendorarch/Slurm.pm
%_pmdasdir/mssql
%_pmdasdir/netcheck
%_pmdasdir/bonding
%_pmdasdir/bind2
%_pmdasdir/dbping
%_pmdasdir/ds389log
%_pmdasdir/ds389
%_pmdasdir/elasticsearch
%_pmdasdir/gpfs
%_pmdasdir/gpsd
%_pmdasdir/docker
%_pmdasdir/lustre
%_pmdasdir/lustrecomm
%_pmdasdir/memcache
%_pmdasdir/named
%_pmdasdir/netfilter
%_pmdasdir/news
%_pmdasdir/nginx
%_pmdasdir/nfsclient
%_pmdasdir/oracle
%_pmdasdir/pdns
%_pmdasdir/postfix
%_pmdasdir/redis
%_pmdasdir/rsyslog
%_pmdasdir/samba
%_pmdasdir/slurm
%_pmdasdir/zimbra
%_pmdasdir/dm
%_pmdasdir/gluster
%_pmdasdir/zswap
%_pmdasdir/unbound
%_pmdasdir/mic
%_pmdasdir/haproxy
%_pmdasdir/lmsensors
%_pmdasdir/apache
%_pmdasdir/bash
%_pmdasdir/cifs
%_pmdasdir/cisco
%_pmdasdir/gfs2
%_pmdasdir/logger
%_pmdasdir/mailq
%_pmdasdir/mounts
%_pmdasdir/nvidia
%_pmdasdir/openvswitch
%_pmdasdir/rabbitmq
%_pmdasdir/roomtemp
%_pmdasdir/rpm
%_pmdasdir/sendmail
%_pmdasdir/shping
%_pmdasdir/smart
%_pmdasdir/summary
%_pmdasdir/systemd
%_pmdasdir/trace
%_pmdasdir/weblog

%files export-tools
%_bindir/pcp2graphite
%_bindir/pcp2json
%_bindir/pcp2spark
%_bindir/pcp2xml
%_bindir/pcp2zabbix
%_libdir/zabbix
%dir %_sysconfdir/zabbix
%dir %_sysconfdir/zabbix/zabbix_agentd.d/
%_sysconfdir/zabbix/zabbix_agentd.d/zbxpcp.conf

%files -n perl-PCP-common
%dir %perl_vendorlib/PCP
%dir %perl_vendorarch/PCP
%dir %perl_vendor_autolib/PCP

%files -n perl-PCP-PMDA
%dir %perl_vendor_autolib/PCP/PMDA
%perl_vendorarch/PCP/PMDA.pm
%perl_vendor_autolib/PCP/PMDA/PMDA.so

%files -n perl-PCP-MMV
%dir %perl_vendor_autolib/PCP/MMV
%perl_vendorarch/PCP/MMV.pm
%perl_vendorarch/PCP/server.pl
%perl_vendor_autolib/PCP/MMV/MMV.so

%files -n perl-PCP-LogImport
%dir %perl_vendor_autolib/PCP/LogImport
%perl_vendorarch/PCP/LogImport.pm
%perl_vendor_autolib/PCP/LogImport/LogImport.so

%files -n perl-PCP-LogSummary
%perl_vendorlib/PCP/LogSummary.pm
%perl_vendorlib/PCP/exceldemo.pl
%perl_vendorlib/PCP/extract.pl

%files -n python3-module-pcp
%python3_sitelibdir/*

%files doc
%_man1dir/*
%_man3dir/*
%_man5dir/*
%_defaultdocdir/pcp-doc/
%dir %_datadir/pcp/
%dir %_datadir/pcp/demos/
%dir %_datadir/pcp/demos/tutorials
%_datadir/pcp/demos/mmv
%_datadir/pcp/demos/pmclient
%_datadir/pcp/demos/procmemstat
%_datadir/pcp/demos/trace
%_datadir/pcp/demos/tutorials/*.tar.gz

%changelog
* Sat Sep 18 2021 Stanislav Levin <slev@altlinux.org> 5.2.0-alt2
- Fixed FTBFS.

* Fri Sep 18 2020 Igor Vlasenko <viy@altlinux.ru> 5.2.0-alt1
- NMU: fixed build by updating to 5.2.0
- (closes: #38912)
- TODO: properly divide newly packaged files to subpackages.

* Thu Apr 09 2020 Igor Vlasenko <viy@altlinux.ru> 5.0.2-alt1.1
- NMU: re-sign pkg - hack around alt bug 38332

* Wed Sep 18 2019 Mikhail Chernonog <snowmix@altlinux.org> 5.0.2-alt1
- Initial build for Sisyphus
