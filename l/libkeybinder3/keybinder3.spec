%def_disable static
%define sname keybinder-3.0

Name: libkeybinder3
Version: 0.3.2
Release: alt1

Summary: keybinder is a library for registering global keyboard shortcuts
License: GPLv2
Group: System/Libraries
Url: https://github.com/engla/keybinder/tree/keybinder-3.0

BuildRequires: libgtk+3-devel xorg-server-common
BuildRequires: libXext-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: gnome-common gtk-doc gtk-doc-mkpdf
# https://github.com/engla/keybinder.git
Source: keybinder-%version.tar

%description
keybinder is a library for registering global keyboard shortcuts.
Keybinder works with GTK-based applications using the X Window System.
The library contains:
 - A C library, libkeybinder
 - Gobject introspection library


%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%package -n python-module-keybinder3
Summary: Python binding to %name
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-keybinder3
Python binding to %name

%prep
%setup -n keybinder-%version

%build
./autogen.sh
%configure %{subst_enable static}
%make_build V=1

%install
%makeinstall_std

%files
%doc AUTHORS README NEWS
%_libdir/*.so.*

%files devel
%dir %_includedir/%sname/
%_includedir/%sname/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/lib%sname.a
%endif

%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*

%changelog
* Mon Mar 13 2017 Vladimir Didenko <cow at altlinux.org> 0.3.2-alt1
- new version

* Thu Jun 4 2015 Vladimir Didenko <cow at altlinux.org> 0.3.0-alt1.git20120617
- initial build for Sisyphus
