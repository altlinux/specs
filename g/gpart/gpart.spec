Name: gpart
Version: 0.1h
Release: alt8

Summary: Hard disk partition table reconstruction
Group: System/Configuration/Hardware
License: GPL

Url: http://home.pages.de/~michab/gpart/
Source: %name-%version.tar.bz2
Patch0: gpart-0.1h-ALT-cflags.patch
# The right way to use errno:
Patch1: gpart-errno.patch
# Portability fixes to 64-bit & big-endian platforms (mdk):
Patch2: gpart-0.1h-fixes.patch
Patch3: ftp://ftp.namesys.com/pub/misc-patches/gpart-0.1h-reiserfs-3.6.patch.gz
Patch4: gpart-0.1h-reiserfs-3.6-typo-fix.patch
Patch6: gpart-0.1h-deb-ext3.patch
Patch7: gpart-0.1h-deb-llseek.patch
Patch8: gpart-0.1h-alt-open.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: common-licenses

# Automatically added by buildreq on Thu Dec 20 2007
BuildRequires: common-licenses

Summary(ru_RU.KOI8-R): Восстановление таблицы разделов жёсткого диска

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

%description -l ru_RU.KOI8-R
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
%patch0 -p1 -b .cflags
%patch1 -p1 -b .errno
%patch2 -p1 -b .fixes
%patch3 -p2 -b .reiser
%patch4 -p1 -b .reiser-typo
%patch6 -p1 -b .ext3
%patch7 -p1 -b .llseek
%patch8 -p1 -b .open

%build
%make_build
ln -sf %_licensedir/GPL-2 COPYING

%install
%makeinstall mandir=%buildroot%_mandir bindir=%buildroot/sbin

%files
/sbin/%name
%_mandir/*/*
%doc README Changes 
%doc --no-dereference COPYING

%changelog
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
