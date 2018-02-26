Name: rootfiles
Version: alt
Release: alt11

Summary: The basic required files for the root user's directory
License: GPLv2+
Group: System/Base
Packager: Etcskel Development Team <etcskel@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

Conflicts: rpm < 0:4.0.4-alt1

%description
This package contains basic required files that are placed in the
root user's account.  These files are basically the same as the
files found in the etcskel package, which are placed in regular
users' home directories.

%prep
%setup

%install
mkdir -p %buildroot/root/tmp
cp -a . %buildroot/root
chmod -R go-rwx %buildroot/root

%files
%defattr(-,root,root,700)
%config(noreplace) /root/.??*
%dir /root/tmp

%changelog
* Wed Jun 09 2010 Dmitry V. Levin <ldv@altlinux.org> alt-alt11
- .i18n: cleaned up.
- .tcshrc: synced with .bashrc.
- .cshrc: dropped in favour of .tcshrc.
- .ssh: imported from etcskel.
- .z*: synced with .bash* (by raorn@).

* Wed Jan 09 2008 Stanislav Ievlev <inger@altlinux.org> alt-alt10
- remove .vimrc

* Wed Dec 27 2006 Stanislav Ievlev <inger@altlinux.org> alt-alt9.3
- resurrect .rpmmacros

* Wed Dec 20 2006 Stanislav Ievlev <inger@altlinux.org> alt-alt9.2
- setup LC_CTYPE to en_US.utf8 in unicode, integrate this patch into tarball
- fix building from gear (missing /tmp directory)
- remove /usr/X11R6/bin from path
- remove alias for df (excluding of supermount filesystems)
- remove .rpmmacros

* Wed Aug 17 2005 Stanislav Ievlev <inger@altlinux.org> alt-alt9.1
- search for sysfont also in /etc/sysconfig/consolefont
- added "need unicode_start" detection

* Mon Dec 02 2002 Dmitry V. Levin <ldv@altlinux.org> alt-alt9
- Fixed rpm dependence.

* Fri Nov 15 2002 Dmitry V. Levin <ldv@altlinux.org> alt-alt8
- Cleaned up .i18n file.

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> alt-alt7
- rebuild

* Thu Aug 29 2002 Dmitry V. Levin <ldv@altlinux.org> alt-alt6
- Added default .rpmmacros (requires recent rpm).

* Fri Apr 13 2002 Ivan Zakharyaschev <imz@altlinux.ru> alt-alt5
- Dropped: .emacs (now provided by emacsen-startscripts-0.0.1-alt3;
  it is the second part of the fix of \#808 at bugs.altlinux.ru)

* Fri Dec 07 2001 Dmitry V. Levin <ldv@alt-linux.org> alt-alt4
- Honor RPM_INSTALL_LANG from /etc/sysconfig/i18n (#0000165).
- Updated: .bashrc.
- Dropped: .kderc, .Xdefaults.

* Wed Jun 13 2001 Dmitry V. Levin <ldv@altlinux.ru> alt-alt3
- Honor SYSFONT* from /etc/sysconfig/i18n.

* Tue Jun 05 2001 Stanislav Ievlev <inger@altlinux.ru> alt-alt2
- Force to use POSIX locale for root.

* Mon May 28 2001 Stanislav Ievlev <inger@altlinux.ru> alt-alt1
- Remove KDE and Netscape directories. Now all packages must put root's
  default settings itself.

* Fri Jan 26 2001 AEN <aen@logic.ru>
- RE adaptation
- version changed to 7.25
* Wed Nov 08 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-2mdk
- Use config(noreplace)

* Mon Oct  9 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 7.2-1mdk
- rebuild for 7.2

* Mon Jul 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 7.1-9mdk
- rootfiles.spec: BM.

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 7.1-8mdk
- Desktop/DrakConf.kdelnk: Don't launch with kdesu for root.

* Mon May 08 2000 dam's <damien@mandrakesoft.com> 7.1-7mdk
- corrected vimrc

* Mon May 08 2000 dam's <damien@mandrakesoft.com> 7.1-6mdk
- added no wrap in vimrc

* Sun Apr 30 2000 dam's <damien@mandrakesoft.com> 7.1-5mdk
- re-added XKill in Desktop

* Thu Apr 27 2000 dam's <damien@mandrakesoft.com> 7.1-4mdk
- kde/share/config/kpanelrc :removed DesktopButton section to fix empty panel in root session

* Wed Apr 26 2000 dam's <damien@mandrakesoft.com> 7.1-3mdk
- Desktop : cleaned up kdelnk files.

* Thu Mar 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 7.1-2mdk
- tcshrc: define hard PATH.
- cshrc: define hard PATH.
- rootfiles.spec: adjust groups.
- rootfiles.spec: Add ChangeLog in %%doc
- bashrc: cleanup.

* Wed Mar 22 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 7.1-1mdk
- Remove .emacs (moved to his package).
- Remove .zshrc (moved to his package).

* Mon Jan 10 2000 Pixel <pixel@mandrakesoft.com>
- added a kfmrc (for Templates directory)

* Tue Jan 04 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Sync .kdelnk.

* Tue Dec 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- add kppp icons for kde.
- True makefile and cvs.

* Wed Dec 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- fix vimrc with vim-minimal.

* Tue Dec 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- put ~/tmp as 700.

* Sat Dec 18 1999 Pixel <pixel@mandrakesoft.com>
- added .netscape/(cache|archive)

* Thu Dec 16 1999 François PONS <fpons@mandrakesoft.com>
- removed Cd-Rom.kdelnk and floppy.kdelnk, since handled by DrakX.

* Thu Dec 16 1999 Pixel <pixel@mandrakesoft.com>
- moved Templates from Desktop to .kde
- better .emacs (especially gnu-emacs)

* Fri Dec 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Syn Desktop.

* Thu Dec 02 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Alias df to -x supermount.

* Wed Dec 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove the export XAUTHORITY for root.

* Sat Nov 27 1999 Pixel <pixel@linux-mandrake.com>
- .vimrc: `syntax on' only if vim-common is there

* Mon Nov 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add hwiz.kdelnk in Autostart of kde package.

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix .emacs (<c> Chmouel All right reserved).

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- fix stupid path in .bashrc (thanks john).

* Tue Sep 07 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Add Desktop directory.
- Kde in English.

* Tue Sep 07 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Insert kde configuration and Desktop of kde directly here.

* Fri Aug 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Fix typo.

* Fri Aug 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Bind Windows key to (K)menu.

* Sun Aug  8 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- zshrc: by defaut we launch the completion machine.

* Thu Aug 05 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Fix typo in .vimrc.

* Mon Aug  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Syn on only with enhanced vim.
- Add statusbar for vim
- New alias in bashrc.

* Tue Jun 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Tmp for root.

* Tue May 18 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Fix locales bug rapport by Jean Michel <jmdault@netrevolution.com>

* Wed May 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Security path for root.
- Suppr work now for root.

* Tue May 11 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- a /sbin and /usr/sbin for root even for telnet.

* Sun May 09 1999 Gaël Duval <gael@linux-mandrake.com>

- Added .kderc for root
- changed the version number (5.2->6.0)

* Sun May 09 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Mandrake adaptations.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- add %clean (#719)

* Tue Dec 29 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0

* Wed Oct  9 1998 Bill Nottingham <notting@redhat.com>
- remove /root from %files (it's in filesystem)

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- portability fix for .cshrc (problem #235)
- change version to be same as release.

* Tue Sep 09 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Thu Mar 20 1997 Erik Troan <ewt@redhat.com>
- Removed .Xclients and .Xsession from package, added %pre to back up old
  .Xclients if necessary.
# Local Variables:
# compile-command: "rpmbuild -ba rootfiles.spec"
# End:
