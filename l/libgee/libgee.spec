%def_disable static

Name: libgee
Version: 0.6.4
Release: alt1
Summary: a collection library providing GObject-based interfaces
License: LGPL
Group: System/Libraries
Url: http://live.gnome.org/Libgee
Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name-%version.tar

BuildRequires: glib2-devel vala gobject-introspection-devel

%description
libgee is a collection library providing GObject-based interfaces and classes
for commonly used data structures.

The ArrayList, HashSet, and HashMap classes provide a reasonable sample
implementation of the List, Set, and Map interfaces. ReadOnlyCollection,
ReadOnlyList, ReadOnlySet, and ReadOnlyMap are read-only wrapper classes that
prevent modification of the underlying collection.

libgee is written in Vala and can be used like any GObject-based C library. It's planned to provide bindings for further languages.

%package devel
Group: Development/C
Summary: Development files of %name
Requires: %name = %version-%release

%description devel
libgee is a collection library providing GObject-based interfaces and classes
for commonly used data structures.

This package contains the C headers and libs required for building programs
with %name.

%package gir
Summary: GObject introspection data for the libgee library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the libgee library

%package gir-devel
Summary: GObject introspection devel data for the libgee library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the libgee library

%if_enabled static
%package devel-static
Group: Development/C
Summary: Static library of %name
Requires: %name-devel = %version-%release

%description devel-static
libgee is a collection library providing GObject-based interfaces and classes
for commonly used data structures.

This package contains the static library required for statically linking
applications with %name.

%endif #enabled static

%prep
%setup -q
echo "See changes in the GIT tree" > ChangeLog

%build
mkdir -p m4
%autoreconf
%configure %{subst_enable static}
%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog* MAINTAINERS NEWS README

%files devel
%_includedir/gee-1.0
%_libdir/*.so
%_pkgconfigdir/gee-1.0.pc
%_datadir/vala/vapi/*

%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Jan 30 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Fri Oct 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.2.1-alt1
- 0.6.2.1

* Tue Jun 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt2
- rebuild with rpm-build-vala

* Mon Jan 31 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Oct 18 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0
- add gir subpackages

* Mon May 24 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.5.0_9_g9a3d481-alt1
- minor new version compatible with current vala

* Mon Oct 05 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.5.0-alt1
- new version

* Mon Oct 05 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.4.0-alt1
- new version
- moved *.vapi to devel subpackage

* Mon Jul 20 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.1.6-alt1
- new version

* Sat Feb 21 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.1.5-alt1
- new version

* Sat Oct 04 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.1.4-alt1.20081001
- initial build for ALTLinux
