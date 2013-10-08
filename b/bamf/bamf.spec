# TODO: add gtk2 support

Name: bamf
Version: 0.2.126
Release: alt1

Summary: BAMF Application Matching Framework
License: GPLv3/LGPLv3
Group: Graphical desktop/Other
Url: https://launchpad.net/bamf

Source0: %{name}_%{version}.orig.tar.gz

# Ubuntu
Patch0: bamf_0.2.126-0ubuntu1.diff.gz

# ALT
Patch1: bamf-0.2.126-alt-configure.patch

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: libgtk+3-devel libgtk+2-devel gtk-doc gnome-common
BuildRequires: libdbus-glib-devel libwnck3-devel libgtop-devel
BuildRequires: gobject-introspection-devel

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n bamfdaemon
%_libexecdir/bamfdaemon
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

%changelog
* Tue Oct 08 2013 Igor Zubkov <icesik@altlinux.org> 0.2.126-alt1
- build for Sisyphus

