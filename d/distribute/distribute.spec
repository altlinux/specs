Name: distribute
Version: 0.4.1
Release: alt8

Summary: Distribute a collection of packages on multiple CDs (especially good for future use with APT)
Summary(ru_RU.KOI8-R): Программа для подготовки набора пакетов к распространению на компакт-дисках (и использования с APT)

Group: Development/Other
Url: http://people.altlinux.ru/imz/devel/distribute
License: GPL

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
Source1: %name-disk-description.template
Patch: %name-%version.patch
Patch1: %name-php.patch

BuildArch: noarch

Requires: common-licenses

#for colorification utils:
Requires: termutils

%description
`%name' program makes doing the tasks related to creating a CD set for
distribution of a collection of packages easier. The tasks include:
laying out the CDs filesystem (splitting the large amount of packages into
several discs etc.), preparing the collection for use by APT
(indexing), creating ISO images and recording the discs.

Periodical updates to the initially distributed collection can be issued with
help of `%name'.

This utility will be useful to you, if you have a collection of
packages on one machine (probably a mirror or a development site), and
you want to bring them to your home computer (and install them
to/upgrade the system there), or if you want to give them to a friend,
or if you would like to distribute the collection of packages for some
other purpose.

Particularly, if you have an ALTLinux Sisyphus based system at home,
and if you want to upgrade it to the current state of Sisyphus, you can
download them to another machine, use `%name' utility there to create a
CD set, come home and use APT to upgrade.

You don't need to be your system's administrator to use `%name': you
can extract the contents to your home directory and use it (by setting
apropriate P_ROOT). For distributing Sisyphus, have a look at
%_sysconfdir/%name/tasks/Sisyphus.

%description -l ru_RU.KOI8-R
Программа `%name' предназначена для упрощения создания компакт-дисков,
содержащих репозиторий пакетов, и позволяет следующее: разделение
пакетов на части по размеру компакт-дисков, создание индексов пакетов
для программы управления пакетами APT, создание образов компакт-дисков
и запись компакт-дисков.

Также с помощью `%name' можно создавать диски, содержащие только обновления
к первоначально сформированному набору пакетов.

Эта программа может быть полезна вам, если вы имеете набор пакетов на
одном компьютере и хотите перенести его на другой компьютер (и установить
их или обновить там систему), или если вы хотите их кому-то передать,
или собираетесь распространять набор пакетов с какими-то другими целями.

В частности, если у вас дома установлена система, периодически обновляемая
из ALTLinux Sisyphus, и вы хотите обновить её до текущего состояния
Сизифа, вы можете скачать пакеты на одном компьютере, затем использовать
программу `%name' для создания набора дисков, прийти домой и обновить
систему с помощью APT.

Вам не требуется быть системным администратором для использования
'%name': вы можете распаковать содержимое пакета в ваш домашний каталог и
использовать программу (установив переменную P_ROOT). Для распространения
Сизифа смотрите в файл %_sysconfdir/%name/tasks/Sisyphus.

%prep
%setup
%patch
%patch1

%build
cp %SOURCE1 usr/lib/distribute
find . -type f | xargs %__subst "s|/usr/lib|%_datadir|g"
mv usr/lib .%_datadir

%install
mkdir -p  %buildroot/
cp -a etc/ usr/ %buildroot/

%files
%doc I_am_not_the_admin Sisyphus example.ru ABOUT NEWS
%_bindir/%name
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/tasks
%_datadir/%name/
%config(noreplace) %_sysconfdir/%name/tasks/Sisyphus

%changelog
* Mon Nov 24 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt8
- use subst instead php for template filling

* Tue Jan 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt7
- move data files to _datadir/name

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt6
- cleanup spec, add packager

* Fri Jul 22 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt5
- add description for recordcd/dvd

* Wed Jun 15 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt4
- enable globals again for php script
- fix description

* Sat Feb 26 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt3
- add --recordcd option for record CD immediately

* Fri Sep 10 2004 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt2
- add russian translation for description
- fix bug #4992
- add --recorddvd option for record DVD immediately (bug #4799)

* Wed Dec 18 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.4.1-alt1
- Remove symbols that apt-0.5 doesn't like from disk identification names
  (`#'; fixes No. 0001720; thanks to pg).
  (For old disks, call `apt-cdrom --rename add' and give them simpler names!)

* Tue Oct 22 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.4.0-alt1
- Fix stopping after clearing is PASSED (when nothing to clear):
  + make all echo_*() always return successfully;
  + make passed() return successfully.

* Tue Oct  8 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.93-alt1
- Rewrite the layouting code (splitMirrorDir()):
  + fix too long args list when creating links
  + fix not counting the first package's size in every disk (that's why they used to be a little larger tahn requested)
  + speed up by means of less calls to getSize() utility (also new)
    and no calls to `basename' (use shell param expansion which I consider
    to be '\n'-safer and faster)
  + use a format-argument for stat (in getSize())
- more strict error code monitoring (should fail on any errors)
- add messages to the clearing stage
- FIXME: now using cp instead of ln in eatFiles() (due to a present bug in ln)
- the pkg requires termutils (the new name for the required ncurses part)

* Sat Jul 11 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.92-alt1
- replace $COLUMNS by ncurses' $(tput cols) (due to changes in bash).

* Thu Jul 11 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.91-alt1
- fix TERM exporting in functions for tput;
- remove -speed option when we call cdrecord(1)
  (please use env vars instead!);

* Thu Jul 11 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.9-alt1
- fix snap-shooting (fix-base) when the source mirror directory is a symlink;
- use ncurses tput(1) program to format messages;
- pass PREFIX and main ARCH to disk-description.php4 (and make use of them);
- add an optional comment for supplementary archs in disk-description.php4;

* Wed Jul 10 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.8-alt1
- generate small srclists for supplemetary archs (like i686 for Sisyphus);
- minor fixes (colored FAILED msgs);
- more GPL notices, updated docs a bit, added NEWS.

* Wed Jul 05 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.7-alt1
- support multiple architectures (i586, i686, ...): one main with SRPMS
  and others without SRPMS-indices (like ALT Sisyphus/i586 and i686 now);
- colorized.

* Wed Jul 03 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.6-alt1
- add the "publish plain lists on remote site" feature.

* Tue Jul 02 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.5-alt1
- add an index.html file on each disk describing how to use various files
  on it;
- fix working with SRPMS-only disks;
- list disk layouts before making ISOs (to check whether all package files
  are there at the moment).

* Fri Feb 15 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.4-alt1
- write full lists of rpm-files in a base-state to every CD (.disk/; both for
  full sets and diffs; suggested by Andrew Borodin in sysiphus@altlinux.ru);
  add a command to generate such lists;
- changed date format used for the title of a fixed base-state;
- add more information about the author and the license;
- fixed some other minor bugs and added minor features;
- (not important for those who install this RPM package)
  renamed the param for specifying the installation (relocation) root, the
  new name is P_ROOT (the old was PREFIX which conflicted with another param).

* Tue Sep 18 2001 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.3-alt1
- An example of using the tool added (comments in Russian).

* Tue Sep 18 2001 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.2-alt1
- Info about the title added.

* Tue Sep 18 2001 Ivan Zakharyaschev <imz@altlinux.ru> 0.3.1-alt1
- more accurate doumentation (see: distribute --help) added.

* Fri Sep 14 2001 Ivan Zakharyaschev <imz@altlinux.ru> 0.2-alt1
- new version: generation of CDs only with the differences made possible
- task configuration file name changed: sisyphus -> Sisyphus

* Wed Sep  5 2001 Ivan Zakharyaschev <imz@altlinux.ru> 0.1-alt1
- first release
# Local Variables:
# compile-command: "rpmbuild -ba distribute.spec"
# End:
