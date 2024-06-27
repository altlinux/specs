Name: alterator-zabbix-node
Version: 1.3.3
Release: alt3

Summary: Deployment tool for a Zabbix node
License: GPLv2+
Group: System/Configuration/Other

Source: %name-%version.tar.gz

BuildPreReq: help2man alterator-service-functions alterator-php-functions
BuildPreReq: alterator >= 5.0
BuildRequires: alterator-fbi

BuildRequires: guile22-devel

Requires:  zabbix-phpfrontend-php5 zabbix-phpfrontend-engine zabbix-agent
Requires: alterator-service-functions >= 2.0.0-alt1
Requires: alterator-DBTYPE-functions

%description
This package contains utilities for configuration of Zabbix nodes based
on offline prepared configuration packages.

%package common
Summary: Library files for Zabbix node configuration programs
Group: System/Configuration/Other
BuildArch: noarch

%description common
Library files for Zabbix node configuration programs.

%package -n zabbix-mysql-data-altlinux
Summary: Base dump with ALT linux templates to grow from (MySQL version)
Group: System/Configuration/Other
BuildArch: noarch

%description -n zabbix-mysql-data-altlinux
Base dump with ALT linux templates to grow from.
This pacakge contains the MySQL version of the dump.


%package -n alterator-zabbix-agent
Summary: Alterator module for the Zabbix agent configuration
Group: System/Configuration/Other
Requires: zabbix-agent
Requires: alterator >= 5.0
Requires: alterator-l10n >= 2.9-alt21

%description -n alterator-zabbix-agent
Alterator module for the Zabbix agent configuration

%package -n zabbix-chainmail-parameters
Summary: IVK ChainMail configuration files for Zabbix agent
Group: System/Configuration/Other
Requires: zabbix-agent
Requires: alterator-l10n >= 2.9-alt21
BuildArch: noarch

%description -n zabbix-chainmail-parameters
IVK ChainMail configuration files for Zabbix agent

%prep
%setup

%build
%make_build

%install
%makeinstall

%files common
%_bindir/zabbix-sh-functions

%files -n zabbix-mysql-data-altlinux
%_datadir/zabbix-altlinux/data.sql

%files -n alterator-zabbix-agent
%_sysconfdir/zabbix/zabbix_agentd.conf.d/Ident.conf
%_alterator_datadir/applications/zabbix-agent.desktop
%_alterator_datadir/ui/zabbix-agent
%_alterator_backend3dir/zabbix-agent
%_alterator_libdir/ui/*

%files -n zabbix-chainmail-parameters
%_sysconfdir/zabbix/zabbix_agentd.conf.d/Chainmail.conf

%changelog
* Thu Jun 27 2024 Michael Shigorin <mike@altlinux.org> 1.3.3-alt3
- Clarify License:.

* Thu Jun 27 2024 Michael Shigorin <mike@altlinux.org> 1.3.3-alt2
- Use guile22 on e2k too.

* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt1.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Mon Jun 05 2017 Mikhail Efremov <sem@altlinux.org> 1.3.3-alt1
- Update spec for guile22.
- Don't allow some symbols in hostname.

* Mon May 25 2015 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- simplified creation of zabbix node
- fixed zabbix_agent restart, when button "apply" was used in WEB-interface
- add default items system.version (which alaways returns uname) and MetadataItem=system.version for zabbix_agent
- always set ServerActive in alterator-zabbix-agent with Server value
- add zabbix-chainmail-parameters subpackage with default zabbix agent config for IVK Chainmail

* Tue Sep 16 2014 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1
- Fix alterator menu category.

* Thu Mar 21 2013 Paul Wolneykien <manowar@altlinux.org> 1.3-alt1
- Modify the package for the new version of
  alterator-service-functions.

* Thu Sep 06 2012 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt4
- Restart zabbix-agentd while applying the configuration.

* Wed Sep 05 2012 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt3
- Update the 'ids' table after new data insert.

* Fri Aug 31 2012 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt2
- Use X-Alterator-Monitoring-Control category.

* Wed Aug 29 2012 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt1
- Alterator module:
 + Manual control of the "Listen IP" option.
 + Control the "EnableRemoteCommands" parameter.
 + Fix/improve the UI layout.

* Thu Dec 16 2010 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt4
- Fix system hostname mode in agent module.

* Wed Dec 15 2010 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt3
- Fix/update of the Jupiter templates.

* Wed Dec 15 2010 Aleksey Avdeev <solo@altlinux.ru> 1.1-alt2
- Update the agent configuration module.

* Thu Dec 09 2010 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Add the agent configuration module.

* Fri Nov 19 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt7
- Fix the path of the traceroute command in the base configurations.

* Thu Nov 18 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt6
- Add support for firewall rules adjustment.

* Tue Nov 16 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt5
- Optionally controls Apache2 PHP module configuration.
- Optionally controls the database service configuration.
- Move MySQL functions to the alterator-mysql-functions.
- Later-binding of database access functions.
- Add XML template bundles and dumps (MySQL).

* Sun Oct 31 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Add support for template (initial, empty) configurations.

* Sat Oct 30 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Use source base name as the database name by default.
- Restart Zabbix-related services after the successful reconfiguration.
- Add zabbix-agent to the set of requisites.

* Tue Oct 26 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Use attributes/tags to specify the name of a host group.
- Add option for character set to use loading a DB dump (MySQL).

* Sat Oct 23 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial version for Sisyphus.
