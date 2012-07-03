Name:		wmcube-gdk
Version:	0.98p2
Release:	alt5.qa2

Packager:	Alexey Voinov <voins@altlinux.ru>

Summary:	It's dockapp that displays a rotating 3d-object and the CPU load
Group:		Graphical desktop/Window Maker
License: 	GPL
Url: 		http://www.ne.jp/asahi/linux/timecop/#wmcube
Source0: 	%name-%version.tar.bz2
Source1: 	%name.menu
Source2:	peace.wmc

Patch0:		%name-%version-alt-linux26.patch
Patch1:		%name-%version-alt-zoom.patch
Patch2:		%name-%version-alt-autodock.patch

# Automatically added by buildreq on Tue Dec 12 2006
BuildRequires: gtk+-devel

%description 
wmCube is a dockapp that displays a realtime rotating 3d-object
and the current CPU load.

%prep
%setup -q -n %name-%version
%patch -p1
%patch1 -p1
%patch2 -p1

%build
%make_build INCDIR="`gtk-config --cflags` `glib-config --cflags`" CFLAGS="$RPM_OPT_FLAGS -DLINUX" \
	    LIBS="-lgdk -lm -lX11"

%install
install -p -D -m755 wmcube $RPM_BUILD_ROOT%_bindir/wmcube
install -p -D -m644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name
install -d $RPM_BUILD_ROOT%_datadir/wmcube/
install -p -D -m644 3dObjects/* $RPM_BUILD_ROOT%_datadir/wmcube/
install -p -D -m644 %SOURCE2 $RPM_BUILD_ROOT%_datadir/wmcube/peace.wmc

%files
%doc README README.GDK INSTALL CHANGES TODO
%_bindir/wmcube
%_menudir/*
%_datadir/wmcube/*

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.98p2-alt5.qa2
- Fixed build

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.98p2-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmcube-gdk
  * postclean-05-filetriggers for spec file

* Thu Dec 28 2006 Alexey Voinov <voins@altlinux.ru> 0.98p2-alt5
- support for linux 2.6.x.

* Tue Dec 12 2006 Alexey Voinov <voins@altlinux.ru> 0.98p2-alt4
- libm added [fixes build]
- buildreqs updated
- /usr/X11R6 -> /usr

* Tue Oct 07 2003 Alexey Voinov <voins@altlinux.ru> 0.98p2-alt3
- buildreq fixed
- peace.wmc fixed

* Wed Oct 23 2002 Alexey Voinov <voins@voins.program.ru> 0.98p2-alt2
- new version (0.98p2)
- spec cleanup

* Fri Sep 14 2001 Alexey Voinov <voins@voins.program.ru> 0.98p1-alt2
- autodock patch added

* Thu Sep 13 2001 Alexey Voinov <voins@voins.program.ru>
- initial build
- zoom patch (now zoom level can be set from command line)

