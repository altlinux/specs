%global _unpackaged_files_terminate_build 1

Name:       alerta-webui
Version:    8.7.1
Release:    alt1
Summary:    Alerta monitoring web interface
License:    Apache-2.0
Group:      Monitoring
URL:        https://github.com/alerta/alerta-webui

Source0:    %name-%version.tar
Source1:    dist.tar
Source2:    alerta-webui.nginx.conf
Source3:    alerta-webui.config.json

BuildArch:  noarch

BuildRequires: rpm-macros-webserver-common

# /var/www/webapps
Requires: webserver-common

%description
Alerta is a monitoring system that provides a web interface for
managing alerts. This package contains the compiled static web UI
(Vue.js) for the Alerta monitoring system.

%package nginx
Summary:    Nginx configuration for %name
Group:      System/Servers
Requires:   %name = %EVR
Requires:   nginx

%description nginx
Nginx site configuration for Alerta web UI.

%prep
%setup -a 1

%install
# extract static data
mkdir -p %buildroot%webserver_webappsdir/%name
cp -r dist/* %buildroot%webserver_webappsdir/%name/

# remove example config
rm -f %buildroot%webserver_webappsdir/%name/config.json.example

# user-editable UI config
install -Dpm0644 %SOURCE3 %buildroot%_sysconfdir/%name/config.json
ln -s %_sysconfdir/%name/config.json \
	%buildroot%webserver_webappsdir/%name/config.json

# nginx config
install -Dpm0644 %SOURCE2 \
	%buildroot%_sysconfdir/nginx/sites-available.d/%name.conf

%files
%doc README.md LICENSE
%webserver_webappsdir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.json

%files nginx
%config(noreplace) %_sysconfdir/nginx/sites-available.d/%name.conf

%changelog
* Wed Sep 30 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 8.7.1-alt1
- Initial build for ALT.

