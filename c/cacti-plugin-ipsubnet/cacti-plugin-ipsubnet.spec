%define _name ipsubnet
Name: cacti-plugin-%_name
Version: 0.4f
Release: alt1

%define cactiplugindir %_datadir/cacti/plugins

Summary: IP subnet calculator for IPv4 and IPv6

License: GPLv2+
Group: Monitoring

URL: http://cactiusers.org
Source0: %_name%version.zip

Requires: cacti
BuildArch: noarch
BuildRequires: unzip

%description
IP subnet calculator for IPv4 and IPv6

%prep
%setup -q -n %_name

# fix dir perms
find . -type d | xargs chmod 755
# fix file perms
find . -type f | xargs chmod 644

%build

%install -n %name-%version
mkdir -p %buildroot%cactiplugindir/%_name

cp -a * %buildroot%cactiplugindir/%_name/
rm -rf %buildroot%cactiplugindir/%_name/{LICENSE,README}

%files
%doc LICENSE Manual.txt
%cactiplugindir/*

%changelog
* Thu Oct 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4f-alt1
- initial build
