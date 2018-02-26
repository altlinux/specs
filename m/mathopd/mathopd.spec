Name: mathopd
Version: 1.5p6
Release: alt1

Summary: Fast, lightweight, non-forking HTTP server for UN*X systems.
License: GPL
Group: System/Servers

Url: http://www.%name.org/

Source: %url/dist/%name-%version.tar.gz
Source1: %name.8.gz
Source2: %name.conf.5.gz
Source3: %name.init
Source4: %name.conf
Source5: %name.logrotate
Source6: %url/dist/dir_cgi.c.txt
Source7: %name.cron
Source9: TODO
Source10: %name.sysconfig

Patch: %name-1.5p5-alt-pidfile.patch
Patch1: %name-alt-dircgi.patch
Patch2: %name.getline.patch

#equires: logrotate
Requires: crontabs, gzip, findutils

%define mylogdir	%_logdir/%name
%define logrotate_dir	%_sysconfdir/logrotate.d
%define crondaily_dir   %_sysconfdir/cron.daily

Summary(ru_RU.KOI8-R): Компактный быстрый HTTP-сервер для Юникс-систем

%description
Mathopd is a very small, yet very fast HTTP server for UN*X systems.

Mathopd supports useful features of HTTP/1.1, such as persistent connections,
partial responses and pipelining. It does not support things like content
negotation. The latest version of the software (1.5) also supports CGI/1.1.

Mathopd was designed specifically to run as a single process,
and to never grow in size. When this software was first written (early 1996)
this is something that other HTTP servers were not very good at.

For preventing conflicts with another HTTP-services Mathopd in ALTLinux
listens on port 8000 instead of standard port 80.

%description -l ru_RU.KOI8-R
Mathopd - это очень компактный и быстрый сервер HTTP для Юникс-систем.

Mathopd поддерживает многие возможности протокола HTTP/1.1,
такие как постоянные (persistent) соединения для серий запросов, конвейер
(приём новых запросов через постоянное соединение до того, как будут готовы
ответы на предыдущие), отправка данных по частям (partial responses)
и, начиная с версии 1.5 - запуск внешних приложений по протоколу CGI/1.1.

Mathopd выполняется как один-единственный процесс и никогда не запрашивает
для работы дополнительной памяти. Используйте его для простых задач
(статические страницы с документацией, файлопомойка с доступом по HTTP и т.д.),
для которых функциональность Веб-сервера Apache избыточна.

Чтобы не конфликтовать с другими HTTP-серверами, по умолчанию Mathopd
в ALTLinux ожидает подключений через порт 8000 вместо стандартного 80.

%prep
%setup -q
%patch0 -p1
%__cp -a %SOURCE6 ./dir_cgi.c
%patch1
%patch2 -p2

%build
%__cc -O3 -DFORMAT_V2=1 -o dir_cgi dir_cgi.c
cd src
%make_build

%install
%__mkdir -p %buildroot{%_bindir,%_sbindir,%_initdir,%_man5dir,%_man8dir,%mylogdir,%logrotate_dir,%crondaily_dir}

%makeinstall -C src SBINDIR=%buildroot%_sbindir PREFIX=%buildroot install
%__cp -a   %SOURCE1 %buildroot%_man8dir/
%__cp -a   %SOURCE2 %buildroot%_man5dir/
%__install %SOURCE3 %buildroot%_initdir/%name
%__cp -a   %SOURCE4 %buildroot%_sysconfdir/
%__cp -a   %SOURCE5 %buildroot%logrotate_dir/%name
%__install -p  %SOURCE7  %buildroot%crondaily_dir/%name
%__install -pD -m600 %SOURCE10 %buildroot%_sysconfdir/sysconfig/%name
%__install -p  dir_cgi   %buildroot%_bindir/
/bin/touch %buildroot%mylogdir/{errorlog,childlog}

%files
%_bindir/*
%_sbindir/*
%_man8dir/*
%_man5dir/*
%attr(0700,root,root) %_initdir/%name
%exclude %mylogdir/*log*
%attr(0750,%name,%name) %mylogdir
%ghost %mylogdir/*log*
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%exclude %logrotate_dir/%name
%crondaily_dir/%name
%doc doc/* README COPYING

%pre
id -un %name >/dev/null 2>&1 || /usr/sbin/useradd -s /dev/null -d %mylogdir -r %name

%post
%post_service %name

%preun
%preun_service %name
echo "NOTE: %name account still exist, remove it manually if you need"

%changelog
* Wed Jul 01 2009 Denis Smirnov <mithraen@altlinux.ru> 1.5p6-alt1
- update to 1.5p6
- Mathopd can now (optionally) allow //, /./ and /../ in URL paths. Thanks for
  Peter Pentchev for suggesting this and providing initial patches.

* Tue Oct 31 2006 Ilya Evseev <evseev@altlinux.ru> 1.5p5-alt3
- improvements for dir_cgi: display dates and sizes

* Wed Oct 19 2005 Ilya Evseev <evseev@altlinux.ru> 1.5p5-alt2
- errorlog and childlog are now created with timestamp suffix
- use cron instead of logrotate for compressing/removing old logs
- minor specfile bugfixes:
   + enable 'noreplace' attribute for configuration file
   + dont try to create %name account if it already exists.
- improve service script:
   + support settings file in /etc/sysconfig,
   + support multiple daemon configurations,
   + try to fetch account name for service actions from daemon config.
- additional CGI-BIN executables/extensions in daemon configuration sample
- lot of bugfixes in specfile macros (missing docs, service uninstall, etc.)

* Wed Sep  7 2005 Ilya Evseev <evseev@altlinux.ru> 1.5p5-alt1
- updated to next version
- more definitive description, russian translation added
- added minimal configuration file for running directly after install
- include dir_cgi helper
- create log directory and logrotate script (see also TODO file)
- specfile changes:
   + create "mathopd" account
   + register/unregister service
   + simplified installation stage
- additional targets in service script: reload, drop, safestop, debug,
  based on http://www.mail-archive.com/mathopd@mathopd.org/msg00064.html
- bugfix: PID-file is now created before reducing privileges, not after

* Fri Feb 11 2005 Denis Smirnov <mithraen@altlinux.ru> 1.5p4-alt1
- version update
- initscript added

* Fri Mar 12 2004 Denis Smirnov <mithraen@altlinux.ru> 1.5p2-alt1
- build

## EOF ##
