Name: ash
Version: 0.5.7
Release: alt1.20120623

%define real_name dash

Summary: A smaller version of the Bourne shell
License: BSD
Group: Shells

Packager: Alexey Gladkov <legion@altlinux.ru>

Url:	http://gondor.apana.org.au/~herbert/dash/

Source: %name-%version.tar
Patch0: dash-0.5.4-alt-losetup.patch
Patch2: dash-0.5.6-alt-cleanup-warnings.patch
Patch6: dash-0.5.3-makefile-cflags.patch
Patch7: dash-0.5.6-string_literal.patch

PreReq: coreutils, grep
Conflicts: mkinitrd <= 1:1.7
Provides: dash

# Automatically added by buildreq on Mon Jun 19 2006
BuildRequires: glibc-devel-static

%description
The %name shell is a clone of Berkeley's Bourne shell.  Ash
supports all of the standard sh shell commands, but is considerably
smaller than bash.  The %name shell lacks some features (for example,
command-line histories), but needs a lot less memory.

You should install %name if you need a lightweight shell with many of the
same capabilities as the bash shell.

%package static
Summary: A smaller version of the Bourne shell statically linked
License: BSD
Group: Shells

%description static
The %name shell is a clone of Berkeley's Bourne shell.  Ash
supports all of the standard sh shell commands, but is considerably
smaller than bash.  The %name shell lacks some features (for example,
command-line histories), but needs a lot less memory.

You should install %name if you need a lightweight shell with many of the
same capabilities as the bash shell.

This version is statically compiled.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch6 -p1
%patch7 -p1

sed -i -e 's,\$(tempfile),`mktemp -t ash.XXXXXX`,' src/mkbuiltins

%build
BUILD_FLAGS="%optflags_warnings -Wunused-function -Wunused-label -Wunused-variable -Wunused-value"

%autoreconf
%define _configure_script ../configure
rm -rf build-dynamic build-static
mkdir -p build-dynamic build-static

cd build-dynamic
	export CFLAGS="$BUILD_FLAGS -Werror"
	%configure --disable-dependency-tracking
	%make_build
	mv src/%real_name sh.dynamic
cd -

cd build-static
	export CFLAGS="$BUILD_FLAGS -Werror"
	%configure --disable-dependency-tracking --enable-static
	%make_build 
	mv src/%real_name sh.static
cd -

%install
mkdir -p %buildroot/lib/mkinitrd/initramfs/bin

install -m755 -pD build-dynamic/sh.dynamic %buildroot/bin/%name
install -m755 -pD build-static/sh.static %buildroot/bin/%name.static
ln -s %name %buildroot/bin/bsh
ln -s %name %buildroot/bin/dash

install -m644 -pD src/%real_name.1 %buildroot/%_man1dir/%name.1
ln -s %name.1 %buildroot/%_man1dir/bsh.1
ln -s %name.1 %buildroot/%_man1dir/dash.1

%files
/bin/%name
/bin/bsh
/bin/dash
%_man1dir/*

%files static
/bin/%name.static

%changelog
* Sat Jun 23 2012 Alexey Gladkov <legion@altlinux.ru> 0.5.7-alt1.20120623
- New release (0.5.7) and update from upstream git.

* Sun Mar 13 2011 Alexey Gladkov <legion@altlinux.ru> 0.5.6-alt1.20110313
- Update from upstream git.

* Thu Mar 10 2011 Alexey Gladkov <legion@altlinux.ru> 0.5.6-alt1.20110310
- Update from upstream git.

* Thu Feb 24 2011 Alexey Gladkov <legion@altlinux.ru> 0.5.6-alt1.20110216
- New release (0.5.6) and update from upstream git.
- This build provides the following fixes:
  + Fix corruption of readcmd with byte 0x81 (ALT#25090).

* Sun Apr 04 2010 Alexey Gladkov <legion@altlinux.ru> 0.5.5.1-alt7
- Fix conflicts.

* Wed Nov 11 2009 Alexey Gladkov <legion@altlinux.ru> 0.5.5.1-alt6
- Remove klibc support.

* Wed Aug 26 2009 Alexey Gladkov <legion@altlinux.ru> 0.5.5.1-alt5
- Revert "Honor tab as IFS whitespace when splitting fields in readcmd" (ALT#21229).

* Tue Aug 25 2009 Alexey Gladkov <legion@altlinux.ru> 0.5.5.1-alt4
- Update from upstream git.
- Add klibc build for initramfs.

* Mon May 25 2009 Alexey Gladkov <legion@altlinux.ru> 0.5.5.1-alt3
- Fix string literal error.

* Thu Feb 26 2009 Alexey Gladkov <legion@altlinux.ru> 0.5.5.1-alt1
- New release (0.5.5.1) and update from upstream git.
- This build provides the following fixes:
  + Fix dowait signal race (ALT#15136).
  + Do not close stderr when /dev/tty fails to open.
  + Allow newlines after var name in for statements.
  + Use CHKNL to parse case statements.

* Tue Jun 17 2008 Alexey Gladkov <legion@altlinux.ru> 0.5.4-alt4
- Update from upstream git.
- This build provides the following fixes:
  + Fixed non-leading slash treatment in expmeta.
  + Fixed lexical error on & and |.
  + Fix slash treatment in expmeta.
  + Add set +o support.
  + Expand here-documents in the current shell environment.
  + Removed noexpand/length check on eofmark.
  + Fix here-doc corruption.
  + Disallow completely blank strings in non-arithmetic context.
  + Fixed execing of scripts with no hash-bang.

* Sat Oct 13 2007 Alexey Gladkov <legion@altlinux.ru> 0.5.4-alt3
- Update from upstream git.
- This build provides the following fixes:
  + Report substition errors at expansion time.
  + Treat OPTIND=0 in the same way as OPTIND=1.
  + Fix parsing of ${##1}.
  + Recognise here-doc delimiters terminated by EOF.
  + Move parse-time quote flag detection to run-time.
  + Do not quote back slashes in parameter expansions outside quotes.
  + Perform tilde expansion in all parameter expansion words.
  + White space fixes for test(1).
  + Use direct comparison instead of strcmp in test(1).

* Mon Oct 01 2007 Alexey Gladkov <legion@altlinux.ru> 0.5.4-alt2
- Update from upstream git.
- This build provides the following fixes:
  + Restore foreground process group on exit.
  + Do not quote back slashes in parameter expansions outside quotes.
  + Perform tilde expansion in all parameter expansion words.
  + Do not expand tilde in parameter expansion within quotes.
  + Recognise here-doc delimiters terminated by EOF.

* Wed Jul 18 2007 Alexey Gladkov <legion@altlinux.ru> 0.5.4-alt1
- New version (0.5.4).

* Wed May 30 2007 Alexey Gladkov <legion@altlinux.ru> 0.5.3-alt8
- Update from upstream git.

* Tue Oct 17 2006 Alexey Gladkov <legion@altlinux.ru> 0.5.3-alt6
- Update from upstream git.
- This build provides the following fixes:
  + Fixed command -v segmentation fault.
  + Fixed inverted char class matching.
  + Check return code for getgroups and fwrite.

* Mon Jun 19 2006 Alexey Gladkov <legion@altlinux.ru> 0.5.3-alt5
- removed ash.interactive

* Fri May 12 2006 Alexey Gladkov <legion@altlinux.ru> 0.5.3-alt4
- Upstream patch: 
  + don't remove special chars on expansion (closes: #349855).

* Tue Mar 07 2006 Alexey Gladkov <legion@altlinux.ru> 0.5.3-alt3
- new gcc with new problems:
  + patch1 fix: LDFLAGS -> LIBS
- fix to prevent using 'getpwnam' in static build (patch3)

* Mon Feb 13 2006 Alexey Gladkov <legion@altlinux.ru> 0.5.3-alt2
- fix exit status of eval with null arguments.
- rebuild with libedit-2.9.20060213

* Wed Nov 30 2005 Alexey Gladkov <legion@altlinux.ru> 0.5.3-alt1
- 0.5.3
- New package ash-interactive was added. This shell linked with libedit.

* Fri May 06 2005 Alexey Gladkov <legion@altlinux.ru> 0.5.2-alt1
- 0.5.2
- large spec modifications

* Fri Apr 02 2004 Stanislav Ievlev <inger@altlinux.org> 0.4.25-alt1
- 0.4.25

* Thu Sep 11 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.17-alt1
- 0.4.17, fix building in hasher

* Tue Mar 18 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.10-alt1
- move to dash (Debian's ash port)
- removed post/preun scripts (we already have ash in /etc/shells)

* Mon Nov 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.8-alt4
- rebuild
- update debian patch (-38)

* Mon Jan 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.3.8-alt3
- Added losetup builtin.

* Tue Oct 16 2001 Stanislav Ievlev <inger@altlinux.ru> 0.3.8-alt2
- fix Buildreqs

* Mon Oct 15 2001 Stanislav Ievlev <inger@altlinux.ru> 0.3.8-alt1
- 0.3.8
- Move to Debian ash

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 0.2-ipl24mdk
- RE adaptions.

* Tue Dec  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.2-24mdk
- upgrade test.c to get at least [ -e ] evaluation.

* Tue Dec  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.2-23mdk
- Split -static package and classic.

* Thu Jul 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.2-22mdk
- BM

* Wed Mar 22 2000 Daouda LO <daouda@mandrakesoft.com> 0.2-21mdk
- match new group architecture

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- fix bogosity with fd's > 0 (r).
- fix builtin echo to understand -n & -e at the same time (r).

* Fri Apr  9 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man pages
- correct download URL

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- build on glibc 2.1

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- updated to correct path on SunSITE.

* Fri Aug 28 1998 Jeff Johnson <jbj@redhat.com>
- recompile statically linked binary for 5.2/sparc

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- made /bin/ash built shared
- added ash.static
- uses a buildroot and %%attr

* Sun Aug 24 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- statically linked

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- fixed preinstall script to >> /etc/shells for bsh.
