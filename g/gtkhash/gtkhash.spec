Name:    gtkhash
Version: 1.5
Release: alt2

Summary: A cross-platform desktop utility for computing message digests or checksums
License: GPL-2.0
Group:   Other
Url:     https://github.com/tristanheaven/gtkhash

Source: %name-%version.tar
Patch0: gtkhash-alt-disable-some-altorithms.patch
Patch1: gtkhash-use-gost-2012.patch

BuildRequires: desktop-file-utils
BuildRequires: gettext-tools
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: libappstream-glib
#BuildRequires: libb2-devel
BuildRequires: libgcrypt-gost-devel
BuildRequires: libgio-devel
#BuildRequires: libmbedtls-devel
#BuildRequires: libmhash-devel
BuildRequires: librsvg-utils
#BuildRequires: libssl-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libcaja-extension)
#BuildRequires: pkgconfig(libnautilus-extension-4)
BuildRequires: pkgconfig(libnemo-extension)
#BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(thunarx-3)
#BuildRequires: pkgconfig(zlib)

%description
GtkHash is a GTK+ utility for computing message digests or checksums.
This package contains the GTK+3 version of the program.

%package nautilus
Group: Graphical desktop/GNOME
Summary: GtkHash extension for nautilus
Requires: libnautilus nautilus
Requires: %{name}3 = %{version}
Requires: GConf libGConf

%description nautilus
GtkHash extension for the nautilus file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%package thunar
Group: Graphical desktop/XFce
Summary: GtkHash extension for Thunar
Requires: libthunar thunar
Requires: %{name} = %{version}

%description thunar
GtkHash extension for the Thunar file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%package nemo
Group: Graphical desktop/Other
Summary: GtkHash extension for Nemo
Requires: nemo
Requires: %{name} = %{version}

%description nemo
GtkHash extension for the Nemo file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%package caja
Group: Graphical desktop/MATE
Summary: GtkHash extension for Caja
Requires: mate-file-manager
Requires: %{name} = %{version}

%description caja
GtkHash extension for the Caja file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure --with-gtk=3.0 \
  --disable-linux-crypto \
  --enable-gcrypt \
  --disable-glib-checksums \
  --disable-mhash \
  --disable-internal-md6 \
  --enable-libcrypto="no" \
  --disable-blake2 \
  --disable-mbedtls \
  --enable-thunar \
  --disable-nautilus \
  --enable-nemo \
  --enable-caja \
  --disable-schemas-compile
%make_build

%install
%makeinstall_std
find %buildroot -name '*.la' -exec rm -f {} ';'
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS
%_bindir/%name
%_datadir/applications/org.%name.%name.desktop
%_datadir/glib-2.0/schemas/org.%name.gschema.xml
%_datadir/glib-2.0/schemas/org.%name.plugin.gschema.xml
%_datadir/icons/hicolor/*/apps/org.%name.%name.png
%_datadir/icons/hicolor/scalable/apps/org.%name.%name.svg
%_datadir/metainfo/org.%name.%name.appdata.xml

#files nautilus
#_libdir/nautilus/extensions-3.0/libgtkhash-properties-nautilus.so
#_datadir/metainfo/org.gtkhash.nautilus.metainfo.xml

%files thunar
%_libdir/thunarx-3/libgtkhash-properties-thunar.so
%_datadir/metainfo/org.gtkhash.thunar.metainfo.xml

%files nemo
%_libdir/nemo/extensions-3.0/libgtkhash-properties-nemo.so
%_datadir/metainfo/org.gtkhash.nemo.metainfo.xml

%files caja
%_libdir/caja/extensions-2.0/libgtkhash-properties-caja.so
%_datadir/caja/extensions/libgtkhash-properties-caja.caja-extension
%_datadir/metainfo/org.gtkhash.caja.metainfo.xml

%changelog
* Tue Oct 08 2024 Andrey Cherepanov <cas@altlinux.org> 1.5-alt2
- Disabled libnettle support.
- Used GOST R 34.11-2012 (Stribog) hash function.

* Tue Apr 16 2024 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- Initial build for Sisyphus
