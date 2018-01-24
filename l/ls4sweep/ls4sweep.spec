Name: ls4sweep
Version: 0.3.0
Release: alt2

Summary: Policy-based listing old backups for sweeping
License: GPL
Group: Archiving/Backup
Url: http://ilya-evseev.narod.ru/posix/%name
Source0: %url/%name-%version.tar.gz

BuildPreReq: help2man, gcc, glibc-devel, make
BuildPreReq: xsltproc, docbook-dtds, docbook-style-xsl

# %define rman1dir %_mandir/ru/man1

Summary(ru_RU.KOI8-R): Прореживание ежедневных архивных копий по заданным правилам

%description
%name should be used as helper for removing extra old daily-created backups.

Sweeping policy consists from the set of records, where each record contains
the count of intervals (or periods) and the length of one period (in days).
%name checks creation or modification time of given files and displays names
of those when they mismatch policy. Only one file is keeping in each interval.

Consider following command:
    ls4sweep 3:1,2:3,2:10,2:30,3:90,5:365 *.zip
This means:
 - keep daily ZIP-archives in current directory for last 3 days
 - older than 3 days - keep 2 archives with 3-days delta
 - older than 9 days (3*1 + 2*3) - 2 archives with 10-days delta
 - older than one month (3*1 + 2*3 + 2+10) - 2 archives with monthly delta
 - older than 3 months - 3 archives with 90-days delta
 - older than one year - yearly archive for five years
 - display filenames of all remaining stuff

%name output can be directly passed to '| xargs -r /bin/rm -f' command.
When you create archives via cron(8), you can put cleanup via %name call
after creation.

%description -l ru_RU.KOI8-R
Утилита %name предназначена для удаления лишних архивных файлов.
Она проверяет время создания или изменения у указанных файлов
в соответствии с политикой прореживания и распечатывает имена тех из них,
которые могут быть удалены, чтобы не занимать лишнее место.

Политика прореживания состоит из списка, каждый элемент которого
включает в себя количество временнЫх отрезков и длину одного отрезка в днях.
Если в одном отрезке найдено несколько архивов, %name выведет их имена,
за исключением имени самого старого из них.

Например, ls4sweep '3:1,2:3,2:10,2:30,3:90,5:365' *.zip означает:
 - оставить по одному архиву за последние три дня,
 - старше трёх дней - два архива с трёхдневным интервалом,
 - старше девяти дней (3*1 + 2*3) - два с десятидневным интервалом,
 - старше месяца (3*1 + 2*3 + 2*10) - два с месячным интервалом,
 - старше трёх месяцев - три архива с трёхмесячным интервалом,
 - старше года - пять ежегодных архивов,
 - имена всех прочих архивов вывести на консоль.

Созданный ею листинг может быть передан команде '| xargs -r /bin/rm -f'.
Если архивные копии автоматически создаются каждый день через cron(8),
рекомендуется добавить туда и удаление старых архивов с помощью %name.

%prep
%setup -qc

%build
%make

%install
%__mkdir_p %buildroot{%_bindir,%_man1dir}
%__cp -a %name     %buildroot%_bindir/%name
%__cp -a %name.man %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.1*
#rman1dir/%name.1.gz
%doc %name.html TODO LICENSE

%changelog
* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt2
- Updated spec to allow any man page compression.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jan  6 2009 Ilya Evseev <evseev@altlinux.ru> 0.3.0-alt1
- updated to new version 0.3.0 with 64-bit filesystems support

* Fri Oct 14 2005 Ilya Evseev <evseev@altlinux.ru> 0.2.1-alt1
- spec bugfix: URL macro
- added LICENSE file for conforming GNU GPL requirements

* Mon Jun 13 2005 Ilya Evseev <evseev@altlinux.ru> 0.2.0-alt1
- version 0.2.0

* Thu May  5 2005 Ilya Evseev <evseev@altlinux.ru> 0.1.1-alt1
- Initial build

## EOF ##
