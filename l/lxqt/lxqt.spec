Name: lxqt
Version: 0.12
Release: alt2
Summary: Meta package for install LxQt
Group: Graphical desktop/Other
License: GPL
Url: https://lxqt.org
BuildArch: noarch

# core componenets
Requires: liblxqt-data lxmenu-data lxqt-about lxqt-common lxqt-globalkeys lxqt-notificationd lxqt-panel lxqt-powermanagement lxqt-qtplugin lxqt-runner lxqt-session pcmanfm-qt lxqt-l10n qterminal
# system configuration tools
Requires: lxqt-config obconf-qt
# themes
Requires: icon-theme-oxygen

Requires: openbox eject

# sound mixer
Requires: qasmixer

# optional components
Requires: lxqt-openssh-askpass lxqt-policykit

%description
%summary

%files
%changelog
* Mon Mar 26 2018 Anton Midyukov <antohami@altlinux.org> 0.12-alt2
- Added Url

* Fri Mar 23 2018 Anton Midyukov <antohami@altlinux.org> 0.12-alt1
- Initial build for ALT
