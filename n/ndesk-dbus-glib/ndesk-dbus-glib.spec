Name: ndesk-dbus-glib
Version: 0.4.1
Release: alt6

Summary: GLib integration for NDesk.DBus, the D-Bus IPC library
License: X11/MIT
Group: Development/Other
URL: http://www.ndesk.org/DBusSharp

Source0: %name-%version.tar.gz
Patch0: %name-fix-path.patch

Packager: Mono Maintainers Team <mono@packages.altlinux.org>

BuildPreReq: /proc
BuildRequires: mono-mcs ndesk-dbus-devel mono-devel

%description
ndesk-dbus-glib provides glib integration for NDesk.DBus.

%package devel
Summary: Ndesk-dbus-glib development files
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the ndesk-dbus-glib.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING README
%_monogacdir/*
%_monodir/ndesk-dbus-glib-1.0

%files devel
%_pkgconfigdir/*

%changelog
* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt6
- move pkgconfig files from main to devel package

* Mon Feb 16 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt5
- change packager
- add mono-devel to BuildRequires

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 0.4.1-alt4
- don't use obsolete macros

* Sat Dec 29 2007 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt3
- change %%_libdir to %%_monodir and %%_monogacdir
- add patch for changing $(libdir) to $(prefix)/lib (mono policy)

* Sat Dec 22 2007 Igor Zubkov <icesik@altlinux.org> 0.4.1-alt2
- remove BuildArch: noarch from spec file

* Thu Dec 20 2007 Igor Zubkov <icesik@altlinux.org> 0.4.1-alt1
- 0.3 -> 0.4.1

* Sun Dec 16 2007 Igor Zubkov <icesik@altlinux.org> 0.3-alt1
- build for Sisyphus

* Thu Jun 21 2007 maw@suse.de
- Don't build as root.
* Tue Feb 27 2007 andreas.hanke@gmx-topmail.de
- Initial package, version 0.4.1
