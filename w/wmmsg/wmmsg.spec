Name:		wmmsg
Version:	1.0.1
Release:	alt4.1
Packager:	Alexey Voinov <voins@altlinux.ru>

Summary:	dockapp that notifies you of events
Group:		Graphical desktop/Window Maker
License:        GPL
#Url:           http://taxiway.swapspace.net:81/~matt/wmmsg
URL:            http://freshmeat.net/projects/wmmsg
Source0:        %name-%version.tar
Source1:        %name.menu
Patch0:         %name-1.0.1-alt-DSO.patch


# Automatically added by buildreq on Wed May 12 2010
BuildRequires: gtk+-devel imake imlib2-devel libICE-devel libXext-devel libXpm-devel xorg-cf-files


%description 
wmmsg is a dock app that notifies you of events, and the time
they arrived.  Typical use includes visual notification of
chat messages such as those from AIM, ICQ, and IRC.  It is
especially convenient for when chat windows are covered up or
on another virtual desktop, and is much less intrusive than
audible notification.

%prep
%setup -q
%patch0 -p2
%autoreconf

%build
%configure
%make_build

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -p -D -m644 %SOURCE1 $RPM_BUILD_ROOT%_menudir/%name

%files
%doc README INSTALL AUTHORS wmmsgrc
%_bindir/*
%_man1dir/*
%_menudir/*

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt4.1
- Fixed build

* Wed May 12 2010 Alexey Voinov <voins@altlinux.ru> 1.0.1-alt4
- buildreqs updated

* Sat Jun 06 2009 Alexey Voinov <voins@altlinux.ru> 1.0.1-alt3
- use pkg-config instead of older *-config scripts
- menu macros removed
- buildreqs fixed

* Sun Mar 26 2006 Alexey Voinov <voins@altlinux.ru> 1.0.1-alt2
- url now points to freshmeat.net
- makefile patch added. fixes build with new xorg
- desktop patch added. fixes monitor_desktop option

* Tue Oct 05 2004 Alexey Voinov <voins@altlinux.ru> 1.0.1-alt1
- new verision(1.0.1)

* Tue Jan 13 2004 Alexey Voinov <voins@altlinux.ru> 1.0-alt2
- fix buildreq

* Tue Apr 01 2003 Alexey Voinov <voins@altlinux.ru> 1.0-alt1
- initial build
