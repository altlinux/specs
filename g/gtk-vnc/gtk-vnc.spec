%def_disable static
%def_with python
%def_with gtk
%def_with gtk3
%def_enable introspection
%def_enable vala
%def_disable vapi

Name: gtk-vnc
Version: 0.5.0
Release: alt3

Summary: VNC viewer widget
Group: System/Libraries
License: LGPL
Url: http://gtk-vnc.sourceforge.net/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
Source: http://download.sourceforge.net/%name/%name-%version.tar.xz

Requires: libgtkvnc = %version-%release

%{?_with_gtk:BuildRequires: libgtk+2-devel}
%{?_with_gtk3:BuildRequires: libgtk+3-devel}
# pod2man
BuildRequires: perl-podlators
BuildRequires: libgnutls-devel libgcrypt-devel libcairo-gobject-devel libsasl2-devel zlib-devel perl-Text-CSV intltool
BuildRequires: libpulseaudio-devel
%{?_enable_vala:BuildRequires: vala-tools}
%{?_with_python:BuildRequires: python-module-pygobject-devel}
%{?_with_gtk:%{?_with_python:BuildRequires: python-module-pygtk-devel}}
%{?_enable_introspection:BuildRequires: %{?_with_gtk:libgtk+2-gir-devel} %{?_with_gtk3:libgtk+3-gir-devel}}

%description
gtk-vnc is a project providing client side APIs for the RFB protocol/VNC
remote desktop technology.It provides two core C libraries, libgvnc for
interacting with the core RFB protocol and libgtk-vnc for a GTK display
widget.

This package provides gvnccapture and gvncviewer - utilities that use
gtk-vnc libraries.

%package -n libgvnc
Summary: GVnc library
Group: System/Libraries

%description -n libgvnc
gtk-vnc is a project providing client side APIs for the RFB protocol/VNC
remote desktop technology.

This package contains the GObject-based library to interact with the RFB
protocol.

%package -n libgvnc-devel
Summary: GVnc library
Group: Development/C
Requires: libgvnc = %version-%release
%{?_disable_vapi:Obsoletes: libgvnc-vala}
%{?_disable_vapi:Provides: libgvnc-vala = %version-%release}

%description -n libgvnc-devel
gtk-vnc is a project providing client side APIs for the RFB protocol/VNC
remote desktop technology.

This package provides development files for the GVnc library.

%package -n libgtkvnc
Summary: VNC viewer widget library
Group: System/Libraries
Requires: libgvnc = %version-%release

%description -n libgtkvnc
gtk-vnc is a project providing client side APIs for the RFB protocol/VNC
remote desktop technology.

This package provides GtkVnc widget library.

%package -n libgtkvnc-devel
Summary: Development package for VNC viewer widget library
Group: Development/C
Requires: libgtkvnc = %version-%release
Requires: libgvnc-devel = %version-%release

%description -n libgtkvnc-devel
gtk-vnc is a VNC viewer widget for GTK. It is built using
coroutines allowing it to be completely asynchronous while
remaining single threaded.

This package provides development files for the GtkVnc widget library.

%package -n libgtk3vnc
Summary: VNC viewer widget library
Group: System/Libraries
Requires: libgvnc = %version-%release

%description -n libgtk3vnc
gtk-vnc is a VNC viewer widget for GTK. It is built using
coroutines allowing it to be completely asynchronous while
remaining single threaded.

%package -n libgtk3vnc-devel
Summary: Development package for VNC viewer widget library
Group: Development/C
Requires: libgtk3vnc = %version-%release
Requires: libgvnc-devel = %version-%release
%{?_disable_vapi:Obsoletes: libgtk3vnc-vala}
%{?_disable_vapi:Provides: libgtk3vnc-vala = %version-%release}

%description -n libgtk3vnc-devel
gtk-vnc is a VNC viewer widget for GTK. It is built using
coroutines allowing it to be completely asynchronous while
remaining single threaded.

This package provides development files for the GtkVnc widget library.

%package -n python-module-gtkvnc
Summary: Python module for %name
Group: Development/Python
Requires: libgtkvnc = %version-%release

%description -n python-module-gtkvnc
gtk-vnc is a VNC viewer widget for GTK. It is built using
coroutines allowing it to be completely asynchronous while
remaining single threaded.

This package provides Python language bindings for for the GtkVnc
library.

%package -n libgvnc-gir
Summary: GObject introspection data for the CVnc library
Group: System/Libraries
Requires: libgvnc = %version-%release

%description -n libgvnc-gir
GObject introspection data for the GVnc library

%package -n libgvnc-gir-devel
Summary: GObject introspection devel data for the GVnc library
Group: System/Libraries
BuildArch: noarch
Requires: libgvnc-gir = %version-%release

%description -n libgvnc-gir-devel
GObject introspection devel data for the GVnc library

%package -n libgvnc-vala
Summary: Vala bindings for GVnc library
Group: Development/C
BuildArch: noarch
Requires: libgvnc = %version-%release

%description -n libgvnc-vala
This package provides Vala language bindings for for the GVnc library.

%package -n libgtkvnc-gir
Summary: GObject introspection data for the GtkVnc library
Group: System/Libraries
Requires: libgtkvnc = %version-%release
Requires: libgvnc-gir = %version-%release

%description -n libgtkvnc-gir
GObject introspection data for the GtkVnc widget library

%package -n libgtkvnc-gir-devel
Summary: GObject introspection devel data for the GtkVnc library
Group: System/Libraries
BuildArch: noarch
Requires: libgtkvnc-gir = %version-%release
Requires: libgvnc-gir-devel = %version-%release

%description -n libgtkvnc-gir-devel
GObject introspection devel data for the GtkVnc widget library

%package -n libgtk3vnc-gir
Summary: GObject introspection data for the GtkVnc library
Group: System/Libraries
Requires: libgtk3vnc = %version-%release
Requires: libgvnc-gir = %version-%release

%description -n libgtk3vnc-gir
GObject introspection data for the GtkVnc widget library

%package -n libgtk3vnc-gir-devel
Summary: GObject introspection devel data for the GtkVnc library
Group: System/Libraries
BuildArch: noarch
Requires: libgtk3vnc-gir = %version-%release
Requires: libgvnc-gir-devel = %version-%release

%description -n libgtk3vnc-gir-devel
GObject introspection devel data for the GtkVnc widget library

%package -n libgtk3vnc-vala
Summary: Vala bindings for GtkVnc library
Group: Development/C
Requires: libgtk3vnc = %version-%release

%description -n libgtk3vnc-vala
This package provides Vala language bindings for for the GtkVnc widget
library.

%prep
%setup -q -c %name
mkdir gtk3-build
cp -R %name-%version/* gtk3-build/

%build
pushd %name-%version
%autoreconf
%configure \
	%{subst_enable static} \
	--with-examples \
	%{subst_with python} \
	--with-libview \
	%{subst_enable introspection} \
	--disable-vala

%make_build
popd

pushd gtk3-build
%autoreconf
%configure \
	%{subst_enable static} \
	--with-examples \
	%{subst_with python} \
	--with-libview \
	%{subst_enable introspection} \
	%{subst_enable vala} \
	--with-gtk=3.0 \
	--program-suffix=-3

%make_build
popd

%install
pushd %name-%version
%make DESTDIR=%buildroot install
%find_lang %name --output %_builddir/%name.lang
popd

pushd gtk3-build
%make DESTDIR=%buildroot install
popd

%files -f %_builddir/%name.lang
%_bindir/*
%exclude  %_bindir/*-3
#%_man1dir/*
#%exclude %_man1dir/*-3.*

%files -n libgvnc
%_libdir/libgvnc-1.0.so.*
%_libdir/libgvncpulse-1.0.so.*

%files -n libgvnc-devel
%_libdir/libgvnc-1.0.so
%_libdir/libgvncpulse-1.0.so
%_includedir/gvnc-1.0/
%_includedir/gvncpulse-1.0/
%_pkgconfigdir/gvnc-1.0.pc
%_pkgconfigdir/gvncpulse-1.0.pc

%if_enabled vala
%{?_enable_vapi:%files -n libgvnc-vala}
%_vapidir/gvnc-1.0.vapi
%_vapidir/gvncpulse-1.0.vapi
%endif

%files -n libgtkvnc
%_libdir/libgtk-vnc-1.0.so.*

%files -n libgtkvnc-devel
%_libdir/libgtk-vnc-1.0.so
%_includedir/gtk-vnc-1.0
%_pkgconfigdir/gtk-vnc-1.0.pc

%if_with gtk3
%files -n libgtk3vnc
%_libdir/libgtk-vnc-2.0.so.*

%files -n libgtk3vnc-devel
%_libdir/libgtk-vnc-2.0.so
%_includedir/gtk-vnc-2.0
%_pkgconfigdir/gtk-vnc-2.0.pc

%if_enabled vala
%{?_enable_vapi:%files -n libgtk3vnc-vala}
%_vapidir/gtk-vnc-2.0.deps
%_vapidir/gtk-vnc-2.0.vapi
%endif
%endif

%if_with python
%files -n python-module-gtkvnc
%python_sitelibdir/*
%endif

%if_enabled introspection
%files -n libgvnc-gir
%_libdir/girepository-1.0/GVnc-1.0.typelib
%_libdir/girepository-1.0/GVncPulse-1.0.typelib

%files -n libgvnc-gir-devel
%_datadir/gir-1.0/GVnc-1.0.gir
%_datadir/gir-1.0/GVncPulse-1.0.gir

%files -n libgtkvnc-gir
%_libdir/girepository-1.0/GtkVnc-1.0.typelib

%files -n libgtkvnc-gir-devel
%_datadir/gir-1.0/GtkVnc-1.0.gir

%if_with gtk3
%files -n libgtk3vnc-gir
%_libdir/girepository-1.0/GtkVnc-2.0.typelib

%files -n libgtk3vnc-gir-devel
%_datadir/gir-1.0/GtkVnc-2.0.gir
%endif
%endif

%changelog
* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt3
- updated buildreqs

* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt2
- move .vapi-files to *-devel subpackages

* Sun Jan 08 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Nov 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4
- new *-vala subpackages

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.3-alt3.1
- Rebuild with Python-2.7

* Tue Mar 08 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt3
- updated buildreqs

* Sat Feb 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt2
- build against GTK+3 too

* Fri Feb 18 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Tue Feb 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt2
- updated buildreqs

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.10-alt1.1
- Rebuilt with python 2.6

* Wed Oct 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.10-alt1
- 0.3.10

* Thu Aug 13 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9
- updated buildreqs

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8
- updated buildreqs

* Thu Apr 24 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.5-alt2
- fix #15449

* Sun Apr 13 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.5-alt1
- First build for ALTLinux


