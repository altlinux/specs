%def_disable snapshot

%define _name appstream-glib
%define ver_major 0.8
%define api_ver 1.0
%define asb_ver 5

%if "%(rpmvercmp '%{get_version librpm-devel}' '4.13')" >= "0"
%def_enable rpm
%endif

%def_enable stemmer
%def_enable installed_tests
%def_enable gtk_doc
%def_enable check

Name: lib%_name
Version: %ver_major.2
Release: alt1

Summary: Library for AppStream metadata
Group: System/Libraries
License: LGPLv2+
Url: http://www.freedesktop.org/wiki/Distributions/AppStream/

%if_disabled snapshot
Source: http://people.freedesktop.org/~hughsient/%_name/releases/%_name-%version.tar.xz
%else
Vcs: https://github.com/hughsie/appstream-glib.git
Source: %_name-%version.tar
%endif

%define glib_ver 2.58
%define curl_ver 7.56
%define json_glib_ver 1.1.2

Obsoletes: appdata-tools < 0.1.9
Provides: appdata-tools = %version-%release
Provides: %_bindir/appstream-util
Provides: %_bindir/appstream-builder

Obsoletes: libappstream-builder < 0.9.15
Conflicts: libappstream-builder < 0.9.15

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson glib2-devel >= %glib_ver
BuildRequires: libarchive-devel libcurl-devel >= %curl_ver
BuildRequires: libgdk-pixbuf-devel libpango-devel pkgconfig(gdk-3.0)
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
Obsoletes: libappstream-builder-devel < 0.9.15
Conflicts: libappstream-builder-devel < 0.9.15

%description devel
GLib headers and libraries for appstream-glib.

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %version-%release
Obsoletes: libappstream-builder-gir < 0.9.15
Conflicts: libappstream-builder-gir < 0.9.15

%description gir
GObject introspection data for the AppStream metadata library.

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release
Obsoletes: libappstream-builder-gir-devel < 0.9.15
Conflicts: libappstream-builder-gir-devel < 0.9.15

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
%meson \
       %{?_enable_rpm:-Drpm=true} \
       %{?_enable_stemmer:-Dstemmer=true} \
       %{?_enable_gtk_doc:-Dgtk-doc=true}
%meson_build

%install
%meson_install
%find_lang %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/appstream-util
%_bindir/appstream-compose
%_bindir/appstream-builder
%_libdir/%name.so.*
%dir %_libdir/asb-plugins-%asb_ver
%_libdir/asb-plugins-%asb_ver/*.so
%_man1dir/appstream-util.1.*
%_man1dir/appstream-compose.1.*
%_man1dir/appstream-builder.1.*
%_datadir/bash-completion/completions/appstream-util
%_datadir/bash-completion/completions/appstream-builder
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

%if_enabled installed_tests
%files tests
%_datadir/installed-tests/%_name/
%endif


%changelog
* Fri Nov 11 2022 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Thu Aug 11 2022 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Tue Jul 19 2022 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- updated to appstream_glib_0_8_0-5-g674490b (ported from libsoup to libcurl)

* Mon Sep 07 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.18-alt1
- 0.7.18

* Wed Mar 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.17-alt1
- 0.7.17

* Tue Oct 01 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.16-alt1
- 0.7.16

* Fri Mar 01 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.15-alt1
- 0.7.15 (libappstream-builder shared library is no longer installed)

* Tue Oct 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.14-alt1
- 0.7.14

* Sat Sep 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.13-alt1
- 0.7.13

* Mon Aug 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.12-alt1
- 0.7.12

* Thu Aug 09 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.11-alt1
- 0.7.11

* Wed Jul 11 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.10-alt1
- 0.7.10

* Tue Jun 05 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.9-alt1
- 0.7.9

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.8-alt1
- 0.7.8

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.7-alt1
- 0.7.7

* Fri Feb 09 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.6-alt1
- 0.7.6

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

