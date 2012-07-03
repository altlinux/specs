Name: php-base
Version: 2.7
Release: alt3
Group: Development/Other
Packager: Sergey Kurakin <kurakin@altlinux.org>

Source0: php-scripts-%version.tar
Source1: php-control-%version.tar
Source10: php-packaging.alt

License: GPL

Provides: %_libdir/php
Provides: %_datadir/php/scripts
Provides: %_datadir/php/modules
Provides: %_datadir/php/control
Provides: %_datadir/php/control/php.control
Provides: %_sysconfdir/php/control.d

Requires(pre): control

Conflicts: apache-mod_php5 <= 5.2.12.20091216-alt5
Conflicts: apache2-mod_php5 <= 5.2.12.20091216-alt5

Summary: Package with common data for various PHP packages

%description
The %name package contains parts of PHP distribution which are in use
by other PHP-related packages.

%prep
%setup -b1 -c -n %name-%version
cp %SOURCE10 .

%build

%install
mkdir -p \
	%buildroot/%_bindir \
	%buildroot/%_libdir/php \
	%buildroot/%_datadir/php \
	%buildroot/%_sysconfdir/php \
	%buildroot/%_datadir/php/scripts \
	%buildroot/%_datadir/php/modules \
	%buildroot/%_sysconfdir/control.d

install -m 644 php-scripts/phpfunctions %buildroot/%_sysconfdir/control.d
install -m 700 php-scripts/*.sh %buildroot/%_datadir/php/scripts
install -m 755 php-scripts/phpini-migrate %buildroot/%_bindir/

install -d %buildroot/%_datadir/php/control/
install -m 755 php-control/php.control %buildroot/%_datadir/php/control/

install -d %buildroot/%_sysconfdir/php/control.d/
install -m 644 php-control/modes/* %buildroot%_sysconfdir/php/control.d/

install -d %buildroot%_rpmlibdir/
cat <<\EOF >%buildroot%_rpmlibdir/%name-files.req.list
# %name dirlist for %_rpmlibdir/files.req
%_libdir/php/	%name
%_datadir/php/scripts/	%name
%_datadir/php/modules/	%name
%_datadir/php/control/	%name
%_sysconfdir/php/control.d/	%name
EOF

%files
%doc php-packaging.alt
%_bindir/*
%dir %_libdir/php
%dir %_datadir/php
%dir %_sysconfdir/php
%dir %_sysconfdir/php/control.d/
%config(noreplace) %_sysconfdir/php/control.d/*
%config %_sysconfdir/control.d/*
%dir %_datadir/php/scripts
%dir %_datadir/php/modules
%dir %_datadir/php/control/
%_datadir/php/scripts/*
%_datadir/php/control/*
%_rpmlibdir/%name-files.req.list

%changelog
* Mon Nov 15 2010 Aleksey Avdeev <solo@altlinux.ru> 2.7-alt3
- Fix: Remove in the Provides %%_sysconfdir/php/control.d/php.control
  and added %%_datadir/php/control/php.control

* Sun Nov 14 2010 Aleksey Avdeev <solo@altlinux.ru> 2.7-alt2
- %%_sysconfdir/php/control.d/php.control added to the Provides

* Thu Nov 04 2010 Aleksey Avdeev <solo@altlinux.ru> 2.7-alt1
- phpfunctions: Added new functions:
  + php_read_dir_rulefiles(): directory traversal
    /ets/php/{,$PHP_SAPI/}{,$PHP_MAJOR/}control.d in order of priority
    and load rulefiles
  + php_autocontrol(): function calls php_read_dir_rulefiles()
    and php_control
- phpfunctions: Added global variables:
  + PHP_ETCDIR="/etc/php"
  + php_timezone=$(php_get_timezone)
- Add a template for creating control facilitie
  (see %%_datadir/php/control/php.control)
- Add control file for the states: alt_default, public, relaxed,
  restricted, dev_relaxed, dev_restricted, production_relaxed
  and production_restricted

* Tue Oct 26 2010 Sergey Kurakin <kurakin@altlinux.org> 2.6-alt2
- fixed issue with php_get_timezone feature and missing tzdata
  (closes: #24266)
- php-packaging.readme updated and moved here from php5 package
  as php-packaging.alt

* Thu Sep 23 2010 Sergey Kurakin <kurakin@altlinux.org> 2.6-alt1
- phpfunctions: corrected to support significant changes
  in the new AltLinux php 5.3.x builds, keeping backward
  compatibility with recent php 5.x and 4.x builds too
- phpfunctions: new feature to get system timezone
  in "Area/City" format, useful in php-control engine
- phpfunctions: new feature to make detailed modes descriptions
  beside of parameters list
- phpini_migrate script corrected (obsoleted by new AltLinux
  php 5.3.x builds, but kept for backward compatibility reasons)


* Sat Feb 13 2010 Sergey Kurakin <kurakin@altlinux.org> 2.5-alt1
- service restart mechanism moved to filetriggers in respective
  sapi packages

* Wed Jan 27 2010 Sergey Kurakin <kurakin@altlinux.org> 2.4-alt3
- extra check to assure the sapi config directory exists

* Sat Jan 23 2010 Sergey Kurakin <kurakin@altlinux.org> 2.4-alt2
- bugfixes in php_postin.sh and php_preun.sh scripts (#22718)

* Fri Oct 10 2008 Alexey Gladkov <legion@altlinux.ru> 2.4-alt1
- Create .phpnew only if config file changed.
- Change license.
- Fix Requires.

* Tue Oct 07 2008 Alexey Gladkov <legion@altlinux.ru> 2.3-alt2
- Fix BuildArch.

* Sun Jun 29 2008 Alexey Gladkov <legion@altlinux.ru> 2.3-alt1
- Add php_fatal() function.
- Use phpinfo utility to parse php.ini and add backward
  compatibility with php-4.x.

* Sat Nov 11 2006 Alexey Gladkov <legion@altlinux.ru> 2.2-alt1
- Add new utility: phpini-migrate.
- phpfunctions: Change regexp to parse php.ini.

* Thu Jan 26 2006 Alexey Gladkov <legion@altlinux.ru> 2.1-alt1
- php_postin.sh and php_preun.sh updated.
- phpfunctions - common functions for a php control.
- scripts runs with -e -u -f shell options.

* Mon Aug 01 2005 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1
- directory %%_datadir/php/modules added;

* Thu Apr 08 2004 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- ALT Linux Sisyphus first build.
