%define _name mactrack
Name: cacti-plugin-%_name
Version: 2.9
Release: alt1

%define cactiplugindir %_datadir/cacti/plugins

Summary: The Mac Track plugin for Cacti

License: GPLv2+
Group: Monitoring

URL: http://cactiusers.org
Source0: %_name-v%version-1.tgz

Requires: cacti
BuildArch: noarch

%description
This plugin scan's network devices and locates where a specific device is
located.  It's a good tool for finding virus' and stolen equipment.

Features:
    Scans Devices
    Finds Macs
    Associates Macs with their IP's
    Keeps a Nice Inventory of Port Counts
    Finds Stolen/Lost PC's
    Tells You When Someone is Connected Who Shouldn't be

%prep
%setup -q -n %_name

%build

%install -n %name-%version
mkdir -p %buildroot%cactiplugindir/%_name

cp -a * %buildroot%cactiplugindir/%_name/
rm -rf %buildroot%cactiplugindir/%_name/docs

%files
%doc docs/*
%cactiplugindir/*

%changelog
* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 2.9-alt1
- 2.9

* Mon Mar 29 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- initial build
