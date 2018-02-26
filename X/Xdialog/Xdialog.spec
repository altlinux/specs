Name: Xdialog
Version: 2.3.1
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary:Xdialog in replacement for the cdialog program.
Group: Development/Other
Url: http://xdialog.dyns.net/
License: GPL

Source: http://www.chez.com/godefroy/%name-%version.tar

# Automatically added by buildreq on Fri Jul 06 2007
BuildRequires: libgtk+2-devel

%description
Xdialog is designed to be a drop in replacement for the cdialog program.
It converts any terminal based program into a program with an X-windows
interface. The dialogs are easier to see and use and Xdialog adds even
more functionalities (help button+box, treeview, editbox, file selector,
range box, and much more).

%prep
%setup -q
chmod -x samples/*

%build
%configure --with-gtk2

%__subst 's,-lgetopt,,' src/Makefile

%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc samples doc/*.html doc/*.png README
%_mandir/man?/*
%_bindir/*

%changelog
* Fri Jul 06 2007 Stanislav Ievlev <inger@altlinux.org> 2.3.1-alt1
- 2.3.1, build with gtk2

* Tue Jun 27 2006 Stanislav Ievlev <inger@altlinux.org> 2.2.1-alt1
- 2.2.1

* Tue Oct 05 2004 Stanislav Ievlev <inger@altlinux.org> 2.1.2-alt1
- 2.1.2

* Wed Sep 10 2003 Stanislav Ievlev <inger@altlinux.ru> 2.1.1-alt1
- 2.1.1, fix building in hasher

* Tue Mar 25 2003 Stanislav Ievlev <inger@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Wed Dec 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.6-alt3
- remove dep on xlockmore

* Wed Oct 23 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.6-alt2
- rebuild with gcc3

* Tue Apr 23 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Tue Mar 26 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Fri Jul 27 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Wed May 23 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Fri May 18 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.1-alt1
- 2.0.1. Added russian po.

* Wed May 16 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Tue Apr 03 2001 Stanislav Ievlev <inger@altlinux.ru> 1.5.3-alt1
- ALT adaptation. Now we have dialog & Xdialog.

* Sun Mar 18 2001 Thierry Godefroy <xdialog@free.fr>
- Xdialog v1.5.3: Bug fixed (introduced in v1.5.1) that caused Xdialog to
		  segfault when closed while a timeout function was updating
		  the widget. The tailbox may now be closed or resized while
		  it updates the text in its window. The --gauge now updates
		  100 times each second (should hopefully be enough !).Removed
		  the possibility to setup a "Help" button into an infobox
		  (this makes no sense for a temporary widget). The menu/lists/
		  tree can now auto-size when the <list/menu height> parameter
		  is set to 0. The Add/Remove buttons are now greyed out when
		  no item is available into the associated list (Hi Albert !
		  ;-). New --item-help (dialog-compatible) transient option
		  implemented. New --check transient option implemented. Some
		  code cleanup. Doc updates and improvements. xlock-wrapper
		  sample script added and older sample scripts changed so to
		  make use of the lists/menu/tree auto-size feature.

See the ChangeLog (or changelog.html) file for details about older changes...
