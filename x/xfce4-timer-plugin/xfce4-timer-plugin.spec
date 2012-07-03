Name: xfce4-timer-plugin
Version: 0.6.2
Release: alt3

Summary: Timer plugin for XFCE 4.4
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4util-devel libxfcegui4-devel libxfce4panel-devel
BuildRequires: perl-XML-Parser intltool

%description
Nothing to describe really. Use the options menu to add timers. You can
choose them to be countdown periods or alarms at certain times. Only one
of them can be run at a time.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_libexecdir/xfce4/panel-plugins/*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt2
- Rebuild with xfce4-panel-4.9.

* Wed Jun 22 2011 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Drop obsoleted patch.
- Updated to 0.6.2.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt2
- Fix segfault when creating plugin in 4.8 panel.
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.6.1-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.6-alt1
- new version
- add watch file

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.5.1-alt1
- First build
