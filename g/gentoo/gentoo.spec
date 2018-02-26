%define name	gentoo
%define version	0.19.13
%define release	alt1

Summary: gentoo is a Gtk+ file manager for Linux
Name: %name
Version: %version
Release: %release
License: GPL
Group: File tools
# Automatically added by buildreq on Thu Nov 10 2005
BuildRequires: glib2-devel libgtk+2-devel

Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://www.obsession.se/gentoo
Source: ftp://ftp.obsession.se/gentoo/%name-%version.tar.gz
Source1: gentoo_16.xpm.bz2
Source2: gentoo_32.xpm.bz2
Source3: gentoo_48.xpm.bz2
Patch1: gentoo-0.15.3-0.2-nmu.diff
Requires: gtk+ >= 1.2.3

%description
gentoo is a file manager for Linux written from scratch in pure C. It
uses the GTK+ toolkit for all of its interface needs. gentoo provides
100%% GUI configurability; no need to edit config files by hand and re-
start the program. gentoo supports identifying the type of various
files (using extension, regular expressions, and/or the 'file' command),
and can display files of different types with different colors and icons.
gentoo borrows some of its look and feel from the classic Amiga
file manager "Directory OPUS"(TM) (written by Jonathan Potter).

%prep
%setup -q
#patch1 -p0


# Don't define GTK_DISABLE_DEPRECATED since GtkComboBoxEntry is deprecated in
# GTK 2.23
sed -i -e '/GTK_DISABLE_DEPRECATED/d' configure

%build
%configure
%make_build

%install
install -d $RPM_BUILD_ROOT%_bindir
install -d $RPM_BUILD_ROOT%_libdir/gentoo/icons
install -d $RPM_BUILD_ROOT%_mandir/man1

install -s -m 755 src/gentoo	$RPM_BUILD_ROOT%_bindir
install -m 644 icons/*		$RPM_BUILD_ROOT%_libdir/gentoo/icons
install -m 644 docs/gentoo.1x*	$RPM_BUILD_ROOT%_mandir/man1

mkdir -p $RPM_BUILD_ROOT%_menudir
cat << EOF >  $RPM_BUILD_ROOT%_menudir/%name
?package(%name): \
	needs="x11" \
	section="Applications/File tools" \
	title="Gentoo" \
	longtitle="Gtk File Manager" \
	command="%_bindir/gentoo" \
	icon="%name.xpm"
EOF

mkdir -p $RPM_BUILD_ROOT%_niconsdir $RPM_BUILD_ROOT%_miconsdir $RPM_BUILD_ROOT%_liconsdir
bzcat %SOURCE1 > $RPM_BUILD_ROOT/%_miconsdir/%name.xpm
bzcat %SOURCE2 > $RPM_BUILD_ROOT/%_niconsdir/%name.xpm
bzcat %SOURCE3 > $RPM_BUILD_ROOT/%_liconsdir/%name.xpm

%files
%doc docs BUGS COPYING INSTALL README*
%_bindir/gentoo
%_libdir/gentoo
%_mandir/man1/gentoo.1x*
#_menudir/*
%_niconsdir/*.xpm
%_liconsdir/*.xpm
%_miconsdir/*.xpm

%changelog
* Sun Apr 22 2012 Ilya Mashkin <oddity@altlinux.ru> 0.19.13-alt1
- 0.19.13

* Wed Sep 14 2011 Ilya Mashkin <oddity@altlinux.ru> 0.19.11-alt1
- 0.19.11

* Sun Jun 19 2011 Ilya Mashkin <oddity@altlinux.ru> 0.19.10-alt1
- 0.19.10

* Fri May 06 2011 Ilya Mashkin <oddity@altlinux.ru> 0.19.9-alt1
- 0.19.9

* Sun Dec 26 2010 Ilya Mashkin <oddity@altlinux.ru> 0.19.7-alt1
- 0.19.7

* Fri Dec 03 2010 Ilya Mashkin <oddity@altlinux.ru> 0.19.6-alt1
- 0.19.6

* Wed Oct 20 2010 Ilya Mashkin <oddity@altlinux.ru> 0.19.3-alt1
- 0.19.3

* Mon Sep 27 2010 Ilya Mashkin <oddity@altlinux.ru> 0.15.6-alt1
- 0.15.6

* Fri Jan 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.11.56-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gentoo
  * pixmap-in-deprecated-location for gentoo
  * postclean-05-filetriggers for spec file

* Mon Mar 26 2007 Sergey Ivanov <seriv@altlinux.ru> 0.11.56-alt1
- update version to 0.11.56

* Thu Nov 10 2005 Sergey Ivanov <seriv@altlinux.ru> 0.11.55-alt1
- reanimate from orphaned and update version

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation

* Wed Sep  6 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.11.14-5mdk
- Add new icons

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.11.14-4mdk
- automatically added BuildRequires

* Wed Jul 26 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.11.14-3mdk
- BM + macroszification
- embed menu in specfile

* Tue Jun 20 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.11.14-2mdk
- Updated to version 0.11.14

* Fri Apr 07 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.11.13-2mdk
- Fixed spec file to add menu and icon

* Thu Apr 06 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.11.13-1mdk
- Updated groups for mandrake
- version update to 0.11.13

* Mon Mar 20 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.13-1]
- Fixed incredibly stupid bug (reported by plenty of people, it's
  nice to know people care :) which prevented the text viewer
  window from closing when it should. It's a two-line fix.
- If you enable the "System Default" Control key mode in the
  dirpane config, it will now work.
- There was some broken logic related to quitting and the dialog
  that asks about saving changed configs. Fixed that, and also
  cleaned up the code significantly, removing duplicate stuff.

* Mon Mar  6 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.12-1]
- I'm reasonably sure I fixed a bug which caused a crash if you
  hit enter after entering an *empty* directory using the key-
  board-controlled focusing mechanism.
- Added support for tall, thin, parent buttons along the outer
  edges in the panes. Enable through the "Huge Parent Button?"
  checkbox in the config. The position and action of these is
  currently not configurable; it's always outer edge & DirParent.
- Incorporated alternative implementation of the GtkLabel widget
  provided by Johan Hanson. This label implementation is only used
  for the status line in the top of the window, which reportedly
  had refresh-problems with some pixmap-based GTK+ themes.
- Redid the code for the textviewer, which was very old and some-
  what confused. This might make it support mouse wheel scrolling
  better. Since I don't have a wheelie mouse, I can't test it...
- Fixed tiny bug which caused GTK+ warnings if you hit TAB in the
  command selection dialog without having typed anything first.
- Implemented a Join command, to counter the (still incomplete)
  Split command. Pretty neat, with DnD reordering.
- gentoo can now optionally ignore the state of the NumLock key
  when parsing keyboard and mouse input. Enable the check button
  in the bottom of the Controls config page. Note that only the
  input event is filtered, not the definition (do not use NumLock
  in actual mappings with this flag on).
- New version of the odscrolledbox widget, provided by Johan
  Hanson as always. Should fix some smudgy redrawing problems.
- Brought the (c) in the About box into the 21th century, added
  acknowledgement (and mail address) of Johan Hanson's work.
- Added recognition and viewing of LHa compressed files to the
  example config. Requires the 'lha' external command.
- gentoo can now remember the position and size of the config and
  textviewer windows, in addition to the main window. See config
  page labeled "Windows" (was "Pos & Size" previously). Eh, also
  see the BUGS file, since this feature has a few problems still. :(
- Tweaked code that dealt with 64-bit stuff; gentoo should now
  compile better on Linux/Alpha platforms.
- Selected content in the right-hand list in the Dirpane config
  page can now be reordered directly, by dragging. You can still
  use the up/down buttons below the list, like always.
- Er, not a fix per se, but this version of gentoo has been
  compiled and executed using GTK+ 1.2.7. No extensive tests,
  though.

* Mon Nov 22 1999 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.11-1]
- Tweaked the FileAction command slightly: now it will stop running
  the action if the selection is empty. This helps when you run a
  command containing e.g. a {Fu} code on more than one file, since
  it will then just run the command once, then stop since the {Fu}
  "consumed" the entire selection. Hopefully this is not a bad thing.
- The GetSize command no longer loses track of the pane's vertical
  position.
- The pane centering on startup was changed back to the pre-0.11.10
  behavior, since the "fix" didn't help the user who reported the
  problem. Weird.
- Rewrote core file copying routine, used by Copy, CopyAs, Move,
  and other commands. It now handles "magic" files whose length
  looks like zero (like most files in the /proc filesystem). It's
  also shorter, simpler, and possibly a tiny bit faster.
- Fixed semi-obscure bug in the Split command; it wouldn't close
  output files on failed writes. Oops.
- In an attack of POSIX panic, I removed all my symbols whose names
  ended in _MAX, leaving only standard ones. Touched ~130 places.
- The SelectRE command now lets you chose what column content you
  wish to match against. This is sometimes useful, for example you
  could use the following command to select all rows whose files
  have an odd size: 'SelectRE glob=0 full=0 content=size [13579]$'.
     See "docs/scratch/command_args.txt" for a brief table of
  content names.
- Removed all uses of stdlib's malloc() & free(), replacing them
  with glib's g_XXX work-alikes, making the code more consistent.
- Added tooltips to the pane control widgets (the parent button,
  the path entry field, and the cryptic 'H' hide button).
- RTFM:ed a bit, and fixed example config's "view_man" command to
  stop emitting control codes for bold and underline. This makes
  it work better with gentoo's viewer. Unsure about portability.
- Added type, style, and view support for AVI and MPEG video clips
  to the example config. Both use 'xanim' for view. Untested. Also
  added support for IFF-ILBM bitmap images, through 'xv' as always.
- Added a new command, DpFocusPath, which moves GTK+'s input focus
  to the current pane's path entry box. Bound to shift+Return in
  the example config. Call with select=1 to select contents, too.
- Fixed buglet which made it annoying to bind commands to Return,
  since the config window's default button ("OK") would trigger.

* Tue Nov  9 1999 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.10-1]
- Got mail from Jesse Perry <jap@unx.dec.com>, reporting problems
  building gentoo on an Alpha, running Tru64. Luckily, the report
  (and followups) included lots of detail and helpful hints, so I
  went over the offending code. Hopefully it works now.
- I still got the expand/collapse tracking in the Styles config
  page wrong. <HOMER>Duh!</HOMER> Fixed again. This time, for sure!
- Wrote a new command, RenameRE. It provides two ways of doing search
  and replace over selected file names, and then renaming the files.
  Learn about in "docs/scratch/renamere.txt". Recommended reading!
- Fixed bug which prevented an error from the Rename command (and
  others, no doubt) from showing up.
- Did a long-overdue, minimal, change in the way the active pane gets
  hilighted, now uses Johan Hanson's code in "colorutil.c". Should
  work better if you're running a themed GTK+.
- Pressing return after entering a path name now causes that path
  to be entered, instead of (uselessly) popping up the combo menu
  showing directory history. Oops.
- When running a command bound to a key, the key press signal is
  no longer propagated to GTK+; gentoo consumes it. This makes things
  work better when you bind stuff to e.g. cursor keys, which are
  used by GTK+ to control focus. A neat one-line fix.
- The 'view_tar_bzip2' command in the example config has been made
  more portable (uses --use-compress-prog=bzip2 rather than -y).
- If you attempt to DirRescan a directory which no longer exists,
  you will get an informative message. Better than silence.
- Included a new icons package from Johan Hanson (<johan@tiq.com>).
  There are around 20 new icons, including a very cute Commodore
  logo for SID music files! Check them out in the icons/ subdir!
- Fixed a portability problem in dirpane.c; a reference to strncmp().
- Upgraded my home development machine to GTK+/glib 1.2.6, which
  went fairly smooth. It exposed a bug in the config GUI, though.
- The centering of the panes is now done later during startup,
  since one user reported problems with it. This is too bad, since
  it now looks kind of worse during startup. :(

