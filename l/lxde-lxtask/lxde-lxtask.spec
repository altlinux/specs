%define upstreamname lxtask
%define gtkver 2
Name: lxde-%upstreamname
Version: 0.1.8
Release: alt1

Summary: Task manager for LXDE
License: GPL
Group: Graphical desktop/Other
Url: http://git.lxde.org/gitweb/?p=lxde/lxtask.git
Packager: LXDE Development Team <lxde at packages.altlinux.org>

Source: %upstreamname-%version.tar

BuildPreReq: libgtk+%gtkver-devel intltool

%description
LXTask - lightweight and desktop-independent task manager derived from
xfce4-taskmanager with all dependencies on xfce removed, new features,
and some improvement of the user interface.

%prep
%setup -n %upstreamname-%version

%build
%autoreconf
%if %gtkver==3
    %configure --enable-gtk3
%else
    %configure
%endif
#touch -r po/Makefile po/stamp-it
%make_build

%install
%makeinstall_std
%find_lang %upstreamname

%files -f %upstreamname.lang
%doc ChangeLog INSTALL README TODO
%_bindir/*
%_desktopdir/*
%_man1dir/*

%changelog
* Wed Feb 15 2017 Anton Midyukov <antohami@altlinux.org> 0.1.8-alt1
- new version 0.1.8

* Tue May 17 2016 Anton Midyukov <antohami@altlinux.org> 0.1.7-alt1
- New version
- Remove lxtask-fix-usage-tt.patch.

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
