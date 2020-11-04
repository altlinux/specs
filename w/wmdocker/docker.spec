# vim: set ft=spec: -*- rpm-spec -*-
# $Id: docker,v 1.2 2006/04/03 13:32:55 raorn Exp $

%define oname docker

Name: wmdocker
Version: 1.5
Release: alt3

Summary: Docker is a docking application (WindowMaker dock app) which acts as a system tray for KDE and GNOME2. 
License: GPL
Group: Graphical desktop/Window Maker

Url: http://icculus.org/openbox/2/docker

# Source-url: %url/%oname-%version.tar.gz
Source: %name-%version.tar
Patch: %oname-1.5-alt-link.patch

Obsoletes: docker < 1.5-alt3

# Automatically added by buildreq on Mon Apr 03 2006
BuildRequires: glib2-devel libX11-devel pkg-config

%description
Docker is a docking application (WindowMaker dock app) which acts as a system 
tray for KDE and GNOME2. It can be used to replace the panel in either 
environment, allowing you to have a system tray without running the KDE/GNOME 
panel or environment.

%prep
%setup
%patch -p1

%build
%make_build CC="%__cc" CFLAGS="%optflags"

%install
%__mkdir_p %buildroot%_bindir
%make install PREFIX=%buildroot%_prefix

# see https://bugzilla.altlinux.org/show_bug.cgi?id=29990
# see https://fedorahosted.org/fpc/ticket/341
mv %buildroot/%_bindir/%oname %buildroot/%_bindir/%name

%files
%doc README COPYING
%_bindir/%name

%changelog
* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt3
- NMU: rename package and command to wmdocker (ALT bug 29990)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.5-alt2.qa1
- NMU: rebuilt for debuginfo.

* Mon Apr 03 2006 Sir Raorn <raorn@altlinux.ru> 1.5-alt2
- Spec cleanup, updated buildreqs
- Fixed link with -Wl,--as-needed
- Honor %%__cc and %%optflags

* Mon Jul 19 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.5-alt1
-  initial build.

