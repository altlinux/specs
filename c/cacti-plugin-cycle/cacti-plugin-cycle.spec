%define _name cycle
Name: cacti-plugin-%_name
Version: 2.3
Release: alt1

%define cactiplugindir %_datadir/cacti/plugins

Summary: Automatically cycle through cacti graphs

License: GPLv2+
Group: Monitoring

URL: http://cactiusers.org
Source0: %_name-v%version-1.tgz

Requires: cacti
BuildArch: noarch

%description
This plugin allows you to automatically view the Cacti graphs one by one
after a specified time delay.
Features:
    You can set cycle time delay.
    Can set permissions on who can view.
    Graph height and width can be specified.
    Graphs are not displayed if the user does not have access to them.
    Title of graph is displayed, font face, size and color can be changed.
    You can use the Prev/Next buttons to change graph.
    You can stop the rotation with the Stop button.
    The time until the next graph change is displayed under the title.
    It can use a custom graph list and only cycle through those.

%prep
%setup -q -n %_name

%build

%install -n %name-%version
mkdir -p %buildroot%cactiplugindir/%_name

cp -a * %buildroot%cactiplugindir/%_name/
rm -rf %buildroot%cactiplugindir/%_name/{LICENSE,README}
rm -f %buildroot%cactiplugindir/%_name/*.orig

%files
%doc LICENSE README
%cactiplugindir/*

%changelog
* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 2.3-alt1
- 2.3

* Wed Dec 21 2011 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2

* Thu Oct 06 2011 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2-alt1
- 1.2

* Mon Mar 29 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- initial build
