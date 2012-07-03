# This spec is backported to ALTLinux 4.0 automatically by rpmbh script. Do not edit it.
%define webdir /var/www/html

Name: sams
Version: 1.0.5
Release: alt1
Summary: SAMS (Squid Account Management System)
License: GPLv2 or later
Group: System/Servers

Url: http://sams.perm.ru/

Summary(ru_RU.UTF-8): Программное средство для администрирования доступа пользователей к прокси-серверу squid

Packager: Anton A. Vinogradov <arc@altlinux.org>

Source: %url/download/%name-%version.tar.bz2
Source2: %name-README.alt
Source3: %name.service.alt
# sams doesn't read access.log in alt
Patch1: %name-1.0.4-alt.patch
Patch2: %name-1.0.5-alt.patch
Patch3: %name-1.0.5-crypt.patch

# Automatically added by buildreq on Wed Mar 29 2006

BuildRequires(pre): libMySQL-devel libpcre-devel
Requires: %name = %version-%release %name-server = %version-%release

BuildRequires: rpm-build-compat >= 0.4

%description
SAMS (Squid Account Management System)

%description -l ru_RU.UTF-8
Программное средство для администрирования доступа пользователей к прокси-серверу squid

# -- Server --
%package server
Summary: %name daemon
Summary(ru_RU.UTF-8): Сервер %name
License: GPLv2 or later
Group: System/Servers
Requires: %name = %version-%release
Requires: MySQL-client

%description server
Server %name

%description server -l ru_RU.UTF-8
Сервер %name

# -- Web interface--
%package web
Summary: Handle the adminstration of %name over the web
Summary(ru_RU.UTF-8): Управление %name через web
License: GPLv2 or later
Group: System/Servers
Requires: %name = %version-%release
Requires: webserver,php-engine,php5-mysql

%description web
%name is a WEB-based interface and tool to manage users of SQUID proxy
 - manage users access to SQUID - proxy with NTLM, NCSA authorization or IP address
 - manage prohibition of users to access to URL
 - manage to rewrite requested URL to graphical resources (banners, counters)
 - save and build reports of users statistic
 - switch of users access to SQUID proxy if his traffic quota is off
 - manage a delay pools for users groups

%description web -l ru_RU.UTF-8
%name это WEB интерфейс и инструменты для администрирования пользователей к прокси-серверу squid
 - Администрирование системы через web интерфейс
 - Ограничение объема трафика пользователей на месяц
 - Автоматическое отключение пользователей, превысивших лимит.
 - Ведение списков запрещенных для доступа пользователей ресурсов интернет.
 -  Настройка доступа пользователей через механизм шаблонов. Шаблоны позволяют:
    + назначить списки запрещенных сайтов для пользователей данного шаблона
    + определить объем трафика пользователя шаблона по умолчанию
    + назначить скорость доступа к интернет для пользователей шаблона (delay_pools)
    + ограничение доступа пользователей по времени и дням недели
 - Разбиение пользователей на группы для удобства администрирования системы
 - Формирование отчетов по трафику пользователей за любой отрезок времени:
    + Полученный пользователями трафик
    + Посещенные пользователями сайты
    + Полученные пользователями файлы
 - Поддержка видов авторизации SQUID:
    + NTLM авторизация в домене Windows
    + NCSA авторизация
    + доступ по ip адресу
 - Поддержка использования редиректоров SQUID:
    + Rejik
    + SquidGuard
 - Категории пользователей SAMS:
    + пользователи с правами администрирования SAMS
    + пользователь Аудитор, для контроля трафика пользователей, без возможности администрирования системы
    + пользователи сети с расширенными правами, получают расширенный доступ к web интерфейсу, для контроля трафика пользователей своей группы
    + пользователи сети получают доступ к web интерфейсу для контроля своего трафика
 - Посылку сообщений администратору при отключении пользователей при превышении трафика
 - Для хранения данных используется СУБД MySQL

%prep
%setup -n %name-%version
cp %SOURCE2 README.alt
cp %SOURCE3 etc/sams

%patch1 -p1
%patch2 -p0
%patch3 -p1

#find %_builddir/%name -type d -name CVS -print0 | xargs -r0 rm -fr
rm -f php/lang/koi8r-2-win1251.php

#find %_builddir/%name -type f -print0 | xargs -r0 subst "s|LIBS = -I. \$(MYSQLLIBS) \$(PCRELIBS) \$(SUNLIB)|LIBS = -I. \$(MYSQLLIBS) \$(PCRELIBS) \$(SUNLIB) -lm|g"

%__subst 's|$prefix/share/sams|%webdir/sams|g' configure

%build
%configure \
%ifarch x86_64
        --with-mysql-libpath=/usr/lib64/ \
        --with-pcre-libpath=/usr/lib64/ \
%endif #x86_64
        --with-configfile=%_sysconfdir/%name.conf \
        --with-rcd-locations=%_initdir \
	--with-httpd-locations=%webdir

%make_build

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%webdir/%name
##mkdir -p %buildroot%_datadir/%name

%makeinstall \
        RCDPATH=%buildroot%_initdir \
        HTTPDPATH=%buildroot%webdir \
	datadir=%buildroot%webdir

%__subst "s|/usr/local/rejik|%_sysconfdir/squid/redirector|g" %buildroot%_sysconfdir/%name.conf
%__subst "s|SAMSPATH=/usr/local|SAMSPATH=/usr|g" %buildroot%_sysconfdir/%name.conf
#%__subst "s|daemon|start_daemon|g" %buildroot%_initdir/samsd
#%__subst "s|killproc|stop_daemon|g" %buildroot%_initdir/samsd
#%__subst "s|samsstart_daemon|samsdaemon|g" %buildroot%_initdir/samsd

%post server
%post_service %name
%preun server
%preun_service %name
%files
%doc CHANGELOG COPYING INSTALL README README.alt mysql update etc/sams.conf.default
#%files config
%config(noreplace) %_sysconfdir/%name.conf

%files server
%_bindir/*
%config %_initdir/%name

%files web
%webdir/sams
%dir %attr(2775,root,apache) %webdir/sams
%dir %attr(2775,root,apache) %webdir/sams/data

%changelog
* Mon Oct 18 2010 Anton A. Vinogradov <arc@altlinux.org> 1.0.5-alt1
- build for ALT Linux Sisyphus

* Fri Apr 02 2010 Alexei Takaseev <taf@ilim.ru> 1.0.5-alt0.P5.1
- Build for Platforma 5

* Tue Dec 09 2008 Alexander Volkov <vaa@altlinux.org> 1.0.4-alt0.M40.1
- backport to ALTLinux 4.0 (by rpmbph script)

* Sun Nov 23 2008 Alexander Volkov <vaa@altlinux.org> 1.0.4-alt1
- New version

* Sat Sep 13 2008 Alexander Volkov <vaa@altlinux.ru> 1.0.3-alt1
- new bugfix upstream release

* Mon Mar 03 2008 Alexander Volkov <vaa@altlinux.ru> 1.0.1-alt1
- next build

* Thu Nov 08 2007 Alexander Volkov <vaa@altlinux.ru> 1.0-alt1
- new version, old bugs

* Tue Jul 31 2007 Alexander Volkov <vaa@altlinux.ru> 20070524-alt2
- fix sams binary for correct path to access.log

* Wed Jul 18 2007 Alexander Volkov <vaa@altlinux.ru> 20070524-alt1
- new bugfix version (see CHANGELOG)

* Sun Jun 17 2007 Alexander Volkov <vaa@altlinux.ru> 20070129-alt3
- moved web content from /usr/share to /var/www/html

* Fri Apr 06 2007 Alexander Volkov <vaa@altlinux.ru> 20070129-alt2
- minor changes, README.alt added

* Fri Mar 09 2007 Alexander Volkov <vaa@altlinux.ru> 20070129-alt1
- New release, spec fixes

* Wed Mar 29 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 20051107-alt0
- initial build 4 Sisyphus
