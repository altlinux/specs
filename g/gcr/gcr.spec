%define _libexecdir %_prefix/libexec
%define ver_major 3.4
%def_enable introspection

Name: gcr
Version: %ver_major.1
Release: alt1

Summary: A GNOME crypto viewer and prompter
Group: Graphical desktop/GNOME
License: LGPLv2+
Url: http://live.gnome.org/CryptoGlue/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: %name-libs = %version-%release
Conflicts: gnome-keyring < 3.3.0

BuildRequires: intltool glib2-devel libgtk+3-devel libp11-kit-devel
BuildRequires: libgcrypt-devel libtasn1-devel libtasn1-utils gnupg2-gpg
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
BuildRequires: chrpath

%description
GCR is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides the viewer for crypto files on the GNOME
desktop.

GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package libs
Summary: Development files for GCR
Group: System/Libraries
Obsoletes: gnome-keyring-libs < 3.3.0
Provides: gnome-keyring-libs = %version-%release

%description libs
GCR is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides the viewer for crypto files on the GNOME
desktop.

GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package libs-devel
Summary: Development files for GCR
Group: Development/C
Obsoletes: gnome-keyring-libs-devel < 3.3.0
Provides: gnome-keyring-libs-devel = %version-%release
Requires: %name-libs = %version-%release

%description libs-devel
The gcr-devel package includes the header files for the GCR libraries.

%package libs-gir
Summary: GObject introspection data for GCR libraries
Group: System/Libraries
Requires: %name-libs = %version-%release

%description libs-gir
GObject introspection data for GCR libraries.

%package libs-gir-devel
Summary: GObject introspection devel data for the GCR libraries
Group: System/Libraries
BuildArch: noarch
Requires: %name-libs-gir = %version-%release
Requires: %name-libs-devel = %version-%release

%description libs-gir-devel
GObject introspection devel data for the GCR libraries.

%package libs-devel-doc
Summary: Development documentation for GCR libraries
Group: Development/C
Conflicts: %name-libs < %version-%release
BuildArch: noarch

%description libs-devel-doc
This package contains development documentation for GCR libraries.


%prep
%setup

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

chrpath --delete %buildroot%_libdir/*.so.*
chrpath --delete %buildroot%_bindir/gcr-viewer
chrpath --delete %buildroot%_libexecdir/gcr-prompter

%find_lang %name

%files -f %name.lang
%_bindir/gcr-viewer
%_libexecdir/gcr-prompter
%_datadir/applications/gcr-viewer.desktop
%_datadir/applications/gcr-prompter.desktop
%dir %_datadir/GConf
%dir %_datadir/GConf/gsettings
%_datadir/GConf/gsettings/org.gnome.crypto.pgp.convert
%_datadir/GConf/gsettings/org.gnome.crypto.pgp_keyservers.convert
%_datadir/glib-2.0/schemas/org.gnome.crypto.pgp.gschema.xml
%_datadir/gcr-3
%_datadir/icons/hicolor/*/apps/*
%_datadir/mime/packages/gcr-crypto-types.xml
%_datadir/dbus-1/services/org.gnome.keyring.PrivatePrompter.service
%_datadir/dbus-1/services/org.gnome.keyring.SystemPrompter.service

%files libs
%_libdir/libgck-1.so.*
%_libdir/libgcr-3.so.*
%_libdir/libgcr-base-3.so.*

%exclude %_libdir/libmock-test-module.so

%files libs-devel
%_includedir/gck-1
%_includedir/gcr-3
%_libdir/libgck-1.so
%_libdir/libgcr-3.so
%_libdir/libgcr-base-3.so
%_libdir/pkgconfig/gck-1.pc
%_libdir/pkgconfig/gcr-3.pc
%_libdir/pkgconfig/gcr-base-3.pc

%files libs-devel-doc
%_datadir/gtk-doc/html/gck
%_datadir/gtk-doc/html/gcr-3

%if_enabled introspection
%files libs-gir
%_typelibdir/Gck-1.typelib
%_typelibdir/Gcr-3.typelib

%files libs-gir-devel
%_girdir/Gck-1.gir
%_girdir/Gcr-3.gir
%endif

%changelog
* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Thu Mar 01 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.90-alt1
- 3.3.90

* Fri Jan 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.3.1-alt1
- first build for Sisyphus.

