%define _libexecdir %_prefix/libexec
%define _name spice-gtk
%def_enable introspection
%def_with sasl
%def_enable vala
%def_enable smartcard
%def_enable usbredir
# gstreamer/pulse/no
%define audio pulse
%def_with gtk3

Name: libspice-gtk
Version: 0.12
Release: alt1
Summary: A GTK widget for SPICE clients

Group: System/Libraries
License: LGPLv2+
Url: http://spice-space.org/page/Spice-Gtk

Source: %name-%version.tar
Source2: spice-common.tar
Source3: spice-protocol.tar
# Patch: %name-%version-%release.patch
# Patch2: %name-alt-fix.patch

%define vala_ver 0.14

Requires: libspice-glib = %version-%release

# use pnp.ids from hwdatabase package
Requires: hwdatabase >= 0.3.31-alt1
BuildRequires: hwdatabase >= 0.3.31-alt1

BuildRequires: gcc-c++ gtk-doc intltool
BuildRequires: libjpeg-devel libpixman-devel libssl-devel zlib-devel
BuildRequires: spice-protocol >= 0.10.1
BuildRequires: libgio-devel libcairo-devel
BuildRequires: libcelt051-devel >= 0.5.1.1
%{?_with_sasl:BuildRequires: libsasl2-devel}
%{?_enable_vala:BuildRequires: libvala-devel >= %vala_ver vala >= %vala_ver vala-tools}
%{?_enable_smartcard:BuildRequires: libcacard-devel >= 0.1.2}
%{?_enable_usbredir:BuildRequires: libgudev-devel libusb-devel >= 1.0.9 libusbredir-devel >= 0.4.2}
BuildRequires: libgtk+2-devel
BuildRequires: libpolkit-devel >= 0.96 libacl-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+2-gir-devel}
%if_with gtk3
BuildRequires: libgtk+3-devel
%{?_enable_introspection:BuildRequires: libgtk+3-gir-devel}
%endif
BuildRequires: libXrandr-devel libX11-devel
%if %audio == gstreamer
BuildRequires: gstreamer-devel gst-plugins-devel
%endif
%if %audio == pulse
BuildRequires: libpulseaudio-devel
%endif
BuildRequires: perl-Text-CSV perl-Text-CSV_XS python-module-pygtk-devel python-module-pyparsing

%description
A Gtk client and libraries for SPICE remote desktop servers.

%package devel
Summary: Development files to build GTK2 applications with spice-gtk
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Requires: libspice-glib-devel = %version-%release

%description devel
spice-client-glib is a SPICE client library for GLib.
spice-client-gtk provides a SPICE viewer widget for GTK.

Libraries, includes, etc. to compile with the spice-gtk libraries

%package devel-doc
Summary: Development docs package for spice-gtk libraries
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Development docs package for spice-gtk libraries

%package -n libspice-glib
Summary: A GObject for communicating with Spice servers
Group: System/Libraries

%description -n libspice-glib
spice-client-glib-2.0 is a SPICE client library for GLib2.

%package -n libspice-glib-devel
Summary: Development files to build Glib2 applications with spice-glib-2.0
Group: Development/C
Requires: libspice-glib = %version-%release

%description -n libspice-glib-devel
spice-client-glib-2.0 is a SPICE client library for GLib2.

Libraries, includes, etc. to compile with the spice-glib-2.0 libraries

%package -n libspice-gtk3
Summary: A GTK2 widget for SPICE clients
Group: System/Libraries
Requires: libspice-glib = %version-%release

%description -n libspice-gtk3
spice-client-glib-3.0 is a SPICE client library for Gtk3.

%package -n libspice-gtk3-devel
Summary: Development files to build GTK3 applications with spice-gtk-3.0
Group: Development/GNOME and GTK+
Requires: libspice-gtk3 = %version-%release
Requires: libspice-glib-devel = %version-%release

%description -n libspice-gtk3-devel
spice-client-gtk-3.0 provides a SPICE viewer widget for GTK3.

Libraries, includes, etc. to compile with the spice-gtk3 libraries

%package -n libspice-glib-gir
Summary: GObject introspection data for the spice-glib-2.0 library
Group: System/Libraries
Requires: libspice-glib = %version-%release

%description -n libspice-glib-gir
GObject introspection data for the spice-glib-2.0 library

%package -n libspice-glib-gir-devel
Summary: GObject introspection devel data for the spice-glib-2.0 library
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: libspice-glib-gir = %version-%release
Requires: libspice-glib-devel = %version-%release

%description -n libspice-glib-gir-devel
GObject introspection devel data for the spice-glib-2.0 library

%package gir
Summary: GObject introspection data for the spice-gtk library
Group: System/Libraries
Requires: %name = %version-%release
Requires: libspice-glib-gir = %version-%release

%description gir
GObject introspection data for the spice-gtk library

%package gir-devel
Summary: GObject introspection devel data for the spice-gtk library
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: libspice-glib-gir-devel = %version-%release

%description gir-devel
GObject introspection devel data for the spice-gtk library

%package -n libspice-gtk3-gir
Summary: GObject introspection data for the spice-gtk library
Group: System/Libraries
Requires: libspice-gtk3 = %version-%release
Requires: libspice-glib-gir = %version-%release

%description -n libspice-gtk3-gir
GObject introspection data for the spice-gtk library

%package -n libspice-gtk3-gir-devel
Summary: GObject introspection devel data for the spice-gtk library
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: libspice-gtk3-gir = %version-%release
Requires: libspice-glib-gir-devel = %version-%release

%description -n libspice-gtk3-gir-devel
GObject introspection devel data for the spice-gtk library

%package -n python-module-%_name
Summary: Python bindings for the spice-gtk library
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%_name
SpiceClientGtk module provides a SPICE viewer widget for GTK.

A module allowing use of the spice-gtk widget from python

%package tools
Summary: Spice-gtk tools
Group: Networking/Remote access
Requires: %name = %version-%release

%description tools
Provides useful utilities for interacting with
SPICE servers. Includes snappy, a program for capturing
screen-shots of a SPICE desktop

%prep
%setup -q -c
%__tar -xf %SOURCE2 -C %name-%version/spice-common
%__tar -xf %SOURCE3 -C %name-%version/spice-common/spice-protocol
mv %name-%version %_name-%version
cd %_name-%version
# %patch -p1
# %patch2 -p1
echo "%version" > .tarball-version
cd ..
%if_with gtk3
cp -a %_name-%version spice-gtk3-%version
%endif

%build
cd %_name-%version
%autoreconf
%configure \
	%{subst_enable introspection} \
	%{subst_with sasl} \
	%{subst_enable vala} \
	%{subst_enable smartcard} \
%if_disabled usbredir
	--enable-usbredir=no \
%endif
	--disable-static \
	--disable-rpath \
	--enable-polkit \
	--with-usb-acl-helper-dir=%_libexecdir/spice-gtk/ \
	--enable-gtk-doc \
	--with-pnp-ids-path=%_datadir/misc \
	--with-usb-ids-path=%_datadir/misc \
	--with-gtk=2.0 \
	--with-audio=%audio

%make_build
cd ..

%if_with gtk3
cd spice-gtk3-%version
%autoreconf
%configure \
	%{subst_enable introspection} \
	%{subst_with sasl} \
	%{subst_enable vala} \
	%{subst_enable smartcard} \
%if_disabled usbredir
	--enable-usbredir=no \
%endif
	--disable-static \
	--disable-rpath \
	--enable-polkit \
	--with-usb-acl-helper-dir=%_libexecdir/spice-gtk/ \
	--with-pnp-ids-path=%_datadir/misc \
	--with-usb-ids-path=%_datadir/misc \
	--with-gtk=3.0 \
	--with-audio=%audio

%make_build
cd ..
%endif

%install
%if_with gtk3
cd spice-gtk3-%version
%make DESTDIR=%buildroot install
cd ..
%endif

cd %_name-%version
%make DESTDIR=%buildroot install
cd ..

%find_lang %_name

%files
%_libdir/libspice-client-gtk-2.0.so.*

%files devel
%_libdir/libspice-client-gtk-2.0.so
%_includedir/spice-client-gtk-2.0
%_pkgconfigdir/spice-client-gtk-2.0.pc
%_datadir/vala/vapi/spice-client-gtk-2.0.*

%files -n libspice-gtk3
%_libdir/libspice-client-gtk-3.0.so.*

%files -n libspice-gtk3-devel
%_libdir/libspice-client-gtk-3.0.so
%_includedir/spice-client-gtk-3.0
%_pkgconfigdir/spice-client-gtk-3.0.pc
%_datadir/vala/vapi/spice-client-gtk-3.0.*

%files -n libspice-glib  -f %_name.lang
%_libdir/libspice-client-glib-2.0.so.*
%_libdir/libspice-controller.so.*
%_libexecdir/spice-gtk/spice-client-glib-usb-acl-helper
%_datadir/polkit-1/actions/org.spice-space.lowlevelusbaccess.policy

%files -n libspice-glib-devel
%_libdir/libspice-client-glib-2.0.so
%_libdir/libspice-controller.so
%_includedir/spice-client-glib-2.0
%_includedir/spice-controller/*
%_pkgconfigdir/spice-client-glib-2.0.pc
%_pkgconfigdir/spice-controller.pc
%_datadir/vala/vapi/spice-protocol.vapi
%_datadir/vala/vapi/spice-client-glib-2.0.vapi
%_datadir/vala/vapi/spice-client-glib-2.0.deps

%files devel-doc
%_datadir/gtk-doc/html/*

%files -n python-module-%_name
%python_sitelibdir/*.so
%exclude %python_sitelibdir/*.la

%files tools
%_bindir/*

%if_enabled introspection
%files -n libspice-glib-gir
%_typelibdir/SpiceClientGLib-2.0.typelib

%files -n libspice-glib-gir-devel
%_girdir/SpiceClientGLib-2.0.gir

%files gir
%_typelibdir/SpiceClientGtk-2.0.typelib

%files gir-devel
%_girdir/SpiceClientGtk-2.0.gir

%files -n libspice-gtk3-gir
%_typelibdir/SpiceClientGtk-3.0.typelib

%files -n libspice-gtk3-gir-devel
%_girdir/SpiceClientGtk-3.0.gir

%endif

%changelog
* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12

* Thu Mar 01 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10-alt1
- 0.10

* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9-alt1
- 0.9

* Wed Nov 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt2.git.4f767d4
- git snapshot
- enable usbredir

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.1
- Rebuild with Python-2.7

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- 0.7
- build with gtk+3 and gtk+2
- build with smartcard support
- add build condition for audio (pulse or gstreamer)

* Fri May 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt1
- 0.6
- build with sasl support

* Wed Apr 13 2011 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt2
- update BR:

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt1
- 0.5

* Tue Jan 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt1
- 0.4

* Thu Dec 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt1
- initial build for ALTLinux
