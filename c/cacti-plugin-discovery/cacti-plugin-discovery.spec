%define _name discovery
Name: cacti-plugin-%_name
Version: 1.5
Release: alt1

%define cactiplugindir %_datadir/cacti/plugins

Summary: View Hosts on a Subnet that are not monitored by Cacti

License: GPLv2+
Group: Monitoring

URL: http://cactiusers.org
Source0: %_name-v%version-1.tgz

Requires: cacti
BuildArch: noarch

%description
This plugin adds the ability to auto-discover devices on a subnet 
that are not monitored by Cacti and and tells you if they are SNMP enabled.
Features:
        Host Filter
        Displays Host Status
        Displays DNS Name
        Displays SNMP Status and Information
        Link to add device to Cacti.
        Allows Discovery Templates to allow auto-creating graphs and adding the device to Cacti

%prep
%setup -q -n %_name

%build

%install -n %name-%version
mkdir -p %buildroot%cactiplugindir/%_name

cp -a * %buildroot%cactiplugindir/%_name/
rm -rf %buildroot%cactiplugindir/%_name/{LICENSE,README}

%files
%doc LICENSE README
%cactiplugindir/*

%changelog
* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.5-alt1
- 1.5

* Thu Oct 06 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3-alt1
- 1.3

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- 1.1

* Mon Mar 29 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.5-alt1
- initial build
