%define _name ssl
Name: cacti-plugin-%_name
Version: 0.1
Release: alt1

%define cactiplugindir %_datadir/cacti/plugins

Summary: SSL Redirector for Cacti

License: GPLv2+
Group: Monitoring

URL: http://cactiusers.org
Source0: http://mirror.cactiusers.org/downloads/plugins/%_name-%version.tar.gz

Requires: cacti
BuildArch: noarch

%description
This plugin will force your users to access Cacti in SSL mode.

%prep
%setup -q -n %_name

%build

%install -n %name-%version
mkdir -p %buildroot%cactiplugindir/%_name
cp -a * %buildroot%cactiplugindir/%_name/

%files
%cactiplugindir/*

%changelog
* Mon Mar 29 2010 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build
