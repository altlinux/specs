%define _name appstream-glib
%define ver_major 0.7
%define api_ver 1.0
%define asb_ver 5

%if "%(rpmvercmp '%{get_version librpm-devel}' '4.13')" >= "0"
%def_enable rpm
%endif

%def_enable stemmer
%def_enable installed_tests
%def_enable gtk_doc

Name: lib%_name
Version: %ver_major.5
Release: alt1

Summary: Library for AppStream metadata
Group: System/Libraries
License: LGPLv2+
Url: http://www.freedesktop.org/wiki/Distributions/AppStream/

Source: http://people.freedesktop.org/~hughsient/%_name/releases/%_name-%version.tar.xz

%define glib_ver 2.46
%define soup_ver 2.52
%define json_glib_ver 1.1.1

Obsoletes: appdata-tools < 0.1.9
Provides: appdata-tools = %version-%release
Provides: %_bindir/appstream-util

BuildRequires: meson glib2-devel >= %glib_ver libgtk+3-devel
BuildRequires: libarchive-devel libsoup-devel >= %soup_ver libgdk-pixbuf-devel
BuildRequires: libpango-devel libsqlite3-devel
BuildRequires: gobject-introspection-devel libgdk-pixbuf-gir-devel
BuildRequires: gtk-doc docbook-utils docbook-dtds
BuildRequires: libyaml-devel gcab libgcab-devel gperf libuuid-devel
BuildRequires: libjson-glib-devel >= %json_glib_ver
BuildRequires: librpm-devel
%{?_enable_stemmer:BuildRequires: libstemmer-devel}
%description
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata. It also provides a simple DOM implementation that
makes it easy to edit nodes and convert to and from the standardized XML
representation.

%package devel
Summary: GLib Libraries and headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
GLib headers and libraries for appstream-glib.

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the AppStream metadata library.

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the AppStream metadata library.

%package devel-doc
Summary: Development package for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package provides development documentation for the AppStream
metadata library.

%package -n libappstream-builder
Summary: A library and tools to build an AppStream database
Group: System/Libraries
Requires: %name = %version-%release

%description -n libappstream-builder
This library provides GObjects and helper methods to make it easy to
build AppStream database.

%package -n libappstream-builder-devel
Summary: Development files for libappstream-bulder
Group: Development/C
Requires: libappstream-builder = %version-%release
Requires: %name-devel = %version-%release

%description -n libappstream-builder-devel
This package provides development files for libappstream-bulder.

%package -n libappstream-builder-gir
Summary: GObject introspection data for the libappstream-bulder library
Group: System/Libraries
Requires: libappstream-builder = %version-%release
Requires: %name-gir = %version-%release

%description -n libappstream-builder-gir
GObject introspection data for the AppStream builder library.

%package -n libappstream-builder-gir-devel
Summary: GObject introspection devel data for the libappstream-bulder library
Group: Development/Other
BuildArch: noarch
Requires: libappstream-builder-gir = %version-%release
Requires: %name-gir-devel = %version-%release
Requires: libappstream-builder-devel = %version-%release

%description -n libappstream-builder-gir-devel
GObject introspection devel data for the AppStream builder library.

%package tests
Summary: Tests for the %_name package
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %_name library.


%prep
%setup -n %_name-%version

%build
%meson -Denable-gtk-doc=true \
        %{?_enable_rpm:-Denable-rpm=true} \
        %{?_enable_stemmer:-Denable_stemmer=true} \
        %{?_enable_gtk_doc:-Dgtk-doc=true}
%meson_build

%install
%meson_install

%find_lang %_name

%files -f %_name.lang
%_bindir/appstream-util
%_bindir/appstream-compose
%_libdir/%name.so.*
%_man1dir/appstream-util.1.*
%_man1dir/appstream-compose.1.*
%_datadir/bash-completion/completions/appstream-util
%doc README.md AUTHORS NEWS

%files devel
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%_name.pc
%_datadir/aclocal/appstream-xml.m4
%_datadir/aclocal/appdata-xml.m4
%_datadir/gettext/its/appdata.its
%_datadir/gettext/its/appdata.loc

%files gir
%_typelibdir/AppStreamGlib-%api_ver.typelib

%files gir-devel
%_girdir/AppStreamGlib-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/%_name/

%files -n libappstream-builder
%_bindir/appstream-builder
%_libdir/libappstream-builder.so.*
%dir %_libdir/asb-plugins-%asb_ver
%_libdir/asb-plugins-%asb_ver/*.so
%_man1dir/appstream-builder.1.*
%_datadir/bash-completion/completions/appstream-builder


%files -n libappstream-builder-devel
%_libdir/libappstream-builder.so
%_pkgconfigdir/appstream-builder.pc
%_includedir/libappstream-builder/

%files -n libappstream-builder-gir
%_typelibdir/AppStreamBuilder-%api_ver.typelib

%files -n libappstream-builder-gir-devel
%_girdir/AppStreamBuilder-%api_ver.gir

%if_enabled installed_tests
%files tests
%_datadir/installed-tests/%_name/
%endif

#%files -n libappstream-builder-devel-doc
#%_datadir/gtk-doc/html/appstream-builder/

%changelog
* Wed Jan 24 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- 0.7.5

* Sat Nov 11 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4

* Tue Oct 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- 0.7.3

* Tue Aug 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Thu Aug 03 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sun Jun 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.13-alt1
- 0.6.13

* Thu Apr 13 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.12-alt1
- 0.6.12

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.11-alt1
- 0.6.11

* Tue Mar 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.10-alt1
- 0.6.10

* Wed Mar 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.9-alt1
- 0.6.9

* Fri Feb 03 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.8-alt1
- 0.6.8

* Thu Jan 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.7-alt1
- 0.6.7

* Thu Dec 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.6.6-alt1
- 0.6.6

* Fri Dec 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.6.5-alt2
- enabled rpm support

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 0.6.5-alt1
- 0.6.5

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.6.4-alt1
- 0.6.4

* Fri Sep 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- 0.6.3

* Thu Aug 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.18-alt1
- 0.5.18

* Wed Jul 13 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.17-alt1
- 0.5.17

* Thu Jun 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.16-alt1
- 0.5.16

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.15-alt1
- 0.5.15

* Fri Apr 22 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.14-alt1
- 0.5.14

* Fri Apr 01 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.13-alt1
- 0.5.13

* Tue Mar 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.12-alt1
- 0.5.12

* Wed Mar 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.11-alt1
- 0.5.11

* Sun Feb 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.10-alt1
- 0.5.10

* Mon Feb 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.9-alt1
- 0.5.9

* Wed Feb 03 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.8-alt1
- 0.5.8

* Tue Jan 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- 0.5.6

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Thu Nov 19 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Thu Nov 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Tue Oct 27 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Fri Aug 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Jul 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue May 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Tue Mar 31 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Sat Mar 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Tue Jan 20 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Thu Nov 27 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2
- obsoletes/provides appdata-tools

* Fri Sep 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Sun Aug 24 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Mon Jul 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Sun Jun 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Thu Jun 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- first build for Sisyphus

