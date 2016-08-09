%define _sbindir /sbin

Name: gpart
Version: 0.3
Release: alt1

Summary: Hard disk partition table reconstruction
Group: System/Configuration/Hardware
License: GPL
Url: https://github.com/baruch/%name/
Packager: Michael Shigorin <mike@altlinux.org>

Source: %url/archive/%version.tar.gz#/%name-%version.tar.gz
Patch: %name-0.3-alt-lfs.patch

Requires: common-licenses

BuildRequires: common-licenses

Summary(ru_RU.UTF-8): Восстановление таблицы разделов жёсткого диска

%description
A tool which tries to guess the partition table of a PC-type
hard disk in case the primary partition table in sector 0 is damaged,
incorrect or deleted.  This is performed by analyzing either hard
disk or its exact copy.

The guessed table can be written to a file or device. Supported
(guessable) filesystem or partition types: DOS/Windows FAT, Linux
ext2 and swap, OS/2 HPFS, Windows NTFS, FreeBSD and Solaris/x86
disklabels, Minix FS, QNX 4 FS, Reiser FS, LVM physical volumes,
BeOS FS, SGI XFS.

%description -l ru_RU.UTF-8
Эта программа пытается определить расположение разделов на
жестком диске в случае, если таблица разделов повреждена,
нарушена или удалена. Для этого анализируется содержимое жесткого
диска (или его побитовой копии). Воссозданная на основании
собранных данных таблица разделов может быть записана в файл или
на устройство.

Поддерживаются следующие типы разделов: DOS/Windows FAT, Linux
ext2 и swap, OS/ 2 HPFS, Windows NTFS, FreeBSD и Solaris/x86
disklabels, Minix FS, QNX 4 FS, Reiser FS, физические тома LVM,
BeOS FS, SGI XFS.

%prep
%setup
%patch

%build
%autoreconf
%configure
%make_build
ln -sf %_licensedir/GPL-2 COPYING

%install
%makeinstall mandir=%buildroot%_mandir bindir=%buildroot/sbin

%files
/sbin/%name
%_man8dir/%name.8*
%doc README* Changes
%doc --no-dereference COPYING

%changelog
* Tue Aug 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- 0.3 (new url)

* Thu Dec 24 2009 Sergey Vlasov <vsu@altlinux.ru> 0.1h-alt8
- Fixed cflags patch:
  + added -fno-strict-aliasing for sloppy old code
  + added -D_FILE_OFFSET_BITS=64 to fix large file support (#22612)
- Dropped broken largefile patch (-D_FILE_OFFSET_BITS=64 is enough).

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 0.1h-alt7
- fixed FTBFS against recent glibc

* Tue Apr 01 2008 Grigory Batalov <bga@altlinux.ru> 0.1h-alt6
- Debian: avoid _llseek call.
- Debian: ext3 mount count fix.

* Wed Dec 26 2007 Michael Shigorin <mike@altlinux.org> 0.1h-alt5
- fixed description (#6418)
- added Packager:

* Thu Dec 20 2007 Michael Shigorin <mike@altlinux.org> 0.1h-alt4
- added O_LARGEFILE patch by Konstantin Uvarin (khedin mail ru)
  (fixes #12117)
- spec macro abuse cleanup
- buildreq

* Tue May  4 2004 Ivan Zakharyaschev <imz@altlinux.ru> 0.1h-alt3
- recognize ReiserFS better (patches by ReiserFS authors; closes: #2853);
- fix compilation (errno issue; Mdk);
- added portability fixes to 64-bit & big-endian platforms (Mdk).

* Sun Nov  3 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.1h-alt2
- add Russian summary & description.

* Thu May  9 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.1h-alt1
- first build for ALT Sisyphus;
- install to /sbin (as other partition and FS management tools);
- include docs: README, COPYING (symlink), Changes;

* Thu Jul 19 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1h-2mdk
- rebuild

* Sun Feb 18 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.1h-1mdk
- First mandrake version.

# end of file
# Local Variables:
# compile-command: "rpmbuild -ba --target=i586 gpart.spec"
# End:
