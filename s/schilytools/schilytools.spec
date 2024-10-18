%define cdr_major 3.02
%define iso_major %cdr_major
%define star_major 1.7.0
%define smake_major 1.7
%define btcflash_major 1.1
%define cdr_name cdrtools
%define minor %nil
%define alt_rel alt2
%def_with bootstrap

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: schilytools
Version: 2024.03.21
Release: %alt_rel%minor
Epoch: 7

Summary: A collection of command-line utilities originally written by J.Schilling
License: CDDL.Schily and GPL-2.0 and LGPL-2.1 and BSD
Group: Archiving/Cd burning
Url: https://codeberg.org/schilytools/schilytools

# https://codeberg.org/schilytools/schilytools/releases/download/2024-03-21/schily-2024-03-21.tar.bz2
Source: %name-%version.tar

Patch1: cdrtools-mdk-arch-fix.patch
Patch2: cdrtools-3.02a09-alt-conf.patch
Patch3: cdrtools-2.01-alt-rcmdrsh.patch
Patch4: schily-2021.09.18-natspec.patch
Patch5: cdrtools-2.01.01a50-alt-rscsi-man.patch
Patch6: schily-alt-ved.help.patch

# alternatives
BuildRequires(pre): alternatives
%define weight 10

# Automatically added by buildreq on Tue May 25 2004
BuildRequires: libacl-devel libalsa-devel libnatspec-devel
BuildRequires: recode libe2fs-devel gcc-c++ libpulseaudio-devel
%if_without bootstrap
BuildRequires: smake
%endif

# due bindir/compare
Conflicts: ImageMagick-tools

Packager: L.A. Kostis <lakostis@altlinux.ru>

%package -n rscsi
Version: %cdr_major
Summary: The Remote-SCSI protocol gives you SCSI-Anywhere features
Summary(ru_RU.UTF-8): Утилита для работы со SCSI-устройствами по протоколу Remote-SCSI
Group: Archiving/Cd burning
Requires(pre): rscsi-control

%package -n isoutils
Version: %cdr_major
Summary: Utility programs for dumping and verifying iso9660 images
Summary(ru_RU.UTF-8): Утилиты для просмотра и проверки образов в формате iso9660
Group: Archiving/Cd burning
Provides: devdump = %cdr_major, isoinfo = %cdr_major, isovfy = %cdr_major, isodump = %cdr_major

%package -n readcd
Version: %cdr_major
Summary: readcd read or write data Compact Discs
Summary(ru_RU.UTF-8): Утилита для чтения/записи данных с CD
Group: Archiving/Cd burning
Requires(pre): readcd-control

%package -n mkisofs
Version: %iso_major
Summary: Creates an image of an ISO9660 filesystem
Summary(ru_RU.UTF-8): Утилита для создания образов ISO9660
Group: Archiving/Cd burning
Provides: %cdr_name-mkisofs = %cdr_major, cdrecord-mkisofs = %cdr_major
Obsoletes: %cdr_name-mkisofs, cdrecord-mkisofs, mkhybrid, cdrecord-mkhybrid

%package -n cdrecord-classic
Version: %cdr_major
Summary: A command line CD/DVD-Recorder
Summary(ru_RU.UTF-8): Консольная утилита для записи CD/DVD
Group: Archiving/Cd burning
Provides: %cdr_name-cdrecord = %cdr_major, cdrecord = %EVR, dvdrecord = %EVR
Obsoletes: %cdr_name-cdrecord, cdrecord, dvdrecord
Requires(pre): cdrtools-control

%package -n cdda2wav
Version: %cdr_major
Summary: A utility for sampling/copying .wav files from digital audio CDs
Summary(ru_RU.UTF-8): Утилита для копирования треков с Audio CD
Group: Sound
Provides: %cdr_name-cdda2wav = %cdr_major, cdrecord-cdda2wav = %cdr_major
Obsoletes: %cdr_name-cdda2wav, cdrecord-cdda2wav

%package -n star
Version: %star_major
Summary: An alternative implementation of the tar command
Group: Archiving/Backup
Conflicts: rmt

%package -n smake
Version: %smake_major
Summary: An alternative implementation of the make command
Group: Development/Tools

%package -n btcflash
Version: %btcflash_major
Summary: Flash tool for BTC CD drives
Group: Development/Tools

%description
The "Schily" Tool Box is a set of tools originally written by Joerg Schilling.

%description -l ru_RU.UTF-8
Консольные утилиты для работы CD/DVD-рекордерами.
Включает cdrecord, mkisofs, readcd, isoinfo и т.п.

%description -n cdrecord-classic
Cdrecord is an application for creating audio and data CDs on
a CD-Recorder (SCSI/ATAPI).  Cdrecord works with many different
brands of CD recorders, fully supports data, audio, mixed,
multi-session, CD+ discs and provides human-readable error messages.

%description -n cdrecord-classic -l ru_RU.UTF-8
cdrecord - приложение для записи компакт-дисков.  Программа
работает с большинством CD-рекордеров.  Реализована полная
поддержка аудио-, смешанных, мультисессионных и CD+ дисков.

%description -n mkisofs
The mkisofs program is used as a pre-mastering program; i.e., it
generates the ISO9660 filesystem.  Mkisofs takes a snapshot of
a given directory tree and generates a binary image of the tree
which will correspond to an ISO9660 filesystem when written to
a block device.  Mkisofs is used for writing CD-ROMs, and includes
support for creating bootable El Torito CD-ROMs.

Install the mkisofs package if you need a program for writing CD-ROMs.

%description -n mkisofs -l ru_RU.UTF-8
mkisofs - подготавливает данные для записи на компакт-диск,
создавая файловые системы ISO9660.  Программа создает снимок
указанного дерва каталогов и записывает его в виде двоичного
образа, соответствующего файловой системе ISO9660.  mkisofs
можно использовать для создания загрузочных компакт-дисков.

Этот пакет необходим для записи компакт-дисков.

%description -n cdda2wav
Cdda2wav is a sampling utility for CD-ROM drives that are capable of
providing a CD's audio data in digital form to your host.  Audio data
read from the CD can be saved as .wav or .sun format sound files.
Recording formats include stereo/mono, 8/12/16 bits and different
rates.  Cdda2wav can also be used as a CD player.

%description -n cdda2wav -l ru_RU.UTF-8
cdda2wav - программа для копирования треков с аудио компакт-дисков.
Прочитанные данные могут записываться в форматах .wav или .sun.
При записи файлов можно варьировать количество битов на сэмпл и
частоту дискретизации.  cdda2wav можно использовать как плейер.

%description -n rscsi
The Remote-SCSI protocol gives you SCSI-Anywhere features

%description -n rscsi -l ru_RU.UTF-8
Утилита для работы со SCSI-устройствами по протоколу Remote-SCSI

%description -n isoutils
devdump,  isoinfo,  isovfy,  isodump - Utility programs for dumping and
verifying iso9660 images.

%description -n readcd
Readcd is used to read or write Compact Discs.

%description -n star
An alternative implementation of the tar command.

%description -n smake
An alternative implementation of the make command

smake is powerful, but not compatible with GNU make (which is used
by just about everything).

%description -n btcflash
Flash tool for BTC CD drives.

%prep
%setup
%patch1 -p2
%patch2 -p2
%patch3 -p1
%patch4 -p2 -b .natspec
%patch5 -p2
%patch6 -p1

find -type f -print0 |
	xargs -r0 grep -EZl '/etc/default/(cdrecord|rscsi|cdda2ogg|cdda2mp3)' -- |
	xargs -r0 subst 's,/etc/default/\(cdrecord\|rscsi\|cdda2ogg\|cdda2mp3\),/etc/\1.conf,g' --

ln -sf i586-linux-cc.rul RULES/amd64-linux-cc.rul
ln -sf i686-linux-cc.rul RULES/athlon-linux-cc.rulf
find . -name \*.mk|xargs subst 's/INSDIR=\s*lib\s*$/INSDIR=%_lib\n/g'

sed -i -e 's,^INS_BASE=.*,INS_BASE=%prefix,g' DEFAULTS/*
sed -i -e 's,-noclobber,,' cdrecord/Makefile.dfl

# Get rid of old ISO-8859-1 encoded umlaut characters
find . -name "*.c" -o -name "*.h" -o -name "*README*" -type f |xargs recode ISO-8859-1..UTF-8

# Remove lib*/*_p.mk to skip the compilation of profiled libs
rm -f lib*/*_p.mk

%build
%if_with bootstrap
export MAKEPROG=gmake
%else
export MAKEPROG=smake
%endif
# MAKEFLAGS set by rpm confuse psmake :(
unset MAKEFLAGS
# The Makefile system isn't 100%% ready for an SMP build -- can't use -j
$MAKEPROG CC=gcc COPTOPT="%optflags" RUNPATH="" LDOPTX="" SCCS_BIN_PRE="" SCCS_HELP_PRE="" XK_ARCH=%_target_cpu config
$MAKEPROG CC=gcc COPTOPT="%optflags" RUNPATH="" LDOPTX="" SCCS_BIN_PRE="" SCCS_HELP_PRE="" XK_ARCH=%_target_cpu all

%install
%if_with bootstrap
export MAKEPROG=gmake
%else
export MAKEPROG=smake
%endif
unset MAKEFLAGS
$MAKEPROG RUNPATH="" COPTOPT="%optflags" LDOPTX="" SCCS_BIN_PRE="" SCCS_HELP_PRE="" DESTDIR="%buildroot" INS_BASE="%prefix" XK_ARCH=%_target_cpu MANBASE=share install

# We don't need any Solaris-isms in our filesystem...
# Kill dupes
rm %buildroot%prefix/xpg4/bin/{make,sh,od}
# And move the rest to a more reasonable place
mv %buildroot%prefix/xpg4/bin/* %buildroot%prefix/ccs/bin/* %buildroot%_bindir
rmdir %buildroot%prefix/xpg4/bin %buildroot%prefix/ccs/bin
rmdir %buildroot%prefix/xpg4 %buildroot%prefix/ccs

[ -d %buildroot%prefix/sbin ] && mv %buildroot%prefix/sbin/* %buildroot%_bindir && rm -rf %buildroot%prefix/sbin

%if "%_lib" != "lib"
mkdir -p %buildroot%_libdir
mv %buildroot%prefix/lib/*.so* %buildroot%_libdir
%endif

# Not much of a point in shipping static libs and headers for libs used
# only by cdrtools
rm -rf \
%if "%_lib" != "lib"
	%buildroot{%_libdir,%_prefix/lib}/*.a \
%else
	%buildroot%_libdir/*.a \
%endif
	%buildroot%_includedir

# The libraries/headers aren't installed, so we don't need their man
# pages either
rm -rf %buildroot%_man3dir

# Don't conflict with standard tools
# The tools are still available via their s* name
rm -f %buildroot%_bindir/{make,tar,gnutar,sh,cal,diff,od,printf,help} \
%buildroot%_man1dir/{make,tar,gnutar,sh,bosh,jsh,pfsh,pbosh,cal,diff,od,printf,help}.1
rm -f %buildroot%_bindir/{bosh,pfsh,jsh}
for prog in bosh pfsh jsh; do
	ln -s -nf /bin/sh %buildroot%_bindir/"$prog"
done

install -p -m755 cdda2wav/cdda2ogg %buildroot%_bindir/

ln -s -nf mkisofs %buildroot%_bindir/mkhybrid
rm -f %buildroot%_bindir/sccspatch
ln -s -nf spatch %buildroot%_bindir/sccspatch

for prog in cdrecord rscsi; do
	mv %buildroot%_sysconfdir/default/"$prog" %buildroot%_sysconfdir/"$prog".conf
done
touch %buildroot%_sysconfdir/{cdda2mp3,cdda2ogg}.conf

# rename cdrecord to -classic
mv %buildroot%_bindir/cdrecord %buildroot%_bindir/cdrecord-classic
mv %buildroot%_man1dir/cdrecord.1 %buildroot%_man1dir/cdrecord-classic.1
mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/rscsi %buildroot%_sbindir/rscsi
mv %buildroot%_bindir/rmt %buildroot%_sbindir/rmt
# rename other tools to -classic for alternatives
for prog in readcd cdda2wav; do
	mv %buildroot%_bindir/"$prog" %buildroot%_bindir/"$prog"-classic
	mv %buildroot%_man1dir/"$prog".1 %buildroot%_man1dir/"$prog"-classic.1
done

for prog in mkisofs mkhybrid; do
	mv %buildroot%_bindir/"$prog" %buildroot%_bindir/"$prog"-classic
done

chmod 700 %buildroot%_bindir/{cdrecord-classic,readcd-classic}
chmod 700 %buildroot%_sbindir/rscsi

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir/{cdrecord,mkisofs,cdda2wav}
install -p -m644 AN-* *GPL* *CDDL* COPYING \
	%buildroot%docdir/

# get rid of README* madness
install -p -m644 READMEs/README.linux* cdrecord/README.* \
	%buildroot%docdir/cdrecord/

pushd mkisofs
	install -p -m644 ChangeLog* README* hdisk.pl \
		%buildroot%docdir/mkisofs/
popd

pushd cdda2wav
	install -p -m644 Frontends HOWTOUSE OtherProgs README THANKS TODO \
		cdda2mp3* cdda_links pitchplay readmult tracknames.* FAQ \
		%buildroot%docdir/cdda2wav/
popd

mkdir -p %buildroot%_altdir
cat <<__EOF__ >%buildroot%_altdir/cdrecord-classic
%_bindir/cdrecord	%_bindir/cdrecord-classic	%weight
%_man1dir/cdrecord.1.xz	%_man1dir/cdrecord-classic.1.xz	%_bindir/cdrecord-classic
%_bindir/dvdrecord	%_bindir/cdrecord-classic	%weight
%_man1dir/dvdrecord.1.xz	%_man1dir/cdrecord-classic.1.xz	%_bindir/cdrecord-classic
__EOF__

cat <<__EOF__ >%buildroot%_altdir/readcd
%_bindir/readcd	%_bindir/readcd-classic	%weight
%_man1dir/readcd.1.xz	%_man1dir/readcd-classic.1.xz	%_bindir/readcd-classic
__EOF__

cat <<__EOF__ >%buildroot%_altdir/mkisofs
%_bindir/mkisofs	%_bindir/mkisofs-classic	%weight
%_man1dir/mkisofs.1.xz	%_man8dir/mkisofs.8.xz	%_bindir/mkisofs-classic
%_bindir/mkhybrid	%_bindir/mkhybrid-classic	%weight
%_man1dir/mkhybrid.1.xz	%_man8dir/mkhybrid.8.xz	%_bindir/mkhybrid-classic
__EOF__

cat <<__EOF__ >%buildroot%_altdir/cdda2wav
%_bindir/cdda2wav	%_bindir/cdda2wav-classic	%weight
%_man1dir/cdda2wav.1.xz	%_man1dir/cdda2wav-classic.1.xz	%_bindir/cdda2wav-classic
__EOF__

%pre -n cdrecord-classic
%pre_control cdrecord-classic

%post -n cdrecord-classic
%post_control cdrecord-classic

%triggerpostun -- cdrecord <= 5:2.01-alt6a37
%preun -n cdrecord-classic

%pre -n rscsi
%pre_control rscsi

%post -n rscsi
%post_control rscsi

%pre -n readcd
%pre_control readcd-classic

%post -n readcd
%post_control readcd-classic

%files
%_sysconfdir/sformat.dat
%_bindir/Cstyle
%_bindir/admin
%_bindir/bdiff
%_bindir/bosh
%_bindir/bsh
#%%_bindir/cal # conflicts with file from package util-linux
%_bindir/calc
%_bindir/calltree
%_bindir/cdc
%_bindir/change
%_bindir/comb
%_bindir/compare
%_bindir/copy
%_bindir/count
%_bindir/cstyle.js
%_bindir/ctags
%_bindir/delta
#%%_bindir/diff # conflicts with file from package diffutils
%_bindir/dmake
%_bindir/fdiff
%_bindir/fifo
%_bindir/fsdiff
%_bindir/get
%_bindir/hdump
#%%_bindir/help # conflicts with file from package bash
%_bindir/jsh
%_bindir/krcpp
%_bindir/label
%_bindir/lndir
%_bindir/match
%_bindir/mdigest
%_bindir/mt
%_bindir/obosh
#%%_bindir/od # conflicts with file from package coreutils
%_bindir/opatch
%_bindir/p
%_bindir/pbosh
%_bindir/pfbsh
%_bindir/pfsh
#%%_bindir/printf # conflicts with file from package coreutils
%_bindir/prs
%_bindir/prt
%_bindir/rcs2sccs
%_bindir/rmchg
%_bindir/rmdel
%_bindir/sact
%_bindir/sccs
%_bindir/sccscvt
%_bindir/sccsdiff
%_bindir/sccslog
%_bindir/sccspatch
%_bindir/scgskeleton
%_bindir/scut
%_bindir/sdd
%_bindir/sfind
%_bindir/sformat
%_bindir/sgrow
%_bindir/smt
%_bindir/spaste
%_bindir/spatch
%_bindir/spax
%_bindir/svr4.make
%_bindir/tartest
%_bindir/termcap
%_bindir/translit
%_bindir/udiff
%_bindir/unget
%_bindir/val
%_bindir/vc
%_bindir/vctags
%_bindir/ved
%_bindir/ved-e
%_bindir/ved-w
%_bindir/what
%prefix/etc/termcap
%prefix/lib/cpp
%_libdir/diffh
%prefix/lib/help/locale/C/ad
%prefix/lib/help/locale/C/bd
%prefix/lib/help/locale/C/cb
%prefix/lib/help/locale/C/cm
%prefix/lib/help/locale/C/cmds
%prefix/lib/help/locale/C/co
%prefix/lib/help/locale/C/de
%prefix/lib/help/locale/C/default
%prefix/lib/help/locale/C/ge
%prefix/lib/help/locale/C/he
%prefix/lib/help/locale/C/pr
%prefix/lib/help/locale/C/prs
%prefix/lib/help/locale/C/rc
%prefix/lib/help/locale/C/sc
%prefix/lib/help/locale/C/un
%prefix/lib/help/locale/C/ut
%prefix/lib/help/locale/C/va
%prefix/lib/help/locale/C/vc
%prefix/lib/svr4.make
%doc %_docdir/bosh
%doc %_docdir/bsh
%doc %_docdir/ved
%dir %_datadir/ved
%_datadir/ved/ved.help
%_man1dir/bsh.1*
%_man1dir/admin.1*
%_man1dir/bdiff.1*
%_man1dir/calc.1*
%_man1dir/calltree.1*
%_man1dir/cdc.1*
%_man1dir/change.1*
%_man1dir/comb.1*
%_man1dir/compare.1*
%_man1dir/copy.1*
%_man1dir/count.1*
%_man1dir/cstyle.1*
%_man1dir/delta.1*
%_man1dir/dmake.1*
%_man1dir/fdiff.1*
%_man1dir/fifo.1*
%_man1dir/fsdiff.1*
%_man1dir/get.1*
%_man1dir/hdump.1*
%_man1dir/krcpp.1*
%_man1dir/label.1*
%_man1dir/lndir.1*
%_man1dir/match.1*
%_man1dir/mdigest.1*
%_man1dir/mt.1*
%_man1dir/obosh.1*
%_man1dir/opatch.1*
%_man1dir/p.1*
%_man1dir/pfbsh.1*
%_man1dir/prs.1*
%_man1dir/prt.1*
%_man1dir/rcs2sccs.1*
%_man1dir/rmdel.1*
%_man1dir/sact.1*
%_man1dir/sccs-add.1*
%_man1dir/sccs-admin.1*
%_man1dir/sccs-branch.1*
%_man1dir/sccs-cdc.1*
%_man1dir/sccs-check.1*
%_man1dir/sccs-clean.1*
%_man1dir/sccs-comb.1*
%_man1dir/sccs-commit.1*
%_man1dir/sccs-create.1*
%_man1dir/sccs-cvt.1*
%_man1dir/sccs-deledit.1*
%_man1dir/sccs-delget.1*
%_man1dir/sccs-delta.1*
%_man1dir/sccs-diffs.1*
%_man1dir/sccs-edit.1*
%_man1dir/sccs-editor.1*
%_man1dir/sccs-enter.1*
%_man1dir/sccs-fix.1*
%_man1dir/sccs-get.1*
%_man1dir/sccs-help.1*
%_man1dir/sccs-histfile.1*
%_man1dir/sccs-info.1*
%_man1dir/sccs-init.1*
%_man1dir/sccs-istext.1*
%_man1dir/sccs-ldiffs.1*
%_man1dir/sccs-log.1*
%_man1dir/sccs-print.1*
%_man1dir/sccs-prs.1*
%_man1dir/sccs-prt.1*
%_man1dir/sccs-rcs2sccs.1*
%_man1dir/sccs-remove.1*
%_man1dir/sccs-rename.1*
%_man1dir/sccs-rmdel.1*
%_man1dir/sccs-root.1*
%_man1dir/sccs-sact.1*
%_man1dir/sccs-sccsdiff.1*
%_man1dir/sccs-status.1*
%_man1dir/sccs-tell.1*
%_man1dir/sccs-unedit.1*
%_man1dir/sccs-unget.1*
%_man1dir/sccs-val.1*
%_man1dir/sccs.1*
%_man1dir/sccscvt.1*
%_man1dir/sccsdiff.1*
%_man1dir/sccslog.1*
%_man1dir/sccspatch.1*
%_man1dir/scgskeleton.1*
%_man1dir/scut.1*
%_man1dir/sdd.1*
%_man1dir/sfind.1*
%_man1dir/sgrow.1*
%_man1dir/smt.1*
%_man1dir/spaste.1*
%_man1dir/spatch.1*
%_man1dir/spax.1*
%_man1dir/sysV-make.1*
%_man1dir/tartest.1*
%_man1dir/termcap.1*
%_man1dir/translit.1*
%_man1dir/udiff.1*
%_man1dir/unget.1*
%_man1dir/val.1*
%_man1dir/vc.1*
%_man1dir/vctags.1*
%_man1dir/ved-e.1*
%_man1dir/ved-w.1*
%_man1dir/ved.1*
%_man1dir/what.1*
%_man5dir/changeset.5*
%_man5dir/sccschangeset.5*
%_man5dir/sccsfile.5*
%_man5dir/streamarchive.5*
%_mandir/man8/sformat.8*

%files -n star
%doc %_docdir/rmt
%doc %_docdir/star
%config(noreplace) %_sysconfdir/default/rmt
%config(noreplace) %_sysconfdir/default/star
%_sbindir/rmt
%_bindir/scpio
%_bindir/star
%_bindir/suntar
%_bindir/star_sym
%_bindir/strar
%_bindir/ustar
%_man1dir/rmt.1*
%_man1dir/scpio.1*
%_man1dir/star.1*
%_man1dir/suntar.1*
%_man1dir/star_sym.1*
%_man1dir/ustar.1*
%_man1dir/strar.1*
%_man5dir/star.5*

%files -n smake
%_libdir/libmakestate.so*
%_bindir/smake
%_man1dir/smake.1*
%_man5dir/makefiles.5*
%_man5dir/makerules.5*
%_datadir/lib/make
%_datadir/lib/smake

%files -n btcflash
%_bindir/btcflash
%_man1dir/btcflash.1*

%files -n mkisofs
%_altdir/mkisofs
%_bindir/mk*
%dir %_datadir/lib/siconv
%_datadir/lib/siconv/*
%_man8dir/mk*.*
%dir %docdir
%docdir/mkisofs

%files -n cdrecord-classic
%attr(640,root,cdwriter) %config(noreplace) %_sysconfdir/cdrecord.conf
%_altdir/cdrecord-classic
%_bindir/cdrecord-classic
%_bindir/scgcheck
%_man1dir/cdrecord-classic.*
%_man1dir/scgcheck.*
%dir %docdir
%docdir/AN-*
%docdir/COPYING
%docdir/*GPL*
%docdir/*CDDL*
%docdir/cdrecord

%files -n cdda2wav
%ghost %attr(640,root,cdwriter) %config(missingok) %_sysconfdir/cdda2*.conf
%_altdir/cdda2wav
%_bindir/cdda2*
%_man1dir/cdda2*.*
%dir %docdir
%docdir/cdda2wav

%files -n rscsi
%attr(640,root,cdwriter) %config(noreplace) %_sysconfdir/rscsi.conf
%_sbindir/rscsi
%_man1dir/rscsi.*

%files -n isoutils
%_bindir/devdump
%_bindir/iso*
%_man8dir/iso*.*
%_man8dir/devdump.*

%files -n readcd
%_altdir/readcd
%_bindir/readcd-classic
%_man1dir/readcd-classic.*

%changelog
* Sat Sep 14 2024 L.A. Kostis <lakostis@altlinux.ru> 7:2024.03.21-alt2
- Added boostrap knob.
- cdda2wav: build with pulseaudio.
- star: fix conflict with rmt.
- schilytools: fix more conflicts.
- schilytools/ved: move ved.help to share/ved.
- provide most tools via alternatives.

* Fri Sep 13 2024 L.A. Kostis <lakostis@altlinux.ru> 7:2024.03.21-alt1
- 2024.03.21.
- Update Url.
- Set version for separate components (as upstream set them too).
- Added schilytools packages (sccs, ved, star etc).

* Thu Sep 12 2024 L.A. Kostis <lakostis@altlinux.ru> 7:2021.09.18-alt1
- Switch to schily sources.
- Massive .spec cleanup.
- Update all -alt patches.
- Added provides/obsoletes to existing replacements.

* Mon Mar 02 2009 L.A. Kostis <lakostis@altlinux.ru> 6:2.01.01-alt4a57
- Version 2.01.01a57.
- remove obsoleted macros.

* Sun Oct 05 2008 L.A. Kostis <lakostis@altlinux.ru> 6:2.01.01-alt3a50
- Version 2.01.01a50:
  + remove obsoleted patches (-sux,UTF8,iconv).
  + disable skip_priv patch (FIXME!).
  + update existing patches (mdk-arch-fix,alt-conf).
  + update natspec patch (FIXME!).
  + update .spec.

* Thu Sep 07 2006 L.A. Kostis <lakostis@altlinux.ru> 6:2.01.01-alt2a03
- Massive update:
  + split to many packages (isoutils,readcd) closes #9196;
  + add trigger for proper upgrade from older versions (fix #9489);
  + add iconv support to mkisofs (fix #9088) tnx to Gentoo for writing and
    Dmitriy Khanzhin <jinn at altlinux.ru> for testing;
  + use tabs instead spaces in alternatives (tnx inger@ for notify).
  + update Url.

* Sat Jan 07 2006 LAKostis <lakostis at altlinux.ru> 6:2.01.01-alt1a03
- new version 2.01.01a03.
- update patches.
- x86_64 fix by mouse@ (closes #7637).
- fix mispelled summary and desc for rscsi (closes #8122).
- add alternatives for dvdrecord.
- rename cdrecord->cdrecord-classic.
- remove ossdvd patch because it has more problems than benefits.

* Thu Aug 04 2005 LAKostis <lakostis at altlinux.ru> 5:2.01-alt6a37
- add ossdvd patch and hack it for skipcheck_priv.
- update libnatspec patch (#7412).

* Fri Apr 22 2005 LAKostis <lakostis at altlinux.ru> 5:2.01-alt5a37
- add libnatspec patch.

* Wed Jan 05 2005 LAKostis <lakostis at altlinux.ru> 5:2.01-alt4a37
- reworked skipcheck_priv patch.

* Sun Dec 13 2004 LAKostis <lakostis at altlinux.ru> 5:2.01-alt3a37
- move rscsi to separate package (as ns@ suggest in #5240)
- add rscsi docs
- update skipcheck_priv patch

* Sun Dec 12 2004 LAKostis <lakostis at altlinux.ru> 5:2.01-alt2a37
- add rscsi to cdrecord package.
- add patch for linux kernel >= 2.6.8.1 compatibility.

* Tue Aug 24 2004 Dmitry V. Levin <ldv@altlinux.org> 5:2.01-alt1a37
- Updated to 2.01a37.
- Moved control files to separate package.
- Keep tools at mode "restricted" in the package, but default it
  to "public" in %%post when the package is first installed.
  This avoids a race and fail-open behaviour.

* Wed Aug 11 2004 Alexey Voinov <voins@altlinux.ru> 5:2.01-alt1a36
- new version (2.01a36)

* Wed May 26 2004 Alexey Voinov <voins@altlinux.ru> 5:2.01-alt1a30
- new version (2.01a30)

* Tue May 25 2004 Alexey Voinov <voins@altlinux.ru> 5:2.01-alt1a29
- use automake 1.7
- new version (2.01a29)
- remove dependancy on /etc/cdda2ogg.conf

* Wed May 14 2003 Dmitry V. Levin <ldv@altlinux.org> 5:2.0-alt4
- Backported format fixes from 2.01a14.

* Thu Jan 23 2003 Rider <rider@altlinux.ru> 5:2.0-alt3
- Build Requires fix (groff-base)

* Thu Jan 09 2003 Dmitry V. Levin <ldv@altlinux.org> 5:2.0-alt2
- Fixed %_includedir/*.h permissions (#0001788).
- Added %_bindir/cdda2ogg script.

* Fri Dec 27 2002 Dmitry V. Levin <ldv@altlinux.org> 5:2.0-alt1
- 2.0 release.
- Support for Code Page 1251 merged upstream.

* Mon Nov 25 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.9a40
- 1.11a40.

* Mon Oct 28 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.9a39
- 1.11a39.

* Sat Oct 26 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.9a37
- Corrected control dependence (cdrtools -> cdrecord) (#0001444).
- Don't use mmap to get shared memory (to support kernel < 2.4).

* Fri Oct 18 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.8a37
- 1.11a37, updated patches.
- Added control support for cdrecord and readcd.

* Mon May 13 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.7a23
- 1.11a23.

* Mon Apr 22 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.7a21
- 1.11a21.

* Fri Apr 05 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.7a20
- 1.11a20.
- zisofs patch merged upstream.
- Relocated docs.

* Wed Mar 13 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.7a17
- Fixed docs error made in prev package release.
- Fixed devel subpackage broken in prev package release.
- Fixed build to avoid use of kernel sources.
- Added buildconflicts on %name-devel.

* Tue Mar 12 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.5a17
- 1.11a17.

* Mon Mar 04 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.5a16
- 1.11a16.

* Tue Feb 26 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.5a15
- 1.11a15.

* Mon Feb 11 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.5a14
- 1.11a14.

* Wed Jan 30 2002 Andrey Astafiev <andrei@altlinux.ru> 5:1.11-alt0.5a013
- 1.11a13.
- Updated zisofs patch.

* Tue Jan 15 2002 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.4a12
- 1.11a12.

* Thu Nov 15 2001 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.4a11
- 1.11a11.

* Mon Nov 12 2001 Dmitry V. Levin <ldv@altlinux.org> 5:1.11-alt0.3a10
- 1.11a10.

* Tue Oct 16 2001 Andrey Astafiev <andrei@altlinux.ru> 1.11-alt0.2a08
- Small fix for nls_1251 support.
- Added zisofs patch for mkisofs.

* Tue Oct 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.11-alt0.1a08
- 1.11a08.

* Wed Sep 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.11-alt0.1a07
- 1.11a07.

* Tue Aug 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.11-alt0.1a06
- 1.11a06.
- Added nls_1251 support for mkisofs by John Profic <profic@lrn.ru>.

* Mon Apr 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.10-alt1
- 1.10 release.

* Mon Apr 16 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.10a19-alt1
- 1.10a19

* Tue Apr 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.10a18-ipl1mdk
- 1.10a18

* Sat Mar 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.10pre17-ipl1mdk
- 1.10pre17

* Wed Mar 07 2001 Dmitry V. Levin <ldv@fandra.org> 1.10a16-ipl1mdk
- 1.10a16

* Wed Feb 28 2001 Dmitry V. Levin <ldv@fandra.org> 1.10a15-ipl1mdk
- 1.10a15

* Sun Feb 25 2001 Dmitry V. Levin <ldv@fandra.org> 1.10a14-ipl1mdk
- 1.10a14

* Fri Feb 23 2001 Dmitry V. Levin <ldv@fandra.org> 1.10a13-ipl2mdk
- Raised suid on cdrecord and readcd.

* Fri Jan 26 2001 Dmitry V. Levin <ldv@fandra.org> 1.10a13-ipl1mdk
- 1.10a13

* Wed Jan 24 2001 Dmitry V. Levin <ldv@fandra.org> 1.10a12-ipl1mdk
- 1.10a12

* Thu Sep 28 2000 Dmitry V. Levin <ldv@fandra.org> 1.9-ipl1mdk
- 1.9
- Merge with RH and MDK.

* Thu May 04 2000 Dmitry V. Levin <ldv@fandra.org>
- Merge with MDK.
- Fandra adaptions.
- Imported spec from Ryan Weaver <ryanw@infohwy.com>
