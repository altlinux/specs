Name: xfce4-eyes-plugin
Version: 4.4.5
Release: alt1

Summary: Eyes plugin for Xfce Desktop
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

# git://git.xfce.org/panel-plugins/xfce4-eyes-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel
BuildRequires: intltool libxml2-devel

Requires: xfce4-panel >= 4.8

%description
Eyes is a xfce4 panel plugin that adds eyes which watch your every step.
Scary!

%prep
%setup
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag eyes_version_tag configure.ac.in

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
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/eyes/
%_datadir/xfce4/panel/plugins/*.desktop
%_liconsdir/*.png

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Wed Apr 27 2016 Mikhail Efremov <sem@altlinux.org> 4.4.5-alt1
- Updated to 4.4.5.

* Mon Mar 16 2015 Mikhail Efremov <sem@altlinux.org> 4.4.4-alt1
- Updated to 4.4.4.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 4.4.3-alt2
- Rebuild with libxfce4util-4.12.

* Mon Dec 29 2014 Mikhail Efremov <sem@altlinux.org> 4.4.3-alt1
- Fix build: create m4/ directory.
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 4.4.3.

* Mon Mar 04 2013 Mikhail Efremov <sem@altlinux.org> 4.4.2-alt1
- Fix build: use LT_PREREQ.
- Updated translations from upstream git.
- Updated to 4.4.2.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 4.4.1-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 4.4.1-alt2
- Rebuild with xfce4-panel-4.9.

* Sat Feb 05 2011 Mikhail Efremov <sem@altlinux.org> 4.4.1-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.
- Updated to 4.4.1

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt1
- new version
- add watch file

* Mon Dec 18 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- new version

* Thu Aug 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.3.0-alt1
- First build for Sisyphus.

