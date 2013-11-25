Name: gala
Version: 0.1
Release: alt1.r363

Summary: Pantheon Window Manager
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/gala

Source0: %name.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Mon Nov 25 2013
# optimized out: at-spi2-atk cmake-modules fontconfig fontconfig-devel glib2-devel gobject-introspection gsettings-desktop-schemas-devel libEGL-devel libX11-devel libXcomposite-devel libXdamage-devel libXext-devel libXfixes-devel libXi-devel libXrandr-devel libat-spi2-core libatk-devel libbamf3-0 libcairo-devel libcairo-gobject libcairo-gobject-devel libcanberra-gtk3 libclutter-devel libclutter-gtk3 libcogl-devel libdbus-glib libevdev-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgee-devel libgio-devel libgnome-desktop3 libgtk+3-devel libgudev-devel libjson-glib libjson-glib-devel libpango-devel libstartup-notification libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-cursor-devel libwayland-egl libwayland-egl-devel libwayland-server libxkbcommon-devel pkg-config vala xorg-fixesproto-devel xorg-inputproto-devel xorg-xproto-devel xz
BuildRequires: cmake gcc-c++ libbamf3-devel libclutter-gtk3-devel libgranite-devel libgranite-vala libmutter-devel libplank-devel libplank-vala

%description
gala is a window & compositing manager based on libmutter. It manages the
various windows a user has open.
It takes care of behaviors such as moving windows around, window switching,
window overview, animating windows, maximization, multiple workspaces,
providing accessibility features like zoom, and more.

%prep
%setup -q -n %name

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%files
%doc HACKING INSTALL
%_bindir/*
%_datadir/applications/gala.desktop
%_datadir/gala/gala.css
%_datadir/gala/texture.png
%_datadir/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml

%changelog
* Mon Nov 25 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.r363
- build for Sisyphus

