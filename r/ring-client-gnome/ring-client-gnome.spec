Name: ring-client-gnome
Version: 1.0.0
Release: alt1

Summary: Ring client written in GTK+3

Group: Networking/Instant messaging
License: GPLv3

Url: https://ring.cx
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://gitlab.savoirfairelinux.com/ring/ring-client-gnome
Source: %name-%version.tar

# manually removed: git-core graphviz i586-libxcb mariadb-common python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope  ruby ruby-stdlibs selinux-policy

# Automatically added by buildreq on Fri Feb 17 2017
# optimized out: at-spi2-atk cmake cmake-modules evolution-data-server fontconfig gcc-c++ glib2-devel libEGL-devel libX11-devel libXcomposite-devel libXdamage-devel libXext-devel libXfixes-devel libXi-devel libXrandr-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libclutter-devel libclutter-gtk3 libcogl-devel libdb4-devel libdrm-devel libgbm-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgtk+3-devel libjson-glib libjson-glib-devel libpango-devel libqt5-core libqt5-dbus libsecret-devel libsoup-devel libsqlite3-devel libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-cursor-devel libwayland-egl libwayland-egl-devel libwayland-server libwayland-server-devel libxkbcommon-devel libxml2-devel pkg-config python-base python-modules python3 python3-base xml-utils xorg-xproto-devel
BuildRequires: gcc-c++ ccmake doxygen evolution-data-server-devel libclutter-gtk3-devel libnotify-devel libpcre-devel libpixman-devel qt5-base-devel libexpat-devel gnome-icon-theme-symbolic

# fixme
BuildRequires: libringclient-devel >= 1.0.0

%description
Ring is free software for universal communication which respects freedoms
and privacy of its users.

Ring-client-gnome is a Ring client written in GTK+3. It uses libRingClient to
communicate with the Ring daemon and for all of the underlying models and their
logic. Ideally ring-client-gnome should only contain UI related code and any
wrappers necessary for interacting with libRingClient.

%prep
%setup
%__subst "s|<codecmodel.h>|<audio/codecmodel.h>|g" src/*.cpp

%build
%cmake \
        -DGSETTINGS_LOCALCOMPILE=OFF
%cmake_build
#        -DLibRingClient_PROJECT_DIR=%{_builddir}/ring-project/lrc \

%install
%cmakeinstall_std
rm -f %buildroot%{_bindir}/ring
%find_lang %name

%files -f %name.lang
%{_bindir}/gnome-ring
%{_datadir}/glib-2.0/schemas/cx.ring.RingGnome.gschema.xml
%{_datadir}/applications/gnome-ring.desktop
%{_datadir}/gnome-ring/gnome-ring.desktop
%{_datadir}/icons/hicolor/scalable/apps/ring.svg
%{_datadir}/appdata/gnome-ring.appdata.xml

%changelog
* Fri Feb 17 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
