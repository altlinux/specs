Name: telepathy-inspector
Version: 0.5.3
Release: alt1

Summary: The swiss-army knife of every telepathy developer
License: LGPL
Group: Development/Debuggers
Url: http://telepathy.freedesktop.org/wiki/TelepathyInspector

Source: http://telepathy.freedesktop.org/releases/%name/%name-%version.tar.gz

# Automatically added by buildreq on Wed Apr 30 2008
BuildRequires: gcc-c++ libdbus-glib-devel libglade-devel libtelepathy-glib-devel python-module-PyXML xsltproc

%description
Telepathy Inspector is a telepathy client (GTK+) whose objective is to expose
all interfaces and functionalities implemented by a given connection manager
along with its connections, channels, etc.

The idea is to enable the user (likely to be a Telepathy developer) to easily
view and access all methods and interfaces of all Telepathy entities (CMs,
connections, etc), which could not be easily achieved using a regular
telepathy client since it would (and should!) hide all Telepathy logic
behind a pleasant, usability oriented, GUI.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*
%_datadir/telepathy-inspector/*.xml

%changelog
* Sun Nov 09 2008 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Wed Apr 30 2008 Igor Zubkov <icesik@altlinux.org> 0.5.2-alt1
- 0.5.1 -> 0.5.2
- buildreq

* Mon Apr 28 2008 Igor Zubkov <icesik@altlinux.org> 0.5.1-alt2
- fix rebuild

* Wed Feb 27 2008 Igor Zubkov <icesik@altlinux.org> 0.5.1-alt1
- 0.5.0 -> 0.5.1
- buildreq

* Thu Jul 12 2007 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt1
- build for Sisyphus

