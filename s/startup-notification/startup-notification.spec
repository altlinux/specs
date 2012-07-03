%define ver_major 0.12
%def_disable static

Name: startup-notification
Version: %ver_major
Release: alt1

Summary: Startup Notification Library
License: LGPL
Group: System/Libraries
URL: http://www.freedesktop.org/wiki/Software/%name

Source: http://www.freedesktop.org/software/%name/releases/%name-%version.tar.gz

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

# Automatically added by buildreq on Sun Apr 26 2009
BuildRequires: libSM-devel libX11-devel libxcbutil-devel xorg-cf-files

%description
Startup Notification Library

%package -n lib%name
Summary: Startup Notification Library
Group: Development/GNOME and GTK+

%description -n lib%name
This package contains startup-notification shared libraries.

%package -n lib%name-devel
Summary: Header and development libraries for %name
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header and development libraries for %name

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for %name
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the lib%name static libraries.
%endif

%prep
%setup -q

%build
%configure \
	%{subst_enable static}

%make_build

%install
%makeinstall

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS ChangeLog

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Wed May 25 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12

* Mon May 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt4
- update from upstream git

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt3
- rebuild for debuginfo

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt2
- rebuild for set-version

* Sun Apr 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- new version (ALT#19777)
- changes url's
- removed obsolete %%post{,un}_ldconfig

* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 0.9-alt2
- add Packager tag
- buildreq

* Thu May 24 2007 Igor Zubkov <icesik@altlinux.org> 0.9-alt1
- 0.8 -> 0.9

* Thu Feb 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.8-alt2
- updated buildreqs, minor spec cleanup

* Fri Jan 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.8-alt1
- 0.8

* Tue Aug 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt1
- 0.7

* Thu Apr 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6-alt1
- 0.6
- do not build devel-static subpackage by default.

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt2
- do not package .la files.

* Wed Jan 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt1
- 0.5

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt1
- 0.4

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3-alt1
- First build for Sisyphus.
