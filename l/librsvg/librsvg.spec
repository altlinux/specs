%def_disable bootstrap

%define bname librsvg
%define ver_major 2.59
%define namespace Rsvg
%define api_ver 2.0
%define gtk_api_ver 2.0
%define gtk3_api_ver 3.0

%define _libexecdir %_prefix/libexec

%def_disable static
%def_enable docs
%def_enable man
%def_enable pixbuf_loader
%def_enable introspection
%def_enable vala
%def_enable avif
%def_disable installed_tests
%def_disable check

Name: %bname
Version: %ver_major.1
Release: alt1
Epoch: 1

Summary: SVG rendering library
License: LGPL-2.1
Group: System/Libraries
Url: https://wiki.gnome.org/action/show/Projects/LibRsvg

Source: ftp://ftp.gnome.org/pub/gnome/sources/%bname/%ver_major/%bname-%version.tar.xz
# since 2.55 no longer contains vendored Rust dependencies
%{?_disable_bootstrap:Source1: %name-%version-cargo.tar}

%define rust_ver 1.77.2
%define cargo_c_ver 0.9.19
%define glib_ver 2.52.0
%define pango_ver 1.46
%define gtk3_ver 3.10.0
%define libxml2_ver 2.9.0
%define cairo_ver 1.18.0
%define vala_ver 0.18
%define freetype_ver 2.9
%define harfbuzz_ver 2.0.0

BuildRequires: rpm-macros-meson %{?_enable_introspection:rpm-build-gir} %{?_enable_vala:rpm-build-vala}
BuildRequires: meson /proc rust >= %rust_ver rust-cargo rust-cargo-c >= %cargo_c_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libpango-devel >= %pango_ver
BuildRequires: libgtk+3-devel >= %gtk3_ver
BuildRequires: libxml2-devel >= %libxml2_ver
BuildRequires: libcairo-devel >= %cairo_ver
BuildRequires: libfreetype-devel >= %freetype_ver
BuildRequires: libharfbuzz-devel >= %harfbuzz_ver
BuildRequires: libX11-devel libXt-devel zlib-devel
%{?_enable_avif:BuildRequires: pkgconfig(dav1d)}
%{?_enable_docs:BuildRequires: gi-docgen}
%{?_enable_man:BuildRequires: /usr/bin/rst2man}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgdk-pixbuf-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools >= %vala_ver}
%{?_enable_check:BuildRequires: libgtest-devel}

%description
A high performance SVG rendering library associated with the Gnome Project.

%package devel
Summary: Libraries and include files for developing with librsvg
Group: Development/C
Requires: %bname = %EVR

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%package devel-doc
Summary: Development documentation for %bname
Group: Development/Documentation
BuildArch: noarch
Conflicts: %bname < %EVR

%description devel-doc
%bname is a SVG library based on libart.
This package contains development documentation for %bname

%package devel-static
Summary: Static libraries for developing with librsvg
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
This package provides the necessary static libraries files to allow you
to build static software with librsvg.

%package utils
Summary: Utilities to manipulate SVG files
Group: Graphics
Requires: %bname = %EVR

%description utils
This package contains small utilities to manipulate SVG files found in
%bname package.

%package -n libgtk-engine-svg
Summary: A GTK+ engine for graphical themes that use SVG images.
Group: Graphical desktop/GNOME
Requires: %bname = %EVR

%description -n libgtk-engine-svg
This package contains a GTK+2 engine that renders graphical themes with SVG
images in them.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %name library

%package tests
Summary: Tests for %name
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %name.

%prep
%setup -n %bname-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson \
    %{subst_enable_meson_feature introspection introspection} \
    %{subst_enable_meson_feature docs docs} \
    %{subst_enable_meson_feature pixbuf_loader pixbuf-loader} \
    %{subst_enable_meson_feature vala vala} \
    %{subst_enable_meson_feature avif avif} \
    %{subst_enable_meson_bool check tests}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_libdir/*.so.*
%{?_enable_pixbuf_loader:%_libdir/gdk-pixbuf-%gtk_api_ver/*/loaders/*.so}
%_datadir/thumbnailers/librsvg.thumbnailer
%doc AUTHORS NEWS* README*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%bname-%gtk_api_ver.pc
%{?_enable_vala:%_vapidir/%name-%api_ver.vapi
%_vapidir/%name-%api_ver.deps}

%if_enabled docs
%files devel-doc
%_datadir/doc/Rsvg-%api_ver
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%{?_enable_pixbuf_loader:%_libdir/gdk-pixbuf-%gtk_api_ver/*/loaders/*.a}
%endif

%files utils
%_bindir/*
%{?_enable_man:%_man1dir/*}

%if_enabled introspection
%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/RSVG/
%_datadir/installed-tests/RSVG/
%endif

%changelog
* Sat Sep 28 2024 Yuri N. Sedunov <aris@altlinux.org> 1:2.59.1-alt1
- 2.59.1

* Fri Sep 13 2024 Yuri N. Sedunov <aris@altlinux.org> 1:2.59.0-alt1
- 2.59.0

* Sat Apr 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1:2.58.91-alt1
- 2.58.91

* Sat Apr 13 2024 Yuri N. Sedunov <aris@altlinux.org> 1:2.58.90-alt1
- 2.58.90 (ported to Meson build system)

* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1:2.58.0-alt1
- 2.58.0

* Sat Mar 09 2024 Yuri N. Sedunov <aris@altlinux.org> 1:2.57.2-alt1
- 2.57.2

* Sat Dec 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1:2.57.1-alt1
- 2.57.1

* Thu Sep 14 2023 Yuri N. Sedunov <aris@altlinux.org> 1:2.57.0-alt1
- 2.57.0

* Fri Jul 21 2023 Yuri N. Sedunov <aris@altlinux.org> 1:2.56.3-alt1
- 2.56.3

* Sat Jul 01 2023 Yuri N. Sedunov <aris@altlinux.org> 1:2.56.2-alt1
- 2.56.2

* Wed May 31 2023 Yuri N. Sedunov <aris@altlinux.org> 1:2.56.1-alt1
- 2.56.1

* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 1:2.56.0-alt1
- 2.56.0

* Thu Mar 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1:2.55.2-alt1
- 2.55.2

* Tue Sep 06 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.55.1-alt1
- 2.55.1

* Sat Aug 27 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.54.5-alt1
- 2.54.5

* Sat Jun 11 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.54.4-alt1
- 2.54.4

* Sat May 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.54.3-alt1
- 2.54.3

* Fri May 13 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.54.2-alt1
- 2.54.2

* Sat Apr 23 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.54.1-alt1
- 2.54.1

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.54.0-alt1
- 2.54.0

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.52.8-alt1
- 2.52.8

* Sat Mar 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.52.7-alt1
- 2.52.7

* Tue Mar 01 2022 Yuri N. Sedunov <aris@altlinux.org> 1:2.52.6-alt1
- 2.52.6

* Fri Dec 17 2021 Yuri N. Sedunov <aris@altlinux.org> 1:2.52.5-alt1
- 2.52.5

* Sat Nov 13 2021 Yuri N. Sedunov <aris@altlinux.org> 1:2.52.4-alt1
- 2.52.4

* Sat Jun 05 2021 Yuri N. Sedunov <aris@altlinux.org> 1:2.50.7-alt1
- 2.50.7

* Wed May 26 2021 Yuri N. Sedunov <aris@altlinux.org> 1:2.50.6-alt1
- 2.50.6

* Fri Apr 30 2021 Yuri N. Sedunov <aris@altlinux.org> 1:2.50.5-alt1
- 2.50.5

* Tue Apr 13 2021 Yuri N. Sedunov <aris@altlinux.org> 1:2.50.4-alt1
- 2.50.4
- enabled %%check

* Thu Jan 28 2021 Yuri N. Sedunov <aris@altlinux.org> 1:2.50.3-alt1
- 2.50.3

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.50.2-alt1
- 2.50.2

* Fri Oct 02 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.50.1-alt1
- 2.50.1

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.50.0-alt1
- 2.50.0

* Fri Jul 03 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.48.8-alt1
- 2.48.8

* Thu Jun 04 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.48.7-alt1
- 2.48.7

* Tue Jun 02 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.48.6-alt1
- 2.48.6

* Sat May 30 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.48.5-alt1
- 2.48.5

* Thu Apr 23 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.48.4-alt1
- 2.48.4

* Fri Apr 10 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.48.3-alt1
- 2.48.3

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.48.2-alt1
- 2.48.2
- enabled %check

* Sat Mar 28 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.48.1-alt1
- 2.48.1

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1:2.48.0-alt1
- 2.48.0

* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 1:2.46.4-alt1
- 2.46.4

* Wed Oct 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1:2.46.3-alt1
- 2.46.3

* Mon Oct 14 2019 Yuri N. Sedunov <aris@altlinux.org> 1:2.46.2-alt1
- 2.46.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1:2.46.1-alt1
- 2.46.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1:2.46.0-alt1
- 2.46.0

* Tue Sep 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.15-alt1
- 2.44.15

* Tue May 14 2019 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.14-alt1
- 2.44.14

* Sat Feb 16 2019 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.13-alt1
- 2.44.13

* Mon Jan 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.12-alt1
- 2.44.12

* Sun Dec 30 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.11-alt1
- 2.44.11

* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.10-alt1
- 2.44.10

* Mon Nov 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.9-alt1
- 2.44.9

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.8-alt1
- 2.44.8

* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.7-alt1
- 2.44.7

* Thu Sep 27 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.6-alt1
- 2.44.6

* Wed Sep 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.4-alt1
- 2.44.4

* Thu Sep 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.3-alt1
- 2.44.3

* Thu Aug 30 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.44.2-alt1
- 2.44.2

* Thu Aug 23 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.42.7-alt1
- 2.42.7

* Wed Aug 08 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.42.6-alt1
- 2.42.6

* Sat Jun 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.42.5-alt1
- 2.42.5

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.42.4-alt1
- 2.42.4

* Mon Mar 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.42.3-alt1
- 2.42.3

* Fri Feb 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.42.2-alt1
- 2.42.2

* Wed Jan 24 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.42.1-alt1
- 2.42.1

* Wed Jan 10 2018 Yuri N. Sedunov <aris@altlinux.org> 1:2.42.0-alt1
- 2.42.0

* Sat Dec 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1:2.41.2-alt1
- 2.41.2

* Tue Dec 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.20-alt1
- 2.40.20

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.19-alt1
- 2.40.19

* Thu Jul 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.18-alt1
- 2.40.18 (fixed CVE-2017-11464)

* Fri Apr 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.17-alt1
- 2.40.17

* Thu Jun 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.16-alt1
- 2.40.16

* Sat Apr 02 2016 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.15-alt1
- 2.40.15

* Fri Jan 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.13-alt1
- 2.40.13

* Wed Dec 02 2015 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.12-alt1
- 2.40.12

* Sat Oct 10 2015 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.11-alt1
- 2.40.11

* Sat Aug 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.10-alt1
- 2.40.10

* Fri Mar 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.9-alt1
- 2.40.9

* Fri Feb 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.8-alt1
- 2.40.8

* Sat Feb 14 2015 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.7-alt1
- 2.40.7

* Wed Dec 03 2014 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.6-alt1
- 2.40.6

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.5-alt1
- 2.40.5

* Sun Sep 14 2014 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.4-alt1
- 2.40.4

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.3-alt1
- 2.40.3

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.2-alt1
- 2.40.2

* Tue Nov 19 2013 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.1-alt1
- 2.40.1

* Thu Oct 17 2013 Yuri N. Sedunov <aris@altlinux.org> 1:2.40.0-alt1
- 2.40.0

* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1:2.36.4-alt2
- back to 2.36.4

* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 2.39.0-alt1
- 2.39.0

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.36.4-alt1
- 2.36.4

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 2.36.3-alt1
- 2.36.3

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt1
- 2.36.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.2-alt1
- 2.34.2

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.34.1-alt1.1
- Rebuild with Python-2.7

* Wed Sep 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.1-alt1
- 2.34.1

* Sat May 14 2011 Dmitry V. Levin <ldv@altlinux.org> 2.34.0-alt1.qa1
- Rebuilt with libcairo-1.10.2-alt7.

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Wed Mar 09 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- rebuilt for debuginfo

* Sat Nov 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3 

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.26.0-alt2.1
- Rebuilt with python 2.6

* Mon Jul 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- removed gdk-pixbuf-query-loaders call in %post

* Wed Mar 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- removed obsolete %%post{,un}_ldconfig
- drop upstreamed patch
- mozilla plugin disabled (not ready for our new xulrunner)

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version 2.22.3
- build devel-doc as noarch

* Thu Mar 20 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version 2.22.2
- cleanup spec (remove gnome-vfs, gnomeprint)
- plug memory leaks(patch1 from RH)

* Sun Jan 07 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.1-alt2
- from now on, two librsvg packages are built, one with gnome-vfs
  (librsvg-gnome) and the other without it (librsvg).
- use xulrunner instead of seamonkey to build the browser plugin.

* Fri Jan 05 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.1-alt1
- new version (2.16.1)
- fixed packaging for the case when mozilla plugin is not built.
- added a subpackage for the GTK+ engine.

* Sun Sep 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version 2.16.0 (with rpmrb script)

* Wed Aug 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt2
- fixed Provides/Obsoletes pairs.

* Tue Aug 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt1
- new version (2.15.90)
- updated dependencies
- spec cleanup
- removed '2' from package name

* Thu Mar 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version (2.14.2)

* Mon Feb 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version
- spec cleanup, dependencies revised.

* Fri Oct 07 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.5-alt1
- new version

* Fri Sep 23 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.1-alt1
- 2.11.1
- Removed excess buildreqs.

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.5-alt1
- 2.9.5.
- development documentation moved to devel-doc subpackage.

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0
- mozilla-plugin-svg subpackage.

* Wed Mar 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Fri Mar 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Thu Jan 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt3
- do not package .la files.
- do not build devel-static subpackage by default.

* Tue Oct 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- no more gimp plugin.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt2
- rebuild for new gimp2 (1.3.18).

* Tue Jul 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sat Jul 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt3
- disable croco support.

* Thu Jul 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt2
- rebuild with new libgimp.
- css support via libcroco enabled.

* Tue Apr 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue Mar 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.5-alt1
- 2.2.5

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.4-alt1
- 2.2.4

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Sun Feb 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Jan 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Mon Jan 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt2
- rebuild with new gtk-2.1.5.

* Mon Nov 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Nov 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt2
- rebuild with new gtk+2.
- Run gdk-pixbuf-query-loaders in %%post.
- utils subpackage.

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Thu Oct 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Sun Jun 23 2002 Igor Androsov <blake@altlinux.ru> 2.0.0-alt1
- Adopted for AltLinux
- .a moved to %name-devel-static
- Fix *Req*

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu May 02 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Apr 18 2002 Havoc Pennington <hp@redhat.com>
- 1.1.6

* Mon Feb 11 2002 Alex Larsson <alexl@redhat.com> 1.1.3-1
- Update to 1.1.3

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- new CVS snap 1.1.0.91
- remove automake/autoconf calls

* Mon Nov 26 2001 Havoc Pennington <hp@redhat.com>
- convert to librsvg2 RPM

* Tue Oct 23 2001 Havoc Pennington <hp@redhat.com>
- 1.0.2

* Fri Jul 27 2001 Alexander Larsson <alexl@redhat.com>
- Add a patch that moves the includes to librsvg-1/librsvg
- in preparation for a later librsvg 2 library.

* Tue Jul 24 2001 Havoc Pennington <hp@redhat.com>
- build requires gnome-libs-devel, #49509

* Thu Jul 19 2001 Havoc Pennington <hp@redhat.com>
- own /usr/include/librsvg

* Wed Jul 18 2001 Akira TAGOH <tagoh@redhat.com> 1.0.0-4
- fixed the linefeed problem in multibyte environment. (Bug#49310)

* Mon Jul 09 2001 Havoc Pennington <hp@redhat.com>
- put .la file back in package

* Fri Jul  6 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Put changelog at the end
- Move .so files to devel subpackage
- Don't mess with ld.so.conf
- Don't use %%{prefix}, this isn't a relocatable package
- Don't define a bad docdir
- Add BuildRequires
- Use %%{_tmppath}
- Don't define name, version etc. on top of the file (why do so many do that?)
- s/Copyright/License/

* Wed May  9 2001 Jonathan Blandford <jrb@redhat.com>
- Put into Red Hat Build system

* Tue Oct 10 2000 Robin Slomkowski <rslomkow@eazel.com>
- removed obsoletes from sub packages and added mozilla and trilobite
subpackages

* Wed Apr 26 2000 Ramiro Estrugo <ramiro@eazel.com>
- created this thing
