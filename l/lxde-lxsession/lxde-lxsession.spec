%define upstreamname lxsession
Name: lxde-%upstreamname
Version: 0.4.6.1
Release: alt3

Summary: LXSession is the default X11 session manager of LXDE.
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net

Provides: lxde-lxsession-lite
Obsoletes: lxde-lxsession-lite

Provides: lxde-settings-daemon
Obsoletes: lxde-settings-daemon

Source: %upstreamname-%version.tar.gz
Patch: lxsession-0.4.6.1-alt-kdmfix.patch

# Automatically added by buildreq on Tue May 19 2009
BuildRequires: cvs intltool libXau-devel libdbus-devel libgtk+2-devel xsltproc docbook-dtds docbook-style-xsl

%description
LXSession is lightweiht, and it's not tighted to "any" desktop environment.
It's desktop-independent and can be used with any window manager.
With proper configuration, you can make your own desktop environment with
LXSession. This is very useful to the users and developers of non-mainstream
window managers and desktop environemts.

%prep
%setup -n %upstreamname-%version
%patch -p2

%build
%__sed -i '/m4/ d' Makefile.am
%autoreconf
%configure --enable-man

%make_build

%install
%makeinstall_std
%find_lang %upstreamname

%files -f %upstreamname.lang
%doc ChangeLog NEWS README
%_bindir/*
%_datadir/%upstreamname
%_man1dir/*

%changelog
* Mon Jun 11 2012 Radik Usupov <radik@altlinux.org> 0.4.6.1-alt3
- new upstream snapshot

* Tue Jan 31 2012 Radik Usupov <radik@altlinux.org> 0.4.6.1-alt2
- Added kdm support (Closes: 26823)

* Mon Aug 29 2011 Radik Usupov <radik@altlinux.org> 0.4.6.1-alt1
- new upstream snapshot

* Wed Apr 27 2011 Mykola Grechukh <gns@altlinux.ru> 0.4.5-alt1
- new upstream snapshot

* Mon Apr 12 2010 Nick S. Grechukh <gns@altlinux.ru> 0.4.4-alt1
- new version

* Fri Mar 12 2010 Nick S. Grechukh <gns@altlinux.ru> 0.4.2-alt1
- new version

* Tue Dec 22 2009 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt3
- settings daemon now integrated into lxsession

* Sat Dec 12 2009 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt2
- provides lxsession-lite to satisfy dependencies

* Sat Dec 12 2009 Nick S. Grechukh <gns@altlinux.ru> 0.4.1-alt1
- new version

* Wed Dec 09 2009 Mykola Grechukh <gns@altlinux.ru> 0.4.0-alt1
- new version

* Tue May 19 2009 Nick S. Grechukh <gns@altlinux.org> 0.3.8-alt1
- new version. Now lxsession is replaced by lxsession-lite in upstream.

* Fri Jan 09 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2-alt2
- Add conflicts to lxde-lxsession
- remove obsoletes %%update_menu macros

* Fri Jul 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2-alt1
- new version 

* Fri May 23 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
