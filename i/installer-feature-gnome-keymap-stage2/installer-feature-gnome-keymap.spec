Name: installer-feature-gnome-keymap-stage2
Version: 0.1
Release: alt1

Summary: Simulating the presence of GNOME for alterator-sysconfig
License: GPL-3.0-or-later
Group: System/Configuration/Other

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot/%_datadir/install2/initinstall.d
cat > %buildroot/%_datadir/install2/initinstall.d/95-gnome-keymap.sh << EOF
#!/bin/sh

# Simulating the presence of GNOME for alterator-sysconfig

dconf_config=/etc/dconf/db/local.d/01-gnome-keymap
dconf_gdm_config=/etc/dconf/db/gdm.d/01-gnome-keymap

mkdir -p /etc/dconf/db/local.d
mkdir -p /etc/dconf/db/gdm.d
mkdir -p /usr/share/wayland-sessions
touch /usr/share/wayland-sessions/gnome.desktop
EOF

chmod +x %buildroot/%_datadir/install2/initinstall.d/95-gnome-keymap.sh

%files
%_datadir/install2/initinstall.d/95-gnome-keymap.sh

%changelog
* Fri Jan 02 2026 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build.
