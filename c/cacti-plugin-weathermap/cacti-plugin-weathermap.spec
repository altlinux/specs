# TODO
# change location of configs and output dirs

%define _name weathermap
Name: cacti-plugin-weathermap
Version: 0.98
Release: alt1

%define cactiplugindir %_datadir/cacti/plugins

Summary: Weathermap is a network visualisation tool.

License: GPLv2+
Group: Monitoring

URL: http://www.network-weathermap.com
Source0: %name-%version.tar
Source1: editor-config.php
Patch: %name-%version-%release.patch

Requires: cacti
BuildArch: noarch
BuildPreReq: rpm-macros-webserver-common unzip

# Automatically added by buildreq on Thu May 13 2010
BuildRequires: unzip

%description
Weathermap is a network visualisation tool,
to take data you already have and show you an overview of your network in map form.

%prep
%setup -q
%patch -p1

%build

%install -n %name-%version
mkdir -p %buildroot{%cactiplugindir/%_name,%_sysconfdir/cacti,%_localstatedir/cacti/plugins/%_name}

cp -a * %buildroot%cactiplugindir/%_name/
cp  %SOURCE1 %buildroot%_sysconfdir/cacti/weathermap-editor-config.php
rm -rf %buildroot%cactiplugindir/%_name/docs
rm -rf %buildroot%cactiplugindir/%_name/random-bits
rm -f %buildroot%cactiplugindir/%_name/{weathermap.conf,editor-config.php-dist}

mv -f %buildroot%cactiplugindir/%_name/{output,configs} %buildroot%_localstatedir/cacti/plugins/%_name/
pushd %buildroot%cactiplugindir/%_name/
    ln -s %_localstatedir/cacti/plugins/%_name/output output
    ln -s %_localstatedir/cacti/plugins/%_name/configs configs
popd

%files
%doc docs/* random-bits
%attr(640,root,%webserver_group) %config(noreplace) %_sysconfdir/cacti/weathermap-editor-config.php
%cactiplugindir/*
%attr(2775,root,%webserver_group) %dir %_localstatedir/cacti/plugins/%_name/configs
%_localstatedir/cacti/plugins/%_name/configs
%attr(2775,root,%webserver_group) %dir %_localstatedir/cacti/plugins/%_name/output
%_localstatedir/cacti/plugins/%_name/output


%changelog
* Thu Oct 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.98-alt1
- svn snapshot r520

* Tue May 11 2010 Alexey Shabalin <shaba@altlinux.ru> 0.97a-alt1
- initial build
