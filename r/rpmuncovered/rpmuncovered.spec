Name:		rpmuncovered
Version:	0.3
Release:	alt2
Summary:	Check files for owning by RPM and modification status after installing
License:	GPL
Group:		System/Configuration/Packaging
URL:		http://ilya-evseev.narod.ru/posix/%name
BuildArch:	noarch

Source:		%name-%version.tar.gz

Requires:	perl-RPM
Obsoletes:	microbackup-%name
BuildPreReq:	help2man, perl-RPM

Summary(ru_RU.KOI8-R): Проверка файлов на не-принадлежность RPM-пакетам или модификацию

%description
Small utility for processing list of filenames given in command line
or from stdin. For each file checks owning by any RPM package,
then compares modification time of actual file and appropriate
package record. Diplays filenames not owned by RPM or modified.

%description -l ru_RU.KOI8-R
Данная утилита читает список имён файлов со стандартного входа
и проверяет для каждого из них, принадлежит ли он какому-нибудь
RPM-пакету, и (в случае принадлежности) менялся ли он после установки.
Утилита выводит на консоль имена тех файлов, которые либо
не контролируются RPM, либо изменились после установки.

%prep
%setup -q -c

%install
%__install -pD %name %buildroot%_bindir/%name
%__mkdir_p %buildroot%_man1dir
help2man -N --output=%buildroot%_man1dir/%name.1 \
    --name="little RPM helper for Linux console" ./%name

%files
%_bindir/%name
%_man1dir/%name.*

%changelog
* Mon Dec  6 2004 Ilya Evseev <evseev@altlinux.ru> 0.3-alt2
- fixed build bug: added perl-RPM to BuildPreReq
- fixed bug: invalid email in changelog, prohibited by sisyphus_check

* Sun Dec  5 2004 Ilya Evseev <ilya_evseev@mail.ru> 0.3-alt1
- initial build, replaces microbackup-%name helper,
  started from 0.3 to conform helper version
- added manual page and command line switches
- fixed bug with processing symlinks

## EOF ##
