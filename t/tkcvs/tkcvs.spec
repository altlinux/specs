%define pkgversion 8_1

Name: tkcvs
Version: 8.1
Release: alt3.qa1

Summary: A graphical front-end to CVS and Subversion

License: GPL
Group: Development/Other
Url: http://www.twobarleycorns.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.twobarleycorns.net/%{name}_%pkgversion.tar.bz2
Source2: %name.desktop
Source3: %name.png

Patch: tkcvs.tcl.diff

Requires: tk, cvs, subversion
Autoreq: yes, noshell

BuildArch: noarch

%description

TkCVS is a Tk based graphical interface to the CVS and Subversion
version control systems.  For CVS, it includes facilities for providing
"user friendly" names to modules and directories within the repository,
and provides a facility to interactively browse the repository looking for
modules and directories.

%prep
%setup -q -n %{name}_%pkgversion
%patch -p1

%install
mkdir -p %buildroot{%_bindir,%_datadir/%name/bitmaps,%_man1dir,%_sysconfdir/%name}
install tkcvs/tkcvs.tcl %buildroot%_bindir/%name
install -m644 tkcvs/*.* %buildroot%_datadir/%name/
install -m644 tkcvs/tclIndex %buildroot%_datadir/%name/
install -m644 tkcvs/bitmaps/* %buildroot%_datadir/%name/bitmaps
install -m644 tkcvs/*.1 %buildroot%_man1dir
install -m644 tkcvs/tkcvs_def.tcl %buildroot%_sysconfdir/tkcvs/tkcvs_def.tcl
rm -f %buildroot%_datadir/%name/%name.1
rm -f %buildroot%_datadir/%name/mkmanpage.pl

install -D -m644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -D -m644 %SOURCE3 %buildroot%_liconsdir/%name.png

%files
%config(noreplace) %_sysconfdir/%name/tkcvs_def.tcl
%doc CHANGELOG COPYING FAQ 
%_bindir/%name
%dir %_datadir/%name/
%_datadir/%name/*.tcl
#%_datadir/%name/*.pl
%_datadir/%name/tclIndex
%_datadir/%name/bitmaps/
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_man1dir/*

%changelog
* Tue Dec 01 2009 Repocop Q. A. Robot <repocop@altlinux.org> 8.1-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for tkcvs
  * update_menus for tkcvs
  * postclean-05-filetriggers for spec file

* Thu May 15 2008 Vitaly Lipatov <lav@altlinux.ru> 8.1-alt3
- pack /usr/share/tkcvs/bitmaps dir

* Wed Jan 09 2008 Vitaly Lipatov <lav@altlinux.ru> 8.1-alt2
- remove COPYING, vendor5readme.pdf, INSTALL 
- update summary and description

* Tue Jan 08 2008 Vitaly Lipatov <lav@altlinux.ru> 8.1-alt1
- cleanup spec, change Packager
- move tkcvs files to datadir (#8700), move config to /etc/tkcvs

* Tue Oct 31 2006 Mikhail Pokidko <pma@altlinux.ru> 8.0.3-alt1
- Version update.
  Fixed #4473, #8700, #9491, #9914

* Wed Jul 6 2005 Sergey Kalinin <banzaj@altlinux.ru> 7.2.3-alt1

- Close file descriptor for stderr output, which could exhaust the maximum number of open files.
- Re-work the pop-up dialogs so they appear in the center of their parent
  window, not the middle of the screen (or between the two screens.)
- The branch browser can now diff two versions even if it was invoked from
  the Module Browser and the file isn't checked out.
- The bookmarks stay in alphabetical order.

* Wed Feb  9 2005 Sergey Kalinin <banzaj@altlinux.ru> 7.2.2-alt1
- new version release

* Mon May 16 2004 Sergey Kalinin <banzaj@altlinux.ru> 7.1.2-alt3
- SPEC file changes - Summary fixed

* Tue Aug 26 2003 Sergey Kalinin <banzaj@altlinux.ru> 7.1.2-alt2
- tkdiff executing problem fixed
