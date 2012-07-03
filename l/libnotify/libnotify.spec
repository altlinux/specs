%define ver_major 0.7
%def_enable introspection

Name: libnotify
Version: %ver_major.5
Release: alt1
Summary: Desktop notification library
License: LGPLv2.1+
Group: Graphical desktop/GNOME
URL: http://live.gnome.org/libnotify
# git://git.gnome.org/libnotify
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: %{name}4 = %version-%release
Obsoletes: %{name}4

BuildRequires: gtk-doc libgio-devel libgtk+3-devel xmlto
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgdk-pixbuf-gir-devel}


%description
The library that allows applications post notifications on the desktop
in accordance to the proposed Desktop Notification Specification.

%package devel
Summary: Development files for %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Provides: %{name}4-devel = %version-%release
Obsoletes: %{name}4-devel

%description devel
Files needed to develop applications that use libnotify, a desktop
notification library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
BuildArch: noarch
Provides: %{name}4-devel-doc = %version-%release
Obsoletes: %{name}4-devel-doc

%description devel-doc
API documentation for %name in gtk-doc format

%package gir
Summary: GObject introspection data for libnotify
Group: System/Libraries
Requires: %name = %version-%release
Provides: %{name}4-gir = %version-%release
Obsoletes: %{name}4-gir

%description gir
GObject introspection data for the desktop notification library

%package gir-devel
Summary: GObject introspection devel data for libnotify
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Provides: %{name}4-gir-devel = %version-%release
Obsoletes: %{name}4-gir-devel

%description gir-devel
GObject introspection devel data for the desktop notification library

%package -n notify-send
Summary: A program to send desktop notifications
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description -n notify-send
notify-send sends desktop notifications via a notification daemon from
the command line.

%prep
%setup -q
%patch -p1

mkdir -p m4

%build
%autoreconf
%configure \
	--enable-gtk-doc \
	--disable-static \
	%{subst_enable introspection}
%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files -n notify-send
%_bindir/notify-send


%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*

%files gir-devel
%_datadir/gir-1.0/*
%endif

%changelog
* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Thu Oct 13 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Mon May 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.3-alt2
- 0.7.3

* Fri Mar 18 2011 Alexey Tourbin <at@altlinux.ru> 0.6.0-alt3
- libnotify.pc: moved libnotify deps from Requires to Requires.private

* Sun Mar 13 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt2
- rebuild for debuginfo

* Thu Nov 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Nov 09 2010 Victor Forsiuk <force@altlinux.org> 0.4.5-alt2
- Rebuilt for soname set-versions.

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 0.4.5-alt1
- 0.4.5

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 0.4.4-alt1
- 0.4.4

* Tue Jan 09 2007 Victor Forsyuk <force@altlinux.org> 0.4.3-alt1
- 0.4.3

* Tue Sep 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.4.2-alt1
- Rebuilt with GTK+ 0.10 to enable necessary functions
- Added libnotify-devel-doc package
- Buildreq

* Thu Jul 06 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.4.2-alt0.1
- Updated to 0.4.2
- Polished descriptions
- Spec cleanup

* Thu May 04 2006 Vital Khilko <vk@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Thu Feb 02 2006 Vital Khilko <vk@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Sun Sep 17 2005 Vital Khilko <vk@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus

* Sun Sep 17 2005 Vital Khilko <vk@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus
