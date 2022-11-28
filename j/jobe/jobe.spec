%define php_version 8.0

Name:    jobe
Version: 1.7.0
Release: alt1

Summary: jobe is a server that runs small programming jobs in a variety of programming languages
License: MIT
Group:   Networking/WWW
Url:     https://github.com/trampgeek/jobe

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.conf
Source2: jobe-sudoers
Patch1: jobe-alt-fixes.patch

BuildRequires(pre): rpm-macros-apache2
BuildRequires(pre): rpm-build-webserver-common
BuildRequires(pre): rpm-build-python3
#BuildRequires: apache2-devel

%define webappdir %webserver_webappsdir/%name

%description
Jobe (short for Job Engine) is a server that supports running of small
compile-and-run jobs in a variety of programming languages. It was developed as
a remote sandbox for use by CodeRunner, a Moodle question-type plugin that asks
students to write code to some relatively simple specification. However, Jobe
servers could be useful in a variety of other contexts, particularly in
education.

%package -n %name-apache2
Summary: Apache2's requires and config files for %name
Group: Networking/WWW
Requires: %name = %version-%release
Requires: apache2-common >= 2.2.0
Requires: %_initdir/%apache2_dname
Requires: apache2-httpd-prefork
Requires: apache2-mod_php%php_version >= 7.0.0

%description -n %name-apache2
Install this package, if you wish to run %name under apache2 webserver

%package -n %name-mysql
Summary: Virtual package for mysql requires for %name
Group: Networking/WWW
Requires: %name = %version-%release
Requires: php%php_version-mysqli

%description -n %name-mysql
Install this package, if you wish to run %name with MySQL database

%prep
%setup
%patch1 -p1

%build
cd runguard
gcc -o runguard runguard.c
chmod 700 runguard

%install
mkdir -p %buildroot%webappdir
cp -a * %buildroot%webappdir
# sudo configuration
install -Dpm0660 %SOURCE2 %buildroot%_sysconfdir/sudoers.d/jobe-sudoers
# Apache2 configuration
install -pD -m0644 %SOURCE1 %buildroot%apache2_sites_available/%name.conf
# Home for jobe user
mkdir -p %buildroot%_localstatedir/%name/{chrootjail,files,runs}
# Log directory
mkdir -p %buildroot%_logdir/%name

%pre
getent group jobe > /dev/null || /usr/sbin/groupadd -r jobe
getent passwd jobe > /dev/null || \
%_sbindir/useradd -M -r -g jobe -c 'JOBE service user' \
    -d %_localstatedir/%name -s /sbin/nologin jobe 2> /dev/null ||:
for i in `seq 0 9`;do getent passwd jobe$(printf "%%02d" $i) > /dev/null || \
    %_sbindir/useradd jobe$(printf "%%02d" $i) \
    -M -d /var/lib/jobe \
    -g jobe \
    -s /sbin/nologin
done

%post apache2
a2ensite %name
%_initdir/httpd2 condreload

%postun apache2
%_initdir/httpd2 condreload

%files
%doc *.md
%config(noreplace) %_sysconfdir/sudoers.d/jobe-sudoers
%attr(0751,jobe,jobe) %dir %_localstatedir/%name
%attr(0770,jobe,%webserver_group) %dir %_localstatedir/%name/chrootjail
%attr(0770,jobe,%webserver_group) %dir %_localstatedir/%name/files
%attr(0775,jobe,%webserver_group) %dir %_localstatedir/%name/runs
%attr(0770,jobe,%webserver_group) %dir %_logdir/%name
%attr(2750,root,%webserver_group) %dir %webappdir
%webappdir/*
%config(noreplace) %webappdir/application/config/config.php

%files -n %name-apache2
%config(noreplace) %apache2_sites_available/*.conf

%files -n %name-mysql

%changelog
* Mon Nov 28 2022 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- New version.

* Tue Aug 23 2022 Andrey Cherepanov <cas@altlinux.org> 1.6.7-alt1
- New version.
- Requires PHP 8.0.

* Fri Aug 06 2021 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus.
