# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize /usr/bin/icon-slicer /usr/bin/pygtk-codegen-2.0 pkgconfig(cairo) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) python-devel
# END SourceDeps(oneline)
Name: sugar-presence-service
Version: 0.90.2
Release: alt1_1
Summary: The Sugar presence service

Group: System/Libraries
License: GPLv2+
URL: http://dev.laptop.org/
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.bz2
BuildArch: noarch


Requires: python-module-telepathy
Requires: dbus-python
Requires: telepathy-gabble
Requires: telepathy-mission-control
Requires: telepathy-salut
Source44: import.info

%description
The Sugar presence service.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

%files
%doc COPYING
%{_bindir}/sugar-presence-service
%{_datadir}/sugar-presence-service
%{_datadir}/dbus-1/services/org.laptop.Sugar.Presence.service

%changelog
* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.90.2-alt1_1
- new version; import from fc17 release

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.88.0-alt1.1
- Rebuild with Python-2.7

* Tue Apr 06 2010 Aleksey Lim <alsroot@altlinux.org> 0.88.0-alt1
- Sucrose 0.88.0 release

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.84.0-alt2.1
- Rebuilt with python 2.6

* Tue Apr 28 2009 Aleksey Lim <alsroot@altlinux.org> 0.84.0-alt2
- fix %files warnings

* Tue Mar 17 2009 Aleksey Lim <alsroot@altlinux.org> 0.84.0-alt1
- update Sucrose to 0.84.0 version

* Tue Jan 20 2009 Aleksey Lim <alsroot@altlinux.org> 0.83.3-alt1
- new Sucrose 0.83.4 release

* Tue Dec 23 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.2-alt1
- new upstream release

* Fri Dec 12 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.1-alt1
- Sugar 0.84 release cycle

* Sun Nov 23 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.2-alt2
- change group tag to "Graphical desktop/Sugar"

* Tue Nov 18 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.2-alt1
- first build for ALT Linux Sisyphus
