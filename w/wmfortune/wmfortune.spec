Name:		wmfortune
Version:	0.241
Release:	alt4.qa1

Packager:	Alexey Voinov <voins@altlinux.ru>

Summary:	It's a dock-app that shows you fortune messages
Group:		Graphical desktop/Window Maker
License: 	GPL
URL: 		http://dockapps.org/file.php/id/90
Source0: 	%name-%version.tar.bz2
Source1: 	%name.menu
Requires:	fortune-mod

# Automatically added by buildreq on Mon Nov 13 2006
BuildRequires: libXext-devel libXpm-devel

%description 
It's a dock-app that shows you fortune messages

%prep
%setup -q

%build
%make_build OPTIMIZE="$RPM_OPT_FLAGS"

%install
install -p -D -m755 wmfortune $RPM_BUILD_ROOT%_x11bindir/wmfortune
install -p -D -m644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%doc README INSTALL CHANGES TODO
%_bindir/wmfortune
%_menudir/*

%changelog
* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.241-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for wmfortune
  * postclean-05-filetriggers for spec file

* Sun Aug 05 2007 Alexey Voinov <voins@altlinux.ru> 0.241-alt4
- description fixed [#8161], thanks to php-coder@a.r for a fix.

* Mon Nov 13 2006 Alexey Voinov <voins@altlinux.ru> 0.241-alt3
- summary fixed [#8161]
- url fixed (home page no longer exists)
- buildreqs updated
- path in menu file fixed
- changed default delay to 10000

* Wed Oct 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.241-alt2
- rebuild in new enviroment.
- light spec improvements.
- added packager tag.

* Tue Sep 11 2001 Alexey Voinov <voins@voins.program.ru>
- initial build
