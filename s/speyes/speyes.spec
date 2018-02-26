Name: speyes
Version: 1.2.0
Release: alt6

Packager: Alexey Voinov <voins@altlinux.ru>

Summary: speyes - Eyes for South Park fans
License: GPL
Group: Graphical desktop/Window Maker

URL: http://okb-1.org/speyes/speyes.html
Source: http://okb-1.org/speyes/%name-%version.tar.bz2
Source1: %name.menu

# Automatically added by buildreq on Tue Nov 14 2006
BuildRequires: imake libX11-devel libXext-devel libXmu-devel libXpm-devel xorg-cf-files

%description
But why?:
   That's a question I've asked myself a few times, to be honest.  The idea
   just hit me one day, helped along by a friend of mine who has a Mac that
   has eyes in its menubar.  Between that, and my interest in doing a dock app
   for WindowMaker, this was the result.  I expect any other dock apps I do to
   have somewhat more functionality.

%prep
%setup -q
%__subst 's/OBJS =.*/OBJS = %name.o/' Imakefile

%build
xmkmf
%__subst 's/EXTRA_LDOPTIONS =/EXTRA_LDOPTIONS = -L $(USRLIBDIR)/' Makefile
make speyes

%install
install -D -pm755 speyes $RPM_BUILD_ROOT/%_bindir/%name
install -D -pm644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%doc CHANGES COPYING README
%_bindir/*
%_menudir/*

%changelog
* Mon Sep 21 2009 Alexey Voinov <voins@altlinux.ru> 1.2.0-alt6
- update_menus removed

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt5.1
- NMU:
  * updated build dependencies

* Tue Nov 14 2006 Alexey Voinov <voins@altlinux.ru> 1.2.0-alt5
- /usr/X11R6 -> /usr
- buildreqs updated

* Fri Oct 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.0-alt4
- rebuild with gcc3

* Sat Jun  9 2001 Alexey Voinov <voins@voins.program.ru>
- menu rearranged
- conditional NoSource added.

* Thu Apr 19 2001 Alexey Voinov <voins@voins.program.ru>
- Spring2001 build
- menu added

* Tue Dec 19 2000 Alexey Voinov <voins@voins.program.ru>
- initial revision

