%define installdir %webserver_webappsdir/%name

Name: itop
Version: 2.6.3
Release: alt1

Summary: IT Operations Portal
License: AGPLv3
Group: Networking/Other

URL: http://www.combodo.com/-Overview-.html
Packager: Pavel Zilke <zidex at altlinux dot org>
BuildArch: noarch

Source0: %name-%version.tar.gz
Source1: apache2.conf
Source2: README.ALT

Requires: webserver-common php-engine graphviz
BuildRequires(pre): rpm-macros-webserver-common

%description
IT Operations Portal: a complete open source, ITIL, web based service
management tool including a fully customizable CMDB, a helpdesk system
and a document management tool.
iTop also offers mass import tools and web services to integrate with your IT


%package apache2
Summary: Apache 2.x web-server configuration for %name
Group: Networking/Other
Requires: %name = %version-%release, apache2
%description apache2
Apache 2.x web-server configuration for %name


%package php7
Summary: PHP7 dependencies for %name
Group: Networking/Other
Requires: %name = %version-%release, php7-mysqli, php7-ldap, php7-soap, php7-mcrypt, php7-xmlreader, php7-gd2, php7-zip
                                        
%description php7
PHP5 dependencies for %name


%prep
%setup
# %setup -T -D -a 1

%build

%install
# install apache config
install -pD -m0644 %_sourcedir/apache2.conf %buildroot%_sysconfdir/httpd2/conf/sites-available/%name.conf

# install itop
mkdir -p %buildroot%installdir
mkdir -p %buildroot%installdir/conf
mkdir -p %buildroot%installdir/data
mkdir -p %buildroot%installdir/env-production
mkdir -p %buildroot%installdir/env-production-build
mkdir -p %buildroot%installdir/log
cp -rp web/* %buildroot%installdir/
rm -f %buildroot%installdir/setup/phpinfo.php

#install README.ALT
install -pD -m0644 %_sourcedir/README.ALT README.ALT


# remove files
rm -f %buildroot%installdir/lib/silex/vendor/silex/silex/doc/conf.py
find %buildroot%installdir -name remove.txt -delete
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete


%post apache2
if [ "$1" = "1" ]; then
  a2ensite %name
  %_initdir/httpd2 condreload
fi

%preun apache2
if [ "$1" = "0" ]; then
  a2dissite %name
fi

%postun apache2
if [ "$1" = "0" ]; then
  %_initdir/httpd2 condreload
fi


%files
%dir %installdir
%dir %attr(2770,root,%webserver_group) %installdir/conf
%dir %attr(2770,root,%webserver_group) %installdir/data
%dir %attr(2770,root,%webserver_group) %installdir/env-production
%dir %attr(2770,root,%webserver_group) %installdir/env-production-build
%dir %attr(2770,root,%webserver_group) %installdir/log
%installdir/addons
%installdir/application
%installdir/core
%installdir/css
%installdir/data
%installdir/datamodels
%installdir/dictionaries
%installdir/documentation
%installdir/extensions
%installdir/images
%installdir/js
%installdir/lib
%installdir/log
%installdir/pages
%installdir/portal
%installdir/setup
%installdir/sources
%installdir/synchro
%installdir/webservices
%installdir/*.php
%installdir/*.xml
%installdir/*.config
%doc LICENSE    
%doc README
%doc README.ALT


%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%files php7


%changelog
* Thu Apr 09 2020 Pavel Zilke <zidex at altlinux dot org> 2.6.3-alt1
- New version 2.6.3
- Security fixes:
+ CVE-2019-19821 : Improper Privilege Management
- Removed Python requirements

* Tue Feb 18 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.6.1-alt2
- py2 -> py3

* Tue Apr 16 2019 Pavel Zilke <zidex at altlinux dot org> 2.6.1-alt1
- New version 2.6.1

* Wed Mar 06 2019 Pavel Zilke <zidex at altlinux dot org> 2.6.0-alt1
- New version 2.6.0
- Added PHP7 support
- Deleted PHP5 support
- Deleted Apache1 support

* Sat Dec 29 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2
- NMU: build w/o apache1

* Sat Jan 10 2015 Pavel Zilke <zidex at altlinux dot org> 2.1.0-alt1
- New version 2.1.0

* Wed Dec 18 2013 Pavel Zilke <zidex at altlinux dot org> 2.0.2-alt1
- New version 2.0.2

* Sat Jun 15 2013 Pavel Zilke <zidex at altlinux dot org> 2.0.1-alt1
- Initial build for ALT Linux


