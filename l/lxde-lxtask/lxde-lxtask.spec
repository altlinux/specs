%define upstreamname lxtask
Name: lxde-%upstreamname
Version: 0.1.4
Release: alt4

Summary: Task manager for LXDE
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net

Source: %upstreamname-%version.tar.gz
Patch: lxtask-fix-usage-tt.patch

# Automatically added by buildreq on Mon May 03 2010
BuildRequires: cvs intltool libgtk+2-devel

%description
LXTask - lightweight and desktop-independent task manager derived from
xfce4-taskmanager with all dependencies on xfce removed, new features,
and some improvement of the user interface.

%prep
%setup -n %upstreamname-%version
%patch -p2

%build
%autoreconf
%configure
touch -r po/Makefile po/stamp-it
%make_build

%install
%makeinstall_std
%find_lang %upstreamname

%files -f %upstreamname.lang
%doc ChangeLog INSTALL README TODO
%_bindir/*
%_desktopdir/*

%changelog
* Tue Jun 12 2012 Radik Usupov <radik@altlinux.org> 0.1.4-alt4
- new upstream snapshot

* Thu Sep 22 2011 Radik Usupov <radik@altlinux.org> 0.1.4-alt3
- really usage tt_RU

* Tue Aug 30 2011 Radik Usupov <radik@altlinux.org> 0.1.4-alt2
- new upstream snapshot

* Wed Apr 27 2011 Radik Usupov <radik@altlinux.org> 0.1.4-alt1
- new upstream version

* Mon May 03 2010 Mykola Grechukh <gns@altlinux.ru> 0.1.3-alt2
- new upstream version

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for lxde-lxtask

* Fri May 23 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
