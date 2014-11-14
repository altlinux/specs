
Name: transmageddon
Version: 1.5
Release: alt1

Summary: Video transcoder
Group: Video
License: LGPLv2+
Url: http://www.linuxrising.org/transmageddon

Source: %name-%version.tar
Source2: gstreamer-common.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

Requires: python3 python3-module-pygobject3
Requires: gst-plugins-base1.0 gst-plugins-good1.0 gst-libav gst-plugins-bad1.0 gst-plugins-ugly1.0
Requires: libgtk+3-gir >= 3.10.0
Requires: typelib(GObject)
Requires: typelib(GLib)
Requires: typelib(Gio)
Requires: typelib(Gtk) = 3.0
Requires: typelib(Gdk) = 3.0
Requires: typelib(GdkX11) = 3.0
Requires: typelib(GdkPixbuf)
Requires: typelib(Gst) = 1.0
Requires: typelib(GstPbutils) = 1.0
Requires: typelib(GstTag) = 1.0
Requires: typelib(GUdev)

BuildRequires: intltool libappstream-glib-devel gobject-introspection-devel
BuildRequires: gstreamer1.0-devel >= 1.2.0
BuildRequires: python3 python3-module-pygobject3

%description
Transmageddon Video Transcoding application.

%prep
%setup
tar -xf %SOURCE2 -C common
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING NEWS
%_bindir/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_datadir/appdata/*.xml
%_desktopdir/*
%_man1dir/%name.*

%changelog
* Fri Nov 14 2014 Alexey Shabalin <shaba@altlinux.ru> 1.5-alt1
- 1.5

* Thu Aug 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.3-alt1
- 1.3
- define strict requires (ALT#30250)

* Fri Jul 04 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2-alt1
- 1.2

* Mon May 19 2014 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- 1.1

* Wed Apr 02 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- Initial build
