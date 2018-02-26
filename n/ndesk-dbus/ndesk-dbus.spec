Name: ndesk-dbus
Version: 0.6.0
Release: alt6

Summary: C# implementation of D-Bus
Group: Development/Other
License: X11/MIT
URL: http://www.ndesk.org/DBusSharp

Source0: %name-%version.tar.gz
Patch0: %name-fix-path.patch

Packager: Mono Maintainers Team <mono@packages.altlinux.org>

BuildPreReq: /proc
BuildRequires: mono-mcs mono-devel

%description
ndesk-dbus is a C# implementation of D-Bus. It's often referred to as "managed
D-Bus" to avoid confusion with existing bindings (which wrap libdbus).

D-Bus is an inter-process communication framework that lets applications
interface with the system event bus as well as allowing them to talk to one
another in a peer-to-peer configuration.

%package devel
Summary: Ndesk-dbus development files
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

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
%_monodir/ndesk-dbus-1.0

%files devel
%_pkgconfigdir/*

%changelog
* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt6
- move pkgconfig files from main to devel package

* Mon Feb 16 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt5
- change packager
- add mono-devel to BuildRequires

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 0.6.0-alt4
- don't use obsolete macros

* Sat Dec 29 2007 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt3
- change %%_libdir to %%_monodir and %%_monogacdir
- add patch for changing $(libdir) to $(prefix)/lib (mono policy)

* Sat Dec 22 2007 Igor Zubkov <icesik@altlinux.org> 0.6.0-alt2
- remove BuildArch: noarch from spec file

* Thu Dec 20 2007 Igor Zubkov <icesik@altlinux.org> 0.6.0-alt1
- 0.5.2 -> 0.6.0

* Sun Dec 16 2007 Igor Zubkov <icesik@altlinux.org> 0.5.2-alt1
- build for Sisyphus

* Thu Jun 21 2007 maw@suse.de
- Don't build as root.
* Tue Apr 10 2007 cgaisford@novell.com
- Updated to 0.5.2
- Removed previous patch as it was integrated upstream
* Tue Feb 27 2007 andreas.hanke@gmx-topmail.de
- Initial package, version 0.4.1
