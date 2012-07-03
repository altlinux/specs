%define _name settings
Name: cacti-plugin-%_name
Version: 0.71
Release: alt1

%define cactiplugindir %_datadir/cacti/plugins

Summary: Plugin Settings for Mail and DNS

License: GPLv2+
Group: Monitoring

URL: http://cactiusers.org
Source0: %_name-v%version-1.tgz

Requires: cacti
BuildArch: noarch

%description
Plugin Settings for Mail and DNS

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
* Thu Oct 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.71-alt1
- 0.71

* Mon Mar 29 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt1
- initial build
