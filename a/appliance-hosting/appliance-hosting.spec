Name: appliance-hosting
Summary: virtual package for hosting setup
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

# Appliances
Requires: appliance-base-admin
Requires: appliance-web-mediawiki
Requires: appliance-hosting-pear
Requires: appliance-hosting-php5
Requires: appliance-hosting-mail

# Apache
Requires: mod_fastcgi
Requires: mod_security

# Other services
Requires: monit
Requires: nginx

# FTP service
Requires: vsftpd

# SQL-server
Requires: MySQL-server
Requires: mysqltuner

# syskeeper
Requires: perl-Git

# debugging utilites
Requires: net-tools

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

