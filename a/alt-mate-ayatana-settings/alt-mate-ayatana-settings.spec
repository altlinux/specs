%define _unpackaged_files_terminate_build 1

Name: alt-mate-ayatana-settings
Version: 0.01
Release: alt2

Summary: Special settings for ALT Linux with MATE and Ayatana Indicators
License: GPL-2.0
Group: Graphical desktop/MATE
Url: https://github.com/N0rbert/alt-mate-ayatana-settings

Source: %name-%version.tar

ExcludeArch: ppc64le

# MATE, MATE Tweak and Ayatana-related part
Requires: mate-file-manager-open-terminal
Requires: mate-applets
Requires: mate-media
Requires: mate-tweak
Requires: mate-indicator-applet
Requires: plank
Requires: tilda
Requires: mate-hud
Requires: mate-vala-panel-appmenu-plugin
Requires: brisk-menu
Requires: libmate-document-viewer
Requires: mate-document-viewer
Requires: sound-theme-freedesktop
Requires: ayatana-indicator-application
Requires: ayatana-indicator-datetime
Requires: ayatana-indicator-messages
Requires: ayatana-indicator-notifications
Requires: ayatana-indicator-power
Requires: ayatana-indicator-session
Requires: ayatana-indicator-sound
Requires: accountsservice
Requires: ayatana-settings
Requires: mate-netbook
Requires: mate-window-buttons-applet
Requires: mate-window-menu-applet
Requires: mate-window-title-applet
Requires: mate-dock-applet
Requires: mate-menu

# Docked items
Requires: firefox-esr
Requires: /usr/bin/caja
Requires: mate-control-center
Requires: mate-system-monitor
Requires: mate-terminal
Requires: mate-calc

# Items on MATE Panel
Requires: evolution

%description
Special package for ALT Linux to get fully-featured MATE desktop environment
with Ayatana Indicators, which are currently in wide use only in Ubuntu MATE
flavour (since 20.10 aka groovy) and later on Debian 12 (bookworm) by using
similar approach in the https://github.com/N0rbert/debian-mate-ayatana-settings
repository.

%prep
%setup

%build
# nothing to build here

%install

# etc
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cp -pv etc/profile.d/mate-ayatana.sh %{buildroot}%{_sysconfdir}/profile.d/

# usr/lib
mkdir -p %{buildroot}%{_target_libdir_noarch}/alt-mate
install -p -m755 usr/lib/alt-mate/alt-mate-settings-overlay %{buildroot}%{_target_libdir_noarch}/alt-mate/
install -p -m755 usr/lib/alt-mate/dock-replace %{buildroot}%{_target_libdir_noarch}/alt-mate/

# usr/share
mkdir -p %{buildroot}%{_desktopdir}
cp -pv usr/share/applications/plank-preferences.desktop %{buildroot}%{_desktopdir}/

mkdir -p %{buildroot}%{_datadir}/{alt-mate,glib-2.0,mate,mate-panel,plank}
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
mkdir -p %{buildroot}%{_datadir}/mate/autostart
mkdir -p %{buildroot}%{_datadir}/mate-panel/layouts
mkdir -p %{buildroot}%{_datadir}/plank/themes/{Mutiny-dark,Mutiny-light,Ubuntu-MATE}

cp -pParv usr/share/alt-mate %{buildroot}%{_datadir}/
cp -pv usr/share/glib-2.0/schemas/30_alt-mate.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/
cp -pv usr/share/mate/autostart/*.desktop %{buildroot}%{_datadir}/mate/autostart/
cp -pParv usr/share/mate-panel/layouts/* %{buildroot}%{_datadir}/mate-panel/layouts/
cp -pParv usr/share/plank/themes/* %{buildroot}%{_datadir}/plank/themes/

%post
echo "WARNING: the MATE Panel layout will be automatically set to Traditional on "
echo "         next login. If you are installing this package for the first time "
echo "         and you care about current layout - please save it manually by "
echo "         using MATE Tweak utility!"

%files
%doc LICENSE README.md images
%{_sysconfdir}/*
%dir %{_target_libdir_noarch}/alt-mate
%{_target_libdir_noarch}/alt-mate/*
%{_desktopdir}/*
%dir %{_datadir}/alt-mate
%{_datadir}/alt-mate/*
%{_datadir}/glib-2.0/*
%{_datadir}/mate/*
%{_datadir}/mate-panel/*
%{_datadir}/plank/*

%changelog
* Wed Feb 19 2025 Nikolay Strelkov <snk@altlinux.org> 0.01-alt2
- Use Firefox ESR instead of Firefox
* Tue Feb 18 2025 Nikolay Strelkov <snk@altlinux.org> 0.01-alt1
- Initial build for Sisyphus
