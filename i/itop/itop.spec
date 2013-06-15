%define installdir %webserver_webappsdir/%name


Name: itop
Version: 2.0.1
Release: alt1


Summary: IT Operations Portal
License: AGPLv3
Group: Networking/Other


URL: http://www.combodo.com/-Overview-.html
Packager: Pavel Zilke <zidex at altlinux dot org>
BuildArch: noarch

Source0: %name-%version.tar.gz
Source1: apache.conf
Source2: apache2.conf
Source3: README.ALT

Requires: webserver-common php-engine
BuildRequires(pre): rpm-macros-webserver-common

%description
IT Operations Portal: a complete open source, ITIL, web based service
management tool including a fully customizable CMDB, a helpdesk system
and a document management tool.
iTop also offers mass import tools and web services to integrate with your IT


%package apache
Summary: Apache 1.x web-server configuration for %name
Group: Networking/Other
Requires: %name = %version-%release, apache
%description apache
Apache 1.x web-server configuration for %name


%package apache2
Summary: Apache 2.x web-server configuration for %name
Group: Networking/Other
Requires: %name = %version-%release, apache2
%description apache2
Apache 2.x web-server configuration for %name


%package php5
Summary: PHP5 dependencies for %name
Group: Networking/Other
Requires: %name = %version-%release, php5-mysql, php5-ldap, php5-soap, php5-mcrypt
%description php5
PHP5 dependencies for %name


%prep
%setup
# %setup -T -D -a 1

%build

%install
# install apache config
install -pD -m0644 %_sourcedir/apache.conf %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf
install -pD -m0644 %_sourcedir/apache2.conf %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf

# install glpi
mkdir -p %buildroot%installdir
mkdir -p %buildroot%installdir/conf
mkdir -p %buildroot%installdir/data
mkdir -p %buildroot%installdir/env-production
mkdir -p %buildroot%installdir/log
cp -rp web/* %buildroot%installdir/

#install README.ALT
install -pD -m0644 %_sourcedir/README.ALT README.ALT


# remove files
find %buildroot%installdir -name remove.txt -delete
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete



%post apache
%_initdir/httpd condreload

%postun apache
%_initdir/httpd condreload


%post apache2
%_initdir/httpd2 condreload

%postun apache2
%_initdir/httpd2 condreload


%files
%dir %installdir
%dir %attr(2770,root,%webserver_group) %installdir/conf
%dir %attr(2770,root,%webserver_group) %installdir/data
%dir %attr(2770,root,%webserver_group) %installdir/env-production
%dir %attr(2770,root,%webserver_group) %installdir/log
%installdir/addons
%installdir/application
%installdir/core
%installdir/css
%installdir/datamodels
%installdir/dictionaries
%installdir/documentation
%installdir/extensions
%installdir/images
%installdir/js
%installdir/lib
%installdir/navigator
%installdir/pages
%installdir/portal
%installdir/setup
%installdir/synchro
%installdir/webservices
%installdir/*.php
%installdir/*.xml
%doc LICENSE
%doc README
%doc README.ALT


%files apache
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd/conf/addon-modules.d/%name.conf


%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf


%files php5


%changelog
* Sat Jun 15 2013 Pavel Zilke <zidex at altlinux dot org> 2.0.1-alt1
- Initial build for ALT Linux


