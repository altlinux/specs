Name: elementary-meta
Version: 1.565
Release: alt1

Summary: Seeds and Metapackages used in elementary OS
License: GPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/metapackages

Source: %name-%version.tar
BuildArch: noarch

%description
%summary.

# #
# # NOTE: no reason to create RPM of this package,
# #       as it is used for distro creation, not for desktop environment
# #
#%%package -n elementary-minimal
#Group: Graphical desktop/Other
#BuildArch: noarch
#Summary: Minimal core of elementary OS
#%%description -n elementary-minimal
#This metapackage depends on all of the packages in the elementary minimal
#system, that is a functional command-line system with the following
#capabilities:
#
#- Boot
#- Detect hardware
#- Connect to a network
#- Install packages
#- Perform basic diagnostics
#
#It is also used to help ensure proper upgrades, so it is recommended that
#it not be removed.

# #
# # NOTE: no reason to create RPM of this package,
# #       as it is used for distro creation, not for desktop environment
# #
#%%package -n elementary-standard
#Group: Graphical desktop/Other
#BuildArch: noarch
#Summary: CLI-only components of elementary OS
#%%description -n elementary-standard
#This metapackage depends on most of non-GUI packages from elementary OS.
#
#This set of packages provides a comfortable command-line Unix-like
#environment.
#
#It is used to ensure proper upgrades, so it is recommended that it not be
#removed.

%package -n elementary-desktop
Group: Graphical desktop/Other
BuildArch: noarch
Summary: Complete desktop of elementary OS
# # deb Depends
# # cat desktop-a* | sort -u
# Requires: # deb: alsa-base
# Requires: # deb: alsa-utils
# Requires: # deb: anacron
# Requires: # deb: at-spi2-core
# Requires: # deb: bc
# Requires: # deb: ca-certificates
# Requires: # deb: doc-base
# Requires: # deb: elementary-artwork
Requires: elementary-artwork
# Requires: # deb: fontconfig
# Requires: # deb: fonts-dejavu-core
# Requires: # deb: foomatic-db-compressed-ppds
# Requires: # deb: ghostscript
# Requires: # deb: gnome-menus
# Requires: # deb: gstreamer1.0-alsa
# Requires: # deb: gstreamer1.0-packagekit
# Requires: # deb: gstreamer1.0-plugins-base-apps
# Requires: # deb: gstreamer1.0-pulseaudio
# Requires: # deb: inputattach
# Requires: # deb: libatk-adaptor
# Requires: # deb: libnotify-bin
# Requires: # deb: libsasl2-modules
# Requires: # deb: openprinting-ppds
# Requires: # deb: pantheon
Requires: pantheon
# Requires: # deb: printer-driver-pnm2ppa
# Requires: # deb: rfkill
# Requires: # deb: spice-vdagent
# Requires: # deb: ubuntu-drivers-common
# Requires: # deb: unzip
# Requires: # deb: wpasupplicant
# Requires: # deb: xdg-user-dirs
# Requires: # deb: xdg-user-dirs-gtk
# Requires: # deb: xkb-data
# Requires: # deb: xorg
# Requires: # deb: zip

# # deb Recommends
# # cat desktop-recommends-a* | sort -u
# Requires: # deb: 7zip
# Requires: # deb: avahi-autoipd
# Requires: # deb: avahi-daemon
# Requires: # deb: bluez
# Requires: # deb: bluez-cups
# Requires: # deb: brltty
# Requires: # deb: cups
# Requires: # deb: cups-bsd
# Requires: # deb: cups-client
# Requires: # deb: cups-filters
# Requires: # deb: elementary-default-settings
Requires: elementary-default-settings
# Requires: # deb: elementary-printer-test-page # SKIP conflict
# Requires: # deb: fonts-arphic-ukai
# Requires: # deb: fonts-arphic-uming
# Requires: # deb: fonts-elementary-core
# Requires: # deb: fonts-kacst-one
# Requires: # deb: fonts-noto-cjk
# Requires: # deb: fonts-noto-color-emoji
# Requires: # deb: fonts-noto-core
# Requires: # deb: fonts-sil-padauk
# Requires: # deb: fonts-ubuntu
# Requires: # deb: fwupd
# Requires: # deb: fwupd-signed
# Requires: # deb: geoclue-2.0
# Requires: # deb: gnome-power-manager
# Requires: # deb: gnome-session-bin
# Requires: # deb: grub-efi-arm64
# Requires: # deb: gtk-im-libthai
# Requires: # deb: gvfs-fuse
# Requires: # deb: heif-gdk-pixbuf
# Requires: # deb: heif-thumbnailer
# Requires: # deb: hplip
# Requires: # deb: htop
# Requires: # deb: hunspell-de-at-frami
# Requires: # deb: hunspell-de-ch-frami
# Requires: # deb: hunspell-de-de-frami
# Requires: # deb: hunspell-en-au
# Requires: # deb: hunspell-en-ca
# Requires: # deb: hunspell-en-gb
# Requires: # deb: hunspell-en-us
# Requires: # deb: hunspell-en-za
# Requires: # deb: hunspell-es
# Requires: # deb: hunspell-fr
# Requires: # deb: hunspell-it
# Requires: # deb: hunspell-pt-br
# Requires: # deb: hunspell-pt-pt
# Requires: # deb: hunspell-ru
# Requires: # deb: ibus
Requires: ibus
# Requires: # deb: ibus-chewing
# Requires: # deb: ibus-gtk
# Requires: # deb: ibus-gtk3
# Requires: # deb: ibus-hangul
# Requires: # deb: ibus-libpinyin
# Requires: # deb: ibus-m17n
# Requires: # deb: ibus-mozc
# Requires: # deb: ibus-table
# Requires: # deb: ibus-table-cangjie
# Requires: # deb: ibus-table-quick-classic
# Requires: # deb: ibus-table-wubi
# Requires: # deb: ibus-unikey
# Requires: # deb: im-config
# Requires: # deb: io.elementary.bluetooth-daemon
Requires: elementary-bluetooth-daemon
# Requires: # deb: io.elementary.greeter
Requires: elementary-greeter
# Requires: # deb: io.elementary.initial-setup
Requires: /usr/bin/io.elementary.initial-setup
# Requires: # deb: io.elementary.onboarding
Requires: /usr/bin/io.elementary.onboarding
# Requires: # deb: io.elementary.panel.bluetooth
Requires: wingpanel-indicator-bluetooth
# Requires: # deb: io.elementary.panel.datetime
Requires: wingpanel-indicator-datetime
# Requires: # deb: io.elementary.panel.keyboard
Requires: wingpanel-indicator-keyboard
# Requires: # deb: io.elementary.panel.network
Requires: wingpanel-indicator-network
# Requires: # deb: io.elementary.panel.nightlight
Requires: wingpanel-indicator-nightlight
# Requires: # deb: io.elementary.panel.notifications
Requires: wingpanel-indicator-notifications
# Requires: # deb: io.elementary.panel.power
#Requires: wingpanel-indicator-power # TODO, FIXME - wait for upstream gschema name update
# Requires: # deb: io.elementary.quick-settings
Requires: wingpanel-quick-settings
# Requires: # deb: io.elementary.settings
Requires: switchboard
# Requires: # deb: io.elementary.settings.applications
Requires: switchboard-plug-applications
# Requires: # deb: io.elementary.settings.bluetooth
Requires: switchboard-plug-bluetooth
# Requires: # deb: io.elementary.settings.datetime
Requires: switchboard-plug-datetime
# Requires: # deb: io.elementary.settings.desktop
Requires: switchboard-plug-pantheon-shell
# Requires: # deb: io.elementary.settings.display
Requires: switchboard-plug-display
# Requires: # deb: io.elementary.settings.keyboard
Requires: switchboard-plug-keyboard
# Requires: # deb: io.elementary.settings.locale
Requires: switchboard-plug-locale
# Requires: # deb: io.elementary.settings.mouse-touchpad
Requires: switchboard-plug-mouse-touchpad
# Requires: # deb: io.elementary.settings.network
Requires: switchboard-plug-network
# Requires: # deb: io.elementary.settings.notifications
Requires: switchboard-plug-notifications
# Requires: # deb: io.elementary.settings.onlineaccounts
Requires: switchboard-plug-onlineaccounts
# Requires: # deb: io.elementary.settings.power
Requires: switchboard-plug-power
# Requires: # deb: io.elementary.settings.printers
Requires: switchboard-plug-printers
# Requires: # deb: io.elementary.settings.screentime-limits
Requires: switchboard-plug-parental-controls
# Requires: # deb: io.elementary.settings.security-privacy
Requires: switchboard-plug-security-privacy
# Requires: # deb: io.elementary.settings.sharing
Requires: switchboard-plug-sharing
# Requires: # deb: io.elementary.settings.sound
Requires: switchboard-plug-sound
# Requires: # deb: io.elementary.settings.system # SKIP, no `vapi(appstream)`
# Requires: # deb: io.elementary.settings.useraccounts
Requires: switchboard-plug-useraccounts
# Requires: # deb: io.elementary.settings.wacom
Requires: switchboard-plug-wacom
# Requires: # deb: io.elementary.wingpanel
Requires: wingpanel
# Requires: # deb: language-pack-bg
# Requires: # deb: language-pack-ca
# Requires: # deb: language-pack-cs
# Requires: # deb: language-pack-da
# Requires: # deb: language-pack-de
# Requires: # deb: language-pack-en
# Requires: # deb: language-pack-es
# Requires: # deb: language-pack-fr
# Requires: # deb: language-pack-gnome-bg
# Requires: # deb: language-pack-gnome-ca
# Requires: # deb: language-pack-gnome-cs
# Requires: # deb: language-pack-gnome-da
# Requires: # deb: language-pack-gnome-de
# Requires: # deb: language-pack-gnome-en
# Requires: # deb: language-pack-gnome-es
# Requires: # deb: language-pack-gnome-fr
# Requires: # deb: language-pack-gnome-hu
# Requires: # deb: language-pack-gnome-id
# Requires: # deb: language-pack-gnome-it
# Requires: # deb: language-pack-gnome-ja
# Requires: # deb: language-pack-gnome-ko
# Requires: # deb: language-pack-gnome-nb
# Requires: # deb: language-pack-gnome-nl
# Requires: # deb: language-pack-gnome-pl
# Requires: # deb: language-pack-gnome-pt
# Requires: # deb: language-pack-gnome-ru
# Requires: # deb: language-pack-gnome-sv
# Requires: # deb: language-pack-gnome-th
# Requires: # deb: language-pack-gnome-tr
# Requires: # deb: language-pack-gnome-uk
# Requires: # deb: language-pack-gnome-vi
# Requires: # deb: language-pack-gnome-zh-hans
# Requires: # deb: language-pack-gnome-zh-hant
# Requires: # deb: language-pack-hu
# Requires: # deb: language-pack-id
# Requires: # deb: language-pack-it
# Requires: # deb: language-pack-ja
# Requires: # deb: language-pack-ko
# Requires: # deb: language-pack-nb
# Requires: # deb: language-pack-nl
# Requires: # deb: language-pack-pl
# Requires: # deb: language-pack-pt
# Requires: # deb: language-pack-ru
# Requires: # deb: language-pack-sv
# Requires: # deb: language-pack-th
# Requires: # deb: language-pack-tr
# Requires: # deb: language-pack-uk
# Requires: # deb: language-pack-vi
# Requires: # deb: language-pack-zh-hans
# Requires: # deb: language-pack-zh-hant
# Requires: # deb: laptop-detect
# Requires: # deb: libgail-common
# Requires: # deb: libnss-mdns
# Requires: # deb: libpam-gnome-keyring
# Requires: # deb: mozc-utils-gui
# Requires: # deb: network-manager
# Requires: # deb: network-manager-config-connectivity-ubuntu
# Requires: # deb: network-manager-pptp-gnome
# Requires: # deb: orca
# Requires: # deb: packagekit
# Requires: # deb: pantheon-agent-polkit
# Requires: # deb: pcmciautils
# Requires: # deb: plymouth-theme-elementary
# Requires: # deb: policykit-desktop-privileges
# Requires: # deb: printer-driver-brlaser
# Requires: # deb: printer-driver-c2esp
# Requires: # deb: printer-driver-foo2zjs
# Requires: # deb: printer-driver-m2300w
# Requires: # deb: printer-driver-min12xxw
# Requires: # deb: printer-driver-ptouch
# Requires: # deb: printer-driver-pxljr
# Requires: # deb: printer-driver-sag-gdi
# Requires: # deb: printer-driver-splix
# Requires: # deb: speech-dispatcher
# Requires: # deb: systemd-coredump
# Requires: # deb: wamerican
# Requires: # deb: wbrazilian
# Requires: # deb: wbritish
# Requires: # deb: wbulgarian
# Requires: # deb: wcatalan
# Requires: # deb: wdanish
# Requires: # deb: wdutch
# Requires: # deb: wfrench
# Requires: # deb: witalian
# Requires: # deb: wngerman
# Requires: # deb: wnorwegian
# Requires: # deb: wogerman
# Requires: # deb: wpolish
# Requires: # deb: wportuguese
# Requires: # deb: wspanish
# Requires: # deb: wswedish
# Requires: # deb: wswiss
# Requires: # deb: wukrainian
# Requires: # deb: xdg-utils

# # deb Recommends from noble branch
# Requires: # deb: wingpanel-indicator-sound # TODO, FIXME - FTBFS

# from elsewhere, to sort out
Requires: accountsservice

%description -n elementary-desktop
This metapackage installs the complete elementary desktop.

It is also used to help ensure proper upgrades, so it is recommended that
it not be removed.

%package -n elementary-artwork
Group: Graphical desktop/Other
BuildArch: noarch
Summary: Artwork of elementary OS
# # deb Depends
# # cat artwork-a* | sort -u
# Requires: # deb: adwaita-icon-theme
Requires: adwaita-icon-theme
# Requires: # deb: elementary-icon-theme
Requires: elementary-icon-theme

# # deb Recommends
# # cat artwork-recommends-a* | sort -u
# Requires: # deb: elementary-wallpapers
Requires: elementary-wallpapers
# Requires: # deb: fonts-elementary-extra # SKIP
# Requires: # deb: fonts-inter # SKIP
# Requires: # deb: io.elementary.sound-theme
Requires: elementary-sound-theme
# Requires: # deb: io.elementary.stylesheet
Requires: elementary-stylesheet

%description -n elementary-artwork
This metapackage installs the acclaimed elementary desktop artwork.

It is also used to help ensure proper upgrades, so it is recommended that
it not be removed.

%package -n pantheon-shell
Group: Graphical desktop/Other
BuildArch: noarch
Summary: Modern and modular DE-independent desktop shell
# # deb Depends
# # cat pantheon-shell-a* | sort -u
# Requires: # deb: gala
Requires: gala
# Requires: # deb: io.elementary.notifications
Requires: /usr/bin/io.elementary.notifications
# Requires: # deb: io.elementary.wingpanel
Requires: /usr/bin/io.elementary.wingpanel
# Requires: # deb: pantheon-xsession-settings
Requires: elementary-session-settings

# # deb Recommends
# # cat pantheon-shell-recommends-a* | sort -u

# # deb Depends from noble git-branch
# Requires: # deb: io.elementary.dock
Requires: /usr/bin/io.elementary.dock
# Requires: # deb: touchegg
Requires: /usr/bin/touchegg

# # deb Recommends from noble git-branch
# Requires: # deb: slingshot-launcher # TODO, FIXME - FTBFS

%description -n pantheon-shell
Pantheon Shell is a modern and modular DE-independent desktop shell
developed by elementary Project.

This metapackage installs all components of the shell.
It is also used to help ensure proper upgrades, so it is recommended that
it not be removed.

%package -n pantheon
Group: Graphical desktop/Other
BuildArch: noarch
Summary: Pantheon Desktop Environment

# # deb Depends
# # cat pantheon-a* | sort -u
#
# # deb Recommends
# # cat pantheon-recommends* | sort -u
# Requires: # deb: appcenter # SKIP, no `vapi(appstream)`
# Requires: # deb: contractor
Requires: /usr/bin/contractor
# Requires: # deb: io.elementary.code
Requires: /usr/bin/io.elementary.code
# Requires: # deb: io.elementary.mail
Requires: /usr/bin/io.elementary.mail
# Requires: # deb: io.elementary.monitor
Requires: /usr/bin/io.elementary.monitor
# Requires: # deb: io.elementary.portals
Requires: elementary-portals
# Requires: # deb: io.elementary.settings-daemon
Requires: /usr/bin/io.elementary.settings-daemon
# Requires: # deb: io.elementary.shortcut-overlay
Requires: /usr/bin/io.elementary.shortcut-overlay
# Requires: # deb: io.elementary.sideload
Requires: /usr/bin/io.elementary.sideload
# Requires: # deb: io.elementary.tasks
Requires: /usr/bin/io.elementary.tasks
# Requires: # deb: io.elementary.terminal
Requires: /usr/bin/io.elementary.terminal
# Requires: # deb: pantheon-files
Requires: pantheon-files
# Requires: # deb: pantheon-photos
Requires: elementary-photos
# Requires: # deb: pantheon-shell
Requires: pantheon-shell

# # deb Recommends from noble git-branch

# Requires: # deb: io.elementary.calculator
Requires: /usr/bin/io.elementary.calculator
# Requires: # deb: io.elementary.camera
Requires: /usr/bin/io.elementary.camera
# Requires: # deb: io.elementary.maps
Requires: /usr/bin/io.elementary.maps
# Requires: # deb: io.elementary.music
Requires: /usr/bin/io.elementary.music
# Requires: # deb: io.elementary.print # SKIP, obsolete
# Requires: # deb: io.elementary.screenshot
Requires: /usr/bin/io.elementary.screenshot
# Requires: # deb: io.elementary.videos
Requires: /usr/bin/io.elementary.videos
# Requires: # deb: maya-calendar
Requires: /usr/bin/io.elementary.calendar
# Requires: # deb: org.gnome.epiphany
Requires: epiphany
# Requires: # deb: org.gnome.evince
Requires: evince

%description -n pantheon
Pantheon is a desktop environment based on GNOME with a strong focus
on user experience. It's developed by elementary project.

This metapackage installs all Pantheon apps that are shipped with the OS
by default.

It is also used to help ensure proper upgrades, so it is recommended that
it not be removed.

%package -n elementary-sdk
Group: Graphical desktop/Other
BuildArch: noarch
Summary: elementary Developer Kit

# # deb Depends
# # cat elementary-sdk-a* | sort -u
# Requires: # deb: build-essential
# Requires: # deb: desktop-file-utils
# Requires: # deb: flatpak-builder
# Requires: # deb: gettext
# Requires: # deb: gobject-introspection
# Requires: # deb: libgala-dev
# Requires: # deb: libgee-0.8-dev
# Requires: # deb: libgirepository1.0-dev
# Requires: # deb: libglib2.0-dev
# Requires: # deb: libgranite-7-dev
# Requires: # deb: libgranite-dev
# Requires: # deb: libgtk-3-dev
# Requires: # deb: libgtk-4-dev
# Requires: # deb: libhandy-1-dev
# Requires: # deb: libswitchboard-3-dev
# Requires: # deb: libwingpanel-9-dev
# Requires: # deb: libxml2-dev
# Requires: # deb: libxml2-utils
# Requires: # deb: meson
# Requires: # deb: valac
# Requires: # deb: valadoc

# # deb Recommends
# # cat elementary-sdk-recommends-a* | sort -u
# Requires: # deb: dconf-editor
# Requires: # deb: devscripts
# Requires: # deb: equivs
# Requires: # deb: gdb
# Requires: # deb: git
# Requires: # deb: granite-7-demo
# Requires: # deb: granite-demo
# Requires: # deb: gtk-3-examples
# Requires: # deb: gtk-4-examples
# Requires: # deb: io.elementary.code
Requires: /usr/bin/io.elementary.code
# Requires: # deb: io.elementary.vala-lint
Requires: /usr/bin/io.elementary.vala-lint
# Requires: # deb: python3-debian

%description -n elementary-sdk
Contains recommended packages for developing applications for
elementary OS.

# #
# # NOTE: no reason to create RPM of this package,
# #       as it is used for distro creation, not for desktop environment
# #
#Package: elementary-live
#Architecture: amd64 arm64 armhf
#Depends: ${misc:Depends}, ${germinate:Depends}
#Recommends: ${germinate:Recommends}
#Description: elementary Live Settings
# Configuration for the elementary OS live session

%prep
%setup

%files
%files -n elementary-desktop
%files -n elementary-artwork
%files -n pantheon-shell
%files -n pantheon
%files -n elementary-sdk

%changelog
* Sat Apr 11 2026 Nikolay Strelkov <snk@altlinux.org> 1.565-alt1
- Initial build for Sisyphus
