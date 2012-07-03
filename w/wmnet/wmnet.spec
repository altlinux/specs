Name:		wmnet
Version:	1.06
Release:	alt4
Packager:	Alexey Voinov <voins@altlinux.ru>

Summary:	Applet that monitors the network
Group:		Graphical desktop/Window Maker
License: 	GPL
Url: 		http://www.digitalkaos.net/linux/wmnet/
Source0: 	%name-%version.tar.bz2
Source1: 	%name.menu

# Automatically added by buildreq on Fri Jul 25 2008
BuildRequires: imake libX11-devel libXext-devel xorg-cf-files

%description 
Wmnet uses ip accounting in the Linux kernel
to monitor your network.

%prep
%setup

%build
xmkmf
make CFLAGS="$RPM_OPT_FLAGS"

%install
install -p -D -m 755 wmnet $RPM_BUILD_ROOT%_bindir/%name
install -p -D -m 644 wmnet.man $RPM_BUILD_ROOT%_man1dir/wmnet.1x
install -p -D -m 644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%doc README Changelog
%_bindir/wmnet
%_man1dir/wmnet.1x*
%_menudir/*

%changelog
* Fri Dec 26 2008 Alexey Voinov <voins@altlinux.ru> 1.06-alt4
- update_menus calls were removed

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.06-alt3.1
- NMU:
  * updated build dependencies

* Fri Jul 25 2008 Alexey Voinov <voins@altlinux.ru> 1.06-alt3
- buildreqs updated

* Wed Jun 09 2004 Alexey Voinov <voins@altlinux.ru> 1.06-alt2
- url updated
- spec clean up

* Sat Oct 05 2002 Alexey Voinov <voins@voins.program.ru> 1.06-alt1
- new version(1.06)
- spec cleanup

* Sat Jun  9 2001 Alexey Voinov <voins@voins.program.ru>
- menu rearranged
- conditional NoSource added.

* Thu Apr 19 2001 Alexey Voinov <voins@voins.program.ru>
- menu added
- spec cleanup

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.05-8mdk
- automatically added BuildRequires


* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.05-7mdk
- let spechelcompress man pages
- fix tmmpath

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.05-6mdk
- BM

* Mon Apr 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.05-5mdk
- New group

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com> 1.05-4mdk
- Added PPC support

* Tue Jan 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.05-3mdk
- Don't build for alpha.

* Mon Nov 08 1999 John Buswell <johnb@mandrakesoft.com>
- Fixed Permissions
- Build Release

* Tue May 11 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- Make Mandrake compliant again.

* Fri Apr 30 1999 Alexandre Dussart <adussart@mandrakesoft.com>
- Mandrake Compliant.
- Group changed.

