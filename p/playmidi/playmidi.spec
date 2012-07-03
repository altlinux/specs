Name: playmidi
Version: 2.5
Release: alt4

Summary: A MIDI sound file player
License: GPL
Group: Sound

Url: http://sourceforge.net/projects/playmidi/
Source: %name-%version.tar.bz2
Patch0: %name-2.3-hertz.patch
Patch1: %name-2.3-awe2.patch
Patch2: %name-2.4-make.patch
Patch3: %name-2.4-midimap.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Sep 09 2008
BuildRequires: glib-devel libXaw-devel libncurses-devel libXext-devel

Summary(ru_RU.KOI8-R): Утилита проигрывания MIDI файлов.

%package X11
Summary: An X Window System based MIDI sound file player
Summary(ru_RU.KOI8-R): Проигрыватель MIDI файлов для X Window System
Requires: %name = %version
Group: Sound

%description
Playmidi plays MIDI (Musicial Instrument Digital Interface) sound
files through a sound card synthesizer.  This package includes basic
drum samples for use with simple FM synthesizers.

Install %name if you want to play MIDI files using your computer's
sound card.

%description X11
Playmidi-X11 provides an X Window System interface for playing MIDI
(Musical Instrument Digital Interface) sound files through a sound
card synthesizer.  This package includes basic drum samples for use
with simple FM synthesizers.

Install %name-X11 if you want to use an X interface to play MIDI
sound files using your computer's sound card.

%prep
%setup -q -n %name-2.4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

./Configure << EOF
2
EOF

%build
PATH=.:$PATH
# SMP-incompatible.
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS `glib-config --cflags`" %name x%name

%install
mkdir -p %buildroot{%_sysconfdir/midi,%_bindir,%_man1dir,%_x11dir/{bin,lib/X11/app-defaults}}
install -p -m755 %name %buildroot%_bindir
install -p -m755 x%name %buildroot%_x11dir/bin
install -p -m644 XPlaymidi.ad %buildroot%_x11dir/lib/X11/app-defaults/XPlaymidi
install -p -m644 %name.1 %buildroot%_man1dir

for n in *.o3 *.sb; do
	install -p -m644 $n %buildroot%_sysconfdir/midi
done

# TODO:
# - add desktop file?

%files
%_bindir/%name
%_mandir/man?/*
%dir %_sysconfdir/midi
%config(noreplace) %_sysconfdir/midi/*
%doc QuickStart BUGS

%files X11
%_x11dir/lib/X11/app-defaults/*
%_x11dir/bin/x%name

%changelog
* Mon Dec 01 2008 Michael Shigorin <mike@altlinux.org> 2.5-alt4
- fixed BuildRequires (libXext-devel)

* Sun Nov 09 2008 Michael Shigorin <mike@altlinux.org> 2.5-alt3
- rebuilt against current libXaw-devel

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 2.5-alt2
- fixed build (buildreq)

* Fri Apr 23 2004 Anton Farygin <rider@altlinux.ru> 2.5-alt1
- new version

* Wed Aug 20 2003 Rider <rider@altlinux.ru> 2.4-ipl19mdk
- fix buildrequires (#2144)

* Fri Oct 11 2002 Rider <rider@altlinux.ru> 2.4-ipl18mdk
- rebuild
- russian Summary

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 2.4-ipl17mdk
- rebuild

* Sun Dec 10 2000 Dmitry V. Levin <ldv@fandra.org> 2.4-ipl16mdk
- RE adaptions.

* Mon Sep 25 2000 Maurizio De Cecco <maurizio@mandrakesoft.com> 2.4-16mdk
- Resource file not a config file anymore.

* Mon Aug 09 2000 Maurizio De Cecco <maurizio@mandrakesoft.com> 2.4-15mdk
- Added macros for mandir and bindir.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4-14mdk
- automatically added BuildRequires

* Tue Apr 11 2000 Maurizio De Cecco <maurizio@mandrakesoft.com>
- Fixed Distribution name

* Thu Apr 10 2000 Maurizio De Cecco  <maurizio@mandrakesoft.com>
- Fixed error in the new Group structure

* Thu Mar 16 2000 Maurizio De Cecco  <maurizio@mandrakesoft.com>
- Adapted to the new Group structure

* Wed Nov 17 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Don't ship splaymidi(r).

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 7)

* Tue Feb 23 1999 Bill Nottingham <notting@redhat.com>
- wmconfig goes away

* Mon Dec 28 1998 Bill Nottingham <notting@redhat.com>
- build against glibc-2.1

* Mon Nov 23 1998 Bill Nottingham <notting@redhat.com>
- oops. We broke FM synth. Fixed.

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- updated to version 2.4

* Wed Sep  9 1998 Bill Nottingham <notting@redhat.com>
- added AWE32 support

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root
- sound font data in %_sysconfdir/midi

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
