Name:           snixembed 
Version:        0.3.3
Release:        alt1
Summary:        proxy StatusNotifierItems as XEmbedded systemtray-spec icons
License:        MIT
Group:          Graphical desktop/Other
URL:            https://sr.ht/~steef/snixembed/
Source:         %name-%version.tar.gz

# Automatically added by buildreq on Sat Oct 19 2024
# optimized out: at-spi2-atk bash5 glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libdbusmenu-devel libdbusmenu-gtk3 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgtk+3-devel libharfbuzz-devel libharfbuzz-gobject libpango-devel libwayland-client libwayland-cursor libwayland-egl pkg-config python3 python3-base sh5 vala zlib-devel
BuildRequires: libdbusmenu-gtk3-devel
BuildRequires: vala

%description
While many status bars for simple X window managers do not (yet) support
StatusNotifierItem for displaying system tray icons, some software does
not fall back to the widely supported XEmbed-based tray icon protocol.
snixembed acts as a proxy between the new and old. (It does this by
presenting itself as a StatusNotifierHost on the session bus, and using
GTK+3 to maintain corresponding XEmbed tray icons.)

%prep
%setup
cat > %name-autostart.desktop <<@@@
[Desktop Entry]
Version=1.0
Type=Application
NoDisplay=false
Name=snixembed
GenericName=StatusNotifierItems to X tray
Comment=translate StatusNotifierItems as XEmbedded systemtray-spec icons
Keywords=StatusNotifierItems;tray
TryExec=snixembed
Exec=snixembed
StartupNotify=false
Terminal=false
@@@

%build
%make_build

%install
%makeinstall_std
install -D %name-autostart.desktop %buildroot%_sysconfdir/xdg/autostart/%name.desktop

%files
%_man1dir/*
%_bindir/*
%_sysconfdir/xdg/autostart/%name.desktop

%changelog
* Sat Oct 19 2024 Fr. Br. George <george@altlinux.org> 0.3.3-alt1
- Initial build for ALT
