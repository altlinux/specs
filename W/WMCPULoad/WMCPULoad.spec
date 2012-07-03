Name:		WMCPULoad
Version:	1.1.0
Release:        alt1

Summary:	WindowMaker DockApp that displays current CPU usage
License:	GPL
Group:		Graphical desktop/Window Maker
Packager:	Alexey Voinov <voins@altlinux.ru>
Url:            http://freshmeat.net/projects/wmcpuload/

# Automatically added by buildreq on Sun Jun 07 2009
BuildRequires: imake libICE-devel libXext-devel libXpm-devel xorg-cf-files


Source0:	%name-%version.tar
Source1:	%name.menu

%description
WMCPULoad is an WindowMaker DockApp that displays current CPU usage.

%prep
%setup -q

%build
%configure
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT
install -p -D -m644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%doc README NEWS INSTALL TODO AUTHORS ChangeLog
%_bindir/*
%_man1dir/*
%_menudir/*


%changelog
* Sun Jun 07 2009 Alexey Voinov <voins@altlinux.ru> 1.1.0-alt1
- url updated [#20236]
- buildreqs fixed
- obsolete macros removed

* Sun Mar 05 2006 Alexey Voinov <voins@altlinux.ru> 1.1.0-alt0.1
- new (current) version (1.1.0pre5)
- url updated [#8510]
- fixed build with new xorg
- menu file updated [/usr/X11R6 -> /usr]
- memory leak fixed [#8970, patch by php-coder@]
- buildreqs fixed

* Sun Sep 14 2003 Alexey Voinov <voins@altlinux.ru> 1.0.1-alt2
- buildreq updated

* Mon Mar 10 2003 Alexey Voinov <voins@voins.program.ru> 1.0.1-alt1
- new version (1.0.1)

* Sat Oct 05 2002 Alexey Voinov <voins@voins.program.ru> 1.0.0-alt1
- new version (1.0.0)
- spec cleanup
- iname defined (don't want to change package name still)

* Fri Jun 8 2001 Alexey Voinov <voins@voins.program.ru>
- menu rearranged

* Thu May 3 2001 Alexey Voinov <voins@voins.program.ru>
- initial build

