Name:    glpi-agent
Version: 1.4
Release: alt2

Summary: GLPI Agent
License: GPL-2.0
Group:   Other
Url:     https://github.com/glpi-project/glpi-agent

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

%add_perl_lib_path %buildroot%_datadir/%name/lib
%set_findreq_skiplist %_bindir/%name
%filter_from_provides /perl(setup.pm)/d
%filter_from_requires /perl(setup.pm)/d

BuildRequires: perl-Cpanel-JSON-XS
BuildRequires: perl-Data-UUID
BuildRequires: perl-DateTime
BuildRequires: perl-File-Copy-Recursive
BuildRequires: perl-HTTP-Proxy
BuildRequires: perl-HTTP-Server-Simple
BuildRequires: perl-HTTP-Server-Simple-Authen
BuildRequires: perl-IO-Capture
BuildRequires: perl-IO-Socket-SSL
BuildRequires: perl-IPC-Run
BuildRequires: perl-LWP-Protocol-https
BuildRequires: perl-Memoize
BuildRequires: perl-Module-Install
BuildRequires: perl-Net-IP
BuildRequires: perl-Net-SNMP
BuildRequires: perl-Parallel-ForkManager
BuildRequires: perl-Parse-EDID
BuildRequires: perl-Test-Compile
BuildRequires: perl-Test-Deep
BuildRequires: perl-Test-Exception
BuildRequires: perl-Test-MockModule
BuildRequires: perl-Test-MockObject
BuildRequires: perl-Test-NoWarnings
BuildRequires: perl-Text-Template
BuildRequires: perl-UNIVERSAL-require
BuildRequires: perl-XML-TreePP
BuildRequires: perl-XML-XPath

%description
The GLPI Agent is a generic management agent. It can perform a certain number
of tasks, according to its own execution plan, or on behalf of a GLPI server
acting as a control point.

%prep
%setup
# Remove files only used under win32
rm -rf lib/GLPI/Agent/Daemon

sed \
    -e "s/logger = .*/logger = syslog/" \
    -e "s/logfacility = .*/logfacility = LOG_DAEMON/" \
    -e 's|#include "conf\.d/"|include "conf\.d/"|' \
    -i etc/agent.cfg

cat <<EOF | tee %name.conf
#
# GLPI Agent Configuration File
# used by hourly cron job to override the %name.cfg setup.
#
# /!\
# USING THIS FILE TO OVERRIDE SERVICE OPTIONS NO MORE SUPPORTED!
# See %_unitdir/%name.service notice
#
# Add tools directory if needed (tw_cli, hpacucli, ipssend, ...)
PATH=/sbin:/bin:/usr/sbin:/usr/bin
# Global options (debug for verbose log)
OPTIONS="--debug "

# Mode, change to "cron" to activate
# - none (default on install) no activity
# - cron (inventory only) use the cron.hourly
AGENTMODE[0]=none
# FusionInventory Inventory or GLPI server URI
# AGENTSERVER[0]=your.server.name
# AGENTSERVER[0]=http://your.server.name/
# AGENTSERVER[0]=http://your.glpiserveur.name/glpi/plugins/fusioninventory/
# corresponds with --local=%_localstatedir/%name
# AGENTSERVER[0]=local
# Wait before inventory (for cron mode)
AGENTPAUSE[0]=120
# Administrative TAG (optional, must be filed before first inventory)
AGENTTAG[0]=
EOF

%build
perl Makefile.PL \
     PREFIX=%_prefix \
     SYSCONFDIR=%_sysconfdir/%name \
     LOCALSTATEDIR=%_localstatedir/%name \
     VERSION=%version

%install
%makeinstall_std
install -Dm0644 %name.conf %buildroot%_sysconfdir/sysconfig/%name
install -Dm0755 contrib/unix/glpi-agent.cron %buildroot%_sysconfdir/cron.hourly/%name
install -Dm0644 contrib/unix/glpi-agent.service %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_sysconfdir/%name/conf.d
find %buildroot -name .packlist -delete

%preun
%preun_service %name

%post
%post_service %name

%files
%doc README.md THANKS
%config(noreplace) %_sysconfdir/%name/agent.cfg
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %_sysconfdir/%name/conf.d
%config(noreplace) %_sysconfdir/%name/inventory-server-plugin.cfg
%config(noreplace) %_sysconfdir/%name/proxy-server-plugin.cfg
%config(noreplace) %_sysconfdir/%name/proxy2-server-plugin.cfg
%config(noreplace) %_sysconfdir/%name/server-test-plugin.cfg
%config(noreplace) %_sysconfdir/%name/ssl-server-plugin.cfg
%config(noreplace) %_sysconfdir/%name/toolbox-plugin.cfg
%_bindir/*
%_datadir/%name
%_sysconfdir/cron.hourly/%name
%_unitdir/%name.service
%_man1dir/*.1*
%dir %_localstatedir/%name

%changelog
* Mon Feb 06 2023 Andrey Cherepanov <cas@altlinux.org> 1.4-alt2
- Removed autorequirements of perl(setup.pm).

* Thu Jan 19 2023 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- Initial build for Sisyphus.
