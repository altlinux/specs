%define _unpackaged_files_terminate_build 1

Name: ayatana-webmail
Version: 22.6.28
Release: alt2

Summary: Webmail notifications and actions for any desktop
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-webmail

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: ayatana-indicator-messages
BuildRequires: glib2-devel
BuildRequires: hicolor-icon-theme
BuildRequires: pkg-config
BuildRequires: python3-module-polib
BuildRequires: python3-module-psutil
BuildRequires: python3-module-setuptools

Requires: typelib(AyatanaAppIndicator3)
Requires: python3-module-polib
Requires: python3-module-psutil

%description
Ayatana Webmail is an application that integrates your webmail
into MATE, Xfce, LXDE and other environments.

It displays notifications about incoming mail, shows the number
of unread messages and displays subjects in the Messaging Menu.

The Launcher item also has a quicklist that provides quick access
to your mail folders. It also allows you to quickly compose a new
message.

Ayatana Webmail starts automatically, all you have to do is to
enter your accounts settings in a configuration dialog.

%prep
%setup

# Remove hashbangs on scripts installed into sitelib.
find 'ayatanawebmail' -type 'f' -iname '*.py' -exec sed -i -e '0,/^\s*#!\s*\/.*$/d' '{}' '+'

# Also remove executable flags.
find 'ayatanawebmail' -type 'f' -iname '*.py' -exec chmod -x '{}' '+'
chmod -x 'COPYING' 'README.md'
for base in 'etc' 'usr/share'; do
  find "data/${base}" -type 'f' -exec chmod -x '{}' '+'
done

%build
%python3_build

%install
%python3_install

%files
%doc COPYING AUTHORS NEWS README.md
%_bindir/ayatana-webmail
%_bindir/ayatana-webmail-clear
%_bindir/ayatana-webmail-reset
%_bindir/ayatana-webmail-settings
%_bindir/ayatana-webmail-url
%python3_sitelibdir/ayatanawebmail
%python3_sitelibdir/ayatanawebmail-%{version}*-info
%_datadir/locale/*/LC_MESSAGES/*.mo
%config %_sysconfdir/xdg/autostart/%name-autostart.desktop
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/apps
%_iconsdir/hicolor/scalable/apps/*
%dir %_iconsdir/hicolor/scalable/status
%_iconsdir/hicolor/scalable/status/*
%_datadir/glib-2.0/schemas/org.ayatana.webmail.gschema.xml
%_desktopdir/ayatana-webmail.desktop

%changelog
* Mon Feb 13 2023 Nikolay Strelkov <snk@altlinux.org> 22.6.28-alt2
- removed optional typelib(AppIndicator3) dependency

* Mon Nov 07 2022 Nikolay Strelkov <snk@altlinux.org> 22.6.28-alt1
- Initial build for Sisyphus
