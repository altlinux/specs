%define ver_major 3.3
%define _oldname gnome2-utils

Name: gnome-utils
Version: %ver_major.1
Release: alt1

Summary: Utilities for the GNOME 3 desktop
License: LGPL2+
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

BuildArch: noarch

Provides: %_oldname = %version-%release
Obsoletes: %_oldname < 2.14

Requires: gnome-dictionary >= %version
Requires: gnome-disk-usage >= %version
Requires: gnome-font-viewer >= %version
Requires: gnome-screenshot >= %version
Requires: gnome-search-tool >= %version
Requires: gnome-system-log >= %version

%description
This package provides a set of utilities for the GNOME 3 desktop:

Screenshot	  - make screenshots from desktop.
System Log Viewer - monitor and view system log files.
Search Tool       - search for files on your system using simple
		    and advanced search options.
Dictionary        - look up an online dictionary for definitions
		    and correct spelling of words.
Baobab (Disk Usage) - show the amount of space taken by directories
                    in a nice graphical way.
Font Viewer	  - preview fonts.

%files


%changelog
* Sat Mar 10 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- made virtual package after gnome-utils split

* Mon Jan 30 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- updated to 3.2.1+, fixed ALT #26877

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- fixed build with newer gtk

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Sat Feb 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3
- fixed find_lang usage

* Wed Jan 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Sat Nov 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt2
- removed generated *-.{desktop,schemas} from gsearchtool sources
- fixed "Categories" in .desktop files (closes #21017)

* Mon Oct 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0
- updated buildreqs
- removed obsolete gfloppy package

* Thu Jun 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- new libgdict{,-devel{,-doc}} packages

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Jan 28 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.2-alt1
- 2.25.2
- removed obsolete %%post{,un} scripts
- updated buildreqs

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Mon Sep 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Jun 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.20.0.1-alt2
- %%_datadir/baobab/pixmaps owned by gnome-disk-usage

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.20.0.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for gnome-utils-gfloppy

* Fri Nov 23 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.0.1-alt1
- new version (2.20.0.1)
- add Packager

* Wed Jul 25 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.1-alt2
- rebuild

* Sun Jul 22 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.1-alt1
- new version (2.18.1)
- updated the list of files
- use macros from rpm-build-gnome

* Wed Dec 27 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt1
- new version (2.16.2)
- description of the virtual package updated.

* Sat Sep 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- new subpackage, gnome-disk-usage, for Baobab tool.
- spec improved with some useful macros
- developer's documentation on libgdict now hits gnome-dictionary-devel, not
  gnome-dictionary.

* Sat Apr 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version (2.14.0)
- the package renamed from gnome2-utils to gnome-utils.
- spec cleanup (bless --disable-scrollkeeper and --disable-schemas-install).

* Sat Mar 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.95-alt1
- new version (2.13.95)
- fixed gnome2-utils package requires according to the changes in the names
  of subpackages.

* Sat Feb 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.93-alt1
- new version (2.13.93)
- cleaned up the spec, revised dependencies
- removed Debian menu support
- removed gnome2-utils prefix from names of most packages
- introduced gnome-dictionary-devel package (provides libgdict-devel)

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version

* Sat Oct 22 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version

* Fri Oct 07 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt2
- The menu item for gnome-dictionary is in Applications/Text tools (Bug #4434)

* Wed Oct 05 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Sat Sep 24 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed excess buildreqs.

* Wed Apr 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Mon Feb 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92.

* Wed Feb 09 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1
- 2.9.91

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.91-alt1
- 2.7.91

* Thu Apr 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Tue Oct 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Mon Sep 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- fixed buildreqs.

* Wed Sep 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Thu Sep 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Wed Aug 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Sun Jun 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3
- gdialog obsoletes, raplaced by zenity.
- gnomedesktop2mdkmenu.pl used to generate menu files.
- /etc/pam.d/gnome-system-log adopted for new PAM configuration policy
  (requires pam >= 0.75-alt20).

* Sun May 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2
- Obsoletes gnome2-utils-{calculator,character-map},
  replaced by gcalctool and gucharmap respectively.

* Thu May 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Mar 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon Jan 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.3-alt1
- 2.2.0.3

* Sun Jan 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.2-alt1
- 2.2.0.2

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.90-alt1
- 2.1.90

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Mon Dec 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Tue Nov 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3
- archive-generator removed from project.

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt2
- rebuild with new pango, gtk+

* Thu Oct 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Thu Sep 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.5-alt1.1
- Buildreqs updated
- files section for archive-generator fixed.
- gnome2-utils virtual package install all utils.

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Wed Jun 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt1
- First build for Sisyphus.

