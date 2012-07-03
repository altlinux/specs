Name: alterator-zabbix-node
Version: 1.0
Release: alt7

Summary: Deployment tool for a Zabbix node
License: GPL
Group: System/Configuration/Other
Packager: Paul Wolneykien <manowar@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar.gz

BuildPreReq: help2man alterator-service-functions alterator-php-functions

Requires: zabbix-phpfrontend-apache2 zabbix-phpfrontend-php5 zabbix-phpfrontend-engine apache2-mod_php5 zabbix-agent
Requires: alterator-service-functions >= 1.0-alt5
Requires: alterator-DBTYPE-functions

%description
This package contains utilities for configuration of Zabbix nodes based
on offline prepared configuration packages.

%package common
Summary: Library files for Zabbix node configuration programs
Group: System/Configuration/Other

%description common
Library files for Zabbix node configuration programs.

%package -n grow-zabbix-node
Summary: Tool for preparing a Zabbix node configuration package offline
Group: System/Configuration/Other
Requires: grow-zabbix-node-db
Requires: %name-common

%description -n grow-zabbix-node
Grows a complete configuration of a Zabbix node including database
contents and configuration files from an initial database dump and
a simple XML configuration file.

%package -n grow-zabbix-node-examples
Summary: Example base configuration files for grow-zabbix-node
Group: System/Configuration/Other

%description -n grow-zabbix-node-examples
Example base configuration files for grow-zabbix-node program.

%package -n grow-zabbix-node-mysql
Summary: Zabbix DB dump generation transformers for MySQL
Group: System/Configuration/Other
Requires: grow-zabbix-node
Provides: grow-zabbix-node-db

%description -n grow-zabbix-node-mysql
The set of XSLTs for "unfolding" of a rather simple XML configuration
file to the corresponding Zabbix DB dump of a DM node.

%package mysql
Summary: Deployment tool for a Zabbix node (Zabbix-MySQL dependencies)
Group: System/Configuration/Other
Requires: %name zabbix-server-mysql
Requires: alterator-mysql-functions
Provides: alterator-DBTYPE-functions
Provides: alterator-DBTYPE-functions(mysql)

%description mysql
Grows a complete configuration of a Zabbix node including database
contents and configuration files from an initial database dump and
a simple XML configuration file.

This package has dependencies for the MySQL verision of the Zabbix
server.

%package -n grow-zabbix-node-altlinux-dump-mysql
Summary: Base dump with ALT linux templates to grow from (MySQL version)
Group: System/Configuration/Other

%description -n grow-zabbix-node-altlinux-dump-mysql
Base dump with ALT linux templates to grow from.
This pacakge contains the MySQL version of the dump.

%package -n grow-zabbix-node-altlinux-chainmail-dump-mysql
Summary: Base dump with ALT linux and Chainmail templates to grow from (MySQL version)
Group: System/Configuration/Other

%description -n grow-zabbix-node-altlinux-chainmail-dump-mysql
Base dump with ALT linux and Chainmail templates to grow from.
This pacakge contains the MySQL version of the dump.

%package -n grow-zabbix-node-altlinux-templates
Summary: An XML bundle of ALT linux templates for a Zabbix node
Group: System/Configuration/Other

%description -n grow-zabbix-node-altlinux-templates
An XML bundle of ALT linux templates for a Zabbix node. The templates in
this package can be imported to a working Zabbix configuration using the
"Templates/Import template" operation.

%package -n grow-zabbix-node-chainmail-templates
Summary: An XML bundle of Chainmail templates for a Zabbix node
Group: System/Configuration/Other

%description -n grow-zabbix-node-chainmail-templates
An XML bundle of Chainmail templates for a Zabbix node. The templates in
this package can be imported to a working Zabbix configuration using the
"Templates/Import template" operation.

%prep
%setup

%build
%make_build

%install
%makeinstall

%files common
%_bindir/zabbix-sh-functions

%files
%_sbindir/alterator-zabbix-node-helper
%_mandir/man1/alterator-zabbix-node-helper.1.gz

%files -n grow-zabbix-node
%_bindir/grow-zabbix-node
%_mandir/man1/grow-zabbix-node.1.gz
%dir %_datadir/grow-zabbix-node
%dir %_datadir/grow-zabbix-node/xslt
%_datadir/grow-zabbix-node/xslt/extract-map-filenames.xslt
%_datadir/grow-zabbix-node/xslt/extract-metadata.xslt
%_datadir/grow-zabbix-node/xslt/includes.xslt
%_datadir/grow-zabbix-node/xslt/insert.xslt
%_datadir/grow-zabbix-node/xslt/reset.xslt
%_datadir/grow-zabbix-node/xslt/update-node.xslt
%dir %_datadir/grow-zabbix-node/refconf
%_datadir/grow-zabbix-node/refconf/zabbix.conf.php
%_datadir/grow-zabbix-node/refconf/zabbix_agentd.conf
%_datadir/grow-zabbix-node/refconf/zabbix_server.conf
%dir %_datadir/grow-zabbix-node
%dir %_datadir/grow-zabbix-node/dumps
%dir %_datadir/grow-zabbix-node/templates
%_datadir/grow-zabbix-node/template.xml

%files -n grow-zabbix-node-mysql
%_datadir/grow-zabbix-node/xslt/mysql-includes.xslt
%_datadir/grow-zabbix-node/xslt/mysql-insert.xslt
%_datadir/grow-zabbix-node/xslt/mysql-reset.xslt
%_datadir/grow-zabbix-node/xslt/mysql-update-node.xslt

%files -n grow-zabbix-node-examples
%dir %_docdir/grow-zabbix-node
%dir %_docdir/grow-zabbix-node/examples
%_docdir/grow-zabbix-node/examples/Moscow

%files mysql

%files -n grow-zabbix-node-altlinux-dump-mysql
%_datadir/grow-zabbix-node/dumps/zabbix-mysql-altlinux-dump.sql

%files -n grow-zabbix-node-altlinux-chainmail-dump-mysql
%_datadir/grow-zabbix-node/dumps/zabbix-mysql-altlinux-chainmail-dump.sql

%files -n grow-zabbix-node-altlinux-templates
%_datadir/grow-zabbix-node/templates/base-templates.xml

%files -n grow-zabbix-node-chainmail-templates
%_datadir/grow-zabbix-node/templates/chainmail-templates.xml

%changelog
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
