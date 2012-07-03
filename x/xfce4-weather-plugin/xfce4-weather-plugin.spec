Name: xfce4-weather-plugin
Version: 0.7.4
Release: alt4

Summary: Weather plugin for the XFce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: xfce4-weather-plugin-0.7.4-debian-license.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4util-devel libxfce4ui-devel libxfce4panel-devel

BuildRequires: intltool libxml2-devel

Requires: xfce4-panel >= 4.8.0

%description
%name is the plugin for the XFce panel, that display weather information

%prep
%setup
%patch -p1
%patch1 -p1

%build
%xfce4reconf
%configure \
    --disable-static \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_libexecdir/xfce4/panel-plugins/*
%_datadir/xfce4/weather
%_datadir/xfce4/panel/plugins/*.desktop
%_liconsdir/*.png

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt4
- Change the license key for the one from CTW (patch from Debian).
- Port xfce4-weather-plugin to libxfce4ui (Xfce bug #7956).
- Don't use git snapshot, build 0.7.4 version again.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt3.git20111123
- Rebuild with xfce4-panel-4.9.

* Wed Nov 23 2011 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt2.git20111123
- Changed descpription.
- Upstream git snapshot.

* Thu Feb 10 2011 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Updated to 0.7.4.

* Fri Jun 18 2010 Paul Wolneykien <manowar@altlinux.ru> 0.7.2-alt1
- New upstream version 0.7.2 (closes: 23634)

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux> 0.6.2-alt1
- new version
- add watch file

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.5.99.1-alt1
- 0.5.99.1

* Sun Mar 13 2005 Andrey Astafiev <andrei@altlinux.ru> 0.4.9-alt1
- 0.4.9

* Sat Jan 29 2005 Andrey Astafiev <andrei@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Tue Jan 18 2005 Andrey Astafiev <andrei@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sat Jan 01 2005 Andrey Astafiev <andrei@altlinux.ru> 0.3.0-alt2
- Rebuilt with new xfce4-panel.

* Mon May 17 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.0-alt1
- First version of RPM package for Sisyphus.
