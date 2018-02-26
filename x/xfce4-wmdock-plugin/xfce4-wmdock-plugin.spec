Name: xfce4-wmdock-plugin
Version: 0.3.4
Release: alt3

Summary: Support WindowMaker dockapps for the XFce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Packager: XFCE Team <xfce@packages.altlinux.org>

Url: http://goodies.xfce.org/projects/panel-plugins/%name
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4util-devel libxfcegui4-devel libxfce4panel-devel
BuildRequires: libwnck-devel intltool

Requires: xfce4-panel >= 4.8

%description
The WMdock plugin is a compatibility layer for running WindowMaker
dockapps on the XFCE desktop. It integrates the dockapps into a panel,
closely resembling the look and feel of the WindowMaker dock or clip,
respectively.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_liconsdir/*.png
%_libexecdir/xfce4/panel-plugins/*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).
- Updated translations from upstream git.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt2
- Rebuild with xfce4-panel-4.9.

* Mon Oct 17 2011 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- Drop obsoleted patches.
- Updated to 0.3.4.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Fix indirect linking (backport from upstream).
- Added build support for xfce4-panel 4.7.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.
- Updated to 0.3.2.

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2.0-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1.8-alt1
- First build
