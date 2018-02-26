%define installdir %webserver_webappsdir/%name


Name: glpi
Version: 0.83.2
Release: alt1


Summary: IT and asset management software
License: GPLv2
Group: Networking/Other


URL: http://www.glpi-project.org
Packager: Pavel Zilke <zidex at altlinux dot org>
BuildArch: noarch

Source0: http://www.glpi-project.org/IMG/gz/%name-%version.tar.gz
Source1: fonts.tar.gz
Source2: apache.conf
Source3: apache2.conf
Source4: README.ALT
Patch: patch0.patch

Requires: webserver-common php-engine curl lynx
BuildRequires(pre): rpm-macros-webserver-common

%description
GLPI is the Information Resource-Manager with an additional Administration-
Interface.
You can use it to build up a database with an inventory for your company
(computer, software, printers...).
It has enhanced functions to make the daily life for the administrators easier,
like a job-tracking-system with mail-notification and methods to build a
database with basic information about your network-topology.


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
Requires: %name = %version-%release, php5-mysql, php5-ldap, php5-imap, php5-mbstring
%description php5
PHP5 dependencies for %name


%prep
%setup
%setup -T -D -a 1

%patch -p0

%build

%install
# install apache config
install -pD -m0644 %_sourcedir/apache.conf %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf
install -pD -m0644 %_sourcedir/apache2.conf %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf

# install glpi
mkdir -p %buildroot%installdir
cp -rp * %buildroot%installdir/

# install fonts
cp -rf %buildroot%installdir/fonts/ %buildroot%installdir/lib/ezpdf/
mv -f %buildroot%installdir/lib/ezpdf/fonts/php_Helvetica.font %buildroot%installdir/lib/ezpdf/fonts/php_Helvetica.afm
rm -rf %buildroot%installdir/fonts/

#install README.ALT
install -pD -m0644 %_sourcedir/README.ALT README.ALT

# remove .htaccess files - we're use apache config instead
find %buildroot%installdir -name .htaccess -delete

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
%dir %attr(2770,root,%webserver_group) %installdir/config
%config %attr(0664,root,%webserver_group) %installdir/config/based_config.php
%config %attr(0664,root,%webserver_group) %installdir/config/config.php
%config %attr(0664,root,%webserver_group) %installdir/config/define.php
%dir %attr(2770,root,%webserver_group) %installdir/files
%attr(2770,root,%webserver_group) %installdir/files/*
%installdir/ajax
%installdir/css
%installdir/front
%installdir/inc
%installdir/install
%installdir/lib
%installdir/locales
%installdir/pics
%installdir/plugins
%installdir/scripts
%installdir/*.php
%installdir/*.js
%installdir/COPYING.txt
%doc CHANGELOG.txt
%doc README.txt
%doc README.ALT


%files apache
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd/conf/addon-modules.d/%name.conf


%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf


%files php5


%changelog
* Sat Jun 09 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.2-alt1
- New version 0.83.2

* Thu Apr 19 2012 Pavel Zilke <zidex at altlinux dot org> 0.83.1-alt1
- New version 0.83.1

* Fri Apr 06 2012 Pavel Zilke <zidex at altlinux dot org> 0.83-alt1
- New version 0.83

* Mon Feb 13 2012 Pavel Zilke <zidex at altlinux dot org> 0.80.7-alt1
- New version 0.80.7

* Wed Jan 11 2012 Pavel Zilke <zidex at altlinux dot org> 0.80.61-alt1
- New version 0.80.61

* Tue Oct 25 2011 Pavel Zilke <zidex at altlinux dot org> 0.80.5-alt1
- New version 0.80.5

* Wed Sep 28 2011 Pavel Zilke <zidex at altlinux dot org> 0.80.4-alt1
- New version 0.80.4

* Thu Jul 07 2011 Pavel Zilke <zidex at altlinux dot org> 0.80.1-alt1
- New version 0.80.1 This version correct several bugs.

* Thu Jun 02 2011 Pavel Zilke <zidex at altlinux dot org> 0.80-alt1
- New version 0.80

* Sun Mar 13 2011 Pavel Zilke <zidex at altlinux dot org> 0.78.3-alt1
- New version 0.78.3

* Tue Jan 18 2011 Pavel Zilke <zidex at altlinux dot org> 0.78.2-alt1
- New version 0.78.2

* Tue Nov 23 2010 Pavel Zilke <zidex at altlinux dot org> 0.78.1-alt1
- New version 0.78.1

* Wed Oct 13 2010 Pavel Zilke <zidex at altlinux dot org> 0.78-alt1
- New version 0.78

* Fri Apr 02 2010 Pavel Zilke <zidex at altlinux dot org> 0.72.4-alt1
- New version 0.72.4

* Tue Nov 10 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.3-alt2
- remove Thumbs.db files

* Tue Nov 03 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.3-alt1
- New version 0.72.3

* Wed Oct 07 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.2-alt2
- spec bugfix

* Thu Sep 17 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.2-alt1
- New version 0.72.21
- fixed export to pdf
- fixed import from OCS Inventory NG

* Wed Aug 12 2009 Pavel Zilke <zidex at altlinux dot org> 0.72.1-alt1
- New version 0.72.1-alt1

* Thu Jun 04 2009 Pavel Zilke <zidex at altlinux dot org> 0.71.6-alt2
- Fixed README.ALT location

* Tue Jun 02 2009 Pavel Zilke <zidex at altlinux dot org> 0.71.6-alt1
- New version 0.71.6-alt1

* Mon Feb 02 2009 Pavel Zilke <zidex at altlinux dot org> 0.71.5-alt1
- First build for ALT Linux

