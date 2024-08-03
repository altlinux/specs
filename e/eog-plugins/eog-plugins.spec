%define _name eog
%define ver_major 44
%define beta %nil
%define api_ver 3.0
%def_enable map
%def_disable postr
%def_enable postasa

Name: %_name-plugins
Version: %ver_major.1
Release: alt1%beta

Summary: EOG plugins
License: %gpl2plus
Group: Graphics
Url: https://wiki.gnome.org/Apps/EyeOfGnome
Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz

Requires: eog >= %ver_major libpeas-python3-loader

%add_python3_path %_libdir/%_name/plugins
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
Requires: libpeas-python3-loader

%define libchamplain_ver 0.12
%define gdata_ver 0.6.0
%define peas_ver 1.14.1

BuildRequires(pre): rpm-macros-meson rpm-build-licenses rpm-build-gnome rpm-build-gir
BuildRequires: meson eog-devel >= %ver_major %_bindir/appstream-util
BuildRequires: libpeas-devel >= %peas_ver libgnome-desktop3-devel
%{?_enable_map:BuildRequires: libchamplain-gtk3-devel >= %libchamplain_ver}
%{?_enable_postasa:BuildRequires: libgdata-devel >= %gdata_ver}
BuildRequires: libexempi-devel zlib-devel libjpeg-devel
BuildRequires: libdbus-glib-devel libxml2-devel librsvg-devel libexif-devel
BuildRequires: gsettings-desktop-schemas-devel gnome-icon-theme

%description
This package provides plugins for the Eye of GNOME, an image viewer program.

%package -n %_name-plugins-postr
Summary: Flickr uploader for EOG
Group: Graphics
Requires: %name = %version-%release
Requires: postr

%description -n %_name-plugins-postr
This package provides Eog plugin for upload pictures to Flickr.

%package -n %_name-plugins-postasa
Summary: Picasa uploader for EOG
Group: Graphics
Requires: %name = %version-%release

%description -n %_name-plugins-postasa
This package provides Eog plugin for upload pictures to Picasa web albums.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_libdir/%_name/plugins/*
%_datadir/%_name/plugins/*
%_datadir/metainfo/%_name-*.appdata.xml
%if_enabled postasa
%exclude %_libdir/%_name/plugins/postasa.plugin
%exclude %_libdir/%_name/plugins/libpostasa.so
%exclude %_datadir/metainfo/%_name-postasa.appdata.xml
%endif
%if_enabled postr
%exclude %_libdir/%_name/plugins/postr.plugin
%exclude %_libdir/%_name/plugins/libpostr.so
%exclude %_datadir/metainfo/%_name-postr.appdata.xml
%endif
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.plugins.exif-display.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.plugins.fullscreenbg.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.plugins.pythonconsole.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.plugins.export-to-folder.gschema.xml
%doc AUTHORS NEWS README

%if_enabled postr
%files -n %_name-plugins-postr
%_libdir/%_name/plugins/postr.plugin
%_libdir/%_name/plugins/libpostr.so
%_datadir/metainfo/%_name-postr.metainfo.xml
%endif

%if_enabled postasa
%files -n %_name-plugins-postasa
%_libdir/%_name/plugins/postasa.plugin
%_libdir/%_name/plugins/libpostasa.so
%_datadir/metainfo/%_name-postasa.appdata.xml
%endif

%changelog
* Sat Aug 03 2024 Yuri N. Sedunov <aris@altlinux.org> 44.1-alt1
- 44.1

* Sun Mar 19 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Sun Jan 08 2023 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Sat Apr 23 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sun Mar 06 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc
- 42.rc (ported to Meson build system)

* Sun Jan 09 2022 Yuri N. Sedunov <aris@altlinux.org> 3.26.8-alt1
- 3.26.8

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 3.26.7-alt1
- 3.26.7

* Sat Nov 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.26.6-alt1
- 3.26.6

* Sun May 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.26.5-alt2
- disabled postr plugin

* Sat Jan 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.26.5-alt1
- 3.26.5

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.26.4-alt1
- 3.26.4

* Mon Jul 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Fri Mar 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.26.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Feb 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Sep 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.92-alt1
- 3.25.92

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.16.6-alt1
- 3.16.6

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.16.5-alt1
- 3.16.5

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt1
- 3.16.4

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Mon Sep 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Aug 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sun Aug 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt2
- rebuilt against libgdata.so.22

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt2
- rebuilt against libgdata.so.19

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Thu Sep 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon May 28 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.0-alt2.1
- Rebuild with Python-2.7

* Mon Oct 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- rebuild against libchamplain-0.12

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Sep 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.2-alt1
- 3.1.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sun Apr 10 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.90-alt1
- 2.91.90

* Mon Feb 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Oct 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt2
- rebuild against libchamplain-0.8

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Mon Feb 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt2
- postr and postasa plugins moved to separate subpackages

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.28.1-alt1.1
- Rebuilt with python 2.6

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Fri Sep 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- first build for Sisyphus

