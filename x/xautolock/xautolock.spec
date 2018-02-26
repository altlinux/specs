Name:		xautolock
Version:	2.2
Release:	alt1
Group:		Graphical desktop/Other
Summary:	Monitor X window system activity and fire up a program when idle
License:	GPL
Source:		%name-%version.tgz

# Automatically added by buildreq on Wed Aug 18 2010
BuildRequires: gccmakedep imake libX11-devel libXScrnSaver-devel libXext-devel xorg-cf-files

%description
Xautolock  monitors  console activity  under the X window system, and
fires  up  a  program  of your choice if  nothing  happens  during  a
user configurable  period of time.  You can use this to automatically
start up a screen locker in case you tend to forget to do so manually
before having a coffee break.

Xautolock  will  typically  be used to lock the screen but it  really
doesn't care what program you make it start. The only real assumption
made  by  xautolock  is that  a new countdown  starts  as soon as the
locker exits.

%prep
%setup

%build
xmkmf -a
%make

%install
%makeinstall DESTDIR=%buildroot install.man

%files
%doc Readme
%_bindir/%name
%_man1dir/%name.*

%changelog
* Wed Aug 18 2010 Fr. Br. George <george@altlinux.ru> 2.2-alt1
- Initial build from scratch

