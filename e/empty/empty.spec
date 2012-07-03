Name:    empty
Version: 0.6.18b
Release: alt1

Summary: Run interactive console applications in batch mode
License: Common Public License
Group:   System/Configuration/Other
Url:     http://%name.sourceforge.net
Source:  http://heanet.dl.sourceforge.net/sourceforge/%name/%name-%version.tgz
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildPreReq: glibc-devel >= 2.0

Summary(ru_RU.KOI8-R): Запуск интерактивных консольных приложений в автоматическом режиме

%description
empty is an utility that provides an interface to execute and/or interact
with processes under pseudo-terminal sessions (PTYs). This tool is definitely
useful in programming of shell scripts designed to communicate with interactive
programs like telnet, ssh, ftp, etc. In some cases empty can be the simplest
replacement for TCL/expect or other similar programming tools because empty:

    * can be easily invoked directly from shell prompt or script
    * does not use TCL, Perl, PHP, Python,... as an underlying language
    * is written entirely in C
    * has small and simple source code
    * can easily be ported to almost all UNIX-like systems

%description -l ru_RU.KOI8-R
Empty - это утилита, которая служит для организации автоматического выполнения
интерактивных консольных приложений, таких как telnet, SSH, FTP и т.д.
Для этого Empty создаёт т.н. псевдотерминальную сессию (PTY),
в которой перехватывает вывод приложения на экран и чтение с клавиатуры.
Затем Empty дожидается вывода от приложения заданных пользователем строк
и отправляет приложению назначенные ответы.

Преимущества Empty перед более известными средствами наподобие TCL/Expect:

    * может быть легко вызвана прямо из командной строки или пакетного сценария
    * не требует для работы TCL, Perl, PHP, Python и прочих монстров
    * написана целиком на Си, имеет небольшой и ясный код
    * легко переносима на любые Юникс-подобные системы

В каталоге документации находятся примеры для запуска различных приложений.

%prep
%setup -q

%build
%__cc %optflags -o %name %name.c -lutil

%install
%__mkdir_p %buildroot{%_bindir,%_man1dir}
%__cp -a empty   %buildroot%_bindir/
%__cp -a empty.1 %buildroot%_man1dir/

%files
%_bindir/%name
%_man1dir/%name.*
%doc README CHANGELOG examples

%changelog
* Sat Oct 17 2009 Ilya Mashkin <oddity@altlinux.ru> 0.6.18b-alt1
- update to new version 0.6.18

* Thu Jan 08 2009 Ilya Mashkin <oddity@altlinux.ru> 0.6.16b-alt1
- update to new version 0.6.16

* Wed Apr  2 2008 Ilya Evseev <evseev@altlinux.ru> 0.6.15b-alt1
- update to new version 0.6.15

* Tue Oct 30 2007 Ilya Evseev <evseev@altlinux.ru> 0.6.12b-alt1
- update to new version 0.6.12

* Thu Jan 18 2007 Ilya Evseev <evseev@altlinux.ru> 0.6.11b-alt1
- update to new version 0.6.11

* Wed Mar 22 2006 Ilya Evseev <evseev@altlinux.ru> 0.6.9b-alt1
- update to new version 0.6.9

* Mon Feb 20 2006 Ilya Evseev <evseev@altlinux.ru> 0.6.8b-alt1
- update to new version 0.6.8

* Tue Dec 20 2005 Ilya Evseev <evseev@altlinux.ru> 0.6.5b-alt1
- update to new version 0.6.5

* Tue Sep 20 2005 Ilya Evseev <evseev@altlinux.ru> 0.6.0b-alt1
- Initial build for ALTLinux

## EOF ##
