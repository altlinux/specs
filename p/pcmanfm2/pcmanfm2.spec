Summary: PCMan File Manager
Name: pcmanfm2
Version: 1.1.0
Release: alt1
License: GPL
Group: File tools
Url: http://pcmanfm.sourceforge.net/

Source: %name-%version.tar.gz

Conflicts: pcmanfm < 0.9

BuildRequires: libgtk+2-devel >= 2.18.0
BuildRequires: intltool

BuildRequires: libfm-devel >= 1.0.2

BuildRequires: libgio-devel

%description
Features:
    * Extremly fast and lightweight
    * Can be started in one second on normal machine
    * Tabbed browsing (Similiar to Firefox)
    * Drag & Drop support
    * Files can be dragged among tabs
    * Load large directories in reasonable time
    * File association support (Default application)
    * Basic thumbnail support
    * Bookmarks support
    * Handles non-UTF-8 encoded filenames correctly
    * Provide icon view and detailed list view
    * Standard compliant (Follows FreeDesktop.org)
    * Clean and user-friendly interface (GTK+ 2)

%prep
%setup

%build
# unpack git version with builtin script
./autogen.sh
%configure \
    --enable-largefile

%make

%install
make DESTDIR=%buildroot install
%find_lang pcmanfm
cd %buildroot%_bindir
ln -s pcmanfm pcmanfm2

%files -f pcmanfm.lang
%_bindir/*
%_desktopdir/*.desktop
%_datadir/pcmanfm
%_sysconfdir/xdg/pcmanfm/*
%_mandir/man1/*

%changelog
* Tue Nov 06 2012 Radik Usupov <radik@altlinux.org> 1.1.0-alt1
- new version (1.1.0)

* Wed Oct 31 2012 Radik Usupov <radik@altlinux.org> 1.0.2-alt1
- new version (1.0.2)

* Wed Oct 10 2012 Andriy Grytsenko <andrej@rep.kiev.ua> 1.0.2
- New upstream RC version 1.0.2~alpha1.
- Removed all patches - upstream has changed everything since 0.9.x series.

* Wed Feb 22 2012 Radik Usupov <radik@altlinux.org> 0.9.10-alt2
- Revert "Apply patch #3438582 to fix bug #3325415 - window resize problem." (Closes: 26981)

* Tue Jan 31 2012 Radik Usupov <radik@altlinux.org> 0.9.10-alt1
- new version (0.9.10)

* Wed Aug 31 2011 Radik Usupov <radik@altlinux.org> 0.9.9-alt10
- new upstream snapshot

* Mon Aug 15 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt9
- fixed starting without arguments when daemon running

* Sun Jul 31 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt8
- quick/dirty fix for bug: daemon window lost when unmounting volume
at last (or single) tab

* Thu Jul 14 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt7
- new upstream snapshot

* Wed Jul 06 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt6
- new snapshot

* Tue May 31 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt5
- new snapshot
- fixed bug with closing daemon's last window

* Tue Apr 26 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt3
- new snapshot

* Fri Apr 15 2011 Radik Usupov <radik@altlinux.org> 0.9.9-alt2
- Added requires (Closes: 25204)

* Tue Mar 01 2011 Timur Aitov <timonbl4@altlinux.org> 0.9.9-alt1
- new snapshot

* Wed Dec 08 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt6
- deselect files when clicking with right button too

* Mon Oct 25 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt5
- new snapshot

* Thu Sep 23 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt4
- new snapshot

* Wed Jul 21 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt3
- new git snapshot from upstream

* Fri Jun 11 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt2
- thanks to Alexey Borisenkov fixed #23445

* Sun May 30 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt1
- new version

* Tue May 04 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.5-alt1
- new upstream version (closes: #23425)

* Mon Apr 26 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.4-alt1
- new version

* Fri Mar 12 2010 Nick S. Grechukh <gns@altlinux.ru> 0.9.3-alt1
- new version based on libfm. Package name changed to pcmanfm2
