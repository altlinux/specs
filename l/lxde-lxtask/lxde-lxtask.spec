%define upstreamname lxtask
%define gtkver 3
Name: lxde-%upstreamname
Version: 0.1.12
Release: alt1

Summary: Task manager for LXDE
License: GPL-2.0-or-later
Group: Graphical desktop/Other
URL: https://github.com/lxde/lxtask
VCS: https://github.com/lxde/lxtask.git

Source: %upstreamname-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: libgtk+%gtkver-devel intltool

%description
LXTask - lightweight and desktop-independent task manager derived from
xfce4-taskmanager with all dependencies on xfce removed, new features,
and some improvement of the user interface.

%prep
%setup -n %upstreamname-%version
%autopatch -p1

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
* Sat May 03 2025 Anton Midyukov <antohami@altlinux.org> 0.1.12-alt1
- new version 0.1.12
- build with gtk+3
- convert License tag to SPDX format
- add VCS tag

* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 0.1.10-alt1
- new version 0.1.10
- Fix License Tag
- Update URL Tag

* Thu Mar 21 2019 Anton Midyukov <antohami@altlinux.org> 0.1.9-alt1
- new version 0.1.9

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
