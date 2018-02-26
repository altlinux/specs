# vim: set ft=spec: -*- rpm-spec -*-
# $Id: docker,v 1.2 2006/04/03 13:32:55 raorn Exp $

Name: docker
Version: 1.5
Release: alt2

Summary: Docker is a docking application (WindowMaker dock app) which acts as a system tray for KDE and GNOME2. 
License: GPL
Group: Graphical desktop/Window Maker

Url: http://icculus.org/openbox/2/%name

Source: %url/%name-%version.tar.gz
Patch: %name-1.5-alt-link.patch

# Automatically added by buildreq on Mon Apr 03 2006
BuildRequires: glib2-devel libX11-devel pkg-config

%description
Docker is a docking application (WindowMaker dock app) which acts as a system 
tray for KDE and GNOME2. It can be used to replace the panel in either 
environment, allowing you to have a system tray without running the KDE/GNOME 
panel or environment.

%prep
%setup -q
%patch -p1

%build
%make_build CC="%__cc" CFLAGS="%optflags"

%install
%__mkdir_p %buildroot%_bindir
%make install PREFIX=%buildroot%_prefix

%files
%doc README COPYING
%_bindir/%name

%changelog
* Mon Apr 03 2006 Sir Raorn <raorn@altlinux.ru> 1.5-alt2
- Spec cleanup, updated buildreqs
- Fixed link with -Wl,--as-needed
- Honor %%__cc and %%optflags

* Mon Jul 19 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5-alt1
-  initial build.

