%define _name unique
%define ver_major 3.0
%define api_ver 3.0

Name: lib%{_name}3
Version: %ver_major.2
Release: alt1

Summary: A library for writing single instance applications
License: LGPL
Group: System/Libraries
Url: http://live.gnome.org/LibUnique
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/lib%_name/%ver_major/lib%_name-%version.tar.bz2

BuildPreReq: rpm-build-gnome gnome-common gtk-doc
BuildPreReq: glib2-devel >= 2.27.0
BuildPreReq: libgtk+3-devel >= 2.91.6
BuildRequires: libdbus-devel libgio-devel
BuildRequires: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel

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
Summary: A library for writing single instance applications. Development files.
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

%package devel-doc
Summary: Development documentation for %name.
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Unique is a library for writing single instance application. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.
Unique makes it easy to write this kind of applications, by providing a
base class, taking care of all the IPC machinery needed to send messages
to a running instance, and also handling the startup notification side.
Unique aims to replace the BaconMessageConnection code that has been
copied by many projects and the code using Bonobo and D-Bus.
This package contains development documentation.

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
%setup -q -n lib%_name-%version

%build
%configure --enable-gtk-doc \
	--disable-static \
	--enable-introspection
%make_build

%install
%makeinstall_std

%files
%_libdir/lib%_name-%api_ver.so.*

%files devel
%_includedir/%_name-%api_ver
%_libdir/pkgconfig/%_name-%api_ver.pc
%_libdir/lib%_name-%api_ver.so
%doc AUTHORS ChangeLog NEWS README

%files devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver

%files gir
%_libdir/girepository-1.0/Unique-%api_ver.typelib

%files gir-devel
%_datadir/gir-1.0/Unique-%api_ver.gir

%changelog
* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Dec 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.91.4-alt1
- 2.91.4
- updated buildreqs
- new devel-doc subpackage

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

