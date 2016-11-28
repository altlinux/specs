
%define _libexecdir %_prefix/libexec
%define _name spice-gtk
%def_enable introspection
%def_with sasl
%def_enable vala
%def_enable smartcard
%def_enable usbredir
%def_enable webdav
%def_enable lz4
%def_disable gtk_doc
%def_enable pulse
%def_enable gstaudio
%def_enable gstvideo
%def_enable epoxy

Name: libspice-gtk
Version: 0.33
Release: alt1
Summary: A GTK widget for SPICE clients

Group: System/Libraries
License: LGPLv2+
Url: http://spice-space.org/page/Spice-Gtk

Source: %name-%version.tar
Source2: spice-common.tar
# Patch: %name-%version-%release.patch
# Patch2: %name-alt-fix.patch

%define vala_ver 0.14

Requires: libspice-glib = %version-%release

# use pnp.ids from hwdatabase package
Requires: hwdatabase >= 0.3.31-alt1
BuildRequires: hwdatabase >= 0.3.31-alt1

BuildRequires: gcc-c++ gtk-doc intltool
BuildRequires: libjpeg-devel libpixman-devel >= 0.17.7 libssl-devel zlib-devel
BuildRequires: spice-protocol >= 0.12.12
BuildRequires: glib2-devel >= 2.36 libgio-devel >= 2.36 libcairo-devel >= 1.2.0
BuildRequires: libopus-devel >= 0.9.14
%{?_enable_webdav:BuildRequires: libphodav-devel >= 2.0 glib2-devel >= 2.43.90 libsoup-devel >= 2.49.91}
%{?_with_sasl:BuildRequires: libsasl2-devel}
%{?_enable_vala:BuildRequires: libvala-devel >= %vala_ver vala >= %vala_ver vala-tools}
%{?_enable_smartcard:BuildRequires: libcacard-devel >= 0.1.2}
%{?_enable_usbredir:BuildRequires: libgudev-devel libusb-devel >= 1.0.16 libusbredir-devel >= 0.4.2}
%{?_enable_lz4:BuildRequires: liblz4-devel}
BuildRequires: libpolkit-devel >= 0.96 libacl-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel }
BuildRequires: libgtk+3-devel >= 3.12
%{?_enable_introspection:BuildRequires: libgtk+3-gir-devel}
%{?_enable_epoxy:BuildRequires: libepoxy-devel libdrm-devel}
%{?_enable_gstaudio:BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel gstreamer1.0-utils gst-plugins-base1.0 gst-plugins-good1.0}
%{?_enable_gstvideo:BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-bad1.0 gst-libav}
%{?_enable_pulse:BuildRequires: libpulseaudio-devel}
BuildRequires: perl-Text-CSV perl-Text-CSV_XS python-module-pygtk-devel python-module-pyparsing
BuildRequires: /usr/bin/pod2man

%description
A Gtk client and libraries for SPICE remote desktop servers.

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

%package tools
Summary: Spice-gtk tools
Group: Networking/Remote access
Requires: libspice-gtk3 = %version-%release

%description tools
Provides useful utilities for interacting with
SPICE servers. Includes snappy, a program for capturing
screen-shots of a SPICE desktop

%prep
%setup
%__tar -xf %SOURCE2 -C spice-common
# %patch -p1
# %patch2 -p1
echo "%version" > .tarball-version

%build
%autoreconf
%configure \
	%{subst_enable introspection} \
	%{subst_with sasl} \
	%{subst_enable vala} \
	%{subst_enable smartcard} \
	%{subst_enable webdav} \
	%{subst_enable lz4} \
%if_disabled usbredir
	--enable-usbredir=no \
%endif
	--disable-static \
	--disable-rpath \
	--enable-polkit \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--with-usb-acl-helper-dir=%_libexecdir/spice-gtk/ \
	--with-pnp-ids-path=%_datadir/misc \
	--with-usb-ids-path=%_datadir/misc \
	--with-gtk=3.0

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %_name

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

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%files tools
%_bindir/*
%_man1dir/*.1*

%if_enabled introspection
%files -n libspice-glib-gir
%_typelibdir/SpiceClientGLib-2.0.typelib

%files -n libspice-glib-gir-devel
%_girdir/SpiceClientGLib-2.0.gir

%files -n libspice-gtk3-gir
%_typelibdir/SpiceClientGtk-3.0.typelib

%files -n libspice-gtk3-gir-devel
%_girdir/SpiceClientGtk-3.0.gir

%endif

%changelog
* Mon Nov 28 2016 Alexey Shabalin <shaba@altlinux.ru> 0.33-alt1
- 0.33

* Fri Jun 24 2016 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt1
- 0.32
- drop gtk+ 2.0 support
- drop python module

* Thu May 19 2016 Alexey Shabalin <shaba@altlinux.ru> 0.31-alt1
- 0.31

* Mon Oct 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.30-alt1
- 0.30

* Fri Jul 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.29-alt1
- 0.29

* Thu Apr 09 2015 Alexey Shabalin <shaba@altlinux.ru> 0.28-alt1
- 0.28

* Tue Jan 27 2015 Alexey Shabalin <shaba@altlinux.ru> 0.27-alt1
- git snapshot 4c4d7b20822a8ae916df902dd8218cadfe6f0a17
- build with lz4 support

* Mon Nov 10 2014 Alexey Shabalin <shaba@altlinux.ru> 0.26-alt1
- 0.26

* Tue Jun 24 2014 Alexey Shabalin <shaba@altlinux.ru> 0.25-alt2
- rebuild without libcelt051

* Mon Apr 21 2014 Alexey Shabalin <shaba@altlinux.ru> 0.25-alt1
- 0.25
- build with libphodav support

* Thu Mar 06 2014 Alexey Shabalin <shaba@altlinux.ru> 0.23-alt1
- 0.23

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20-alt1.2
- Fixed build

* Tue Sep 17 2013 Sergey Y. Afonin <asy@altlinux.ru> 0.20-alt1.1
- NMU: rebuilt with cyrus-sasl 2.1.26

* Thu Jul 04 2013 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- 0.20

* Thu Apr 11 2013 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1
- 0.19

* Mon Feb 18 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt1
- 0.18

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- 0.14

* Mon Sep 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.13.29-alt1
- 0.13.29
- disable build gtk-doc

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
