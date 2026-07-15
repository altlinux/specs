%define apiver 0.10
%define sover 0

Name:    aravis
Version: 0.9.2
Release: alt1

Summary: A vision library for genicam based cameras
License: LGPL-2.1-only
Group:   Video
URL:     http://www.genicam.org
VCS:     https://github.com/AravisProject/aravis

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ meson
BuildRequires: glib2-devel libgio-devel libxml2-devel zlib-devel libusb-devel
BuildRequires: libgudev-devel gobject-introspection-devel libgtk+3-devel
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel

ExclusiveArch: x86_64 aarch64

%description
Aravis is a glib/gobject based library for video acquisition using Genicam
cameras. It currently implements the gigabit ethernet and USB3 protocols
used by industrial cameras. It also provides a basic ethernet camera
simulator and a simple video viewer.

%package -n libaravis-%apiver
Summary: Aravis shared library
Group: System/Libraries

%description -n libaravis-%apiver
This package contains the Aravis shared library.

%package -n libaravis-%apiver-devel
Summary: Development files for Aravis
Group: Development/C
Requires: libaravis-%apiver = %EVR
Requires: glib2-devel
Requires: libgio-devel
Requires: libxml2-devel
Requires: zlib-devel
Requires: libusb-devel
Requires: libgudev-devel

%description -n libaravis-%apiver-devel
This package contains the files needed to develop applications that use
Aravis.

%package -n libaravis-%apiver-gir
Summary: GObject introspection data for Aravis
Group: System/Libraries
Requires: libaravis-%apiver = %EVR
Requires: gobject-introspection

%description -n libaravis-%apiver-gir
This package contains GObject introspection data for Aravis.

%package tools
Summary: Command line tools for Aravis cameras
Group: Video
Requires: libaravis-%apiver = %EVR

%description tools
This package contains command line tools for Aravis cameras:
arv-tool, arv-test, arv-camera-test and arv-fake-gv-camera.

%package viewer
Summary: Simple video viewer for Aravis cameras
Group: Video
Requires: libaravis-%apiver = %EVR
Requires: libgtk+3
Requires: gstreamer1.0
Requires: libgst-plugins1.0

%description viewer
This package contains a simple video viewer for Aravis cameras.

%package -n gstreamer1.0-aravis
Summary: GStreamer plugin for Aravis cameras
Group: Video
Requires: libaravis-%apiver = %EVR
Requires: gstreamer1.0
Requires: libgst-plugins1.0

%description -n gstreamer1.0-aravis
This package contains the GStreamer plugin for Aravis cameras.

%prep
%setup

%build
%meson \
    -Dv4l2=enabled

%meson_build

%install
%meson_install

# Fix icon name mismatch: upstream ships PNG icons as aravis-0.8, but desktop
# references aravis-0.10. Rename icons to match and add scalable SVG source.
for size in 22x22 32x32 48x48 128x128 256x256; do
    mv %buildroot%_datadir/icons/hicolor/$size/apps/aravis-0.8.png \
       %buildroot%_datadir/icons/hicolor/$size/apps/aravis-%apiver.png
done
install -Dm644 viewer/icons/src/aravis.svg \
    %buildroot%_datadir/icons/hicolor/scalable/apps/aravis-%apiver.svg

%find_lang aravis-%apiver

%files
%doc COPYING README.md

%files -n libaravis-%apiver
%_libdir/libaravis-%apiver.so.%sover
%_libdir/libaravis-%apiver.so.%version

%files -n libaravis-%apiver-devel
%_includedir/aravis-%apiver/
%_libdir/libaravis-%apiver.so
%_libdir/pkgconfig/aravis-%apiver.pc
%_datadir/gir-1.0/Aravis-%apiver.gir

%files -n libaravis-%apiver-gir
%_libdir/girepository-1.0/Aravis-%apiver.typelib

%files tools
%_bindir/arv-tool-%apiver
%_bindir/arv-test-%apiver
%_bindir/arv-camera-test-%apiver
%_bindir/arv-fake-gv-camera-%apiver

%files viewer -f aravis-%apiver.lang
%_bindir/arv-viewer-%apiver
%_datadir/applications/org.aravis.viewer-%apiver.desktop
%_datadir/metainfo/org.aravis.viewer-%apiver.metainfo.xml
%_datadir/icons/hicolor/*/apps/aravis-%apiver.png
%_datadir/icons/hicolor/scalable/apps/aravis-%apiver.svg

%files -n gstreamer1.0-aravis
%_libdir/gstreamer-1.0/libgstaravis.%apiver.so

%changelog
* Wed Jul 15 2026 Sergey Palcheh <minergenon@altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus
