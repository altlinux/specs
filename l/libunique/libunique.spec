%define s_name unique
%def_disable introspection

Name: lib%s_name
Version: 1.1.6
Release: alt7

Summary: is a library for writing single instance application
License: LGPL
Group: System/Libraries
Url: http://live.gnome.org/LibUnique
Packager: Vladimir Lettiev <crux@altlinux.ru>

Source: %name-%version.tar
Patch: libunique-1.1.6-fc-fix-unused-but-set-variable.patch
Patch1: libunique-1.1.6-fc-fix-disable-deprecated.patch

BuildPreReq: rpm-build-gnome gnome-common
BuildRequires: glib2-devel libdbus-devel libdbus-glib-devel libgtk+2-devel gtk-doc
BuildRequires: gobject-introspection-devel >= 0.9.5 libgtk+2-gir-devel
%{?_enable_introspection: BuildRequires: libgtk+2-gir-devel}

%description
Unique is a library for writing single instance application. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.
Unique makes it easy to write this kind of applications, by providing a
base class, taking care of all the IPC machinery needed to send messages
to a running instance, and also handling the startup notification side.
Unique aims to replace the BaconMessageConnection code that has been
copied by many projects and the code using Bonobo and D-Bus.
This package contains the shared library.

%package devel
Summary: is a library for writing single instance application. Development files.
Group: Development/C
PreReq: %name = %version-%release

%description devel
Unique is a library for writing single instance application. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.
Unique makes it easy to write this kind of applications, by providing a
base class, taking care of all the IPC machinery needed to send messages
to a running instance, and also handling the startup notification side.
Unique aims to replace the BaconMessageConnection code that has been
copied by many projects and the code using Bonobo and D-Bus.
This package contain development files.

%package gir
Summary: GObject introspection data for the Unique library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Unique library

%package gir-devel
Summary: GObject introspection devel data for the Unique library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Unique library

%prep
%setup
%patch -p1 -b .unused-but-set-variable
%patch1 -p1 -b .disable-deprecated

%build
%autoreconf
%configure --enable-gtk-doc --disable-static \
	%{?_disable_introspection:--enable-introspection=no}
%make_build

%install
%makeinstall_std

%files
%_libdir/%name-1.0.so.*

%files devel
%_includedir/%s_name-1.0
%_libdir/pkgconfig/%s_name-1.0.pc
%_libdir/%name-1.0.so
%_datadir/gtk-doc/html/%s_name/*
%doc AUTHORS ChangeLog NEWS README

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/Unique-1.0.typelib

%files gir-devel
%_datadir/gir-1.0/Unique-1.0.gir
%endif

%changelog
* Sat Nov 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt7
- fixed build (fc patches)
- disabled useless introspection support

* Wed Mar 09 2011 Vladimir Lettiev <crux@altlinux.ru> 1.1.6-alt6
- updated buildreqs

* Tue Sep 14 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt5
- rebuild against gobject-introspection-0.9.5
- updated buildreqs

* Thu Apr 01 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt4
- rebuild with new rpm-build-gir
- build -gir-devel package as noarch

* Wed Mar 10 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1.6-alt3
- Rebuild (Closes: #23117)

* Fri Feb 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1.6-alt2
- Enable introspection (Closes: #22944)

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1.6-alt1
- New version 1.1.6

* Thu Oct 22 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.2-alt1
- new version

* Sun May 03 2009 Vladimir Lettiev <crux@altlinux.ru> 1.0.8-alt1
- new version

* Mon Sep 22 2008 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt1
- Initial build for Sisyphus

