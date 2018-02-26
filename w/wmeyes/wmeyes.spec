Name:		wmeyes
Version:	1.2
Release:	alt3

Packager:	Alexey Voinov <voins@altlinux.ru>

Summary:	wmeyes - The world's most useless WindowMaker dock app
License:	MIT
Group:		Graphical desktop/Window Maker
Url:		http://www.bstern.org/wmeyes
Source:		%name-%version.tar.bz2
Source1:	%name.menu

# Automatically added by buildreq on Thu May 08 2008
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

%build
xmkmf
%__subst 's/EXTRA_LDOPTIONS =/EXTRA_LDOPTIONS = -L $(USRLIBDIR)/' Makefile
make wmeyes

%install
install -D -pm755 %name $RPM_BUILD_ROOT/%_bindir/%name
install -D -pm644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%doc README ChangeLog LICENSE
%_bindir/*
%_menudir/*

%changelog
* Mon Nov 09 2009 Alexey Voinov <voins@altlinux.ru> 1.2-alt3
- update_menus removed

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt2.1
- NMU:
  * updated build dependencies

* Thu May 08 2008 Alexey Voinov <voins@altlinux.ru> 1.2-alt2
- /usr/X11R6 -> /usr
- buildreqs updated

* Fri Jan 21 2005 Alexey Voinov <voins@altlinux.ru> 1.2-alt1
- new version
- license fixed again
- url fixed

* Wed Jun 09 2004 Alexey Voinov <voins@altlinux.ru> 1.0-alt5
- fixed license

* Sun Oct 27 2002 Alexey Voinov <voins@voins.program.ru> 1.0-alt4
- removed ownership of /usr/X11R6/bin directory.
- url added
- spec slean up

* Fri Oct 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt3
- rebuild with gcc3

* Sat Jun  9 2001 Alexey Voinov <voins@voins.program.ru>
- menu rearranged
- conditional NoSource added.

* Thu Apr 19 2001 Alexey Voinov <voins@voins.program.ru>
- initial build

