# TODO: add gtk2 support

Name: bamf
Version: 0.5.0
Release: alt2

Summary: BAMF Application Matching Framework
License: GPLv3/LGPLv3
Group: Graphical desktop/Other
Url: https://launchpad.net/bamf

Source0: %name-%version.tar.gz

# ALT
Patch0: bamf-0.5.0-alt-configure.patch
Patch1: bamf-0.5.0-alt-disable-werror.patch

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: libgtk+3-devel libgtk+2-devel gtk-doc gnome-common
BuildRequires: libdbus-glib-devel libwnck3-devel libgtop-devel
BuildRequires: gobject-introspection-devel vala-tools
BuildRequires: python-module-libxml2 python-module-libxslt
BuildRequires: xvfb-run dbus-tools-gui

#Build-Depends: debhelper (>= 8.1.2ubuntu2),
#               cdbs (>= 0.4.90ubuntu9),
#               libglib2.0-dev (>= 2.28.0~),
#               libwnck-dev,
#               libwnck-3-dev,
#               libgtop2-dev,
#               libgtk2.0-dev (>= 2.12.0),
#               libgtk-3-dev (>= 3.0.0),
#               libdbus-glib-1-dev,
#               gtk-doc-tools,
#               gobject-introspection (>= 0.6.5-3),
#               libgirepository1.0-dev,
#               gir1.2-atk-1.0,
#               gir1.2-glib-2.0,
#               gir1.2-gtk-2.0 (>= 2.19.5),
#               gir1.2-gtk-3.0 (>= 3.0.0),
#               gir1.2-pango-1.0,
#               gir1.2-wnck-1.0,
#               xvfb,
#               dbus-x11,

%description
BAMF Application Matching Framework.

%package -n bamfdaemon
Summary: Window matching library - daemon
Group: Graphical desktop/Other

%description -n bamfdaemon
bamf matches application windows to desktop files.

This package contains the daemon used by the library and a gio
module that facilitates the matching of applications started
through GDesktopAppInfo

%package -n libbamf0
Summary: Window matching library - shared library
Group: System/Libraries

#Depends: ${shlibs:Depends},
#         ${misc:Depends},
#         bamfdaemon (= ${binary:Version}),

%description -n libbamf0
bamf matches application windows to desktop files.

This package contains shared libraries to be used by applications.

%package -n libbamf3-0
Summary: Window matching library - shared library
Group: System/Libraries

#Depends: ${shlibs:Depends},
#         ${misc:Depends},
#         bamfdaemon (= ${binary:Version}),

%description -n libbamf3-0
bamf matches application windows to desktop files.

This package contains shared libraries to be used by applications.

%package -n libbamf-devel
Summary: Window matching library - development files
Group: Development/C

#Depends: ${shlibs:Depends},
#         ${misc:Depends},
#         libbamf0 (= ${binary:Version}),
#         libwnck-dev,
#         libglib2.0-dev (>= 2.23.0-1ubuntu3~),

%description -n libbamf-devel
bamf matches application windows to desktop files.

This package contains files that are needed to build applications.

%package -n libbamf3-devel
Summary: Window matching library - development files
Group: Development/C

#Depends: ${shlibs:Depends},
#         ${misc:Depends},
#         libbamf3-0 (= ${binary:Version}),
#         libwnck-3-dev,
#         libglib2.0-dev (>= 2.23.0-1ubuntu3~),

%description -n libbamf3-devel
bamf matches application windows to desktop files.

This package contains files that are needed to build applications.

%package -n libbamf-doc
Summary: Window matching library - documentation
Group: Documentation

#Suggests: devhelp

%description -n libbamf-doc
bamf matches application windows to desktop files.

This package contains the daemon used by the library and a gio
module that facilitates the matching of applications started
through GDesktopAppInfo.

This package contains the documentation.

#Package: gir1.2-bamf-0.2
#Section: libs
#Architecture: any
#Depends: ${gir:Depends},
#         ${shlibs:Depends},
#         ${misc:Depends}
#Description: GObject introspection data for the Bamf 0 library
# This package contains introspection data for the Bamf library.
# .
# It can be used by packages using the GIRepository format to generate
# dynamic bindings.


%package -n libbamf3-vala
Summary: Vala language bindings for bamf3 library
Group: Development/Other
BuildArch: noarch
Requires: libbamf3-0 = %version-%release

%description -n libbamf3-vala
This package provides Vala language bindings for bamf3 library.

%package -n libbamf3-gir
Summary: GObject introspection data for bamf3 library
Group: System/Libraries
Requires: libbamf3-0 = %version-%release

%description -n libbamf3-gir
GObject introspection data for bamf3 library.

%package -n libbamf3-gir-devel
Summary: GObject introspection devel data for bamf3 library.
Group: System/Libraries
BuildArch: noarch
Requires: libbamf3-gir = %version-%release

%description -n libbamf3-gir-devel
GObject introspection devel data for bamf3 library.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure \
  --disable-webapps \
  --enable-headless-tests
%make_build V=1

%check
make check || exit 1

%install
%make_install DESTDIR=%buildroot install

%files -n bamfdaemon
%_libexecdir/bamf/bamfdaemon
%_datadir/dbus-1/services/org.ayatana.bamf.service

%files -n libbamf0
# empty for now

%files -n libbamf3-0
%_libdir/libbamf3.so.*

%files -n libbamf-devel
# empty for now

%files -n libbamf3-devel
%_includedir/libbamf3
%_libdir/libbamf3.so
%_pkgconfigdir/libbamf3.pc

%files -n libbamf-doc
%_datadir/gtk-doc/html/libbamf

%files -n libbamf3-vala
%_datadir/vala/vapi/libbamf3.vapi

%files -n libbamf3-gir
%_libdir/girepository-1.0/Bamf-3.typelib

%files -n libbamf3-gir-devel
%_datadir/gir-1.0/Bamf-3.gir

%changelog
* Sun Nov 24 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt2
- Vala stuff

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Oct 08 2013 Igor Zubkov <icesik@altlinux.org> 0.2.126-alt1
- build for Sisyphus

