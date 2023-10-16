%def_with emacs
%define emacs_mode desktop-entry
%define _emacs_startscriptsdir %_sysconfdir/emacs/site-start.d

Name: desktop-file-utils
Version: 0.26
Release: alt5

Summary: Utilities for manipulating .desktop files
Group: Graphical desktop/Other
License: GPLv2+
URL: http://www.freedesktop.org/software/desktop-file-utils

Source: %name-%version.tar
Patch0: desktop-file-utils-0.23-altlinux-add-de-to-main-categories.patch
Patch1: desktop-file-utils-0.23-altlinux-fix-TextTools.patch
Patch2: desktop-file-utils-0.26-add-DesktopNames.patch

BuildRequires: gcc glibc-devel glib2-devel libpopt-devel pkg-config automake
%{?_with_emacs:BuildRequires: emacs-cedet emacs-common emacs-leim}

%description
.desktop files are used to describe an application for inclusion in
GNOME or KDE menus.  This package contains desktop-file-validate which
checks whether a .desktop file complies with the specification at
http://www.freedesktop.org/standards/, and desktop-file-install 
which installs a desktop file to the standard directory, optionally 
fixing it up in the process.

%package -n emacs-mode-%emacs_mode
Summary: Emacs major mode for editing .desktop files
Group: Editors
Requires: %name = %version-%release
BuildArch: noarch

%description -n emacs-mode-%emacs_mode
emacs-mode-%emacs_mode provides support for editing freedesktop.org
desktop entry files.

All Emacs Lisp code is byte-copmpiled, install emacs-mode-%emacs_mode-el for sources.

%package -n emacs-mode-%emacs_mode-el
Summary: The Emacs Lisp sources for bytecode included in emacs-mode-%emacs_mode
Group: Development/Lisp
BuildArch: noarch

%description -n emacs-mode-%emacs_mode-el
emacs-mode-%emacs_mode provides support for editing freedesktop.org
desktop entry files.

emacs-mode-%emacs_mode-el contains the Emacs Lisp sources for the bytecode
included in the emacs-mode-%emacs_mode package, that extends the Emacs editor.

You need to install emacs-mode-%emacs_mode-el only if you intend to modify any of the
emacs-mode-%emacs_mode code or see some Lisp examples.


%prep
%setup -q
%patch0 -p1 
%patch1 -p1 
%patch2 -p1 

%build
#autoreconf
sh autogen.sh
%configure --disable-static %{?_with_emacs:--with-lispdir=%_emacslispdir}
%make_build

%install
%make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p %buildroot/%_rpmlibdir/
cat <<__TRIGGER__ >%buildroot/%_rpmlibdir/update-desktop-database.filetrigger
#!/bin/sh -e
XDG_DATA_DIRS="\${XDG_DATA_DIRS:-/usr/share:/var/cache}"
echo "\$XDG_DATA_DIRS" | grep '/var/cache' || XDG_DATA_DIRS+=":/var/cache"
export XDG_DATA_DIRS
grep -qs -e '/applications/' && update-desktop-database -q ||:
__TRIGGER__
chmod 0755 %buildroot/%_rpmlibdir/update-desktop-database.filetrigger

%if_with emacs
# Create %emacs_mode-init.el
cat <<__INIT__ >%emacs_mode-init.el
;;; %emacs_mode-init.el --- Startup code for desktop-entry mode
;;;
    
;; load %emacs_mode-mode 
(autoload 'desktop-entry-mode "desktop-entry-mode" "Desktop entry mode." t)
(setq auto-mode-alist (append '(("\\.desktop$" . desktop-entry-mode))
  auto-mode-alist))
(setq auto-coding-alist (append '(("\\.desktop$" . utf-8)) auto-coding-alist))

__INIT__

install -pD -m644 %emacs_mode-init.el %buildroot%_emacs_startscriptsdir/%emacs_mode-init.el
%endif

mkdir -p %buildroot/%_desktopdir/
touch %buildroot/%_desktopdir/mimeinfo.cache

%post
%_bindir/update-desktop-database ||:

%files
%_bindir/*
%_rpmlibdir/*.filetrigger
%ghost %_desktopdir/mimeinfo.cache
%_man1dir/*

%if_with emacs
%files -n emacs-mode-%emacs_mode
%config(noreplace) %_emacs_startscriptsdir/%emacs_mode-init.el
#%_emacslispdir/%emacs_mode-mode.elc

%files -n emacs-mode-%emacs_mode-el
%_emacslispdir/%emacs_mode-mode.el
%endif

%changelog
* Mon Oct 16 2023 Sergey V Turchin <zerg@altlinux.org> 0.26-alt5
- fix package filetrigger

* Tue Jul 04 2023 Sergey V Turchin <zerg@altlinux.org> 0.26-alt4
- don't force custom XDG_DATA_DIRS in filetrigger (closes: 46615)

* Wed Mar 23 2022 Sergey V Turchin <zerg@altlinux.org> 0.26-alt3
- add support SingleMainWindow key from 1.5

* Tue Dec 07 2021 Igor Vlasenko <viy@altlinux.org> 0.26-alt2
- added support for DesktopNames in xsessions and wayland-sessions

* Fri Sep 17 2021 Sergey V Turchin <zerg@altlinux.org> 0.26-alt1
- new version

* Mon Apr 08 2019 Michael Shigorin <mike@altlinux.org> 0.23-alt2
- introduce emacs knob (on by default)

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- sync with 23.0

* Thu Oct 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.22.0.patchset1-alt1
- sync with 22.0 (closes: #30359)

* Wed Apr 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.21.0.patchset1-alt1
- 0.21 patchset1:
  desktop-file-utils-0.21-altlinux-add-de-to-main-categories.patch
  desktop-file-utils-0.21-altlinux-fix-TextTools.patch

* Fri Aug 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.20.0.patchset5-alt1
- patchset5 (added MATE, TDE, Razor as categories)

* Fri Aug 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.20.0.patchset4-alt1
- sync with 20.0

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.18.0.patchset4-alt1
- patchset4 (liberal treatment of Science as main category)

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.18.0.patchset3-alt1
- patchset3 (fix for TextTools)
- added BuildArch: noarch to emacs subpackages

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.18.0.patchset2-alt1
- patchset2 (liberal treatment of Science as main category)

* Wed Apr 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.18.0.patchset1-alt2
- dropped rpm-macros-desktop-file-utils (macros are deprecated)

* Thu Mar 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.18.0.patchset1-alt1
- patchset1 (fixed main categories verification bug)

* Wed Mar 30 2011 Sergey V Turchin <zerg@altlinux.org> 0.18-alt1
- new version

* Wed Oct 13 2010 Sergey V Turchin <zerg@altlinux.org> 0.17-alt1
- new version

* Tue Jan 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.15-alt4
- move rpm macros to separate package

* Tue Aug 11 2009 Sergey V Turchin <zerg@altlinux.org> 0.15-alt3
- fix filetrigger permissions (ALT#20886)

* Fri Apr 17 2009 Sergey V Turchin <zerg@altlinux.org> 0.15-alt2
- package %%_desktopdir/mimeinfo.cache

* Wed Dec 03 2008 Sergey V Turchin <zerg at altlinux dot org> 0.15-alt1
- new version
- remove deprecated macroses from specfile
- add rpm filetrigger to update-desktop-database

* Tue Sep 04 2007 Sergey V Turchin <zerg at altlinux dot org> 0.14-alt1
- new version

* Tue Jun 05 2007 Sergey V Turchin <zerg at altlinux dot org> 0.12-alt1
- new version

* Wed Mar 15 2006 Sergey V Turchin <zerg at altlinux dot org> 0.10-alt4
- fix #9219; thanks eugvv@ALT

* Mon Feb 20 2006 Sergey V Turchin <zerg at altlinux dot org> 0.10-alt3
- fix xdg data dirs list

* Mon Nov 22 2004 Sergey V Turchin <zerg at altlinux dot org> 0.10-alt2
- fix %%post
- don't own %%_sysconfdir/rpm/macros.d
  thanks aris@altlinux

* Mon Nov 15 2004 Sergey V Turchin <zerg at altlinux dot org> 0.10-alt1
- add patch to update-desktop-database for customized menu (not applied)
- thanks mhz@altlinux for previous changes

* Sat Nov 13 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.10-alt0.1mhz1
- 0.10
- Autoreconf to fix emacs configure
- buildreq

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8-alt1
- 0.8
- emacs-mode-desktop-entry{,-el} subpackages. 
- %%{update,clean}_desktopdb macros.
- TODO: move mimeinfo.cache to /var/cache/applications.

* Fri Jun 18 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- new version

* Tue Mar 09 2004 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt1
- new version

* Thu Feb 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.3-alt1
- Ported from RawHide
