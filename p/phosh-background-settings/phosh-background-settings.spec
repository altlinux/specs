Name: phosh-background-settings
Version: 0.1
Release: alt1
Summary: Background settings for phosh
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://www.altlinux.org/ALT_Mobile
BuildArch: noarch
Requires: wallpapers-mobile
Requires: dconf

%description
%summary.

%install
mkdir -p %buildroot/%_sysconfdir/dconf/db/local.d
cat>%buildroot/%_sysconfdir/dconf/db/local.d/00_background<<EOF
[org/gnome/desktop/background]
picture-uri='file:///usr/share/wallpapers/mobile/720x1440/basealt-background.png'
EOF

mkdir -p %buildroot/%_sysconfdir/skel/.config/gtk-3.0
cat>%buildroot/%_sysconfdir/skel/.config/gtk-3.0/gtk.css<<EOF
/* TWEAKS-START phosh-applist-background */
phosh-app-grid {
	background-image: url("file:///usr/share/wallpapers/mobile/720x1440/basealt-background.png");
	background-size: cover;
	background-position: center;
}
/* TWEAKS-END phosh-applist-background */
/* TWEAKS-START phosh-lockscreen-background */
phosh-lockscreen, .phosh-lockshield {
	background-image: url("file:///usr/share/wallpapers/mobile/720x1440/basealt-lockscreen.png");
	background-size: cover;
	background-position: center;
}
/* TWEAKS-END phosh-lockscreen-background */
EOF

%files
%_sysconfdir/dconf/db/local.d/00_background
%_sysconfdir/skel/.config/gtk-3.0/gtk.css

%changelog
* Sun Jan 21 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
