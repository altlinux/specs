Name: cacti
Version: 0.8.8a
Release: alt1

%define cactidir %_datadir/%name
%define cacticonfdir %_sysconfdir/%name
%define username cacti

Summary: The complete RRDTool-based graphing solution.
Summary(ru_RU.UTF8): Полнофункциональная оболочка для RRDTool.

License: GPL
Group: Monitoring

URL: http://www.cacti.net/
Source0: http://www.cacti.net/downloads/%name-%version.tar.gz
Source1: %name.cfg.php
Source2: %name-readme.alt
Source3: %name.logrotate
Source5: %name-rrdpath.sql
Source7: %name-apache.conf
Source8: %name-lighttpd.conf

# official patches

# unofficial patches
Patch11: %name-alt-config.patch
Patch12: %name-alt-system-adodb.patch
Patch13: %name-ioerror.patch
Patch14: %name-webroot.patch
Patch15: %name-linux_memory.patch
Patch16: %name-log-verbosity.patch
Patch17: %name-ss_disk-array-indices.patch
Patch19: %name-host_name-url.patch
Patch20: %name-fix-php_scripts.patch

Requires: %name-config = %version-%release webserver webserver-common rrd-utils net-snmp net-snmp-utils
BuildPreReq: rpm-macros-webserver-common
BuildArch: noarch

%description
Cacti is a complete frontend to RRDTool. It stores all of the necessary 
information to create graphs and populate them with data in a MySQL database. 
The frontend is completely PHP driven. Along with being able to maintain graphs, 
data sources, and round robin archives in a database, Cacti also handles the data 
gathering. There is SNMP support for those used to creating traffic graphs with 
MRTG.

%description -l ru_RU.UTF8
Cacti - это полнофункциональная оболочка для RRDTool. Программа хранит всю
необходимую информацию для создания и наполнения графиков в базе MySQL.
Программа полностью написана на PHP. Вместе с возможностью управления
графиками, источниками данных и архивами round robin Cacti также занимается
сбором данных.

%package config-php
License: GPL
Group: Monitoring
Summary: Virtual package for php's depend.
Requires: php-snmp php-sockets php-mysql
Conflicts: %name-config-php5
Provides: %name-config = %version-%release

%description config-php
Virtual package for php's depend.

%package config-php5
License: GPL
Group: Monitoring
Summary: Virtual package for php's depend.
Requires: php5-snmp php5-sockets php5-mysql php5-gd2 php5-adodb

Conflicts: %name-config-php
Provides: %name-config = %version-%release

%description config-php5
Virtual package for php5's depend.

%package setup
Summary: Cacti setup package
Group: Monitoring
BuildArch: noarch
Requires: %name = %version-%release
Requires: %name-doc = %version-%release

%description setup
Install this package to configure initial Cacti installation. You
should uninstall this package when you're done, as it considered
insecure to keep the setup files in place.

%description -l ru_RU.UTF8 setup
Установите этот пакет для первоначальной инициализации Cacti.
После завершения настройки Cacti Вы должны удалить этот пакет, что бы обеспечить
безопасную работу приложения.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation for %name

%prep
%setup -q -n %name-%version

# add official patches

# sed -i /\$config\ =/a\$url_path\ \=\ \"\/cacti\/\"\; include/global.php

%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch19 -p1
%patch20 -p1


mkdir -p sql
mv *.sql sql
# you should run this sql if your database contains path to %{_datadir}...
cp %SOURCE5 sql

%build

#Add sql to one script
#cat cacti.sql cacti-plugin-arch/pa.sql > cacti_all.sql
#mv -f cacti_all.sql cacti.sql

rm -rf cacti-plugin-arch
rm -rf lib/adodb
rm -f log/.htaccess
rm -f cli/.htaccess
rm -f rra/.placeholder
rm -f log/.placeholder

chmod a+rx scripts/*

chmod a+rx cli/*

# make sure cacti runs out of the box
sed -e "s,new_install,%version," -i sql/cacti.sql

%install -n %name-%version
mkdir -p %buildroot{%_sbindir,%_sysconfdir/cron.d,%cacticonfdir,%cactidir/plugins,%_localstatedir/%name/rra,%_logdir/%name}

cp -a *.php README LICENSE %buildroot%cactidir
cp -a cli images include install lib resource scripts sql plugins %buildroot%cactidir
mv -f %buildroot{%cactidir/poller.php,%_sbindir/cacti-poller}
chmod 755 %buildroot%_sbindir/cacti-poller
cp %SOURCE1 %buildroot%cacticonfdir/config.php
touch %buildroot%_logdir/%name/%name.log

cp %SOURCE2 docs/README_ALT.txt
cp %SOURCE7 docs/
cp %SOURCE8 docs/
ln -sf %_docdir/%name-doc-%version %buildroot%cactidir/docs


# install cron
cat << EOF > %buildroot%_sysconfdir/cron.d/cacti
MAILTO=root

*/5 * * * * cacti umask 022; exec /usr/sbin/cacti-poller > /dev/null
EOF

# logrotate
install -D -m 0644 %SOURCE3 %buildroot%_sysconfdir/logrotate.d/cacti

%pre
%_sbindir/useradd -M -d %cactidir -r %username -G %webserver_group > /dev/null 2>&1 ||:
if LANG=C %_bindir/id %username 2>/dev/null | \
grep -qv "groups=[^[:space:]]*(%webserver_group)"; then
echo 'Warning: User %username was not included in the group %webserver_group!'
%_bindir/gpasswd -a %username %webserver_group 
echo '     Added user %username to group %webserver_group.'
fi

%post
%post_service crond

%triggerpostun -- %name < 0.8.7e-alt1
# Migration from previous version
if [ $2 -gt 0 ]; then
echo "Fixing permissions and location rrd,log files after previous package:"
mv -f %_var/www/html/%name/log/* %_logdir/%name/
mv -f %_var/www/html/%name/rra/* %_localstatedir/%name/rra/
chown -v root:%webserver_group  %_logdir/%name/* %_localstatedir/%name/*
chmod -v 660 %_logdir/%name/* %_localstatedir/%name/*
fi

%files
%doc docs/README_ALT.txt docs/CHANGELOG docs/README docs/CONTRIB docs/*.conf
%config(noreplace) %_sysconfdir/cron.d/cacti
%_sbindir/cacti-poller
%dir %attr(750,root,%webserver_group) %cacticonfdir
%attr(640,root,%webserver_group) %config(noreplace) %cacticonfdir/config.php
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %cactidir
%cactidir/resource
%cactidir/sql
%cactidir/lib
%cactidir/include
%cactidir/images
%cactidir/plugins
%cactidir/*.php

%dir %cactidir/cli
%attr(755,root,root) %cactidir/cli/*

%dir %cactidir/scripts
%attr(755,root,root) %cactidir/scripts/*

%attr(755,root,%webserver_group) %dir %_localstatedir/%name
%attr(2775,root,%webserver_group) %dir %_localstatedir/%name/rra
%attr(730,root,%webserver_group) %dir %_logdir/%name
%attr(660,root,%webserver_group) %ghost %_logdir/%name/cacti.log

%exclude %cactidir/install
%exclude %cactidir/docs

##files config-php

%files config-php5

%files setup
%cactidir/install

%files doc
%doc docs/html docs/txt
%cactidir/docs

%changelog
* Wed May 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.8a-alt1
- 0.8.8a

* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Tue Jan 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.7i-alt2
- add official patch settings_checkbox.patch

* Wed Dec 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7i-alt1
- 0.8.7i

* Wed Oct 05 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7h-alt1
- 0.8.7h

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7g-alt3
- add official patches:
  + Fix issue with multi selection data source deactivation
  + Graph List View Searching
  + Repair various interface display issues
  + Fix LDAP authenication with group restrictions enabled
  + Update script server to properly process command line arguments that are quoted
  + Fixes issue with Cacti ping library
  + Fixes issue with 1 minute polling with 1 minute rra

* Tue Jul 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7g-alt2
- fix url_path in config.php

* Mon Jul 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7g-alt1
- 0.8.7g

* Tue Jun 01 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7f-alt1
- 0.8.7f:
  + SQL injection and shell escaping issues reported by Bonsai Information Security
  + Cross-site scripting issues reported by VUPEN Security
  + MOPS-2010-023: Cacti Graph Viewer SQL Injection Vulnerability
  + Fixed various issues with exporting and importing templates that contain special characters
  + Fixed condition that could cause RRDtool to segfault
  + Many fixes to html generation and presentation

* Tue May 11 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7e-alt4
- Adding official patch to fix sql vulnerability

* Mon Apr 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7e-alt3
- fix permition /var/lib/cacti

* Tue Mar 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7e-alt2
- add cacti/plugins/index.php

* Wed Mar 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7e-alt1
- 0.8.7e
- poller:
 + in sbin
 + no hide of errors in cron
 + use exec to avoid /bin/sh in process table
- cacti in /usr/share
- log in /var/log/cacti
- triggerpostun for migration
- add cacti user to _webserver group

* Wed Dec 10 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7b-alt4
- Fix simlink /var/www/html/cacti/docs -> /usr/share/doc/cacti-doc-0.8.7b (Thanks at@)
- Remove package cacti-config-php

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7b-alt3
- Add new subpackage %name-doc
- Convert spec to UTF8
- Add official patche reset_each_patch

* Thu Mar 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7b-alt2
- Add official patches
- Fix url_path in include/global.php
- Join sql scripts to one
- Add link to docs
- Add README_ALT.txt
- Add version-release to Requires: cacti-config
- Add Conflicts: cacti-config-php to cacti-config-php5
- Add Conflicts: cacti-config-php5 to cacti-config-php

* Tue Feb 19 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7b-alt1
- New version
- Update cacti-plugin-arch

* Fri Nov 30 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7a-alt1
- New version
- Remove all patches (in upstream)

* Fri Apr 13 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.6j-alt1
- Add official patches:
  + %name-%version-thumbnail_graphs_not_working.patch
  + %name-%version-graph_debug_lockup_fix.patch
- Add net-snmp-utils in Requires

* Mon Jan 29 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.8.6j-alt0
- New version
- Add official patches:
  + %name-%version-ping_php_version4_snmpgetnext.patch
  + %name-%version-tree_console_missing_hosts.patch
- Add cacti-plugin-arch
- Separate cactid in own package
- Add BuildArch: noarch (#10675)
- Add %_sysconfdir/cron.d/cacti
- Add virtual packages for different depends

* Sat Jan 13 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6i-alt2
- Security fixes (CVE-2006-6799)

* Mon Dec 04 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6i-alt1
- New version
- Spec cleanups 
- config.php was marked as config with noreplace

* Fri Apr 14 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6h-alt2
- Fixed BuildRequires

* Wed Apr 05 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6h-alt1
- New version
- Spec cleanups

* Sun Jul 10 2005 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6f-alt1
- Many critical security bugfixes in upstream
- Spec fixes (now daemon and main module may have different versions)

* Fri Oct 22 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6b-alt1
- New version

* Sun Sep 19 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt4
- Removed BuildArch tag because our rpm doesn't support multiple buildarch's
  in one spec ;-( Now php stuff has i586 arch ;-)

* Fri Sep 17 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt3
- Spec fixups (correct %%setup macroses)

* Thu Sep 16 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt2
- Spec update (information for upgrade)

* Thu Sep 16 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt1
- New upstream version (has many new features)
- Russian translation for spec
- cactid now in separated package
- spec cleanups (permissions, path)

* Mon Aug 09 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.5a-alt6
- Added missing buildrequires (libssl and other)

* Fri Aug 06 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.5a-alt5
- New version

* Fri Jul 09 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.5-alt4
- New build

* Fri Mar 12 2004 Andrew Kornilov <andy@eva.dp.ua> 0.8.5-alt3
- Removed redundant docs from /var/www/html/cacti

* Fri Mar 12 2004 Andrew Kornilov <andy@eva.dp.ua> 0.8.5-alt2
- Added -M to useradd to skip homedir skeleton 

* Tue Mar 09 2004 Andrew Kornilov <andy@eva.dp.ua> 0.8.5-alt1
- First alpha build for Sisyphus. All works, but...;-)

 
