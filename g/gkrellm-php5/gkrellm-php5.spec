%define oname php-gkrellm
Name: gkrellm-php5
Version: 0.3
Release: alt1

Summary: A set of PHP 5 classes for talking to the gkrellmd monitoring daemon

License: GPL
Group: System/Servers
Url: http://www.openidenabled.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://downloads.sourceforge.net/php-gkrellm/%oname-%version.tar.gz

BuildPreReq: rpm-macros-webserver-common

%description
php-gkrellm is a set of PHP 5 classes for talking to the gkrellmd monitoring daemon.
The information gkrellmd provides includes, but is not limited to, the following:
* CPU usage
* Memory usage
* Network interfaces and connections
* Sensors
* Disk usage
* Mounted filesystems
...and more
gkrellmd may also be extended with plugins.

%prep
%setup -q -n %oname-%version

%build

%install
mkdir -p %buildroot%webserver_manualaddonsdir/%oname/
cp -ar %oname/* %buildroot%webserver_manualaddonsdir/%oname/

%files
%doc CHANGES README examples/
%webserver_manualaddonsdir/%oname/

%changelog
* Sat Dec 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus
