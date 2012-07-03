# hey Emacs, its -*- rpm-spec -*-
# you can build --with/--without:
# - mod_deflate [with]

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define russian_patchlevel PL30.24
%define apache_vanilla_version 1.3.42
%define apache_version %{apache_vanilla_version}rus%russian_patchlevel
%define apache_release %release
%define mod_realip_version 2.0
%define mod_perl_version 1.29
%define mod_perl_version_pad %{mod_perl_version}00
%define mod_perl_doc_version %{mod_perl_version}_%apache_version
%define mod_deflate_version 1.0.21
%define mod_accel_version 1.0.34
%define EAPI_version 2.8.30a
%define mm_version 1.1.3
# EAPI tarball is subset of mod_ssl tarball

# default is 256
%define apache_hard_server_limit 1024

%define old_apache_home /home/httpd
%define suexec_docroot %apache_datadir

%def_with mod_deflate

Name: apache
Version: %apache_version
Release: %branch_release alt4

Summary: The most widely used Web server on the Internet
License: %asl
Group: System/Servers

Url: http://httpd.apache.org
Packager: Michael Shigorin <mike@altlinux.org>

Requires: %name-base = %version-%release
Requires: webserver-cgi-bin
Requires: webserver-html
Requires: webserver-icons

# http://httpd.apache.org/dist/httpd/apache_%apache_vanilla_version.tar.gz
# ftp://apache.lexa.ru/pub/apache-rus/patches_%apache_version.tar.gz
Source0: apache_%apache_version.tar
Source4: apache.logrotate
Source5: httpd.conf
# update EAPI by hand from mod_ssl source tarball
Source9: EAPI-%EAPI_version.tar.bz2
Source12: http://sysoev.ru/mod_deflate/mod_deflate-%mod_deflate_version.tar.gz
Source13: mod_perl-%mod_perl_version.tar.bz2
Source14: mod_realip-%mod_realip_version.tar.gz
Source15: httpd-perl.conf
Source16: proxied_handlers.pl
Source17: http://sysoev.ru/mod_accel/mod_accel-%mod_accel_version.tar.gz
Source23: apache-mime.types
#Source24: logo.gif
Source26: Vhosts.conf
Source27: Vhosts-perl.conf
Source28: sgi_performance.gif
Source29: ra-powered.gif

Source30: altlinux.html

# initscripts for current Sisyphus
Source35: httpd.init
Source36: httpd-perl.init

# scripts for control
Source40: cgi-bin_test-cgi.sh
Source41: cgi-bin_printenv.sh

Source50: DynamicVhosts.conf
Source51: VirtualHomePages.conf
Source52: README.apache
Source53: apache-mod_charset.conf
Source54: apache-mod_realip.conf

# rpm macro definitions
Source61: apache-README.ALT
Source62: 00-example.conf
Source63: TUNING.ALT
Source64: apache.monit

# scripts for condstopstart-web
Source70: server-condstop.sh
Source72: server-condstart.sh

Patch1: apache-1.3.41rusPL30.23-alt-manual-0.1.patch
Patch2: apache-1.3.41rusPL30.23-alt-fix-getline-0.1.patch
Patch3: apache-1.3.31-apxs.patch
Patch4: apache_1.3.27-srvroot.patch
Patch5: apache_1.3.23-nondbm.patch

Patch8: apache-1.3.23-alt-db4.patch
Patch10: apache-1.3.31-acl-support.patch

Patch75: apache-1.3.27-openbsd-tmp.patch
Patch76: apache-1.3.34-alt-linkage.patch

Patch77: apache-1.3.41-unloop-rewrite.patch

Patch80: uneapi.patch
# Expat patch
Patch94: apache-1.3.33-fix-htpasswd-buffer.patch
Patch97: mod_perl-1.29-CVE-2007-1349.patch

# https://rt.cpan.org/Public/Bug/Display.html?id=64999
Patch98: mp1+perl5.14.diff

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-apache
BuildRequires(pre): rpm-macros-condstopstart
BuildPreReq: %_datadir/rpm-build-rpm-eval/rpm-eval.sh
BuildPreReq: rpm-macros-webserver-cgi-bin-control
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Thu Oct 13 2011 (-bi)
BuildRequires: libdb4-devel libgdbm-devel libmm-devel perl-BSD-Resource perl-CGI perl-DBM perl-Devel-Symdump perl-devel perl-libwww

%if_with mod_deflate
BuildRequires: zlib-devel
%endif

BuildConflicts: bind-devel

Summary(ru_RU.KOI8-R): Самый популярный веб-сервер Internet
Summary(uk_UA.KOI8-U): Найб╕льш популярний веб-сервер Internet

%description
Apache is a powerful, full-featured, efficient and freely-available
Web server. Russian Apache is an extended version that supports various
character sets, which are necessary for Russian, Ukrainian, Czech
and other websites.

This special version also includes some optimizations, Extended Application
Programming Interface (EAPI) with the shared memory support,
hooks for SSL module and several cosmetic improvements.
%if_with mod_deflate
It also includes mod_deflate to spare the traffic (needs activation).
%endif

%description -l ru_RU.KOI8-R
Apache - мощный, функциональный, высокопроизводительный и
свободно распространяемый веб-сервер.

Russian Apache - специально доработанная версия сервера с поддержкой различных
кодировок, предназначенная для использования на сайтах с контентом на
русском, украинском, чешском и других языках.

Данная версия также включает некоторые оптимизации,
Extended Application Programming Interface (EAPI) с поддержкой разделяемой
памяти, поддержку модуля SSL и несколько косметических улучшений.
%if_with mod_deflate
Для сохранения трафика включите модуль mod_deflate.
%endif

%description -l uk_UA.KOI8-U
Apache - потужний, функц╕ональний, високопродуктивний та
в╕льно розповсюджуваний веб-сервер.

Russian Apache - спец╕ально дороблена верс╕я серверу ╕з п╕дтримкою р╕зних
кодувань, що застосову╓ться на сайтах ╕з контентом рос╕йською, укра╖нською,
чеською та ╕ншими мовами.

Ця верс╕я також включа╓ деяк╕ оптим╕зац╕╖,
Extended Application Programming Interface (EAPI) ╕з п╕дтримкою розд╕лювано╖
пам'ят╕, п╕дтримку модуля SSL та дек╕лька косметичних покращень.
%if_with mod_deflate
Для збереження траф╕ку ув╕мкн╕ть модуль mod_deflate.
%endif

%package base
Summary: The most widely used Web server on the Internet (base)
Summary(ru_RU.KOI8-R): Самый популярный веб-сервер Internet (база)
Summary(uk_UA.KOI8-U): Найб╕льш популярний веб-сервер Internet (база)
Group: System/Servers

Provides: russian-apache = %russian_patchlevel webserver
Provides: httpd
PreReq: %name-common = %version-%release
Requires: mm >= %mm_version
Requires: monit-base
Requires: service >= 0.5-alt1
Requires: %condstopstart_webdir
Requires: %condstopstart_webrundir

Provides: %apache_moduledir

%description base
Apache is a powerful, full-featured, efficient and freely-available
Web server. Russian Apache is an extended version that supports various
character sets, which are necessary for Russian, Ukrainian, Czech
and other websites.

This special version also includes some optimizations, Extended Application
Programming Interface (EAPI) with the shared memory support,
hooks for SSL module and several cosmetic improvements.
%if_with mod_deflate
It also includes mod_deflate to spare the traffic (needs activation).
%endif

This package does not require a webserver-cgi-bin, webserver-html and
webserver-icons.

%description -l ru_RU.KOI8-R base
Apache - мощный, функциональный, высокопроизводительный и
свободно распространяемый веб-сервер.

Russian Apache - специально доработанная версия сервера с поддержкой различных
кодировок, предназначенная для использования на сайтах с контентом на
русском, украинском, чешском и других языках.

Данная версия также включает некоторые оптимизации,
Extended Application Programming Interface (EAPI) с поддержкой разделяемой
памяти, поддержку модуля SSL и несколько косметических улучшений.
%if_with mod_deflate
Для сохранения трафика включите модуль mod_deflate.
%endif

Данный пакет не требует наличия webserver-cgi-bin, webserver-html и
webserver-icons.

%description -l uk_UA.KOI8-U base
Apache - потужний, функц╕ональний, високопродуктивний та
в╕льно розповсюджуваний веб-сервер.

Russian Apache - спец╕ально дороблена верс╕я серверу ╕з п╕дтримкою р╕зних
кодувань, що застосову╓ться на сайтах ╕з контентом рос╕йською, укра╖нською,
чеською та ╕ншими мовами.

Ця верс╕я також включа╓ деяк╕ оптим╕зац╕╖,
Extended Application Programming Interface (EAPI) ╕з п╕дтримкою розд╕лювано╖
пам'ят╕, п╕дтримку модуля SSL та дек╕лька косметичних покращень.
%if_with mod_deflate
Для збереження траф╕ку ув╕мкн╕ть модуль mod_deflate.
%endif

Данный пакет не требует наличия webserver-cgi-bin, webserver-html и
webserver-icons.

%package full
Summary: The most widely used Web server on the Internet (full)
Summary(ru_RU.KOI8-R): Самый популярный веб-сервер Internet (full)
Summary(uk_UA.KOI8-U): Найб╕льш популярний веб-сервер Internet (full)
Group: System/Servers

Requires: %name = %version-%release
Requires: %name-cgi-bin
Requires: %name-html
Requires: %name-icons

%description full
Apache is a powerful, full-featured, efficient and freely-available
Web server. Russian Apache is an extended version that supports various
character sets, which are necessary for Russian, Ukrainian, Czech
and other websites.

This special version also includes some optimizations, Extended Application
Programming Interface (EAPI) with the shared memory support,
hooks for SSL module and several cosmetic improvements.
%if_with mod_deflate
It also includes mod_deflate to spare the traffic (needs activation).
%endif

This package requires a apache-cgi-bin, apache-html and apache-icons.

%description -l ru_RU.KOI8-R full
Apache - мощный, функциональный, высокопроизводительный и
свободно распространяемый веб-сервер.

Russian Apache - специально доработанная версия сервера с поддержкой различных
кодировок, предназначенная для использования на сайтах с контентом на
русском, украинском, чешском и других языках.

Данная версия также включает некоторые оптимизации,
Extended Application Programming Interface (EAPI) с поддержкой разделяемой
памяти, поддержку модуля SSL и несколько косметических улучшений.
%if_with mod_deflate
Для сохранения трафика включите модуль mod_deflate.
%endif

Данный пакет требует наличия apache-cgi-bin, apache-html и apache-icons.

%description -l uk_UA.KOI8-U full
Apache - потужний, функц╕ональний, високопродуктивний та
в╕льно розповсюджуваний веб-сервер.

Russian Apache - спец╕ально дороблена верс╕я серверу ╕з п╕дтримкою р╕зних
кодувань, що застосову╓ться на сайтах ╕з контентом рос╕йською, укра╖нською,
чеською та ╕ншими мовами.

Ця верс╕я також включа╓ деяк╕ оптим╕зац╕╖,
Extended Application Programming Interface (EAPI) ╕з п╕дтримкою розд╕лювано╖
пам'ят╕, п╕дтримку модуля SSL та дек╕лька косметичних покращень.
%if_with mod_deflate
Для збереження траф╕ку ув╕мкн╕ть модуль mod_deflate.
%endif

Данный пакет требует наличия apache-cgi-bin, apache-html и apache-icons.

%package mod_perl
Summary: Russian Apache Web server with a built-in Perl interpreter
Summary(ru_RU.KOI8-R): Веб-сервер Russian Apache со встроенным интерпретатором Perl
Summary(uk_UA.KOI8-U): Веб-сервер Russian Apache з╕ вбудованим ╕нтерпретатором Perl
Group: System/Servers
Icon: mod_perl.gif
Requires: %name-mod_perl-base = %version-%release
Requires: webserver-cgi-bin
Requires: webserver-html
Requires: webserver-icons

%description mod_perl
Apache is a powerful, full-featured, efficient and freely-available
Web server. Russian Apache is an extended version that supports various
character sets, which are necessary for Russian, Ukrainian, Czech
and other websites.

mod_perl incorporates a Perl interpreter into the Apache web
server, so that the Apache web server can directly execute Perl
code.  Mod_perl links the Perl runtime library into the Apache
web server and provides an object-oriented Perl interface for
Apache's C language API.  The end result is a quicker CGI script
turnaround process, since no external Perl interpreter has to
be started.

This package contains Apache with mod_perl linked statically. You may want to
prefer this configuration rather than use mod_perl as a DSO, because it is more
stable and less prone to memory leaks.

This special version also includes Extended Application Programming Interface
(EAPI) with the shared memory support, hooks for SSL module and several
cosmetic improvements.

%description -l ru_RU.KOI8-R mod_perl
Apache - мощный, функциональный, высокопроизводительный и
свободно распространяемый веб-сервер.

Russian Apache - специально доработанная версия сервера с поддержкой различных
кодировок, предназначенная для использования на сайтах с контентом на
русском, украинском, чешском и других языках.

mod_perl интегрирует в Apache интерпретатор языка Perl и предоставляет
объектно-ориентированный интерфейс из Perl к функциям Apache API. Одно из
преимуществ - ускорение обработки CGI-запросов, поскольку нет нужды
запускать внешний интерпретатор для исполнения Perl-кода.

Пакет содержит Apache со статически скомпонованным mod_perl. Вы можете
предпочесть эту конфигурацию динамически загружаемому mod_perl, так как она
более стабильна и менее подвержена утечкам памяти.

Данная версия также включает Extended Application Programming Interface (EAPI)
с поддержкой разделяемой памяти, поддержку модуля SSL и несколько косметических
улучшений.

%description -l uk_UA.KOI8-U mod_perl
Apache - потужний, функц╕ональний, високопродуктивний та
в╕льно розповсюджуваний веб-сервер.

Russian Apache - спец╕ально дороблена верс╕я серверу ╕з п╕дтримкою р╕зних
кодувань, що застосову╓ться на сайтах ╕з контентом рос╕йською, укра╖нською,
чеською та ╕ншими мовами.

Пакет м╕стить Apache ╕з статично компонованим mod_perl. Ви можете
надати перевагу ц╕й конфигурац╕╖, ан╕ж динам╕чному завантаженню mod_perl,
тому що вона б╕льш стаб╕льна та ма╓ менш проблем з керуванням пам'яттю.

Ця верс╕я також включа╓ Extended Application Programming Interface (EAPI) ╕з
п╕дтримкою розд╕лювано╖ пам'ят╕, п╕дтримку модуля SSL та дек╕лька косметичних
покращень.

%package mod_perl-base
Summary: Russian Apache Web server with a built-in Perl interpreter (base)
Summary(ru_RU.KOI8-R): Веб-сервер Russian Apache со встроенным интерпретатором Perl (база)
Summary(uk_UA.KOI8-U): Веб-сервер Russian Apache з╕ вбудованим ╕нтерпретатором Perl (база)
Group: System/Servers
Icon: mod_perl.gif
Requires: mm >= %mm_version, perl >= 1:5.6.0
PreReq: %name-common = %version-%release
Provides: russian-apache = %russian_patchlevel webserver
Provides: httpd
Provides: mod_perl = %mod_perl_version
Obsoletes: mod_perl < %mod_perl_version

Provides: %apache_moduleperldir
Provides: %apache_addonconfdir
Provides: %apache_datadir/perl

# ugly hack ][
Provides: perl(mod_perl.pm) = %mod_perl_version_pad

%description mod_perl-base
Apache is a powerful, full-featured, efficient and freely-available
Web server. Russian Apache is an extended version that supports various
character sets, which are necessary for Russian, Ukrainian, Czech
and other websites.

mod_perl incorporates a Perl interpreter into the Apache web
server, so that the Apache web server can directly execute Perl
code.  Mod_perl links the Perl runtime library into the Apache
web server and provides an object-oriented Perl interface for
Apache's C language API.  The end result is a quicker CGI script
turnaround process, since no external Perl interpreter has to
be started.

This package contains Apache with mod_perl linked statically. You may want to
prefer this configuration rather than use mod_perl as a DSO, because it is more
stable and less prone to memory leaks.

This special version also includes Extended Application Programming Interface
(EAPI) with the shared memory support, hooks for SSL module and several
cosmetic improvements.

This package does not require a webserver-cgi-bin, webserver-html and
webserver-icons.

%description -l ru_RU.KOI8-R mod_perl-base
Apache - мощный, функциональный, высокопроизводительный и
свободно распространяемый веб-сервер.

Russian Apache - специально доработанная версия сервера с поддержкой различных
кодировок, предназначенная для использования на сайтах с контентом на
русском, украинском, чешском и других языках.

mod_perl интегрирует в Apache интерпретатор языка Perl и предоставляет
объектно-ориентированный интерфейс из Perl к функциям Apache API. Одно из
преимуществ - ускорение обработки CGI-запросов, поскольку нет нужды
запускать внешний интерпретатор для исполнения Perl-кода.

Пакет содержит Apache со статически скомпонованным mod_perl. Вы можете
предпочесть эту конфигурацию динамически загружаемому mod_perl, так как она
более стабильна и менее подвержена утечкам памяти.

Данная версия также включает Extended Application Programming Interface (EAPI)
с поддержкой разделяемой памяти, поддержку модуля SSL и несколько косметических
улучшений.

Данный пакет не требует наличия webserver-cgi-bin, webserver-html и
webserver-icons.

%description -l uk_UA.KOI8-U mod_perl-base
Apache - потужний, функц╕ональний, високопродуктивний та
в╕льно розповсюджуваний веб-сервер.

Russian Apache - спец╕ально дороблена верс╕я серверу ╕з п╕дтримкою р╕зних
кодувань, що застосову╓ться на сайтах ╕з контентом рос╕йською, укра╖нською,
чеською та ╕ншими мовами.

Пакет м╕стить Apache ╕з статично компонованим mod_perl. Ви можете
надати перевагу ц╕й конфигурац╕╖, ан╕ж динам╕чному завантаженню mod_perl,
тому що вона б╕льш стаб╕льна та ма╓ менш проблем з керуванням пам'яттю.

Ця верс╕я також включа╓ Extended Application Programming Interface (EAPI) ╕з
п╕дтримкою розд╕лювано╖ пам'ят╕, п╕дтримку модуля SSL та дек╕лька косметичних
покращень.

Данный пакет не требует наличия webserver-cgi-bin, webserver-html и
webserver-icons.

%package mod_perl-full
Summary: Russian Apache Web server with a built-in Perl interpreter (full)
Summary(ru_RU.KOI8-R): Веб-сервер Russian Apache со встроенным интерпретатором Perl (full)
Summary(uk_UA.KOI8-U): Веб-сервер Russian Apache з╕ вбудованим ╕нтерпретатором Perl (full)
Group: System/Servers
Icon: mod_perl.gif
Requires: %name-mod_perl = %version-%release
Requires: %name-cgi-bin
Requires: %name-html
Requires: %name-icons

%description mod_perl-full
Apache is a powerful, full-featured, efficient and freely-available
Web server. Russian Apache is an extended version that supports various
character sets, which are necessary for Russian, Ukrainian, Czech
and other websites.

mod_perl incorporates a Perl interpreter into the Apache web
server, so that the Apache web server can directly execute Perl
code.  Mod_perl links the Perl runtime library into the Apache
web server and provides an object-oriented Perl interface for
Apache's C language API.  The end result is a quicker CGI script
turnaround process, since no external Perl interpreter has to
be started.

This package contains Apache with mod_perl linked statically. You may want to
prefer this configuration rather than use mod_perl as a DSO, because it is more
stable and less prone to memory leaks.

This special version also includes Extended Application Programming Interface
(EAPI) with the shared memory support, hooks for SSL module and several
cosmetic improvements.

This package requires a apache-cgi-bin, apache-html and apache-icons.

%description -l ru_RU.KOI8-R mod_perl-full
Apache - мощный, функциональный, высокопроизводительный и
свободно распространяемый веб-сервер.

Russian Apache - специально доработанная версия сервера с поддержкой различных
кодировок, предназначенная для использования на сайтах с контентом на
русском, украинском, чешском и других языках.

mod_perl интегрирует в Apache интерпретатор языка Perl и предоставляет
объектно-ориентированный интерфейс из Perl к функциям Apache API. Одно из
преимуществ - ускорение обработки CGI-запросов, поскольку нет нужды
запускать внешний интерпретатор для исполнения Perl-кода.

Пакет содержит Apache со статически скомпонованным mod_perl. Вы можете
предпочесть эту конфигурацию динамически загружаемому mod_perl, так как она
более стабильна и менее подвержена утечкам памяти.

Данная версия также включает Extended Application Programming Interface (EAPI)
с поддержкой разделяемой памяти, поддержку модуля SSL и несколько косметических
улучшений.

Данный пакет требует наличия apache-cgi-bin, apache-html и apache-icons.

%description -l uk_UA.KOI8-U mod_perl-full
Apache - потужний, функц╕ональний, високопродуктивний та
в╕льно розповсюджуваний веб-сервер.

Russian Apache - спец╕ально дороблена верс╕я серверу ╕з п╕дтримкою р╕зних
кодувань, що застосову╓ться на сайтах ╕з контентом рос╕йською, укра╖нською,
чеською та ╕ншими мовами.

Пакет м╕стить Apache ╕з статично компонованим mod_perl. Ви можете
надати перевагу ц╕й конфигурац╕╖, ан╕ж динам╕чному завантаженню mod_perl,
тому що вона б╕льш стаб╕льна та ма╓ менш проблем з керуванням пам'яттю.

Ця верс╕я також включа╓ Extended Application Programming Interface (EAPI) ╕з
п╕дтримкою розд╕лювано╖ пам'ят╕, п╕дтримку модуля SSL та дек╕лька косметичних
покращень.

Данный пакет требует наличия apache-cgi-bin, apache-html и apache-icons.

%package common
Summary: Files common for apache and apache-mod_perl installations
Summary(ru_RU.KOI8-R): Общие файлы для инсталляции apache и apache-mod_perl
Summary(uk_UA.KOI8-U): Сп╕льн╕ файли для ╕нсталяц╕╖ apache та apache-mod_perl
Group: System/Servers
PreReq: webserver-common

Provides: %apache_basedir
Provides: %apache_confdir
Provides: %apache_confdir/vhosts
Provides: %apache_vhconfdir
Provides: %apache_addonconfdir
Provides: %apache_modconfdir
Provides: %apache_logdir
Provides: %_cachedir/httpd
Provides: %apache_tmpdir
Provides: %apache_tmpdir/tmp
Provides: %apache_tmpdir/sessions
Provides: %apache_tmpdir/uploads
Provides: %apache_datadir/apache

%description common
This package contains files required for both apache and apache-mod_perl
package installations. Install this if you want to install Apache or/and
Apache with mod_perl.

%description -l ru_RU.KOI8-R common
В этом пакете находятся файлы, необходимые для apache и apache-mod_perl.
Установите, если собираетесь устанавливать Russian Apache
и/или Russian Apache с mod_perl.

%description -l uk_UA.KOI8-U common
Цей пакунок м╕стить файли, як╕ необх╕дн╕ для apache та apache-mod_perl.
Встанов╕ть його, якщо збира╓тесь використовувати Russian Apache.

%package -n rpm-build-%name
Summary: RPM helper to rebuild Web servers and apps packages
Summary(ru_RU.KOI8-R): Набор утилит для автоматической Web серверов и приложений
Group: Development/Other

Requires: rpm-macros-%name

%description -n rpm-build-%name
These helper provide possibility to rebuild Web servers and applications
packages by some ALT Linux Web Packaging Policy.

%description -n rpm-build-%name -l ru_RU.KOI8-R
Набор утилит для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.

%package devel
Summary: Module development tools for the Apache web server
Summary(ru_RU.KOI8-R): Средства разработки модулей для веб-сервера Apache
Summary(uk_UA.KOI8-U): Засоби розробки модул╕в для веб-серверу Apache
Group: Development/C
BuildArch: noarch
PreReq: %name-base = %version-%release
Requires: rpm-build-%name >= %version-%release

Provides: %_includedir/%name

%description devel
The apache-devel package contains the source code for the Apache
Web server you'll need to build Dynamic
Shared Objects (DSOs) for Apache.

If you are installing the Apache Web server and
you want to be able to compile or develop additional modules
for Apache, you'll need to install this package.

%description -l ru_RU.KOI8-R devel
Пакет содержит заголовочные файлы из исходных текстов веб-сервера Apache,
необходимые для сборки динамически подключаемых модулей (DSO).

Если вы устанавливаете веб-сервер Apache и собираетесь компилировать или
разрабатывать для него дополнительные модули, следует установить этот пакет.

%description -l uk_UA.KOI8-U devel
Пакунок м╕стить заголовков╕ файли з вих╕дних текст╕в веб-серверу Apache,
що необх╕дн╕ для комп╕ляц╕╖ динам╕чно завантажуваних модул╕в (DSO).

Якщо ви встановлю╓те веб-сервер Apache та збира╓теся комп╕лювати чи
розробляти для нього додатков╕ модул╕, треба встановити цей пакунок.

%package suexec
Summary: Suexec binary for Apache
Summary(ru_RU.KOI8-R): Программа suexec для Apache
Summary(uk_UA.KOI8-U): Програма suexec для Apache
Group: System/Servers
PreReq: %name-common = %version-%release

%description suexec
This package adds suexec to Apache. Suexec provides Apache users the ability
to run CGI and SSI programs under user IDs different from the user ID of the
calling web-server. Normally, when a CGI or SSI program executes, it runs as
the same user who is running the web server.

%description -l ru_RU.KOI8-R suexec
Этот пакет добавляет к Apache suexec. Эта программа позволяет запускать CGI-
и SSI-программы под идентификаторами пользователя, отличными от UID
веб-сервера.

%description -l uk_UA.KOI8-U suexec
Цей пакунок дода╓ до Apache suexec. Ця програма дозволя╓ запускати CGI-
та SSI-програми п╕д ╕дентиф╕каторами користувача, що в╕др╕зняються в╕д
UID веб-серверу.

%package -n mod_perl-doc
Summary: mod_perl documentation
Summary(ru_RU.KOI8-R): Документация по mod_perl
Summary(uk_UA.KOI8-U): Документац╕я по mod_perl
Group: System/Servers
Version: %mod_perl_doc_version
PreReq: %name-common = %apache_version-%release
Requires: %apache_htdocsaddondir

%description -n mod_perl-doc
This package contains assorted documentation on the mod_perl Apache module.

%description -l ru_RU.KOI8-R -n mod_perl-doc
Этот пакет содержит документацию к модулю Apache mod_perl.

%description -l uk_UA.KOI8-U -n mod_perl-doc
Цей пакунок м╕стить документац╕ю до модуля Apache mod_perl.

%package manual
Summary: Apache Manual
Summary(ru_RU.KOI8-R): Документация по Apache
Summary(uk_UA.KOI8-U): Документац╕я по Apache
Group: System/Servers
Version: %apache_version
BuildArch: noarch
PreReq: %name-common = %version-%release
AutoReq: no

%description manual
This package contains the Apache server documentation in HTML format.

%description -l ru_RU.KOI8-R manual
Этот пакет содержит документацию к веб-серверу Apache в формате HTML.

%description -l uk_UA.KOI8-U manual
Цей пакунок м╕стить документац╕ю до веб-серверу Apache у формат╕ HTML.

%package datadirs
Summary: data dirs for Apache
Summary(ru_RU.KOI8-R): каталоги данных для Apache
Group: System/Servers
BuildArch: noarch

Provides: %_datadir/%name
Provides: %_datadir/%name/cgi-bin

%description datadirs
This package contains the Apache server data dirs.

%description -l ru_RU.KOI8-R datadirs
Этот пакет содержит каталоги данных к веб-серверу Apache.

%package cgi-bin-test-cgi
Summary: cgi-bin/test-cgi for Apache
Summary(ru_RU.KOI8-R): cgi-bin/test-cgi для Apache
Group: System/Servers
BuildArch: noarch
PreReq: webserver-common
PreReq: %_sysconfdir/control.d/webserver-cgi-bin-functions
Provides: webserver-cgi-bin-test-cgi
Conflicts: apache2-cgi-bin-test-cgi
Conflicts: apache2-cgi-bin < 2.2.9-alt10
Conflicts: apache-common < 1.3.37rusPL30.23-alt1.1

Requires: %_datadir/%name/cgi-bin

%description cgi-bin-test-cgi
This package contains the Apache server test-cgi scripts.

%description -l ru_RU.KOI8-R cgi-bin-test-cgi
Этот пакет содержит test-cgi скрипт для веб-сервера Apache.

%package cgi-bin-printenv
Summary: cgi-bin/printenv for Apache
Summary(ru_RU.KOI8-R): cgi-bin/printenv для Apache
Group: System/Servers
BuildArch: noarch
PreReq: webserver-common
PreReq: %_sysconfdir/control.d/webserver-cgi-bin-functions
Provides: webserver-cgi-bin-printenv
Conflicts: apache2-cgi-bin-printenv
Conflicts: apache2-cgi-bin < 2.2.9-alt10
Conflicts: apache-common < 1.3.37rusPL30.23-alt1.1

Requires: %_datadir/%name/cgi-bin

%description cgi-bin-printenv
This package contains the Apache server printenv scripts.

%description -l ru_RU.KOI8-R cgi-bin-printenv
Этот пакет содержит printenv скрипт для веб-сервера Apache.

%package cgi-bin
Summary: cgi-bin for Apache
Summary(ru_RU.KOI8-R): cgi-bin для Apache
Group: System/Servers
BuildArch: noarch
Requires: %name-cgi-bin-test-cgi
Requires: %name-cgi-bin-printenv
Provides: webserver-cgi-bin
Conflicts: apache2-cgi-bin

%description cgi-bin
This package contains the Apache server cgi-bin dir and cgi scripts.

%description -l ru_RU.KOI8-R cgi-bin
Этот пакет содержит каталог cgi-bin с типовыми скриптами к веб-серверу Apache.

%package html
Summary: html for Apache
Summary(ru_RU.KOI8-R): html для Apache
Group: System/Servers
BuildArch: noarch
PreReq: webserver-common
Provides: webserver-html
Conflicts: apache-common < 1.3.37rusPL30.23-alt1.1
Conflicts: apache2-html

%description html
This package contains the Apache server html dir.

%description -l ru_RU.KOI8-R html
Этот пакет содержит каталог html для веб-сервера Apache.

%package icons
Summary: icons for Apache
Summary(ru_RU.KOI8-R): icons для Apache
Group: System/Servers
BuildArch: noarch
PreReq: webserver-common
Provides: webserver-icons
Conflicts: apache-common < 1.3.37rusPL30.23-alt1.1
Conflicts: apache2-icons

%description icons
This package contains the Apache server icons dir.

%description -l ru_RU.KOI8-R icons
Этот пакет содержит каталог icons для веб-сервера Apache.

%add_findprov_lib_path %_libdir/%name

%prep
%{expand:%%global _builddir %_builddir/apache-%apache_version-%apache_release}
rm -rf %_builddir
mkdir -p %_builddir

%setup -q -n mod_deflate-%mod_deflate_version -T -b 12
%setup -q -n mod_accel-%mod_accel_version -T -b 17
%setup -q -n mod_perl-%mod_perl_version -T -b 13
%setup -q -n apache_%apache_version
%setup -q -n mod_realip-%mod_realip_version -T -b 14

# Install mod_realip
cp $RPM_BUILD_DIR/mod_realip-%mod_realip_version/*.c $RPM_BUILD_DIR/apache_%apache_version/src/modules/extra/

cd $RPM_BUILD_DIR/apache_%apache_version

# fix problem with mod_long_names (by pilot@);
# get apxs to understand Includes (updated patch1)
%patch1 -p1

# fix build
%patch2 -p1

%patch3 -p1
%patch4 -p1
%patch5 -p1

%patch8 -p1

%if_with acl_support
%patch10 -p1
%endif

%patch75 -p1
%patch76 -p1
%patch77 -p1

%patch94 -p1

# should be obsolete with mod_perl-1.30
pwd
pushd ../mod_perl-%mod_perl_version
%patch97 -p1
%patch98 -p1
popd

chmod -x $(find htdocs -type f)
subst 's|" PLATFORM "|%distribution/%apache_release|;' \
	$RPM_BUILD_DIR/apache_%apache_version/src/main/http_main.c

#####
cd ..
rm -rf apache-mod_perl_%apache_vanilla_version

#### EAPI
pushd apache_%apache_version
%setup -q -n apache_%apache_version -T -D -b 9
mv ../EAPI-%EAPI_version/pkg.eapi/*.c src/ap/
mv ../EAPI-%EAPI_version/pkg.eapi/*.h src/include/
mv ../EAPI-%EAPI_version/pkg.addon/*.c src/modules/extra
cp src/modules/extra/mod_define.c src/modules/standard
popd

pushd apache_%apache_version
patch -p0 -s < ../EAPI-%EAPI_version/pkg.addon/addon.patch
patch -p0 -s < ../EAPI-%EAPI_version/pkg.eapi/eapi.patch
popd

cp -pr apache_%apache_version apache-mod_perl_%apache_vanilla_version

%build
echo "### define configure flags"
APFLAGS="--serverroot=%apache_basedir \
	--prefix=%prefix \
	--bindir=%_bindir \
	--sbindir=%_sbindir \
	--mandir=%_mandir \
	--sysconfdir=%apache_confdir \
	--datadir=%apache_datadir \
	--htdocsdir=%apache_htdocsdir \
	--includedir=%_includedir/apache \
	--localstatedir=%_var \
	--runtimedir=%_var/run \
	--logfiledir=%apache_logdir \
	--proxycachedir=%_cachedir/httpd \
	--disable-rule=WANTHSREGEX \
	--disable-rule=EXPAT \
        --with-perl=%__perl \
	--without-confadjust \
	--enable-module=all \
	--enable-module=auth_digest \
	--disable-module=auth_dbm \
	--enable-shared=max \
	--enable-suexec \
	--suexec-caller=%apache_user \
	--suexec-docroot=%suexec_docroot \
	--suexec-userdir=public_html \
	--activate-module=src/modules/extra/mod_realip.o \
%if_with mod_accel
	--activate-module=src/modules/accel/libaccel.a \
%endif
%if_with mod_deflate
	--activate-module=src/modules/extra/mod_deflate.o \
%endif
	"

%if_with mod_deflate
echo "### Patching source of apache to enable mod_deflate"
pushd ../mod_deflate-%mod_deflate_version
./configure --with-apache=../apache_%apache_version
# SMP build incompatible
%make
./configure --with-apache=../apache-mod_perl_%apache_vanilla_version
%make
mv CHANGES CHANGES.mod_deflate
mv CHANGES.rus CHANGES.mod_deflate.rus
mv LICENSE LICENSE.mod_deflate
mv readme.html readme.mod_deflate.ru.html
popd
%endif

%if_with mod_accel
echo "### Patching source of apache to enable mod_accel"
pushd ../mod_accel-%mod_accel_version
./configure --with-apache=../apache_%apache_version
%make
./configure --with-apache=../apache-mod_perl_%apache_vanilla_version
%make
mv CHANGES CHANGES.mod_accel
mv CHANGES.rus CHANGES.mod_accel.rus
mv LICENSE LICENSE.mod_accel
mv readme.html readme.mod_accel.ru.html
popd
%endif

LIMITS="-DHARD_SERVER_LIMIT=%apache_hard_server_limit"

%if_with acl_support
ACL_SUPPORT="-DACL_SUPPORT"
%endif

echo "### Build the *normal* Apache"

OPTIM="%optflags $LIMITS $ACL_SUPPORT" \
EAPI_MM=SYSTEM \
CFLAGS='-DEAPI_MM_CORE_PATH=\\\"%_var/run/mm\\\" -I%_includedir/db4 -I%_includedir/gdbm -DDBM_SUFFIX=\\\".db\\\"' \
LIBS="-ldb -lgdbm -lgdbm_compat -lpthread" \
found_dbm="1" \
./configure \
	--enable-rule=EAPI \
	--libexecdir=%apache_moduledir \
	--enable-rule=SHARED_CORE \
	$APFLAGS

%make

echo "### configure mod_perl"
cd $RPM_BUILD_DIR/mod_perl-%mod_perl_version
perl -pi -e "s|PRODUCT|BASEPRODUCT|;" Makefile.PL
PERL_CC="gcc" \
PERL_CCFLAGS=`perl -V:ccflags|cut -f 2 -d\'` \
perl -I$RPM_BUILD_DIR/mod_perl-%mod_perl_version/lib  Makefile.PL \
    PREFIX=%prefix INSTALLDIRS=vendor \
    USE_APACI=1 \
    APACHE_SRC=../apache-mod_perl_%apache_vanilla_version/src \
    APACHE_HEADER_INSTALL=1 \
    DO_HTTPD=1 \
    PREP_HTTPD=1 \
    EVERYTHING=1

echo "### build Perl-side "
%make
chmod -R o-w t/docs/
cd faq
%make
echo "### build Apache with mod_perl"
cd $RPM_BUILD_DIR/apache-mod_perl_%apache_vanilla_version

OPTIM="%optflags $LIMITS $ACL_SUPPORT" \
PERL_CC="gcc" \
PERL_CCFLAGS=`perl -V:ccflags|cut -f 2 -d\'` \
PERL5LIB=$RPM_BUILD_DIR/mod_perl-%mod_perl_version/lib \
CFLAGS='-I%_includedir/db4 -I%_includedir/gdbm -DDBM_SUFFIX=\\\".db\\\"' \
LIBS="-ldb -lgdbm -lgdbm_compat -lpthread" \
found_dbm="1" \
./configure \
	--enable-rule=EAPI \
	--libexecdir=%apache_moduleperldir \
	$APFLAGS \
	--activate-module=src/modules/perl/libperl.a \
	--activate-module=src/modules/extra/mod_realip.o \
	--disable-shared=include \
	--disable-shared=perl

%make build-std
%make -C src/support apxs

%install
# Generate sed script for substitute the real paths in configs
echo '
s|@RUNDIR@|%condstopstart_webrundir|g
' >> SetMacros.sed

# install the normal Apache
pushd $RPM_BUILD_DIR/apache_%apache_version
%make install-quiet root=%buildroot
install -d %buildroot%apache_tmpdir/{,tmp,sessions,uploads}
popd

# install apache-mod_perl
pushd $RPM_BUILD_DIR/apache-mod_perl_%apache_vanilla_version
install -m755 src/httpd %buildroot%_sbindir/httpd-perl
install -d -m755 %buildroot%apache_moduleperldir/
install -m755 src/modules/*/*.so %buildroot%apache_moduleperldir/
sed  -e 's;^#!/.*;#!/usr/bin/perl;' \
	-e 's;\@prefix\@;%prefix;' \
	-e 's;\@sbindir\@;%_sbindir;' \
	-e 's;\@libexecdir\@;%apache_moduleperldir;' \
	-e 's;\@includedir\@;%_includedir/%name;' \
	-e 's;\@sysconfdir\@;%apache_confdir;' \
	< src/support/apxs > %buildroot%_sbindir/apxs-perl
chmod 755 %buildroot%_sbindir/apxs-perl
popd

ln -snf `relative %apache_logdir %apache_basedir/` \
	%buildroot%apache_loglink
ln -snf `relative %apache_moduledir %apache_basedir/` \
	%buildroot%apache_modulelink
ln -snf `relative %apache_moduleperldir %apache_basedir/` \
	%buildroot%apache_moduleperllink

# install log rotation stuff
install -pD -m644 %SOURCE4 \
	%buildroot%_sysconfdir/logrotate.d/apache

# install configuration files
pushd %buildroot%apache_confdir
	install -m644 %SOURCE5 httpd.conf
	install -m644 %SOURCE15 httpd-perl.conf
	perl -pi -e 's/^\s*User nobody/User %apache_user/;' \
		    -e 's/^\s*Group nobody/Group %apache_group/;' \
		    httpd*.conf
	install -m644 %SOURCE23 apache-mime.types
	cp -a mime.types.default apache-mime.types.default
	install -d -m755 vhosts
	install -p -m644 %SOURCE26 %SOURCE27 %SOURCE50 %SOURCE51 vhosts/
	install -pD -m644 %SOURCE16 addon-modules/proxied_handlers.pl

	install -d -m755 addon-modules.d
	install -pD -m644 %SOURCE53 addon-modules.d/mod_charset.conf
	install -pD -m644 %SOURCE54 addon-modules.d/mod_realip.conf

	install -d -m755 vhosts.d
	install -p -m644 %SOURCE62 vhosts.d/00-example.conf

	install -d -m755 vhosts-perl.d
	
	# purge unneeded ones
	rm -f {{access,srm}.conf,mime.types}{,.default}
popd

# monit support
install -pD -m644 %SOURCE64 %buildroot%_sysconfdir/monitrc.d/apache

#install misc documentation and logos
install -pD -m644 %SOURCE52 %buildroot%apache_htdocsdir/README.txt
install -pD -m644 %SOURCE61 %buildroot%apache_htdocsdir/README.ALT
install -pD -m644 %SOURCE63 %buildroot%apache_htdocsdir/TUNING.ALT
rm -f %buildroot%apache_htdocsdir/index.html.ru{,.ucs*}
for f in %buildroot%apache_htdocsdir/index.html*; do
	perl -pi \
		-e 's|apache_pb\.gif|ra-powered.gif|g;' \
		-e 's|</BODY>|<!--#include file="altlinux.html" -->\n</BODY>|i;' \
		< $f > ${f/.html/.shtml} \
        && rm -f $f
done
perl -pi -e 's|http://www\.apache\.org/httpd|http://apache.lexa.ru/|' \
	%buildroot%apache_htdocsdir/index.shtml.ru*
install -m644 %SOURCE29 %buildroot/%apache_htdocsdir/
install -m644 %SOURCE30 %buildroot/%apache_htdocsdir/
install -d -m755 %buildroot/%apache_htdocsaddondir/
install -m644 $RPM_BUILD_DIR/EAPI-%EAPI_version/pkg.addon/mod_define.html \
	%buildroot/%apache_htdocsdir/manual/mod/mod_define.html

perl -pi -e "s|/usr/local/bin/perl|%__perl|g;" \
	%buildroot/%apache_htdocsdir/manual/misc/howto.html
perl -pi -e "s|/path/to/bin/perl|%__perl|g;" \
	%buildroot/%apache_htdocsdir/manual/mod/mod_rewrite.html
perl -pi -e "s|/usr/local/bin/perl|%__perl|g;" \
	%buildroot/%apache_htdocsdir/manual/search/manual-index.cgi

#install cache_create for mod_accel
%if_with mod_accel
install -m755 $RPM_BUILD_DIR/mod_accel-%mod_accel_version/create_cache \
	%buildroot%_bindir/create_cache
%endif

# install mod_perl files
pushd $RPM_BUILD_DIR/mod_perl-%mod_perl_version
%perl_vendor_install
rm -f %buildroot%perl_vendor_autolib/mod_perl/.packlist
install -d  -m755 %buildroot%apache_datadir/perl
install -pD -m644 eg/README \
	%buildroot%apache_htdocsaddondir/mod_perl/README.eg
install -m644 README SUPPORT Changes faq/*.{html,txt} \
		 apache-modlist.html htdocs/manual/mod/mod_perl.html \
	%buildroot%apache_htdocsaddondir/mod_perl/
perl -pi -e "s|../../../|/manual/images/|g;" \
	%buildroot%apache_htdocsaddondir/mod_perl/mod_perl.html
perl -pi -e 's,/usr/local/bin/perl,%_bindir/perl,' \
	%buildroot%perl_vendor_archlib/Apache/Resource.pm
popd

# install proper initscripts
mkdir -p %buildroot%_sysconfdir/rc.d/init.d

install -m755 %SOURCE35 \
	%buildroot%_sysconfdir/rc.d/init.d/httpd
install -m755 %SOURCE36 \
	%buildroot%_sysconfdir/rc.d/init.d/httpd-perl

# replace the "official" apachectl by a symlink to the init script
rm -f %buildroot%_sbindir/apachectl*
ln -s `relative %_sysconfdir/rc.d/init.d/httpd %_sbindir/` \
	%buildroot%_sbindir/apachectl
ln -s `relative %_sysconfdir/rc.d/init.d/httpd-perl %_sbindir/` \
	%buildroot%_sbindir/apachectl-perl

# take away manuals to place them in docdir
mv %buildroot%apache_htdocsdir/manual/ \
	$RPM_BUILD_DIR/apache_%apache_version/
mv %buildroot%apache_htdocsaddondir/mod_perl/ \
	$RPM_BUILD_DIR/apache_%apache_version/perldocs

# fix manpages
subst 's,/usr/local/apache,%apache_basedir,g' \
	%buildroot/%_mandir/man?/*.[0-9]
subst 's,/usr/local/etc/apache,%apache_confdir,g' \
	%buildroot/%_mandir/man?/*.[0-9]

# check modules for undefined symbols
pushd %buildroot%apache_moduledir
ldd -r libhttpd.so 2>%_builddir/check.log >/dev/null
for f in *.so; do
	[ "$f" != libhttpd.so ] || continue
	[ -f "$f" ] || continue
	LD_PRELOAD=./libhttpd.so ldd -r "$f" 2>&1 >/dev/null ||:
done >>%_builddir/check.log
! [ -s %_builddir/check.log ] || exit 1
popd # %buildroot%apache_moduledir
pushd %buildroot%apache_moduleperldir
for f in *.so; do
	[ -f "$f" ] || continue
	LD_PRELOAD=%buildroot%apache_moduledir/libhttpd.so ldd -r "$f" 2>&1 >/dev/null ||:
done >%_builddir/check.log
! [ -s %_builddir/check.log ] || exit 1
popd # %buildroot%apache_moduleperldir

mkdir -p %buildroot%apache_datadir/apache/

# Install scripts for control
install -pD %SOURCE40 %buildroot%_controldir/cgi-bin_test-cgi
install -pD %SOURCE41 %buildroot%_controldir/cgi-bin_printenv

# Create datadirs
install -d %buildroot%_datadir/%name/cgi-bin/

# Move cgi scripts to data dirs
mv %buildroot%apache_cgibindir/* %buildroot%_datadir/%name/cgi-bin/

# Install condstopstart-web scripts for httpd
install -pD %SOURCE70 %buildroot%condstopstart_webdir/httpd-condstop
ln -s httpd-condstop %buildroot%condstopstart_webdir/httpd-condstop-rpm
install -pD %SOURCE72 %buildroot%condstopstart_webdir/httpd-condstart
ln -s httpd-condstart %buildroot%condstopstart_webdir/httpd-condstart-rpm

sed -i '
s|@SERVER@|httpd|g
s|@LOCKFILE@|%_locksubsysdir/httpd|g
' %buildroot%condstopstart_webdir/httpd-cond*

# Install condstopstart-web scripts for httpd-perl
install -pD %SOURCE70 %buildroot%condstopstart_webdir/httpd-perl-condstop
ln -s httpd-condstop %buildroot%condstopstart_webdir/httpd-perl-condstop-rpm
install -pD %SOURCE72 %buildroot%condstopstart_webdir/httpd-perl-condstart
ln -s httpd-condstart %buildroot%condstopstart_webdir/httpd-perl-condstart-rpm

sed -i '
s|@SERVER@|httpd-perl|g
s|@LOCKFILE@|%_locksubsysdir/httpd-perl|g
' %buildroot%condstopstart_webdir/httpd-perl-cond*

# Substitute the real paths in files
find %buildroot%_sysconfdir %buildroot%condstopstart_webdir \
		-type f -print0 \
	| xargs -r0i %_datadir/rpm-build-rpm-eval/rpm-eval.sh "{}"
find %buildroot%_sysconfdir %buildroot%condstopstart_webdir \
		-type f -print0 \
	| xargs -r0 sed -i -f SetMacros.sed

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%name-files.req.list
# %name dirlist for %_rpmlibdir/files.req
%apache_moduledir/	%name-base
%apache_basedir/	%name-common
%apache_confdir/	%name-common
%apache_confdir/vhosts/	%name-common
%apache_vhconfdir/	%name-common
%apache_addonconfdir/	%name-common
%apache_modconfdir/	%name-common
%apache_logdir/	%name-common
%_cachedir/httpd/	%name-common
%apache_tmpdir/	%name-common
%apache_tmpdir/tmp/	%name-common
%apache_tmpdir/sessions/	%name-common
%apache_tmpdir/uploads/	%name-common
%apache_datadir/apache/	%name-common
%_datadir/%name/	%name-datadirs
%_datadir/%name/cgi-bin/	%name-datadirs
%apache_moduleperldir/	%name-mod_perl-base
%apache_addonconfdir/	%name-mod_perl-base
%apache_datadir/perl/	%name-mod_perl-base
%_includedir/%name/	%name-devel
EOF

# SCRIPTS

%pre common
%_sbindir/groupadd -r -f %apache_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %apache_webmaster 2>/dev/null ||:
%_sbindir/useradd -g %apache_group -c 'WWW server' -d %apache_datadir -s '' \
	-G %webserver_group -r %apache_user 2>/dev/null || :
if LANG=C %_bindir/id %apache_user 2>/dev/null | \
		grep -qv "groups=[^[:space:]]*(%webserver_group)"; then
	echo 'Warning: User %apache_user was not included in the group %webserver_group!'
	%_bindir/gpasswd -a %apache_user %webserver_group
	echo '     Added user %apache_user to group %webserver_group.'
fi
if [ -e %old_apache_home -a ! -e %apache_datadir ]; then
	mkdir -p `dirname %apache_datadir`
	ln -s %old_apache_home %apache_datadir
fi

# FIXME: see #2920
#post common
#find %apache_logdir -group %apache_webmaster -print0 \
#| xargs -0 chgrp %apache_group

%post manual
ln -snf %_docdir/apache-manual-%apache_version %apache_datadir/apache/manual

%preun manual
if [ $1 = 0 ]; then
	rm -f %apache_datadir/apache/manual
fi

%post base
%post_service httpd

%preun base
%preun_service httpd
## XXX: is this correct with standalone httpd-perl??
## => commenting out as of 1.3.32
#if [ $1 = 0 ]; then
#	rm -rf %apache_logdir/*
#fi

%post mod_perl-base
%post_service httpd-perl

%preun mod_perl
%preun_service httpd-perl
%postun mod_perl-base
if [ -e %_sbindir/apachectl ]; then
	%_sbindir/apachectl update
fi

%post -n mod_perl-doc
ln -snf %_docdir/mod_perl-doc-%mod_perl_doc_version \
	%apache_htdocsaddondir/mod_perl

%preun -n mod_perl-doc
if [ $1 = 0 ]; then
	rm -f %apache_htdocsaddondir/mod_perl
fi

%post suexec
if [ -e %_sbindir/apachectl ]; then
	%_sbindir/apachectl update
fi

%postun suexec
if [ -e %_sbindir/apachectl ]; then
	%_sbindir/apachectl update
fi

%pre cgi-bin-test-cgi
%pre_webserver_cgi_bin_control cgi-bin_test-cgi

%post cgi-bin-test-cgi
%post_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_test-cgi

%preun cgi-bin-test-cgi
%preun_webserver_cgi_bin_control cgi-bin_test-cgi

%postun cgi-bin-test-cgi
%postun_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_test-cgi

%triggerpostun cgi-bin-test-cgi -- apache-common < 1.3.37rusPL30.23-alt1.1, apache-cgi-bin < 1.3.41rusPL30.23-alt4.7.3, apache2-cgi-bin < 2.2.9-alt10, apache2-cgi-bin-test-cgi
%triggerpostun_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_test-cgi

%pre cgi-bin-printenv
%pre_webserver_cgi_bin_control cgi-bin_printenv

%post cgi-bin-printenv
%post_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_printenv

%preun cgi-bin-printenv
%preun_webserver_cgi_bin_control cgi-bin_printenv

%postun cgi-bin-printenv
%postun_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_printenv

%triggerpostun cgi-bin-printenv -- apache-common < 1.3.37rusPL30.23-alt1.1, apache-cgi-bin < 1.3.41rusPL30.23-alt4.7.3, apache2-cgi-bin < 2.2.9-alt10, apache2-cgi-bin-printenv
%triggerpostun_webserver_cgi_bin_control -s symlink_root_noexec cgi-bin_printenv

%files datadirs
%dir %_datadir/%name/
%dir %_datadir/%name/cgi-bin/

%files cgi-bin-test-cgi
%_controldir/cgi-bin_test-cgi
%attr(644,root,root) %_datadir/%name/cgi-bin/test-cgi

%files cgi-bin-printenv
%_controldir/cgi-bin_printenv
%attr(644,root,root) %_datadir/%name/cgi-bin/printenv

%files cgi-bin

%files html
%attr(664,root,%apache_webmaster) %config(noreplace) %apache_htdocsdir/*html*
%attr(664,root,%apache_webmaster) %config(noreplace) %apache_htdocsdir/*.txt
%attr(664,root,%apache_webmaster) %config(noreplace) %apache_htdocsdir/*.gif
%attr(604,root,%apache_group) %apache_htdocsdir/README.ALT
%attr(604,root,%apache_group) %apache_htdocsdir/TUNING.ALT

%files icons
%defattr(644,root,%apache_webmaster,2775)
%apache_iconsdir/README*
%apache_iconsdir/*.gif
%apache_iconsdir/*.png
%apache_iconssmalldir/*.gif
%apache_iconssmalldir/*.png

%files common
%dir %apache_basedir/
%dir %apache_datadir/apache/
%_sbindir/ab
%_sbindir/logresolve
%_sbindir/rotatelogs
%_bindir/*

%attr(750,root,%apache_webmaster) %dir %apache_confdir/
%config(noreplace) %apache_confdir/magic
%config(noreplace) %apache_confdir/apache-mime.types
%dir %apache_confdir/vhosts/
%config(noreplace) %apache_confdir/vhosts/*.conf
%dir %apache_vhconfdir/
%config(noreplace) %apache_vhconfdir/*.conf
%dir %apache_addonconfdir/
%dir %apache_modconfdir/
%config(noreplace) %apache_modconfdir/*.conf
%apache_conf.default
%apache_confdir/magic.default
%apache_confdir/apache-mime.types.default
%apache_confdir/tables

%apache_loglink

%defattr(644,root,root,755)
%attr(750,root,%apache_group) %dir %apache_logdir/
%attr(2770,root,%apache_group) %dir %_cachedir/httpd/

%attr(750,root,%apache_group) %dir %apache_tmpdir/
%attr(2770,root,%apache_group) %dir %apache_tmpdir/tmp/
%attr(2770,root,%apache_group) %dir %apache_tmpdir/sessions/
%attr(2770,root,%apache_group) %dir %apache_tmpdir/uploads/

%_mandir/man?/*

%config(noreplace) %_sysconfdir/logrotate.d/apache

%doc README* LICENSE ABOUT_APACHE CHANGES.rus*
%doc ../EAPI-%EAPI_version/pkg.eapi/README.EAPI

%if_with mod_deflate
%doc ../mod_deflate-%mod_deflate_version/CHANGES.mod_deflate*
%doc ../mod_deflate-%mod_deflate_version/LICENSE.mod_deflate
%doc ../mod_deflate-%mod_deflate_version/readme.mod_deflate.ru.html
%endif

%files

%files base
%_initdir/httpd
%_sbindir/apachectl
%_sbindir/httpd
%apache_apxs
%config(noreplace) %apache_conf
%config(noreplace) %_sysconfdir/monitrc.d/apache
%dir %apache_moduledir/
%apache_moduledir/*
%apache_modulelink

%condstopstart_webdir/httpd-cond*

%files full

%files mod_perl

%files mod_perl-base
%_initdir/httpd-perl
%_sbindir/apachectl-perl
%_sbindir/httpd-perl
%dir %apache_moduleperldir/
%apache_moduleperldir/*
%apache_moduleperllink
%_sbindir/apxs-perl
%config(noreplace) %apache_confdir/httpd-perl.conf
%dir %apache_addonconfdir/
%config(noreplace) %apache_addonconfdir/proxied_handlers.pl
%perl_vendor_archlib/Apache*
%perl_vendor_archlib/Bundle*
%perl_vendor_archlib/mod_perl*
%perl_vendor_autolib/Apache*
%attr(3771,root,%apache_group) %dir %apache_datadir/perl/

%condstopstart_webdir/httpd-perl-cond*

%files mod_perl-full

%files -n mod_perl-doc
%doc perldocs/*

%files manual
%doc manual/*

%files -n rpm-build-%name
%_rpmlibdir/%name-files.req.list

%files devel
%dir %_includedir/%name/
%_includedir/%name/*

%files suexec
%attr(4710,root,%apache_group) %_sbindir/suexec

# TODO
# - seperate apache-mod_perl-devel ?
# - buildreq plugs "apache-mod_perl" build dependency somehow :-/
# - update fuzzy patches?
# - seperate htpasswd
# - include /etc/monitrc.d/apache ?
# - control suexec?
# - fix all ugly hacks!
# - macro for %_cachedir/httpd/

%changelog
* Tue Feb 21 2012 Aleksey Avdeev <solo@altlinux.ru> 1.3.42rusPL30.24-alt4
- Add condstopstart-web scripts for httpd-perl

* Tue Feb 14 2012 Aleksey Avdeev <solo@altlinux.ru> 1.3.42rusPL30.24-alt3
- Add scripts for condstopstart-web

* Wed Feb 01 2012 Aleksey Avdeev <solo@altlinux.ru> 1.3.42rusPL30.24-alt2
- Use gpasswd -a in %%pre %%name-common (Closes: #23240)

* Thu Oct 13 2011 Alexey Tourbin <at@altlinux.ru> 1.3.42rusPL30.24-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.3.42rusPL30.24-alt1.1
- rebuilt with perl 5.12

* Tue Mar 16 2010 Aleksey Avdeev <solo@altlinux.ru> 1.3.42rusPL30.24-alt1
- 1.3.42rusPL30.24 (Closes: #22912)
- Security fixes (CVE-2010-0010)
- Generate SSL key from httpd-perl initscript

* Mon Oct 12 2009 Denis Smirnov <mithraen@altlinux.ru> 1.3.41rusPL30.23-alt8
- generate SSL key from initscript

* Fri May 22 2009 Aleksey Avdeev <solo@altlinux.ru> 1.3.41rusPL30.23-alt7
- Update message in %%pre common (Closes: #19602)
  (thanks to Sergey Vlasov <vsu altlinux org>)
- mod_perl-doc: fix package install

* Tue Oct 28 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3.41rusPL30.23-alt6
- Fix symlink for cgi-bin scripts created

* Tue Oct 14 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3.41rusPL30.23-alt5
- Add build subpackages:
  + %%name-datadirs -- data dirs
  + %%name-cgi-bin-test-cgi and %%name-cgi-bin-printenv -- cgi-bin scripts
    (use control for facility)

* Tue Aug 19 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3.41rusPL30.23-alt4.7
- NMU
- Add build subpackages (#16353):
  + %%name-base and %%name-mod_perl-base (not requires a webserver-cgi-bin,
    webserver-html and webserver-icons)
  + %%name-fill and %%name-mod_perl-full (requires a %%name-cgi-bin,
    %%name-html and %%name-icons)
- Add auto adding user %%apache_user to group %%webserver_group
- Add httpd provides in %%name-base and %%name-mod_perl-base subpackages
  (#13665)

* Sat Aug 16 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3.41rusPL30.23-alt4.6
- NMU
- Add %%apache_datadir/apache/ dir in %%name-common subpackage
- Move manual dir (%%apache_htdocsdir/manual) to %%apache_datadir/apache/manual

* Fri Aug 15 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3.41rusPL30.23-alt4.5
- NMU
- Rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Tue Jul 15 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3.41rusPL30.23-alt4.4
- NMU
- Removed version of the webserver-{cgi-bin,html,icons}

* Mon Jul 14 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3.41rusPL30.23-alt4.3
- NMU
- Unset BuildArch %%_target_cpu
- Use rpm-macros-apache (Closes: #16346)
- Add build subpackage for ALT Linux RPM Packaging Policy:
  + rpm-build-%%name

* Thu Jun 26 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3.41rusPL30.23-alt4.2
- NMU
- Add using webserver-common package:
  + removing altlinux.png
  + removing Provides dirs
    %%apache_datadir/{,cgi-bin/,html/{,addon-modules/},icons/{,small/}}
  + adding %%apache_user to %%webserver_group
- Create subpackages:
  + %%name-cgi-bin
  + %%name-manual-addons
  + %%name-html
  + %%name-icons
- Set BuildArch to noarch for subpackages

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.41rusPL30.23-alt4.1
- Automated rebuild with libdb-4.7.so.ALT/Daedalus/apache2/spec

* Sat Apr 19 2008 Michael Shigorin <mike@altlinux.org> 1.3.41rusPL30.23-alt4
- revisit #11053, complete the fix (thanks lakostis@ again)

* Sat Apr 19 2008 Michael Shigorin <mike@altlinux.org> 1.3.41rusPL30.23-alt3
- added monit support
- removed unpackaged sample configuration snippets
- cleaned up pod files packaged into both apache-mod_perl and mod_perl-doc
  (left them in mod_perl-doc package only)

* Mon Mar 31 2008 Michael Shigorin <mike@altlinux.org> 1.3.41rusPL30.23-alt2
- rediffed/applied 1.3.23 patch by Alex Pinzhenin <ap ur ru> to limit
  mod_rewrite looping potential by putting a cap on internal redirect 
  count (50 by default) and RewriteRule-per-query count (300 by default);
  http://www.opennet.ru/base/patch/mod_rewrite_loop.txt.html
  http://www.lexa.ru/apache-talk/msg06354.html

* Sat Jan 19 2008 Michael Shigorin <mike@altlinux.org> 1.3.41rusPL30.23-alt1
- 1.3.41 contains security fix for:
  + CVE-2007-6388: mod_status: ensure refresh parameter is numeric to prevent
    a possible XSS attack caused by redirecting to other URLs)
- 1.3.40 (unreleased) contains security fixes for:
  + CVE-2007-5000: mod_imap: fix cross-site scripting issue
  + CVE-2007-3847: mod_proxy Windows/NetWare-specific DoS
  + CVE-2007-3304: more efficient patch, also fixes bogus "Bad pid" errors
- http://www.apache.org/dist/httpd/CHANGES_1.3.41 for details
- updated EAPI to hand-made 2.8.30a with build fix kindly sent in 
  by Dan Muey <dan cpanel net> (rolled into EAPI tarball by me;
  releasing as 2.8.30a-1.3.41 along with mod_ssl)

* Wed Oct 03 2007 Michael Shigorin <mike@altlinux.org> 1.3.39rusPL30.23-alt2
- modify packaged httpd.conf to disable directory autoindexing by default
  (/home/*/public_html stay indexed though); you might want to reconsider
  that in case the configuration wasn't touched at all (thus will be replaced
  during package upgrade) but directory indexes are needed (fixes #12898,
  thanks Timur Batyrshin <batyrshin ieml ru> for proposal/discussion/patch)

* Thu Sep 13 2007 Michael Shigorin <mike@altlinux.org> 1.3.39rusPL30.23-alt1
- 1.3.39 merges security fixes for:
  + CVE-2006-5752: possible XSS attack against mod_status
    (exploitation requires public server-status page and ExtendedStatus enabled
    and a browser which performs charset "detection")
  + CVE-2007-3304: ensure that the parent process cannot be forced to kill
    non-child processes by checking scoreboard PID data with parent process
    privately stored PID data [this one was fixed by a patch before]
- upstream mime.types updated to current IANA registry and common unregistered
  types that the owners refuse to register (see apache-mime.types.default)
- icons/README.html instead of icons/small/README.txt
- there was no Apache 1.3.38
- updated EAPI to 2.8.30

* Thu Aug 30 2007 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.23-alt6
- changed conftest() usage in initscript so that running processes
  which are still using valid configuration wouldn't be terminated
  if current configuration test fails; thanks nginx.init by mithraen@
  for bringing this to my attention

* Tue Jul 31 2007 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.23-alt5
- merged security fix from RHEL2.1 (RH#245116):
  + CVE-2007-3304 (DoS by referencing an arbitrary process ID in scoreboard
    which then gets SIGUSR1 from master process; requires scripting ability)

* Tue Jun 26 2007 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.23-alt4
- verified and disambiguated mime types; thanks Denis Smirnov (mithraen@)
  for a linter pass (fixes: #12141, #11461)

* Fri Apr 06 2007 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.23-alt3
- rebuilt against recent libmm

* Thu Mar 29 2007 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.23-alt2
- added minimal patch for mod_perl aimed at fixing CVE-2007-1349:
  DoS possibility with specially crafted requests in "PerlRun.pm"
  that uses the "path_info" variable without properly escaping it;
  thanks Randal L. Schwartz (merlyn stonehenge com) for a patch
  (seems to be also in mod_perl SVN)
- NB: mod_perl 1.30 is released but differs quite significantly,
  no time to fix/build/test properly

* Mon Mar 12 2007 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.23-alt1
- updated RA to PL30.23
- wrapped LogFormat in default httpd{,-perl}.conf with IfModule
  (#11053; lakostis@ proposed to borrow from apache2 package)

* Fri Dec 22 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt9
- disable httpd, httpd-perl services startup by default:
  that might lead to undesired consequences in case of 
  "accidentally" installed packages and/or forgetting
  about them while configuring services; see also [ru]:
  http://lists.altlinux.org/pipermail/devel/2006-December/039909.html

* Thu Nov 23 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt8
- bring SysV vhosts configuration support to mod_perl part of apache
  (thanks Alexey I. Froloff (raorn@) for nice #10308):
  + httpd-perl.conf: Include conf/vhosts/Vhosts-perl.conf
  + add vhosts/Vhosts-perl.conf and vhosts-perl.d/
- got back some changes from alt6 (reverted wholesale in alt7):
  + removed remnants of libdb1
  + fixed gdbm support for mod_rewrite
  + move server child hard limit constant to a macro 
    (still 1024 by default, just as in patch9 still left
    in src.rpm just in case too but not applied anymore)
    (the bug was #5748, for reference)
- added TUNING.ALT file with tips on performance tuning 
  (regarding #5748 again)
- minor spec cleanup (more intrusive one pending)

* Sat Oct 21 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt7
- roll back alt6* changes since they are too intrusive by now,
  those who need log files or static content larger than 2Gb
  are advised to rotate logs, use nginx for downloads, or look
  at https://bugzilla.altlinux.org/show_bug.cgi?id=9382 for
  working, but resulting in binary incompatible apache, spec
- added hint on mod_rewrite/mod_security order to default httpd.conf

* Tue Oct 17 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt6.1
- few more feeble tweaks at LFS (these will likely fail -- upstream
  seems to have had hostile enough stand to "that 1.3 being preferred
  to 2.0" to break former ways of enabling LFS on it, telling people
  should wait until 2.2; see also apache bugs #17453, #36417)

* Sun Oct 15 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt6
- scalability improvements:
  + support large logfiles (>2Gb) by default (#9382);
    thanks eostapets@ for alarm and raorn@ for sample spec
  + hopefully fixed gdbm support for mod_rewrite (by raorn@
    in the same stripped-down/fixed-up spec)
  + move server child hard limit constant to a macro
    (still 1024 by default, just as in patch9 still left
    just in case too)
- s/libdb1-devel/libdb4-devel/ (might break 2.2 build?)
- folks, I need proposals on #2907...

* Sat Oct 14 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt5
- added application/x-java-jnlp-file, application/x-xpinstall
  to mime.types (courtesy of zerg@, see bug #10088)
- added commented-out example of editor backup file protection
  to default httpd.conf, httpd-perl.conf (#8489)

* Sat Sep 30 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt4.1
- oops, ServerSignature was really belonging to later 
  section (and "off" was overridden with "on" there");
  thanks to Pavel Usischev <Usischev/gmail> for #10055

* Tue Sep 26 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt4
- implement bugchancement #10038 (ServerSignature Off;
  ServerTokens ProductOnly in default configuration)
  thanks thresh@ and hiddenman@ for reminder

* Fri Sep 01 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt3
- fix #9928 (default mod_realip.conf); thanks vvk@

* Wed Aug 16 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt2
- NameVirtualHost-related fix for default sample configuration
  (what a shame on me!, and thanks Pavel Usischev for #8385)

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 1.3.37rusPL30.22-alt1
- 1.3.37
  + security fix for CVE-2006-3747:
    mod_rewrite: Fix an off-by-one security problem in the ldap scheme
    handling.  For some RewriteRules this could lead to a pointer being
    written out of bounds.  Reported by Mark Dowd of McAfee.

* Mon Jun 19 2006 Michael Shigorin <mike@altlinux.org> 1.3.36rusPL30.22-alt1
- 1.3.36
  + security fixes merged upstream (patch96 removed)
  + 1.3.35 was lucky enough to get missed (regression reported,
    and fixes were irrelevant to this package ayways)

* Tue Mar 21 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.34rusPL30.22-alt4
- Applied additional fixes required for ld --as-needed.
- Added build time check for unresolved symbols in DSOs.
- Replaced macros for standard unix commands with commands themselves.

* Mon Mar 20 2006 Michael Shigorin <mike@altlinux.org> 1.3.34rusPL30.22-alt3
- applied joint fixes by Denis Smirnov (mithraen@) and Dmitry Levin (ldv@):
  + Fixed building with -Wl,--as-needed.
  + Quoted macros in changelog.
- thanks!

* Wed Jan 25 2006 Michael Shigorin <mike@altlinux.org> 1.3.34rusPL30.22-alt2
- security fix for CVE-2005-3352:
  + cross-site scripting (XSS) vulnerability in the mod_imap module of Apache
    httpd before 1.3.35-dev allows remote attackers to inject arbitrary web
    script or HTML via the Referer when using image maps.
  + patch taken from Debian

* Thu Oct 27 2005 Michael Shigorin <mike@altlinux.org> 1.3.34rusPL30.22-alt1
- 1.3.34
- official security fixes:
  + CVE-2005-2088: If a request contains both Transfer-Encoding and
    Content-Length headers, remove the Content-Length, mitigating some HTTP
    Request Splitting/Spoofing attacks.
  + Added TraceEnable [on|off|extended] per-server directive to alter the
    behavior of the TRACE method.
  + please note that CAN-2005-2088 fix (patch95) was already included
    in 1.3.33rusPL30.20-alt4
- added default localhost configuration for mod_realip;
  thanks Denis Smirnov (mithraen@)
- updated EAPI to 2.8.25
- updated RA to PL30.22

* Wed Oct 19 2005 Alexey Gladkov <legion@altlinux.ru> 1.3.33rusPL30.20-alt6
- NMU: rpm macros fix.

* Mon Oct 03 2005 Michael Shigorin <mike@altlinux.org> 1.3.33rusPL30.20-alt5
- Mon Oct 03 2005 Artem K. Jouravsky <ujo@altlinux.ru> 1.3.33rusPL30.20-alt5
  + added mod_accel to current builds; off by default (#8029)
  + removed SMP incompatible build

* Thu Sep 08 2005 Michael Shigorin <mike@altlinux.org> 1.3.33rusPL30.20-alt4
- added SVN patch for CAN-2005-2088 security vulnerability:
  when acting as an HTTP proxy, Apache 1.3 allows remote attackers to poison
  the web cache, bypass web application firewall protection, and conduct XSS
  attacks via an HTTP request with both a "Transfer-Encoding: chunked" header
  and a Content-Length header, which causes Apache to incorrectly handle and
  forward the body of the request in a way that causes the receiving server
  to process it as a separate HTTP request, aka "HTTP Request Smuggling."
  + thanks for SVN pointer to Ubuntu
- fixed small port-related problem in sample Vhosts.conf
  (thanks Alexey Borovskoy (alb@) for notify/fix; also in alt3.M24.1) 

* Fri Sep 02 2005 Michael Shigorin <mike@altlinux.org> 1.3.33rusPL30.20-alt3
- whoops, README.ALT wasn't getting packaged (updated too)
- altlinux-release build dependency appears illegal
  (long unneeded though)
- Wed Aug 24 2005 Michael Shigorin <mike@altlinux.org>
  + exchanged httpd and httpd-perl startup/shutdown order;
    see README.ALT for further details on mod_perl setup (#4994, #6437)
    thanks combr@, tma@, solo@, Ivan Adzhubey for discussion and fixes
    (you *will* need to chkconfig them on for this to apply)
  + rolled back #2928 workarounds (should be unneeded)
  + hard kill remaining processes after normal stop() part
  + fixed #6351 (delaycompress in logrotate; may influence #3153)
    thanks dfo@, sorry ldv@
  + fixed a transition bug in /etc/init.d/httpd::conftest()
  + UseCanonicalName Off in httpd{,-perl}.conf (#7704)
  + updated and extended README.ALT
- Thu Feb 17 2005
  + added missing NameVirtualHost directive to default Vhosts.conf
- Sat Feb 12 2005
  + Vhosts.conf thinko fix suggested by Alexey Morozov (morozov@)
    (Aug 24: could have lost that.... can't remember details now)
- Sat Jan 29 2005
  + macros extended (see README.ALT); also #1735, #5634, #5989
  + re-fixed #4235 (weird hostname hack)
  + implemented separate TMPDIR (addon modules should follow) (#5989)
  + disabled mod_charset for mod_perl (hm... #2941-related)
  + commented out "AddDefaultCharset iso8859-1" by default (#5754)
  + added %%apache_vhostdir and %%apache_vhconfdir (#5634)
  + upped HARD_SERVER_LIMIT from 256 to 1024 (#5748; needs additional
    /etc/security/limits.conf tweaking to actually happen)
  + changed %%suexec_docroot from /home to %apache_home (#2461)
  + changed suexec binary permissions (see #5309)
    from 4711 root:root
      to 4710 root:%apache_group
  + changed TMPDIR in initscripts to use more specific location than /tmp
    so that you can restrict apache access to that by ACL and further
    configure php and other software running as apache (#5989)
  + added patch to consult POSIX ACLs on CGI execution decision
    (#4987; disabled by default, build --with acl_support to enable)

* Mon Dec 20 2004 Denis Smirnov <mithraen@altlinux.ru> 1.3.33rusPL30.20-alt2
- mod_realip added

* Tue Nov 02 2004 Michael Shigorin <mike@altlinux.ru> 1.3.33rusPL30.20-alt1
- 1.3.33 (minor security fixes)
- security fixes officially released (patch93 removed)
- reverse proxy functionality restored (broken in 1.3.32 -- #5435);
  thanks to Leonid Shalupov <ls ls9707 spb edu> for alerting
- added htpasswd patch by Larry Cashdollar <lwc vapid ath cx>
  (unchecked buffer operations; not much of an issue though)

* Wed Oct 27 2004 Michael Shigorin <mike@altlinux.ru> 1.3.32rusPL30.20-alt2.1
- fixed build w/o mod_deflate in addition to -alt2 security fixes
  (thanks to Alexey Beleckiy <sinister emt com ua>)

* Sat Oct 23 2004 Michael Shigorin <mike@altlinux.ru> 1.3.32rusPL30.20-alt2
- updated security fixes (CAN-2004-0940):
  mod_include.c patch from CVS (1.3.33-dev)
  thanks to Vladimir Lettiev (crux@) for reminding
- see also changelog entry for alt1 (CAN-2004-0492)

* Fri Oct 22 2004 Michael Shigorin <mike@altlinux.ru> 1.3.32rusPL30.20-alt1
- 1.3.32 (security fixes)
- CAN-2004-0492 (cve.mitre.org):
  Reject responses from a remote server if sent an invalid (negative)
  Content-Length.
- added fix off/for http://www.securitylab.ru/48807.html;
  thanks to Vladimir Lettiev (crux@) for alerting and verifying
- removed log directory cleanup after package deinstallation
  (seems like a bad practice)

* Mon Aug 16 2004 Michael Shigorin <mike@altlinux.ru> 1.3.31rusPL30.20-alt10
- fixed #5002 (wrong perms on apache-common binaries excl. sample cgi-bin/*),
  thanks Vladimir Lettiev (crux@) for notifying!

* Fri Aug 06 2004 Michael Shigorin <mike@altlinux.ru> 1.3.31rusPL30.20-alt9
- re-fixed #4235.  distributed sourcedir can be evil...
- fixed #1735 (Include conf/addon-modules.d/*.conf), thanks to
  Igor Muratov (migor@) for buggin' me on this long-standing topic

* Thu Jul 22 2004 Michael Shigorin <mike@altlinux.ru> 1.3.31rusPL30.20-alt8
- fixed #4859 (webmaster group could be absent at apache-common installation)
  thanks to Alexander Kuprin (ru_classic mail ru)
- tightened permissions on %apache_root/conf and %apache_home/icons/ as per
  Dmitry Levin's request (#2920) -- please use "webmaster" group for
  content/configuration access and "apache" group for log access

* Wed Jul 07 2004 Michael Shigorin <mike@altlinux.ru> 1.3.31rusPL30.20-alt7
- fixed #4719 (build condition for M22);
  thanks to Pavel Usishev <usishev yandex ru>

* Tue Jun 29 2004 Michael Shigorin <mike@altlinux.ru> 1.3.31rusPL30.20-alt6
- fixed remnants of older internal subpackage versioning
  which barred mod_perl-doc installation; thanks to Dmitry Levin (ldv@)

* Mon Jun 28 2004 Michael Shigorin <mike@altlinux.ru> 1.3.31rusPL30.20-alt5
- finally fixed #3153 (log rotation), thanks to Dmitry Levin (ldv@)
- partially reverted group change introduced in 1.3.28rusPL30.18-alt2:
  %_logdir/httpd permissions changed (#2920)
    from 750,root,%apache_webmaster
    to   750,root,%apache_group
- reworked initscript style detection routine along ldv's advice
  as relying on "Master" in /etc/altlinux-release for old-style seems
  to be getting to the point of being wrong ;-)
- added mod_deflate to current builds; off by default (#2905)
- fixed altlinux.html
- %apache_home/html/*.gif and %apache_home/cgi-bin/* are now
  %%config(noreplace); added %apache_home/html/README.txt (#3715)

* Thu Jun 17 2004 Michael Shigorin <mike@altlinux.ru> 1.3.31rusPL30.20-alt4
- fixed default httpd{-perl,}.conf regarding Ukrainian charsets and content
  preferences; see http://lists.osdn.org.ua/wws/arc/linux/2004-06/msg00103.html,
  thanks to Bohdan Vlasyuk <bohdan kivc vstu vinnica ua>

* Thu Jun 10 2004 Michael Shigorin <mike@altlinux.ru> 1.3.31rusPL30.20-alt3
- fixed mod_proxy security issue; thanks to Dmitry Levin (ldv@) for
  alert/patch.  Details at http://www.guninski.com/modproxy1.html
- fixed "forced localhost" problem (#4235) -- forward-ported the missing part
  from previous initscripts (irrelevant for M22 build)
- RA to PL30.20 (small Referer-related httpd.conf-dist fixes only)

* Fri May 14 2004 Michael Shigorin <mike@altlinux.ru> 1.3.31rusPL30.19-alt2
- fixed ALM2.2 build (release inconsistency barring installation)
- for secfix list see -alt1 changelog record

* Wed May 12 2004 Michael Shigorin <mike@altlinux.ru> 1.3.31rusPL30.19-alt1
- 1.3.31 (security fixes for: CAN-2003-0020, CAN-2003-0987, CAN-2004-0174,
  CAN-2003-0993)
- updated mod_ssl/EAPI to 2.8.17 (for 1.3.31)
- updated RA patch to PL30.19 (for 1.3.29)
- updated mod_perl to 1.29 (minor fixes)
- updated patch1
- refreshed build reqs; put perl-DBM to Sisyphus req branch

* Wed Mar 31 2004 Michael Shigorin <mike@altlinux.ru> 1.3.29rusPL30.18-alt6
- fixed thinko in 1.3.29rusPL30.18-alt3's changelog (s/gorev/horror/)

* Sun Mar 14 2004 Michael Shigorin <mike@altlinux.ru> 1.3.29rusPL30.18-alt6
- hopefully fixed #3153, thanks to Dmitry Alexeyev <dmi qnx org ru>

* Sat Feb 14 2004 Michael Shigorin <mike@altlinux.ru> 1.3.29rusPL30.18-alt5
- rebuilt against libdb4.2

* Wed Jan 28 2004 Michael Shigorin <mike@altlinux.ru> 1.3.29rusPL30.18-alt4
- brought back new and improved ugly hack (since perl and rpm compare
  1.1701 and 1.27 in different the only right ways)

* Mon Jan 19 2004 Michael Shigorin <mike@altlinux.ru> 1.3.29rusPL30.18-alt3
- clarified service version dependency for Sisyphus build
  (#3245; thanks to Andy Gorev (horror@) for investigation)
- added missing /usr/lib/perl5/vendor_perl/i386-linux/cgi_to_mod_perl.pod
  to mod_perl-doc
- rebuilt against recent perl (#3507)

* Sun Nov 02 2003 Michael Shigorin <mike@altlinux.ru> 1.3.29rusPL30.18-alt2
- applied CAN-2003-0020 fix (still not in ASF tree; thanks Dmitry Levin (ldv@)
  for implicit notice and PLD CVS for the patch file)
- updated EAPI to 2.8.16
- introduced %%apache_conf macro (for /path/to/httpd.conf)

* Tue Oct 28 2003 Michael Shigorin <mike@altlinux.ru> 1.3.29rusPL30.18-alt1
- 1.3.29 (major security fixes)
- fixes CAN-2003-0542:
  Fix buffer overflows in mod_alias and mod_rewrite which occurred if
  one configured a regular expression with more than 9 captures.
- 1.3.28rusPL30.18-alt9 didn't really *apply* no_zombies.patch.  Oops.
  Still 1.3.29 has similar change there so should be fixed either.

* Wed Oct 22 2003 Michael Shigorin <mike@altlinux.ru> 1.3.28rusPL30.18-alt9
- FIX:
  appled http://apache.org/dist/httpd/patches/apply_to_1.3.28/no_zombies.patch,
  thanks to Alexey Tourbin (at@) and Alexey Chekushkin <alexey chekushkin com>
  (should eliminate CGI Zombies with suExec, cgiwrap and others)

* Sat Oct 18 2003 Michael Shigorin <mike@altlinux.ru> 1.3.28rusPL30.18-alt8
- fixed %%_sysconfdir/rpm/macros.d/apache (thanks to Alexey Gladkov (legion@)
  for proper file this time)

* Mon Oct 13 2003 Michael Shigorin <mike@altlinux.ru> 1.3.28rusPL30.18-alt7
- fixed #3153 (thanks to Sergey Pinaev <dfo antex ru>):
  /etc/init.d/httpd::reload() was broken

* Tue Oct 07 2003 Michael Shigorin <mike@altlinux.ru> 1.3.28rusPL30.18-alt6
- added %%_sysconfdir/rpm/macros.d/apache (#2463/enhancement);
  needed that for different packages for a long time, thanks for
  initial contents to Alexey Gladkov (legion@)
- removed versioning in perl(mod_perl.pm) provision

* Sun Sep 28 2003 Michael Shigorin <mike@altlinux.ru> 1.3.28rusPL30.18-alt5
- added Provides: perl(mod_perl.pm) to apache-mod_perl
  (should probably seperate extra modules to devel
  and run proper find-requires?)

* Thu Sep 25 2003 Michael Shigorin <mike@altlinux.ru> 1.3.28rusPL30.18-alt4
- updated buildrequires (fix hasher build)

* Thu Sep 11 2003 Michael Shigorin <mike@altlinux.ru> 1.3.28rusPL30.18-alt3
- fixed old-style initscripts for both httpd and httpd-perl (#2950)
  (NB: no changes in Sisyphus initscripts)
- s,/usr/local/apache,%apache_root,g in manpages (TODO)
- changed startup/shutdown order from "85 15" to "81 14" in
  httpd-perl initscripts so that it starts close after httpd (80)
  and stops just before it (15).  This fixes spurious message due
  to #2928 fix (the problem didn't manifest but was here).

* Wed Sep 03 2003 Michael Shigorin <mike@altlinux.ru> 1.3.28rusPL30.18-alt2
- please see changelog for 1.3.28rusPL30.18-alt1
  as more important changes are there
- commented out AddModule mod_charset.c in default config (#2941)
  (in fact, "CharsetDisable On" already keeps it off, but server
  tag would still mention RA and confuse some curious users)
- moved (thanks to pilot@ for notice):
  * %_initdir/httpd and %_sbindir/apachectl
    from %name-common to %name
  * %_sbindir/apachectl-perl
    from %name-common to %name-mod_perl
- %_logdir/httpd permissions changed (#2920)
  from 3770,root,%apache_group
  to    750,root,%apache_webmaster
- %_cachedir/httpd permissions changed (#2921)
  from  750,apache_user,%apache_webmaster
  to   2770,root,%apache_group
- apache.logrotate cleanup/fix:
  * changed "service httpd reload" to use condreload
  * changed create mode from 0664 root.apache to 0644 root.apache
- httpd.init.Sisyphus now checks for some situations involving httpd-perl
  when silent breakage could occur and issues warnings (#2928)
- spec cleanup:
  * switched Url from http://apache.lexa.ru to http://httpd.apache.org:
    focus isn't on RA anymore (left in index.shtml.ru* though)
  * s|%%_var/cache|%%_cachedir|g and similar macro updates
    (ALM2.2 compatible)
  * removed osolete comment-outs:
    + 1.3.23's mod_proxy dance
    + specific treatment of mod_include (generic by now)
    + Obsoletes: secureweb-devel from devel subpackage

* Sun Aug 31 2003 Michael Shigorin <mike@altlinux.ru> 1.3.28rusPL30.18-alt1
- 1.3.28 / RA 30.18
- Major Bugfixes (TM)
- WARNING: VU#379828 (addressed) is suspected to be exploitable
- updated EAPI to 2.8.15
- fixed mod_long_name problem in apxs (by Denis Ovsienko <pilot@>;
  updated to 1.3.28 and merged into Patch1)
- added %%add_findprov_lib_path
- APACHE_HEADER_INSTALL=1 now (#917, #2373)
- workaround for careless: %%config(noreplace) %apache_home/html/*html*
  (#1067, #2510; see also bug comments for proper solution)
- fixed includedir substitution for apxs-perl (#1254)
- *major* revamp of mime.types file (#1331, #2468, #2848)
  (also moved 'application/x-tar' entry there from httpd.conf)
- implemented autodetected / manual distro setting to package initscripts
  for both ALM2.2 (maintenance builds) and Sisyphus (implementation based
  somewhat on aureal-std-up.spec by Alexey Morozov <morozov novosoft ru>)
- %_sysconfdir/httpd/conf/httpd.conf::DirectoryIndex += index.rbx
- spec cleanup:
  * updated BuildRequires
  * fixed Source1 URL typo
  * proper %%SOURCEs instead of poking around in RPM_SOURCE_DIR (%%install)

* Tue Nov 26 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.27rusPL30.16-alt13
- Replaced mdk-mkstemp patch with openbsd-tmp, better optimized one.

* Fri Nov 01 2002 Stanislav Ievlev <inger@altlinux.ru> 1.3.27rusPL30.16-alt12
- rebuild with new perl

* Mon Oct 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.27rusPL30.16-alt11
- %_initdir/httpd: use full path (%_sbindir/httpd).
- %_logdir/httpd: changed permissions to %%attr(3770,root,%apache_group).
- %_sysconfdir/logrotate.d/apache: added directives:
  + sharedscripts;
  + create 0664 root apache.

* Thu Oct 10 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.27rusPL30.16-alt10
- Fixed:
    + access rights for %apache_home/icons/small

* Tue Oct 08 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.27rusPL30.16-alt9
- Security update 1.3.27
- Updated:
    + mod_proxy has been updated to 1.3.27 as well (passes same test suite as 1.3.23's one)
    + mod_perl to 1.27
    + EAPI to 2.8.10 (fixed to be compatible with 1.3.27)

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 1.3.23rusPL30.11-alt8.1
- fixed permisions in mod_perl subpackage

* Tue Jun 18 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.23rusPL30.11-alt8
- Fixed:
    + Apache httpd: vulnerability with chunked encoding (next round)
    + Fix RA patch to suit chunked fixes
    + explicit TMPDIR=/tmp

* Mon Jun 17 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.23rusPL30.11-alt7
- Fixed:
    + Apache httpd: vulnerability with chunked encoding

* Wed Apr 03 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.3.23rusPL30.11-alt6
- Fixed db4 build support.
- Build with db4.
- Build without bind-devel.

* Tue Feb 26 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.23rusPL30.11-alt5
- Updated:
    + EAPI up to 2.8.7 [fixed potential buffer overflow in mod_ssl]

* Fri Feb 22 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.23rusPL30.11-alt4
- Fixed:
    + Configure option SHARED_CORE rule must be exclusive
      for non-mod_perl Apache only (#0000644)
    + Changed (finally) links and logo to ALT Linux

* Thu Feb 21 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.23rusPL30.11-alt3
- Added:
    + SHARED_CORE (libhttpd.so) for Kylix2 Enterprise compatibility
- Reverted:
    + mod_proxy to 1.3.22 state (includes partial EAPI revert)
- spec clean ups

* Thu Feb 21 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.23rusPL30.11-alt2
- Fixed:
    + return codes for 'status' in service scripts

* Fri Feb 08 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.23rusPL30.11-alt1
- 1.3.23 / RA 30.11 / EAPI 2.8.6
- APXS moved to apache-common

* Thu Jan 24 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.22rusPL30.9-alt4
- Fixed:
    + Non-blocked CharsetDisable directive in httpd.conf (#0000441)

* Mon Jan 14 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3.22rusPL30.9-alt3
- Fixed:
    + mod_proxy bug (Andrey Orlov)

* Thu Nov 15 2001 Alexander Bokovoy <ab@altlinux.ru> 1.3.22rusPL30.9-alt2
- Fixed:
    + httpd-perl.conf: Multi language documentation
    + httpd-perl.conf: server side parsed html
    + httpd-perl.conf: enabled mod_negotiation in non-proxied mode

* Wed Oct 24 2001 Alexander Bokovoy <ab@altlinux.ru> 1.3.22rusPL30.9-alt1
- 1.3.22
- Russian Apache PL30.9
- EAPI 2.8.5
- Fixed start up scripts to use sed/tr (PR #0000093)
- Fixed start up script for mod_perl (PR #0000036)
- Fixed typo in Russian summary for mod_perl (PR #0000057)

* Mon Sep 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3.20rusPL30.5-alt2
- Removed duplicated entry of %_sysconfdir/httpd/conf/addon-modules/proxied_handlers.pl
  from %name-common subpackage.
- Built with db3-3.3.11.

* Tue Aug 01 2001 Alexander Bokovoy <ab@altlinux.ru> 1.3.20rusPL30.5-alt1
- New RA patch
- New mod_perl

* Wed Jul 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3.20rusPL30.4-alt5
- Rebuilt with new perl.

* Mon Jun 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3.20rusPL30.4-alt4
- Rebuilt with perl-5.6.1

* Mon Jun 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3.20rusPL30.4-alt3
- Fixed permissions on %apache_home/html.

* Fri Jun 01 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3.20rusPL30.4-alt2
- Fixed permissions in %apache_home.
- Updated init and %%post/%%preun scripts.

* Mon May 21 2001 Alexander Bokovoy <ab@avilink.net>  1.3.20rusPL30.4-alt1
- New Apache version
- Updated:
  + EAPI - 2.8.4
  + CharsetDisable On is set by default
- Fixed:
  + initial fix for permissions in %apache_home
  + dependency for apache-suexec fixed

* Sun Apr 15 2001 Alexander Bokovoy <ab@avilink.net>  1.3.19rusPL30.4-ipl4mdk
- Introducing EAPI to Apache+mod_perl build
- Fixed:
  + logrotate now uses /sbin/service to access httpd and httpd-perl control scripts

* Sun Mar 18 2001 Alexander Bokovoy <ab@avilink.net>  1.3.19rusPL30.4-ipl3mdk
- Disabling expat again

* Sat Mar 17 2001 Alexander Bokovoy <ab@avilink.net>  1.3.19rusPL30.4-ipl2mdk
- Updated:
  + SGI patches took out due unsupported state and many conflicts with 1.3.19
  + httpd.conf (SingleListen unsupported now)
- Fixed:
  + Apache owner/group are apache/apache, not nobody/nobody for httpd.conf/httpd_perl.conf

* Mon Mar 12 2001 Alexander Bokovoy <ab@avilink.net>  1.3.19rusPL30.4-ipl1mdk
- Updated:
  + EAPI 2.8.1
  + RA PL30.4
- Fixed:
  + index.php3 added to the set of index files
  + README.EAPI added to apache-common documentation
  + Use system-wide Expat library

* Mon Mar 05 2001 Alexander Bokovoy <ab@avilink.net>  1.3.19rusPL30.3-ipl1mdk
- Updated:
  + new Apache version
  + 10xpatch ported to 1.3.19 as well as some other patches which were out of sync with Apache source

* Tue Feb 13 2001 Alexander Bokovoy <ab@avilink.net>  1.3.17rusPL30.3-ipl8mdk
- Fixed:
  + logrotate for Apache
  + Documentation for mod_perl
- Updated:
  + mod_perl up to 1.25
- Removed:
  + automatic Apache start

* Wed Feb 08 2001 Alexander Bokovoy <ab@avilink.net>  1.3.17rusPL30.3-ipl7mdk
- Updated:
  + Official Russian Apache PL30.3
- Fixed
  + SGI patch
  + buffered logs
  + Fallback to mod_perl 1.24_01
  + Symlinks to manual

* Sat Feb  3 2001 Mikhail Zabaluev <zabaluev@parascript.com> 1.3.17rusPL30.0-ipl6mdk
- Updated:
  + EAPI 2.8.0
  + mod_perl 1.25
- Added:
  + fix for insecure tempfile creation in htpasswd and htdigest,
    by Vincent Danen, Mandrakesoft

* Thu Feb 01 2001 Alexander Bokovoy <ab@avilink.net>  1.3.17rusPL30.0-ipl5mdk
- Typo fix in httpd.conf
- ra_powered.gif

* Wed Jan 31 2001 Alexander Bokovoy <ab@avilink.net>  1.3.17rusPL30.0-ipl4mdk
- Port to 1.3.17, most patches refreshed
- new httpd.init, http-perl.init

* Wed Dec  6 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.14rusPL30.0-3mdk_mhz
- Added:
  + auto-dependencies (provides) built for perl
- Updated:
  + new, super-robust apxs patch
  + updated init script
  + minor fixes in httpd.conf, protected httpd-perl status from the outside
  + cleaned up spec, ru -> ru_RU.KOI8-R
  + provides pseudo-package 'russian-apache' including patchlevel

* Thu Nov 16 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.14rusPL30.0-2mdk_mhz
- ported 10xpatch for 1.3.14
- changed mod_log_config_buffered patch to apply at the prep stage

* Tue Oct 26 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.14rusPL30.0-1mdk_mhz
- Thee experimental PL30.0

* Wed Oct 25 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.14rusPL29.9-1mdk_mhz
- Apache 1.3.14, EAPI 2.7.1, mod_rewrite patch
- used the last Russian patch considered to be stable (PL30.0 pending)
- applied 10xpatch for 1.3.12 after JMD has tweaked it down
- changed the document root to /var/www, drifting with the RedHad/Mandrake herd
- overhauled config files
- Added KOffice mimetypes
- separate release number for mod_perl-doc
- index.html.ru.* were added to sources, so I revoked my humble one.

* Wed Oct 18 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.7-15mdk_mhz
- the last release before Apache 1.3.14 (waiting for 10xpatch)
- mod_perl 1.24_01
- compiled against perl without largefile support
- mod_perl-doc package
- brought configtest command back to apachectl/init script

* Sat Oct  7 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.7-14mdk_mhz
- merged a bunch of JMD's changes at 1.3.12-30mdk
- added an "official" index.html.ru taken from apache 2.0alpha6
  and slightly modified
- configure without layout using macros supplied by rpm
- macros everywhere

* Thu Aug  3 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.7-13mdk_mhz
- fixed install script problems and paths

* Mon Jul 24 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.7-12mdk_mhz
- new Russian Apache version (further POST fixes) and mm 1.1.3

* Mon Jul 17 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.5-1mdk_mhz
- new version (the patch added in my previous release has been applied)

* Sun Jul 16 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.4-11mdk_mhz
- applied a patch by Viktor Khimenko fixing a bug in charset_bread

* Wed Jul 12 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.4-10mdk_mhz
- disabled EXPAT rule for both servers. PHP 4 builds with its bundled Expat,
  no questions asked
- EAPI 2.6.5

* Thu Jul  6 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.4-9mdk_mhz
- disabled EXPAT rule for apache+mod_perl static build to avoid conflicts
  with XML::Parser

* Mon Jun 26 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.4-8mdk_mhz
- new EAPI, MM and mod_perl versions
- Frontpage and XSSI dropped
- rebuilt against Perl having largefile support stripped

* Thu Apr 27 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.4-7mdk_mhz
- MM lockfiles sit better in /var/lock

* Wed Apr 26 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.4-6mdk_mhz
- fixes to build under an ordinary user
- filelist cleanup

* Mon Apr 24 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.3.12rusPL29.4-5mdk_mhz
- sync with 1.3.12-10mdk
- mm thrown out to be a separate package

* Tue Mar 28 2000 Mikhail Zabaluev <mookid@sigent.ru>
- moved apxs from devel to common -- the tool is too useful

* Fri Mar 24 2000 Mikhail Zabaluev <mookid@sigent.ru>
- mod_perl 1.22. Still leaks memory on restarts being a DSO.

* Tue Mar 21 2000 Mikhail Zabaluev <mookid@sigent.ru>
- Russian Apache 1.3.12 rusPL29.4
- Jean-Michel's add-ons merged back
- SGI patches for 1.3.12 (up to level 1) applied
- index.html.ru translated to Russian :)

* Mon Feb 28 2000 Mikhail Zabaluev <mookid@mu.ru>
- cleaned out apxs

* Sun Feb 20 2000 Mikhail Zabaluev <mookid@mu.ru>
- fixed ServerRoot for good
- fixed MM lockfile path
- added -n mod_perl package for punks

* Mon Feb  7 2000 Mikhail Zabaluev <mookid@mu.ru>
- updated to Russian Apache 1.3.9 rusPL29.2
- fixed .packlist for mod_perl

* Sat Jan 29 2000 Mikhail Zabaluev <mookid@mu.ru>
- ported to Russian Apache PL28.22
- added a version with mod_perl 1.21 linked in
- moved files common for apache and apache-mod_perl to apache-common
- EAPI 2.4.10
- mm and mm-devel are now separate packages too
- most of other add-ons dropped (sorry pals)

* Wed Jan  5 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- moved suexec to another package so it doesn't get installed by default
- added index.php3 as valid index.

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

