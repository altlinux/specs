Name: larswm
Version: 7.5.3
Release: alt2.1.qa1

Group: Graphical desktop/Other
Summary: Lars Tiling Window Manager
License: 9wm-like
Url: http://larswm.fnurt.net

Source: %name-%version.tar.bz2
Source1: %name-logo.png

# Automatically added by buildreq on Tue May 06 2008
BuildRequires: imake libX11-devel libXext-devel libXmu-devel xorg-cf-files

%description
This is not really a completely new window manager, but rather a heavily
modified version of David Hogan's 9wm.  In following his licensing terms, it is
released under a different name than 9wm.

%prep
%setup -q

%build
xmkmf
make

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT
make install.man DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_liconsdir/
install %SOURCE1 $RPM_BUILD_ROOT%_liconsdir/%name-logo.png

# session file
%__install -d $RPM_BUILD_ROOT%_sysconfdir/X11/wmsession.d
%__cat > $RPM_BUILD_ROOT%_sysconfdir/X11/wmsession.d/14%name << EOF
NAME=%name
ICON=%_liconsdir/%name-logo.png
EXEC=%_bindir/%name
DESC=larswm - tiling window manager
SCRIPT:
exec %_bindir/%name
EOF

%files
%doc ChangeLog README README.9menu README.9wm sample.larswmrc sample.xsession
%_bindir/*
%_mandir/man1/*
%_sysconfdir/X11/wmsession.d/*
%_liconsdir/*

%changelog
* Tue Feb 09 2010 Repocop Q. A. Robot <repocop@altlinux.org> 7.5.3-alt2.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_wms for larswm
  * postclean-05-filetriggers for spec file

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.5.3-alt2.1
- NMU:
  * updated build dependencies

* Tue May 06 2008 Alexey Voinov <voins@altlinux.ru> 7.5.3-alt2
- /usr/X11R6/ -> /usr/
- buildreqs updated
- icon added, wmsession entry fixed

* Wed Aug 04 2004 Alexey Voinov <voins@altlinux.ru> 7.5.3-alt1
- initial build

