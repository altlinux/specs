Name: xfce4-mount-plugin
Version: 0.6.3
Release: alt2

Summary: Mount plugin for XFce Desktop
License: %gpl2plus
Group: Graphical desktop/XFce
Packager: XFCE Team <xfce@packages.altlinux.org>

Url: http://goodies.xfce.org/projects/panel-plugins/%name
# Upstream: git://git.xfce.org/panel-plugins/xfce4-mount-plugin
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel
BuildRequires: perl-XML-Parser intltool

Requires: xfce4-panel

%description
%name this little plugin behaves like the "kwikdisk - removable media
utility" shipped Press it and it will display a list of items
representing your various devices. The plugin displays various
information on each device.

%prep
%setup

%build
%xfce4reconf
%configure \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_libdir/xfce4/panel/plugins/*.so
%_iconsdir/hicolor/*/apps/*
%_datadir/xfce4/panel/plugins/*.desktop

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Fri May 04 2012 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt2
- Don't package *.la file.

* Fri Apr 27 2012 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt1
- Require xfce4-panel.
- Updated to 0.6.3.

* Mon Apr 23 2012 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Updated to 0.6.2.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Drop obsoleted patch.
- Updated to 0.6.0.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt4
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt3
- Rebuild with xfce4-panel-4.9.

* Thu Jan 27 2011 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt2
- Fix desktop file path for xfce4-panel >= 4.8.
- Add translations patch from FC.
- Spec update.

* Mon May 19 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.5-alt1
- new fersion

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.4-alt1
- new version
- add watch file

* Thu May 03 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.4.7-alt1
- 0.4.7

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.5-alt1
- 0.4.5 for xfce 4.4rc1

* Sun Sep 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3.1-alt1
- new version
- add russian and ukrainian translation

* Thu Aug 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3-alt1
- First build for Sisyphus.

