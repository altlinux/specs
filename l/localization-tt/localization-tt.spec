Name: localization-tt
Version: 241004
Release: alt1

Summary: Translation files for Tatar language
License: GPLv2+
Group: Text tools

BuildArch: noarch
Source: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/locale/tt/LC_MESSAGES
msgfmt po/lightdm-gtk-greeter.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/lightdm-gtk-greeter.mo
msgfmt po/Linux-PAM.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/Linux-PAM.mo
msgfmt po/NetworkManager.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/NetworkManager.mo
msgfmt po/NetworkManager-applet-gtk.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/NetworkManager-applet-gtk.mo
msgfmt po/NetworkManager-openconnect.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/NetworkManager-openconnect.mo
msgfmt po/NetworkManager-openvpn.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/NetworkManager-openvpn.mo
msgfmt po/NetworkManager-pptp.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/NetworkManager-pptp.mo
msgfmt po/NetworkManager-vpnc.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/NetworkManager-vpnc.mo
msgfmt po/thunar.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/thunar.mo
msgfmt po/thunar-archive-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/thunar-archive-plugin.mo
msgfmt po/thunar-media-tags-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/thunar-media-tags-plugin.mo
msgfmt po/thunar-shares-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/thunar-shares-plugin.mo
msgfmt po/thunar-volman.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/thunar-volman.mo
msgfmt po/xfce4-appfinder.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-appfinder.mo
msgfmt po/xfce4-battery-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-battery-plugin.mo
msgfmt po/xfce4-clipman-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-clipman-plugin.mo
msgfmt po/xfce4-cpufreq-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-cpufreq-plugin.mo
msgfmt po/xfce4-cpugraph-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-cpugraph-plugin.mo
msgfmt po/xfce4-datetime-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-datetime-plugin.mo
msgfmt po/xfce4-diskperf-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-diskperf-plugin.mo
msgfmt po/xfce4-eyes-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-eyes-plugin.mo
msgfmt po/xfce4-fsguard-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-fsguard-plugin.mo
msgfmt po/xfce4-mailwatch-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-mailwatch-plugin.mo
msgfmt po/xfce4-mount-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-mount-plugin.mo
msgfmt po/xfce4-netload-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-netload-plugin.mo
msgfmt po/xfce4-notes-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-notes-plugin.mo
msgfmt po/xfce4-notifyd.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-notifyd.mo
msgfmt po/xfce4-panel.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-panel.mo
msgfmt po/xfce4-places-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-places-plugin.mo
msgfmt po/xfce4-power-manager.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-power-manager.mo
msgfmt po/xfce4-pulseaudio-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-pulseaudio-plugin.mo
msgfmt po/xfce4-screensaver.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-screensaver.mo
msgfmt po/xfce4-screenshooter.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-screenshooter.mo
msgfmt po/xfce4-session.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-session.mo
msgfmt po/xfce4-settings.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-settings.mo
msgfmt po/xfce4-systemload-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-systemload-plugin.mo
msgfmt po/xfce4-taskmanager.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-taskmanager.mo
msgfmt po/xfce4-terminal.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-terminal.mo
msgfmt po/xfce4-time-out-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-time-out-plugin.mo
msgfmt po/xfce4-timer-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-timer-plugin.mo
msgfmt po/xfce4-verve-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-verve-plugin.mo
msgfmt po/xfce4-whiskermenu-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-whiskermenu-plugin.mo
msgfmt po/xfdesktop.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfdesktop.mo
msgfmt po/xdg-user-dirs.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xdg-user-dirs.mo
msgfmt po/xfce4-xkb-plugin.po -o %buildroot%_datadir/locale/tt/LC_MESSAGES/xfce4-xkb-plugin.mo

%files
%_datadir/locale/tt/LC_MESSAGES/*

%changelog
* Fri Oct 04 2024 Kirill Izmestev <felixz@altlinux.org> 241004-alt1
- Added translation files.

* Sun Sep 01 2024 Kirill Izmestev <felixz@altlinux.org> 240901-alt1
- Added translation files.

* Sat Aug 31 2024 Kirill Izmestev <felixz@altlinux.org> 240831-alt1
- Initial build for Sisyphus.
- Added translation files.
