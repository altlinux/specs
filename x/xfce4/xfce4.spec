Name: xfce4
Version: 4.10
Release: alt1
Summary: Set of XFce4 Desktop installers.
License: %gpl2plus
Group: Graphical desktop/XFce
URL: http://www.xfce.org
Packager: XFCE Team <xfce@packages.altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

%description
A set of virtual packages for Xfce4 Desktop installation.

%package minimal
Summary: Minimal installation of XFce4 Desktop
Summary(ru_RU.UTF8): Минимальная установка XFce4
Group: Graphical desktop/XFce
Requires: ConsoleKit
Requires: xfce4-panel
Requires: xfce4-session
Requires: xfce4-settings
Requires: xfconf-utils
Requires: xfdesktop
Requires: xfwm4

%description minimal
%name-minimal is a virtual package to provide minimal installation
of XFce4 Desktop.

%description -l ru_RU.UTF8
%name-minimal устанавливает минимальный набор пакетов необходимых
для работы с окружением рабочего стола Xfce 4.

%package default
Summary: Default installation of XFce4 Desktop
Group: Graphical desktop/XFce
Requires: %name-minimal = %version-%release
Requires: xfce4-power-manager
Requires: xfce4-appfinder
Requires: gtk2-themes-xfce4
Requires: xfce4-notifyd
Requires: xfce4-mixer
Requires: xfce4-volumed
Requires: xfce4-taskmanager
Requires: Terminal
Requires: tumbler
Requires: thunar
Requires: thunar-volman-plugin
Requires: thunar-media-tags-plugin
Requires: thunar-archive-plugin
# Icon themes
Requires: xfce4-icon-theme
# for trash and network in Thunar
Requires: gvfs gvfs-backends
# Screensaver
Requires: screen-saver-engine

%description default
%name-default is a virtual package to provide default installation
of XFce4 Desktop.

%package full
Summary: Default installation of XFce4 Desktop
Group: Graphical desktop/XFce
Requires: %name-default = %version-%release
Requires: xfwm4-themes
Requires: xfce4-session-engines
Requires: xfce4-dict
Requires: orage
Requires: xfce4-screenshooter
Requires: xarchiver
# Panel plugins
Requires: xfce4-clipman-plugin
Requires: xfce4-cpufreq-plugin
Requires: xfce4-xkb-plugin
Requires: xfce4-timer-plugin
Requires: xfce4-datetime-plugin
Requires: xfce4-places-plugin
Requires: xfce4-quicklauncher-plugin
Requires: xfce4-time-out-plugin
Requires: xfce4-fsguard-plugin
Requires: xfce4-mailwatch-plugin
Requires: xfce4-battery-plugin
Requires: xfce4-verve-plugin
Requires: xfce4-diskperf-plugin
Requires: xfce4-eyes-plugin
Requires: xfce4-notes-plugin
Requires: xfce4-netload-plugin
Requires: xfce4-mount-plugin
Requires: xfce4-weather-plugin
Requires: xfce4-genmon-plugin
Requires: xfce4-wmdock-plugin
Requires: xfce4-systemload-plugin
Requires: xfce4-cpugraph-plugin
Requires: xfce4-kbdleds-plugin
Requires: xfce4-sensors-plugin

# Not needed for most users.
#Requires: xfce4-radio-plugin

# Thunar plugins
# It requires additional configuration in /etc/samba/smb.conf.
#Requires: thunar-shares-plugin

%description full
%name-full is a virtual package to provide full installation
of XFce4 Desktop.

%files minimal
%files default
%files full

%changelog
* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.10-alt1
- Bump version to 4.10.
- default: Thunar -> thunar.
- minimal: Drop xfce-utils.
- full: Drop xfce4-radio-plugin.
- full: xfcalendar -> orage.

* Tue Nov 22 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt7
- default: Drop tango-icon-theme.

* Mon Oct 17 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt6
- full: Add xfce4-kbdleds-plugin and xfce4-sensors-plugin.
- full: Add xfce4-session-engines.

* Tue Jun 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt5
- full: Drop xfce4-xfapplet-plugin.

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt4
- full: Drop xfce4-globalmenu-plugin.

* Thu Apr 21 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt3
- default: Add tango-icon-theme.
- full: Drop restretto.

* Mon Apr 18 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt2
- default: Add xfce4-volumed.

* Wed Mar 30 2011 Mikhail Efremov <sem@altlinux.org> 4.8-alt1
- Add xfce4-{minimal,default,full} virtual subpackages.
- Rename to xfce4, rewrite spec.

* Sun May 24 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6-alt1
- Fix for bug #20148.
- Added Thunar as depency.

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.2-alt1
- Added xfce4-session.

* Mon Nov 10 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0-alt2
- Changed Group tag.

* Tue Oct 07 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0-alt1
- 4.0

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Tue Sep 11 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt1
- Doesn't depends on packages version anymore.

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Mon Aug 18 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- First version of RPM package for Sisyphus.
