Name: etcskel
Version: 2.0.13
Release: alt1

%def_enable langify

Summary: %distribution default files for user's home directories
License: GPL
Group: System/Internationalization
BuildArch: noarch

%define old_list uk uk-koi8u uk-cp1251 de ru-koi8r ru-cp1251 be be-cp1251
%define old_provides %(for i in %old_list;do echo -n "%name-$i = %version ";done)
%define old_obsoletes %(for i in %old_list;do echo -n "%name-$i ";done)

Requires: shadow-utils >= 1:4.0.0-alt6
Provides: %old_provides
Obsoletes: %old_obsoletes
Conflicts: rpm-build < 0:4.0.4-alt1, enscript < 1.6.3-alt1
BuildRequires: hardlink

# Get the source from our cvs repository.
Source: %name-%version.tar

%description
The etcskel package is part of the basic %distribution system.
These files are then placed in every user's home directory
when new accounts are created.

%prep
%setup

%build
make

%install
make install

:>%name.locales
for f in %buildroot/etc/skel.*; do
	n=${f##*/}
	s=${n#skel.}
	s=${s%%@*}
	s=${s%%.*}
	s=${s%%_*}
%if_enabled langify
	l="%%lang($s) "
%else
	l=
%endif #enabled langify
	echo "$l%%config(noreplace) %_sysconfdir/$n" >>%name.locales
done

%files -f %name.locales
%config(noreplace) %_sysconfdir/skel

%changelog
* Tue Feb 15 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0.13-alt1
- Removed "Documents" and "tmp" directories (closes: #6323).
- .bash_profile: Removed exporting of XDG_* variables (closes: #21419).

* Thu Jun 25 2009 Dmitry V. Levin <ldv@altlinux.org> 2.0.12-alt1
- Added .xprofile script.
- Added .ssh/authorized_keys file (closes: #12389).
- .bash_profile: Fixed typo to export XDG_CACHE_HOME
  (by Artem Zolochevskiy; closes: #19793).

* Thu Sep 06 2007 Stanislav Ievlev <inger@altlinux.org> 2.0.11-alt2
- add freedesktop standard directories

* Tue Apr 17 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.11-alt1
- .mutt/header: Ignored all headers except essential ones.
- .mutt/{alias,lists}: Updated ALT mailing lists.
- .mutt/set: Added "set sort=threads".
- .mutt/set: Removed "set nosig_dashes" (ALT#10369).
- .rpmmacros: Fixed %%_gpg_name example (ALT#9234).

* Wed Aug 17 2005 Stanislav Ievlev <inger@altlinux.org> 2.0.10-alt1.3
- removed extra LANGUAGE definitions from ~/.i18n

* Sat Jun 26 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.10-alt1.2
- added .xemacs/init.el

* Tue May 06 2003 Stanislav Ievlev <inger@altlinux.ru> 2.0.10-alt1
- fix DICTIONARY in ru_RU.CP1251: must be russianw
- .mutt/set now common (ispell is "/usr/bin/ispell" by default)

* Mon Feb 03 2003 Dmitry V. Levin <ldv@altlinux.org> 2.0.9-alt1
- .mutt/set: updated editor value.

* Fri Dec 20 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.8-alt2
- removed LC_* from .i18n

* Mon Dec 02 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0.8-alt1
- Added .xsession.d directory.

* Fri Oct 25 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-alt5
- removed .lynxrc and .mailcap

* Mon Oct 14 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-alt4
- removed Gnome related files

* Fri Sep 20 2002 Sergey V Turchin <zerg@altlinux.ru> 2.0.7-alt3
- added Documents catalog for different desktop applications

* Tue Sep 10 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-alt2
- move enscript from requires to conflicts

* Thu Aug 29 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0.7-alt1
- Removed RPM tree (requires recent rpm).

* Fri Aug 16 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.6-alt1
- removed enscript configs

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0.5-alt1
- Made all stuff world readable (requires recent useradd).
- Added default .rpmmacros and RPM tree (requires recent rpm).

* Tue Jul 09 2002 ZerG <zerg@altlinux.ru> 2.0.4-alt2
- remove .kde catalog because fail normal first startup of KDE
- move Desktop catalog to kde-desktop package

* Tue Jun 11 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0.4-alt1
- .bash_profile: moved all locale-dependent stuff to .i18n file.

* Fri Jun 07 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0.3-alt1
- .bashrc: removed all aliases (see profile.d/aliases.sh)
- .bashrc: removed INPUTRC initialization (see profile.d/inputrc.*sh)
- .bash_profile: removed initialization for variables:
  HISTIGNORE PATH USERNAME.
- all: chmod -R go-rwx.
- Linkified and langified skels like in glibc-locales.

* Mon Apr  8 2002 Ivan Zakharyaschev <imz@altlinux.ru> 2.0.2-alt1
- .emacs: do not set explicitly selection-coding-system --
  the default 'compound-text-with-extensions' from emacs-21.2-alt1 is OK
  (see further details in \#786 at bugs.altlinux.ru).

* Tue Mar 19 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.1-alt3
- removed ~/.icewm, 'cause Icewm looks only this config, no system
- fixed KDE desktop for Ukrainian locale
- added support for French locale

* Fri Feb 22 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.1-alt2
- fixed Update desktop entry

* Mon Feb 18 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.1-alt1
- moved .Xdefaults as /etc/X11/Xresources.LANG (app-defaults package)

* Mon Feb 18 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0-alt2
- return missing tmp directory

* Mon Feb 18 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0-alt1
- full merge with etcskel

* Fri Feb 15 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt1
- force specs integration
- now we have common directory

* Thu Feb 14 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt1
- some fixes for gnome desktop
- join all skeleton tarballs into one.

* Mon Feb 11 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.4-alt3.1
- sync .emacs with emacs-21.1-alt10; explicitly call all three 
  set-*-coding-system 
- add Emacs examples to .Xdefaults

* Wed Jan 23 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt3
- removed .links

* Mon Jan 21 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt2
- fixed links default options

* Fri Jan 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt1
- Back to Sisyphus.

* Fri Jan 18 2002 AEN <aen@logic.ru> 0.3-alt16master
- .gconf added

* Thu Jan 17 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt15master
- fixed default color scheme for mutt

* Thu Jan 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt14master
- removed .xsession
- s/MandrakeUpdate/synaptic
- clear .Xdefaults
- removed .netscape

* Tue Jan 08 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt13master
- removed "Junior update" button

* Fri Dec 28 2001 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt12master
- replace .xinitrc with .xsession

* Wed Dec 26 2001 Ivan Zakharyaschev <imz@altlinux.ru> 0.3-alt11master
- set global DICTIONARY environment variable
- shorten .emacs, fallback on global Emacs' config file

* Tue Dec 25 2001 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt10master
- added ":ru_RU" to LANGUAGE in user's .i18n file

* Fri Dec 21 2001 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt9master
- added koi8-u tag

* Wed Dec 19 2001 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt8master
- fix again

* Wed Dec 19 2001 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt7master
- fixed .mutt/gpg

* Thu Dec 06 2001 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt6master
- Added .i18n file

* Tue Sep 11 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.3-alt5junior
- Fixed Internet Icon on Desktop

* Sun Sep 09 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.3-alt4junior
- Some fixes for Desktop
- Don't start arts by default

* Thu Aug 30 2001 Konstantin Volckov <goldhead@altlinux.ru>
- Fixed to work with KDE2.2

* Thu Jul 26 2001 Konstantin Volckov <goldhead@altlinux.ru>
- Changes for Junior 1.1

* Fri Jun 1 2001 Konstantin Volckov <goldhead@altlinux.ru>
- Added Junior settings

* Tue Feb 13 2001 AEN <aen@logic.ru>
- Removed export XAUTHORTY from .bashrc

* Wed Feb 7 2001 AEN <aen@logic.ru>
- fixed .xinitrc

* Wed Feb 7 2001 AEN <aen@logic.ru>
- added missing .xinitrc in Makefile

* Wed Jan 31 2001 AEN <aen@logic.ru>
- new version

* Tue Dec 26 2000 AEN <aen@logic.ru>
- new spec, based on MDK spec
# Local Variables:
# compile-command: "rpmbuild -ba etcskel.spec"
# End:

