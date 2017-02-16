%define _name mactrack
Name: cacti-plugin-%_name
Version: 4.0
Release: alt0.1

%define cactiplugindir %_datadir/cacti/plugins

Summary: The Mac Track plugin for Cacti

License: GPLv2+
Group: Monitoring

URL: http://cactiusers.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: cacti >= 1.0.0
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
%setup -q
#%patch -p1

%build

%install
mkdir -p %buildroot%cactiplugindir/%_name

cp -a * %buildroot%cactiplugindir/%_name/
rm -rf %buildroot%cactiplugindir/%_name/docs

%files
%doc docs/*
%cactiplugindir/*

%changelog
* Fri Feb 17 2017 Alexey Shabalin <shaba@altlinux.ru> 4.0-alt0.1
- 4.0 for cacti-1.0.0

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 2.9-alt1
- 2.9

* Mon Mar 29 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- initial build
