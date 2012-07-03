Name: xfce4-cpufreq-plugin
Version: 1.0.0
Release: alt3

Summary: Show CPU freqency and governours plugin for the XFce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfcegui4-devel libxfce4util-devel

BuildRequires: fontconfig libX11-devel libgtk+2-devel libstartup-notification perl-XML-Parser

Requires: xfce4-panel >= 4.8

%description
xfce4-cpufreq-plugin is a Plugin for the Xfce Panel, which
shows CPU Informations

%prep
%setup

%build
# Fix desktop file path for xfce4-panel >= 4.8
sed -i 's|^desktopdir = \$(datadir)/xfce4/panel-plugins|desktopdir = \$(datadir)/xfce4/panel/plugins|' \
   panel-plugin/Makefile.am

%xfce4reconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_liconsdir/*.png
%_miconsdir/*.png
%_iconsdir/hicolor/22x22/apps/*.png
%_libexecdir/xfce4/panel-plugins/*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Rebuild with xfce4-panel-4.9.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.gz -> tar.
- Updated to 1.0.0.

* Wed Dec 26 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2-alt0svn3751
- new build from svn

* Tue Jan 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.0.1-alt1
- First build
