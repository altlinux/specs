#based on atomicorp and open suse specs
%define _unpackaged_files_terminate_build 1
# split installation to several paths to fulfil FHS demands
%define ossec_default_dir %_localstatedir/ossec
%define ossec_sysconf_dir %_localstatedir/ossec
%define ossec_runtime_dir %_localstatedir/ossec
%define ossec_localstate_dir %_localstatedir/ossec
%define ossec_bin_dir %_libdir/ossec
%define asl 1
%def_with systemd
%def_with sysvinit

Name: ossec-hids

Version: 3.6.0
Release: alt2

Summary: OSSEC is a full platform to monitor and control your systems
License: GPLv2
Group: System/Servers
Url: https://www.ossec.net/
#Git: https://github.com/ossec/ossec-hids

Source0: %name-%version.tar
Source1: %name-authd-alt.init
Source2: %name-alt.init
Source3: %name.service
Source4: %name.logrotate

Patch1: ossec-hids-2.9.3-alt-fhs-compliance.patch
Patch2: ossec-hids-2.9.3-alt-email-conf.patch
Patch3: ossec-hids-3.6.0-fix-build-with-gcc-10.patch

BuildRequires(pre): rpm-build-perl

# Automatically added by buildreq on Tue May 08 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcom_err-devel libkrb5-devel libpq-devel libsasl2-3 libssl-devel python-base
BuildRequires: libGeoIP-devel libmysqlclient-devel postgresql-devel
BuildRequires: liblua5-devel zlib-devel libjson-c-devel
BuildRequires: libpcre2-devel libevent-devel libssl-devel

ExclusiveOS: linux
%brp_strip_none %ossec_bin_dir/bin/* %ossec_bin_dir/ossec-agent/bin/*

# Packages notes
# agent - read local files (syslog, snort, etc) and forward
# hybrid - standalone + agent
# server -  above + notifications + remote agents
# local(not implemented) - do everything server does, but not recieve messages
%package agent
Summary: %summary
License: GPLv2
Group: Networking/Remote access
Requires: %name = %version-%release
Requires(post):   /sbin/chkconfig
Requires(preun):  /sbin/chkconfig /sbin/service
Requires(postun): /sbin/service
Conflicts: %name-server

%package hybrid
Summary: %summary
License: GPLv2
Group: Networking/Remote access
Requires: %name = %version-%release
Requires(post):   /sbin/chkconfig
Requires(preun):  /sbin/chkconfig /sbin/service
Requires(postun): /sbin/service
Conflicts: %name-agent

%package mysql
Summary: %summary
License: GPLv2
Group: Networking/Remote access
Requires: %name-server = %version-%release
Conflicts: %name-postgres

%package postgres
Summary: %summary
License: GPLv2
Group: Networking/Remote access
Requires: %name-server = %version-%release
Conflicts: %name-mysql

%package server
Summary: %summary
License: GPLv2
Group: Development/Kernel
Provides: %name-server = %version-%release ossec-server = %version-%release
Requires: %name = %version-%release
Requires(pre):    /usr/sbin/groupadd /usr/sbin/useradd
Requires(post):   /sbin/chkconfig
Requires(preun):  /sbin/chkconfig /sbin/service
Requires(postun): /sbin/service
Conflicts: %name-agent


%define common_description \
OSSEC is a full platform to monitor and control your systems. It mixes together all the aspects of HIDS (host-based intrusion detection), log monitoring and SIM/SIEM together in a simple, powerful and open source solution. Visit our website for the latest information. ossec.github.io

%description
%common_description

%description agent
%common_description

%description hybrid
%common_description

%description mysql
%common_description

%description postgres
%common_description

%description server
%common_description

%prep
%setup

%patch1 -p1	
%patch2 -p1
%patch3 -p1

# fix for FHS
sed -i 's|/var/ossec|%ossec_default_dir|' src/LOCATION
sed -i 's|/var/ossec|%ossec_default_dir|' src/headers/defs.h
sed -i 's|/var/ossec|%ossec_default_dir|' src/Makefile
sed -i 's|/var/ossec|%ossec_default_dir|' doc/nmap.txt
sed -i 's|/var/ossec|%ossec_default_dir|' contrib/ossec-testing/runtests.py
sed -i 's|/var/ossec|%ossec_default_dir|' contrib/add_localfile.sh
sed -i 's|/var/ossec|\/usr|' src/systemd/server/*.service

# Prepare for docs
rm -rf contrib/specs/
rm -rf contrib/debian-packages/
#chmod -x contrib/*

# TODO: edit src/Makefile to use system liblua5.3, zlib, libjson-c
#rm -rf src/external/

%build
CFLAGS="$RPM_OPT_FLAGS -fpic -fPIE -Wformat -Wformat-security -fstack-protector-all --param ssp-buffer-size=4 -D_FORTIFY_SOURCE=2"
%ifnarch %e2k
# unsupported as of lcc 1.23.20
CFLAGS="$CFLAGS -Wstack-protector"
%endif

LDFLAGS="-fPIE -pie -Wl,-z,relro"
SH_LDFLAGS="-fPIE -pie -Wl,-z,relro"
export CFLAGS LDFLAGS SH_LDFLAGS

export LUA_ENABLE=yes

# Agent
pushd ./src
mkdir -p clients/
%make_build TARGET=agent V=1
mv manage_agents clients/manage_agent
mv ossec-logcollector  clients/client-logcollector
mv ossec-syscheckd  clients/client-syscheckd
mv ossec-agentd  clients/
mv ossec-execd  clients/
mv agent-auth  clients/

# Hybrid
%make_build clean
mkdir hybrid/
%make_build TARGET=agent PREFIX=%ossec_default_dir/ossec-agent V=1
mv ossec-agentd hybrid/
mv ossec-execd hybrid/
mv ossec-logcollector hybrid/
mv ossec-syscheckd hybrid/
cp clients/agent-auth hybrid/
mv manage_agents hybrid/manage_agent

# Rebuild for server
%make_build clean
%make_build DATABASE=pgsql MAXAGENTS=16384 USE_GEOIP=1 TARGET=server V=1
mkdir postgres
cp ossec-dbd postgres/

# Rebuild for mysql
%make_build clean
%make_build DATABASE=mysql MAXAGENTS=16384 USE_GEOIP=1 TARGET=server V=1

popd

# Generate the ossec-init.conf template
echo "DIRECTORY=\"%ossec_default_dir\"" >  ossec-init.conf
echo "VERSION=\"%version\""                 >> ossec-init.conf
echo "DATE=\"`date`\""                        >> ossec-init.conf

%install
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir
# leave following dir for DB schema files
mkdir -p %buildroot%_datadir/ossec/contrib
mkdir -p %buildroot%ossec_runtime_dir/run
mkdir -p %buildroot%ossec_localstate_dir/log
mkdir -p %buildroot%ossec_bin_dir/active-response/bin
mkdir -p %buildroot%ossec_bin_dir/agentless
mkdir -p %buildroot%ossec_bin_dir/bin
mkdir -p %buildroot%ossec_localstate_dir/{stats,tmp}

mkdir -p %buildroot%ossec_sysconf_dir/rules
mkdir -p %buildroot%ossec_sysconf_dir/rules/translated/pure_ftpd
mkdir -p %buildroot%ossec_default_dir/lua/
mkdir -p %buildroot%ossec_default_dir/lua/{native,compiled}
mkdir -p %buildroot%ossec_localstate_dir/logs/{archives,alerts,firewall}
mkdir -p %buildroot%ossec_localstate_dir/queue/{alerts,agentless,agent-info,diff,fts,ossec,rids,rootcheck,syscheck}
mkdir -p %buildroot%ossec_runtime_dir/var/run
mkdir -p %buildroot%ossec_sysconf_dir/etc/shared
mkdir -p %buildroot%ossec_sysconf_dir/etc/templates
mkdir -p %buildroot%ossec_sysconf_dir/etc/mysql
mkdir -p %buildroot%ossec_sysconf_dir/etc/decoders.d
mkdir -p %buildroot%ossec_sysconf_dir/etc/rules.d
mkdir -p %buildroot%ossec_localstate_dir/stats
mkdir -p %buildroot%ossec_localstate_dir/tmp
mkdir -p %buildroot%ossec_default_dir/.ssh

mkdir -p %buildroot%ossec_bin_dir/ossec-agent/active-response/bin
mkdir -p %buildroot%ossec_bin_dir/ossec-agent/agentless
mkdir -p %buildroot%ossec_bin_dir/ossec-agent/bin
mkdir -p %buildroot%ossec_sysconf_dir/ossec-agent/etc/shared
mkdir -p %buildroot%ossec_default_dir/ossec-agent/lua/{native,compiled}
mkdir -p %buildroot%ossec_localstate_dir/ossec-agent/queue/{alerts,diff,ossec,rids,syscheck}
mkdir -p %buildroot%ossec_localstate_dir/ossec-agent/tmp
mkdir -p %buildroot%ossec_default_dir/ossec-agent/.ssh

#move variable contents to /var/lib/ossec
mkdir -p %buildroot%ossec_localstate_dir/logs
mkdir -p %buildroot%ossec_localstate_dir/ossec-agent/logs
mkdir -p %buildroot%ossec_runtime_dir/ossec-agent/var/run
mkdir -p %buildroot%_bindir 

install -pD -m 0644 etc/*conf %buildroot%ossec_sysconf_dir/etc/shared/


# active response
install -pD -m 0755 active-response/*.sh %buildroot%ossec_bin_dir/ossec-agent/active-response/bin
install -pD -m 0550 src/agentlessd/scripts/* %buildroot%ossec_bin_dir/ossec-agent/agentless
# bin
install -pD -m 0644 src/hybrid/agent-auth %buildroot%ossec_bin_dir/ossec-agent/bin
install -pD -m 0550 src/hybrid/manage_agent %buildroot%ossec_bin_dir/ossec-agent/bin/
install -pD -m 0550 src/hybrid/ossec-agentd %buildroot%ossec_bin_dir/ossec-agent/bin/
install -pD -m 0550 src/init/ossec-client.sh %buildroot%ossec_bin_dir/ossec-agent/bin/ossec-control
install -pD -m 0550 src/hybrid/ossec-execd %buildroot%ossec_bin_dir/ossec-agent/bin
install -pD -m 0550 src/hybrid/ossec-logcollector %buildroot%ossec_bin_dir/ossec-agent/bin
install -pD -m 0550 src/external/lua/src/ossec-lua %buildroot%ossec_bin_dir/ossec-agent/bin/
install -pD -m 0550 src/external/lua/src/ossec-luac %buildroot%ossec_bin_dir/ossec-agent/bin/
install -pD -m 0550 src/hybrid/ossec-syscheckd %buildroot%ossec_bin_dir/ossec-agent/bin
# etc
install -pD -m 0644 etc/internal_options.conf %buildroot%ossec_sysconf_dir/ossec-agent/etc
install -m 0644 etc/ossec.conf %buildroot%ossec_sysconf_dir/ossec-agent/etc/ossec.conf
install -pD -m 0644 src/rootcheck/db/*.txt %buildroot%ossec_sysconf_dir/ossec-agent/etc/shared

%if_with systemd
mkdir -p %buildroot%_unitdir
install -Dp -m0644 %SOURCE3 %buildroot%_unitdir/ossec-hids.service
install -Dp -m0644 src/systemd/server/* %buildroot%_unitdir 
%endif

%if_with sysvinit
install -m 0755 %SOURCE2 %buildroot%_initdir/%name
install -m 0755 %SOURCE1 %buildroot%_initdir/%name-authd
%endif

install -pD -m 0600 ossec-init.conf %buildroot%_sysconfdir
install -pD -m 0644 etc/ossec.conf %buildroot%ossec_sysconf_dir/etc/ossec.conf.sample
install -pD -m 0644 etc/ossec-{agent,server}.conf %buildroot%ossec_sysconf_dir/etc
install -pD -m 0644 etc/*.xml %buildroot%ossec_sysconf_dir/etc
install -pD -m 0644 etc/internal_options* %buildroot%ossec_sysconf_dir/etc
install -pD -m 0644 etc/rules/*xml %buildroot%ossec_sysconf_dir/rules
install -pD -m 0644 etc/rules/translated/pure_ftpd/* %buildroot%ossec_sysconf_dir/rules/translated/pure_ftpd
install -pD -m 0644 etc/templates/config/* %buildroot%ossec_sysconf_dir/etc/templates/

pushd src
# Client
install -pD -m 0550 clients/agent-auth %buildroot%ossec_bin_dir/bin
install -pD -m 0550 clients/client-logcollector %buildroot%ossec_bin_dir/bin
install -pD -m 0550 clients/client-syscheckd %buildroot%ossec_bin_dir/bin
install -pD -m 0550 clients/manage_agent %buildroot%ossec_bin_dir/bin
install -pD -m 0550 clients/ossec-agentd %buildroot%ossec_bin_dir/bin/

ln -snf  %ossec_bin_dir/bin/agent-auth %buildroot%_bindir/agent-auth
ln -snf  %ossec_bin_dir/bin/client-logcollector %buildroot%_bindir/client-logcollector
ln -snf  %ossec_bin_dir/bin/client-syscheckd %buildroot%_bindir/client-syscheckd
ln -snf  %ossec_bin_dir/bin/manage_agent %buildroot%_bindir/manage_agent
ln -snf  %ossec_bin_dir/bin/ossec-agentd %buildroot%_bindir/ossec-agentd

# Server components
OS_BINARIES="ossec-logcollector ossec-syscheckd ossec-execd manage_agents \
ossec-agentlessd ossec-analysisd ossec-monitord ossec-reportd \
ossec-maild ossec-remoted ossec-logtest ossec-csyslogd \
ossec-authd ossec-makelists verify-agent-conf clear_stats \
list_agents ossec-regex syscheck_update agent_control \
syscheck_control rootcheck_control"
for i in $OS_BINARIES
do
    install -pD -m 0550 $i %buildroot%ossec_bin_dir/bin/
#link %%bindir to ossec binaries for systemd unit convenience
    ln -snf  %ossec_bin_dir/bin/$i         %buildroot%_bindir/$i
done
ln -sf %ossec_bin_dir/bin/ossec-server.sh %buildroot%_bindir/ossec-control

install -pD -m 0550 external/lua/src/ossec-lua %buildroot%ossec_bin_dir/bin/
install -pD -m 0550 external/lua/src/ossec-luac %buildroot%ossec_bin_dir/bin/
install -pD -m 0550 ossec-dbd %buildroot%ossec_bin_dir/bin/ossec-dbd
install -pD -m 0550 postgres/ossec-dbd %buildroot%ossec_bin_dir/bin/ossec-pgsql-dbd

popd

install -pD -m 0755 active-response/*.sh %buildroot%ossec_bin_dir/active-response/bin
install -pD -m 0644 src/rootcheck/db/*.txt %buildroot%ossec_sysconf_dir/etc/shared
install -pD -m 0644 src/os_dbd/mysql.schema %buildroot%_datadir/ossec/contrib
install -pD -m 0644 src/os_dbd/postgresql.schema %buildroot%_datadir/ossec/contrib
install -pD -m 0550 src/init/ossec-{client,server}.sh %buildroot%ossec_bin_dir/bin
install -pD -m 0550 src/agentlessd/scripts/* %buildroot%ossec_bin_dir/agentless

## Install contrib files
#%%add_findreq_skiplist %%buildroot%%_docdir/contrib/*.pl
#pushd contrib
#/bin/install -m 0750 {config2xml,*.pl,*.sh}   %%buildroot%%_datadir/ossec/contrib
#/bin/install -m 0640 *.{conf,pm,sql,txt}      %%buildroot%%_datadir/ossec/contrib
#popd

# create the faux ossec.conf, %%ghost'ed files must exist in the buildroot
touch %buildroot%ossec_sysconf_dir/etc/ossec.conf

%if %asl
mkdir -p %buildroot/etc/logrotate.d
install -m 0644 %SOURCE4 %buildroot/etc/logrotate.d/%name
#file required by agent daemons
touch %buildroot%ossec_sysconf_dir/etc/shared/agent.conf
%endif

# TODO: Consider setting up correctly and running upstream tests
#       Doesn't operate now - lack dependencies?
%check
pushd src
#%%make_build test 
popd

%pre
if ! id -g ossec > /dev/null 2>&1; then
  groupadd -r ossec
fi
if ! id -u ossec > /dev/null 2>&1; then
  useradd -g ossec -G ossec       \
	-d %ossec_default_dir \
	-r -s /sbin/nologin ossec
fi
if ! id -u ossecr > /dev/null 2>&1; then
  useradd -g ossec -G ossec       \
	-d %ossec_default_dir \
	-r -s /sbin/nologin ossecr
fi

%pre server
if ! id -u ossecm > /dev/null 2>&1; then
  useradd -g ossec -G ossec       \
	-d %ossec_default_dir \
	-r -s /sbin/nologin ossecm
fi
if ! id -u ossece > /dev/null 2>&1; then
  useradd -g ossec -G ossec       \
	-d %ossec_default_dir \
	-r -s /sbin/nologin ossece
fi

%post agent
if [ $1 = 1 ]; then
	%post_service %name
fi

echo "TYPE=\"agent\"" >> %_sysconfdir/ossec-init.conf

if [ ! -f  %ossec_sysconf_dir/etc/ossec.conf ]; then
  ln -sf ossec-agent.conf %ossec_sysconf_dir/etc/ossec.conf
fi

ln -sf %ossec_bin_dir/bin/ossec-client.sh %_bindir/ossec-control

# daemon trickery
ln -sf %ossec_bin_dir/bin/client-logcollector  %_bindir/ossec-logcollector
ln -sf %ossec_bin_dir/bin/client-syscheckd  %_bindir/ossec-syscheckd

touch %ossec_localstate_dir/logs/ossec.log
chown ossec:ossec %ossec_localstate_dir/logs/ossec.log
chmod 0664 %ossec_localstate_dir/logs/ossec.log

/sbin/service ossec-hids restart || :

%define sslkey %ossec_sysconf_dir/etc/sslmanager.key
%define sslcert %ossec_sysconf_dir/etc/sslmanager.cert

%post server
if [ $1 = 1 ]; then
	%post_service %name
fi

echo "TYPE=\"server\"" >> %_sysconfdir/ossec-init.conf

if [ ! -f %ossec_sysconf_dir/etc/ossec.conf ]; then
  ln -sf ossec-server.conf %ossec_sysconf_dir/etc/ossec.conf
fi

ln -sf %ossec_bin_dir/bin/ossec-server.sh %_bindir/ossec-control

touch %ossec_localstate_dir/logs/ossec.log
chown ossec:ossec %ossec_localstate_dir/logs/ossec.log

if [ ! -f %sslkey ] ; then
	/usr/bin/openssl genrsa -rand /proc/apm:/proc/cpuinfo:/proc/dma:/proc/filesystems:/proc/interrupts:/proc/ioports:/proc/pci:/proc/rtc:/proc/uptime 2048 > %sslkey 2> /dev/null || :
fi

if [ ! -f %sslcert ] ; then
cat << EOF | /usr/bin/openssl req -new -key %sslkey \
         -x509 -days 1095 -set_serial $RANDOM \
         -out %sslcert 2>/dev/null || :
--
State
City
corp
OrganizationalUnit
${FQDN}
root@${FQDN}
EOF
fi

/sbin/service ossec-hids restart || :

%post hybrid
if [ ! -f %ossec_sysconf_dir/ossec-agent/etc/ossec.conf ]; then
  ln -sf ossec-agent.conf %ossec_sysconf_dir/ossec-agent/etc/ossec.conf
fi
 ln -sf %ossec_sysconf_dir/etc/client.keys %ossec_sysconf_dir/ossec-agent/etc/client.keys

        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ ! -f %ossec_sysconf_dir/ossec-agent/etc/localtime ]; then
	if [ -f %_sysconfdir/localtime ]; then
		cp -fpL %_sysconfdir/localtime %ossec_sysconf_dir/ossec-agent/etc
	fi
fi

%post postgres
ln -sf %ossec_bin_dir/bin/ossec-pgsql-dbd %ossec_bin_dir/bin/ossec-dbd || :

%preun agent
if [ $1 = 0 ]; then
  %preun_service %name

  rm -f %ossec_sysconf_dir/etc/localtime
  rm -f %ossec_sysconf_dir/etc/ossec.conf
  rm -f %_bindir/bin/ossec-control
  rm -f %_bindir/bin/ossec-logcollector
  rm -f %_bindir/bin/ossec-syscheckd
fi

%preun server
if [ $1 = 0 ]; then
  %preun_service %name

  rm -f %ossec_sysconf_dir/etc/localtime
  rm -f %ossec_sysconf_dir/etc/ossec.conf
  rm -f %_bindir/ossec-control
fi

%triggerin -- glibc
[ -r %_sysconfdir/localtime ] && cp -fpL %_sysconfdir/localtime %ossec_sysconf_dir/etc
if [ -f %ossec_sysconf_dir/ossec-agent/etc ]; then
	cp -fpL %_sysconfdir/localtime %ossec_sysconf_dir/ossec-agent/etc
fi

%files
%doc BUGS CONFIG CONTRIBUTORS INSTALL LICENSE README.md CHANGELOG.md doc contrib
%attr(550,root,ossec) %dir %ossec_default_dir
%attr(550,root,ossec) %dir %ossec_bin_dir/active-response
%attr(550,root,ossec) %ossec_bin_dir/active-response/bin
%attr(550,root,ossec) %ossec_bin_dir/agentless
%attr(550,root,ossec) %dir %ossec_bin_dir/bin
%attr(550,root,ossec) %dir %ossec_sysconf_dir/etc
%attr(770,ossec,ossec) %dir %ossec_sysconf_dir/etc/shared
%attr(750,ossec,ossec) %dir %ossec_sysconf_dir/etc/templates
%attr(640,ossec,ossec) %ossec_sysconf_dir/etc/templates/*
%attr(550,root,ossec) %dir %ossec_localstate_dir/tmp
%attr(750,ossec,ossec) %dir %ossec_localstate_dir/logs
%attr(550,root,root) %dir %ossec_default_dir/lua
%attr(550,root,ossec) %dir %ossec_localstate_dir/queue
%attr(770,ossec,ossec) %dir %ossec_localstate_dir/queue/ossec
%attr(750,ossec,ossec) %dir %ossec_localstate_dir/queue/diff
%attr(550,root,ossec) %dir %ossec_runtime_dir/var
%attr(770,root,ossec) %dir %ossec_runtime_dir/var/run
%attr(550,root,root) %ossec_bin_dir/bin/ossec-lua*
%if %asl
%config(noreplace) %_sysconfdir/logrotate.d/%name
%endif

%files agent
%attr(600,root,root) %verify(not md5 size mtime) %_sysconfdir/ossec-init.conf
%_initdir/ossec-hids
%config(noreplace) %ossec_sysconf_dir/etc/ossec-agent.conf
%config(noreplace) %ossec_sysconf_dir/etc/internal_options*
%attr(640,ossec,ossec) %config(noreplace) %ossec_sysconf_dir/etc/shared/*conf
%ossec_sysconf_dir/ossec-agent/etc/shared/*txt
%ossec_sysconf_dir/etc/*.sample
%ossec_bin_dir/bin/ossec-client.sh
%ossec_bin_dir/bin/ossec-agentd
%ossec_bin_dir/bin/client-logcollector
%ossec_bin_dir/bin/client-syscheckd
%ossec_bin_dir/bin/manage_agent
%ossec_bin_dir/bin/ossec-execd
%ossec_bin_dir/bin/agent-auth

%ossec_bin_dir/bin/ossec-analysisd

%_bindir/agent-auth
%_bindir/client-logcollector
%_bindir/client-syscheckd
%_bindir/manage_agent
%_bindir/ossec-agentd
%_bindir/ossec-execd
%_bindir/ossec-analysisd

%attr(550,root,ossec) %dir %ossec_localstate_dir/queue/alerts
#ex775
%attr(775,root,ossec) %dir %ossec_localstate_dir/queue/rids
%attr(550,root,ossec) %dir %ossec_localstate_dir/queue/syscheck

%files hybrid
%config(noreplace) %ossec_sysconf_dir/ossec-agent/etc/ossec.conf
%config(noreplace) %ossec_sysconf_dir/ossec-agent/etc/internal_options.conf
%ossec_bin_dir/ossec-agent/active-response/bin/
%ossec_bin_dir/ossec-agent/agentless/*
%ossec_bin_dir/ossec-agent/bin/*
%ossec_sysconf_dir/ossec-agent/etc/shared/*txt
%attr(550,root,root) %dir %ossec_default_dir/ossec-agent/lua/*
%attr(750,ossec,ossec) %dir %ossec_localstate_dir/ossec-agent/logs
%attr(550,root,ossec) %dir %ossec_localstate_dir/ossec-agent/queue/alerts
%attr(750,ossec,ossec) %dir %ossec_localstate_dir/ossec-agent/queue/diff
%attr(750,ossec,ossec) %dir %ossec_localstate_dir/ossec-agent/queue/ossec
%attr(775,root,ossec) %dir %ossec_localstate_dir/ossec-agent/queue/rids
%attr(550,root,ossec) %dir %ossec_localstate_dir/ossec-agent/queue/syscheck
%attr(1750,root,ossec) %dir %ossec_localstate_dir/ossec-agent/tmp
%attr(550,root,ossec) %dir %ossec_runtime_dir/ossec-agent/var
%attr(770,root,ossec) %dir %ossec_runtime_dir/ossec-agent/var/run

%files server
%attr(600,root,root) %verify(not md5 size mtime) %_sysconfdir/ossec-init.conf
%_initdir/ossec-hids
%_initdir/ossec-hids-authd
%ghost %config(missingok,noreplace) %ossec_sysconf_dir/etc/ossec.conf
%config(noreplace) %ossec_sysconf_dir/etc/ossec-server.conf
%config(noreplace) %ossec_sysconf_dir/etc/internal_options*
%config(noreplace) %ossec_sysconf_dir/etc/shared/*
%dir %_datadir/ossec/contrib
%exclude %_datadir/ossec/contrib/postgresql.schema
%exclude %_datadir/ossec/contrib/mysql.schema
%_datadir/ossec/*
%ossec_sysconf_dir/etc/rules.d/
%ossec_sysconf_dir/etc/decoders.d/
# Legacy
%ossec_sysconf_dir/etc/decoder.xml
%ossec_sysconf_dir/etc/*.sample
%exclude %ossec_bin_dir/bin/ossec-lua*
%exclude %ossec_bin_dir/bin/ossec-dbd
%exclude %ossec_bin_dir/bin/ossec-pgsql-dbd
%exclude %ossec_bin_dir/bin/ossec-client.sh
%exclude %ossec_bin_dir/bin/manage_agent
%exclude %ossec_bin_dir/bin/client-logcollector
%exclude %ossec_bin_dir/bin/client-syscheckd
%ossec_bin_dir/bin/*

%exclude %_bindir/agent-auth
%exclude %_bindir/client-logcollector
%exclude %_bindir/client-syscheckd
%exclude %_bindir/manage_agent
%exclude %_bindir/ossec-agentd
%_bindir/*

%_unitdir/*.service
%_unitdir/*.target
%_initdir/*

%attr(750,ossec,ossec) %dir %ossec_localstate_dir/logs/archives
%attr(770,ossec,ossec) %dir %ossec_localstate_dir/logs/alerts
%attr(750,ossec,ossec) %dir %ossec_localstate_dir/logs/firewall
%attr(755,ossecr,ossec) %dir %ossec_localstate_dir/queue/agent-info
%attr(755,ossec,ossec) %dir %ossec_localstate_dir/queue/agentless
%attr(770,ossec,ossec) %dir %ossec_localstate_dir/queue/alerts
%attr(750,ossec,ossec) %dir %ossec_localstate_dir/queue/fts
%attr(755,ossecr,ossec) %dir %ossec_localstate_dir/queue/rids
%attr(750,ossec,ossec) %dir %ossec_localstate_dir/queue/rootcheck
%attr(750,ossec,ossec) %dir %ossec_localstate_dir/queue/syscheck
%attr(550,root,ossec) %dir %ossec_sysconf_dir/rules
%config %ossec_sysconf_dir/rules/*
%attr(750,ossec,ossec) %dir %ossec_localstate_dir/stats
%attr(550,root,ossec) %dir %ossec_bin_dir/agentless

%files mysql
%ossec_bin_dir/bin/ossec-dbd
%_datadir/ossec/contrib/mysql.schema

%files postgres
%ossec_bin_dir/bin/ossec-pgsql-dbd
%_datadir/ossec/contrib/postgresql.schema

%changelog
* Sat May 20 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 3.6.0-alt2
- Fixed testinstall

* Sat Apr 17 2021 Egor Ignatov <egori@altlinux.org> 3.6.0-alt1
- new version
- fix build with gcc10

* Mon Sep 30 2019 Michael Shigorin <mike@altlinux.org> 3.1.0-alt2
- E2K: avoid lcc-unsupported option

* Tue Nov 27 2018 Nikolai Kostrigin <nickel@altlinux.org> 3.1.0-alt1
- new version
- add missing email setup patch
- remove ubt

* Fri May 04 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.9.3-alt1
- initial release

