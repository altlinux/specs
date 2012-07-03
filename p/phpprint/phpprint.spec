# vim: set ft=spec: -*- rpm-spec -*-

Name: phpprint
Version: 0.2.1
Release: alt1

Summary: Printing via the web
License: %gpl2plus
Group: Networking/WWW

Url: https://sourceforge.net/projects/phpprint/
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar
Source50: %name.apache.conf
Source60: %name.apache2.conf
Source61: %name.apache2.start.extra.conf
Source62: %name.apache2.start.mods.conf

Requires: %webserver_webappsdir
Requires: /usr/bin/lpr

BuildRequires(pre): rpm-macros-apache
BuildRequires(pre): rpm-macros-apache2
BuildPreReq: rpm-build-webserver-common
BuildPreReq: rpm-build-licenses
BuildPreReq: %_datadir/rpm-build-rpm-eval/rpm-eval.sh

%description
With phpPrint you can print with your web-browser even if your
workstation has not got a local printer or cannot print over
the network by using LPRng/CUPS/Samba/etc.You need only a webserver
(e.g.apache) that can print by using lpr (e.g. local printer)

%package apache
Summary: Configuration of apache to phpPrint
Group: Networking/WWW
BuildArch: noarch

Requires: apache-base
Requires: %apache_modconfdir

%description apache
%summary

%package apache2
Summary: Configuration of apache2 to phpPrint
Group: Networking/WWW
BuildArch: noarch

Requires: apache2-base >= 2.2.17-alt3
Requires: %apache2_extra_available
Requires: %apache2_extra_enabled
Requires: %apache2_extra_start
Requires: %apache2_mods_start

%description apache2
%summary

%prep
%setup

%install
# Install phpPrint
install -d %buildroot%webserver_webappsdir/phpprint/
cp -a phpPrint/* %buildroot%webserver_webappsdir/phpprint/

# Install config for apache
install -m 644 -D %SOURCE50 %buildroot%apache_modconfdir/%name.conf

# Install config for apache2
install -m 644 -D %SOURCE60 %buildroot%apache2_extra_available/%name.conf
install -m 644 -D %SOURCE61 %buildroot%apache2_extra_start/100-%name.conf
install -m 644 -D %SOURCE62 %buildroot%apache2_mods_start/100-%name.conf

mkdir -p %buildroot%apache2_extra_enabled/
touch %buildroot%apache2_extra_enabled/%name.conf

# Substitute the real paths in configs
find %buildroot%_sysconfdir -type f -print0 \
	| xargs -r0i %_datadir/rpm-build-rpm-eval/rpm-eval.sh "{}"

%post apache
%post_apacheconf

%postun apache
%postun_apacheconf

%files
%doc CHANGELOG README README_DE
%webserver_webappsdir/%name

%files apache
%config(noreplace) %apache_modconfdir/%name.conf

%files apache2
%config(noreplace) %apache2_extra_available/%name.conf
%ghost %apache2_extra_enabled/%name.conf
%config(noreplace) %apache2_extra_start/100-%name.conf
%config(noreplace) %apache2_mods_start/100-%name.conf

%changelog
* Tue Dec 13 2011 Aleksey Avdeev <solo@altlinux.ru> 0.2.1-alt1
- Initial build for ALT Linux Sisyphus
