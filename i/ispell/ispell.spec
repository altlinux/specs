%def_disable german
Name: ispell
Version: 3.2.06
Release: alt13
Epoch: 1

Summary: The GNU interactive spelling checker program
License: BSD-like
Packager: Igor Vlasenko <viy@altlinux.ru>
Group: Text tools
URL: http://ficus-www.cs.ucla.edu/ficus-members/geoff/ispell.html

Source0: http://fmg-www.cs.ucla.edu/geoff/tars/ispell-%version.tar
Source2: spell
Source3: ispell-3.20-hk2-deutsch.tar

Patch0: ispell-3.1.20-config.patch
Patch1: ispell-3.2.06-german.patch
Patch2: ispell-3.1.20-termio.patch
Patch3: ispell-3.1.20-strcmp.patch
Patch4: ispell-3.1.20-maskbits64_and_british.patch
Patch5: ispell-3.2.06-dont-string.patch
Patch6: ispell-3.20-sh.patch
Patch7: ispell-3.20-missing_prototypes.patch
Patch8: ispell-3.20-increase-max.patch
Patch9: ispell-3.20-xb-options.patch
Patch10: ispell-3.2.06-sq.patch
Patch11: ispell-3.20-man-update.patch
# add missing includes
Patch12: ispell-3.2.06-includes.patch
# use mkdir -p to create directories
Patch13: ispell-3.2.06-mkdir_p.patch
# fix syntax error
Patch14: ispell-3.2.06-syntax.patch

Patch15: ispell-3.2.06-alt-downgrade-english-wordchars.patch
Patch16: ispell-3.2.06-epa7-tmp.patch
Patch17: ispell-3.2.06.epa7-alt-tmp.patch

Patch18: ispell-3.2.06-alt-fix-munchlist.patch
Patch19: ispell-3.2.06-alt-gcc44-system-getline.patch

PreReq: alternatives >= 0:0.3.0
Requires: mktemp >= 1:1.3.1
Provides: /usr/bin/spell

# Automatically added by buildreq on Mon Jun 26 2006
BuildRequires: alternatives libtinfo-devel words

BuildPreReq: alternatives >= 0:0.3.0

%description
Ispell is the GNU interactive spelling checker.  Ispell will check a text
file for spelling and typographical errors.  When it finds a word that is
not in the dictionary, it will suggest correctly spelled words for the
misspelled word.

Note this package has only the spell checker engine; you also need to
install the dictionary files from the ispell-* package for your language.

%package en
Summary: English dictionary for ispell
Group: System/Internationalization
# the binary format changed with ispell 3.2.06
Requires: ispell >= 1:3.2.06
BuildPreReq: words >= 2
Obsoletes: iamerica ispell-english ibritish ispell-british
Provides: ispell-dictionary = 3.2.06

%description en
This package has the English dictionary files for ispell.

With it you can check the spelling of Enlish text files or LaTeX files
written in English.

%package de
Summary: German dictionary for ispell
Group: System/Internationalization
Requires: ispell >= 1:3.2.06
Obsoletes: ispell-german igerman
Provides: ispell-dictionary = 3.2.06

%description de
This package has the German dictionary files for ispell.

%prep
%setup -q -a3

%patch0 -p1
%patch1
%patch2 -p1 -b .termio
%patch3 -p1 -b .strcmp
%patch4 -p1 -b .maskbits
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1 -b .SQ
#%patch11 -p1
%patch12 -p1 -b .includes
%patch13 -p1 -b .mkdir-p
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p0
%patch19 -p1

%build
cat >>./local.h <<\__EOF__
#define CC "gcc"
#define CFLAGS "%optflags"
#define BINDIR "%_bindir"
#define LIBDIR "%_libdir/%name"
#define MAN1DIR "%_man1dir"
#define MAN4DIR "%_man4dir"	/* for upstream releases */
#define MANFDIR "%_man5dir"	/* for unofficial `epa' releases */
#define INSTALL "install -p"
#define MASTERHASH "americanmed+.hash"
#define TERMLIB "-ltinfo"
__EOF__
subst s,/usr/dict/words,%_datadir/dict/words,g local.h

# Make sure that the mtime of files generated during the build
# (especially config.sh) is not in the same second as local.h.
sleep 2

# SMP-incompatible build
%make

%install
# This 'subst' invocation modifies config.sh, which is generated from
# local.h; the following 'make' call must not rebuild config.sh,
# otherwise install will fail.  The '-p' option is also required to
# avoid rebuild of programs (which otherwise may get wrong compiled-in
# paths).  However, 'subst -p' currently does not support sub-second
# timestamps - it silently truncates them to the start of the second,
# therefore config.sh mtime goes backwards and might go before the
# local.h mtime, and in this case make will rebuild config.sh.  The
# 'sleep 2' above works around this problem.
subst -p 's,%_prefix,%buildroot&,g' config.sh

%makeinstall
mv %buildroot%_bindir/ispell %buildroot%_bindir/ispell-real
install -pD %SOURCE2 %buildroot%_bindir/ispell-spell
install -d %buildroot%_altdir
cat > %buildroot%_altdir/%name <<'EOF'
/usr/bin/ispell	/usr/bin/ispell-real	40
EOF
cat > %buildroot%_altdir/%name-spell <<'EOF'
/usr/bin/spell	/usr/bin/ispell-spell	40
EOF

%files
%doc README
%attr(755,root,root) %_bindir/*
%_altdir/%{name}*
%_man1dir/ispell.1*
%_man4dir/ispell.4*
#_infodir/ispell.info*
#_libdir/emacs/site-lisp/ispell.el
%_man1dir/buildhash.1*
%_man1dir/munchlist.1*
%_man1dir/findaffix.1*
%_man1dir/tryaffix.1*
%_man1dir/sq.1*
%_man1dir/unsq.1*
%dir %_libdir/%name

%files en
%_man4dir/english.4*
%_libdir/%name/american.hash
%_libdir/%name/americanmed+.hash
%_libdir/%name/americanxlg.hash
%_libdir/%name/english.aff
%_libdir/%name/english.hash
%_libdir/%name/british.hash
%_libdir/%name/britishmed+.hash
%_libdir/%name/britishxlg.hash

%if_enabled german
%files de
%_libdir/%name/deutsch.aff
%_libdir/%name/deutsch.hash
%_libdir/%name/deutschlxg.hash
%_libdir/%name/deutschmed.hash
%_libdir/%name/german.hash
%endif

%changelog
* Thu Mar 18 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.2.06-alt13
- split ispell and spell alternatives

* Tue May 12 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.2.06-alt12
- fixed build with gcc44

* Sun Apr 12 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.2.06-alt11
- removed ispell-de (now use separate source)

* Mon Apr 06 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.2.06-alt10
- removed obsolete post update_alternatices

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.2.06-alt9
- fixed munchlist

* Tue Sep 09 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.2.06-alt8
- resurrected from orphaned

* Tue Jun 27 2006 Sergey Vlasov <vsu@altlinux.ru> 1:3.2.06-alt7
- Link with -ltinfo instead of -lncurses (fixes build failure with
  -Wl,--as-needed).
- Add 'sleep 2' to %%build to avoid build failure on filesystems with
  sub-second timestamp precision.
- Do not bzip2 patches and tiny sources (spell).
- Fix unescaped '%%' in old changelog.
- Converted alternatives config files to new format (0.2.0).
- Removed all %%__* macro abuse from spec.
- Updated BuildRequires.

* Fri Apr 01 2005 Vital Khilko <vk@altlinux.ru> 1:3.2.06-alt6
- #5589
  #5285

* Thu Jul 22 2004 Vital Khilko <vk@altlinux.ru> 1:3.2.06-alt5
- reverted to previous SMP-incompatible build

* Wed Jul 21 2004 Vital Khilko <vk@altlinux.ru> 1:3.2.06-alt4
- rebuilded for #4441

* Sat Jul 03 2004 Alexey Tourbin <at@altlinux.ru> 1:3.2.06-alt3
- epa7-tmp.patch, alt-tmp.patch: fix insecure tempfile handling
  in munchlist and findaffix
- downgrade-english-wordchars.patch: do not use ISO Latin-1 characters
  like grave and acute for english words
- reworked %%build and %%install scriplets
- licnese: BSD-like, not GPL
- specfile cleanup

* Thu Nov 13 2003 Vital Khilko <vk@altlinux.ru> 1:3.2.06-alt2
- fixed serial missing

* Mon Nov 10 2003 Vital Khilko <vk@altlinux.ru> 3.2.06-alt1
- new version
- add alternatives
- build with german dictionary

* Thu Nov 21 2002 AEN <aen@altlinux.ru> 1:3.1.20-alt2
- %%{un}install_info removed

* Tue Nov 19 2002 AEN <aen@altlinux.ru> 1:3.1.20-alt1
- rebuild with gcc-3.2

* Wed Dec 26 2001 Ivan Zakharyaschev <imz@altlinux.ru> 3.1.10-ipl18mdk
- ispell-en:
  + add americanxlg dictionary
  + *xlg made the default dictionaries

* Wed Jun 13 2001 AEN <aen@logic.ru> 3.1.20-ipl17mdk
- removed Requires: locales-*

* Sun Jan 28 2001 Mikhail Zabaluev <zabaluev@parascript.com> 3.1.20-ipl16mdk
- Added:
  + Russian description
- Fixed:
  + dependencies for RE

* Wed Dec 06 2000 AEN <aen@logic.ru>
- build for RE

* Thu Nov 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.1.20-14mdk
- Dont include broken string.h.

* Tue Sep 19 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 3.1.20-13mdk
- Modify texinfo file for correct installation
- Generate info file instead of using a pre-generated one
- Modify BuildRequires since words package installed must be BM..

* Sun Sep 17 2000 David BAUDENS <baudens@mandrakesoft.com> 3.1.20-12mdk
- Allow to build
- Macros, BM, Linux-Mandrake's specs compliant, etc.

* Thu Jun 06 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 3.1.20-11mdk
- splitted ispell-de to its own package

* Thu Mar 30 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 3.1.20-10mdk
- rebuild for new Group: names
- changed the spec file a bit to leave compression of man pages to spec-helper

* Wed Jan 12 2000 Pablo Saratxaga <pablo@mandrakesoft.com>
- added Provides: ispell-dictionary for ispell-{en,de}
- added Requires: ispell-dictionary to ispell package, so it requires
  at least one dictionary package to be installed

* Tue Dec 07 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added Obsoletes: for easier installation over other rpms of same language
- added british files to ispell-en

* Tue Oct 26 1999 Pawel Jablonski <pj@linux-mandrake.com>
- separate dictionaries ispell-en and ispell-de

* Sun Oct 3 1999 Pawe³ Jab³oñski <pj@linux-mandrake.com>
- increase MASKBITS from 32 to 64 - like in Debian (needed by ispell-pl)

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 15)

* Thu Feb 25 1999 Bill Nottingham <notting@redhat.com>
- add a buildroot

* Tue Jan 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- strcmp may have different forms on different systems;
  do not declare it explicitly, just include <string.h>
- use /var/tmp instead of /usr/tmp

* Sun Nov 8 1998 Patricia Jung <trish@freiburg.linux.de>
- Added German dictionary

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- eliminate /usr/lib/emacs/site-lisp/ispell.el -- use emacs-20.3 version.

* Mon Jun 29 1998 Jeff Johnson <jbj@redhat.com>
- use posix termios (problem #558)
- add build root.

* Sat Jun 27 1998 Trent Jarvi <jarvi@ezlink.com>
- alphahack patch no longer required. struct winsize now in <ioctl-types.h>.
- change MASKWIDTH apropriately on alpha

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 09 1998 Erik Troan <ewt@redhat.com>
- have two Source1 lines isn't terribly brilliant

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- patch to avoid remaking ispell.info

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added a spell program.
- Configured for 8-bit use.
