Name: cdcd
Version: 0.6.6
Release: alt5.qa1
Summary: Command Driven CD player
License: %gpl2plus
Group: Sound
URL: http://libcdaudio.sourceforge.net/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: glib-devel libcdaudio-devel libreadline-devel

%description
%name takes a different approach from conventional console (or X) based
CD players, in that it doesn't keep with the display-oriented paradigm.
Conventional computer-based CD players resemble traditional physical CD
players. This is fine, if your user interface consists of 10 buttons.
However, computers have keyboards, so why not use them? Besides, it's
certainly a waste of a console or an xterm to have a traditional CD
player open anyway.
%name works in two ways, accepting commands directly off the command
line or in a query mode similar to other UNIX programs. To pass a
command to %name, simply run %name with the command as the arguement
(e.g. %name play). This is great for using cron and %name together to
make a CD alarm clock. Or, you can run %name without arguments and you
will be given the %name command prompt.


%prep
%setup
%patch -p1


%build
%define _optlevel s
%add_optflags -D_GNU_SOURCE
%autoreconf
%configure
%make_build
bzip2 --best --force --keep ChangeLog


%install
%make_install DESTDIR=%buildroot install

# menu
install -d %buildroot%_desktopdir
iconv -f cp1251 -t utf-8 > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
GenericName=Command Driven CD player
GenericName[ru]=КД-проигрыватель с командным управлением
GenericName[uk]=КД-програвач з командним керуванням
Name=%name
Exec=%name
Icon=cdaudio_unmount
Type=Application
Terminal=true
Categories=AudioVideo;Audio;Player;ConsoleOnly;
__MENU__


%files
%doc README NEWS AUTHORS ChangeLog.*
%_bindir/*
%_infodir/*
%_man1dir/*
%_desktopdir/*


%changelog
* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.6-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for cdcd
  * postclean-05-filetriggers for spec file

* Sat Dec 27 2008 Led <led@altlinux.ru> 0.6.6-alt5
- cleaned up spec

* Sat Aug 09 2008 Led <led@altlinux.ru> 0.6.6-alt4
- fixed %name.desktop
- fixed License

* Tue Mar 04 2008 Led <led@altlinux.ru> 0.6.6-alt3
- fixed %name.desktop

* Thu Sep 20 2007 Led <led@altlinux.ru> 0.6.6-alt2
- fixed %name.desktop

* Wed Jun 14 2006 Led <led@altlinux.ru> 0.6.6-alt1
- initial build
- removed libcurses checking with %name-0.6.6-curses.patch
