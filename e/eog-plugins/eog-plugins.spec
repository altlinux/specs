%define _name eog
%define ver_major 3.4
%define api_ver 3.0
%def_enable map
%def_enable postasa

Name: %_name-plugins
Version: %ver_major.1
Release: alt1

Summary: EOG plugins
License: %gpl2plus
Group: Graphics
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Requires: eog >= %ver_major

%define libchamplain_ver 0.12
%define gdata_ver 0.6.0

BuildPreReq: rpm-build-licenses rpm-build-gnome intltool
BuildPreReq: eog-devel >= %ver_major
BuildRequires: libpeas-devel libgnome-desktop3-devel
%{?_enable_map:BuildRequires: libchamplain-gtk3-devel >= %libchamplain_ver}
%{?_enable_postasa:BuildRequires: libgdata-devel >= %gdata_ver}
BuildRequires: libexempi-devel zlib-devel libjpeg-devel liblcms-devel
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
%setup -q

%build
%autoreconf
export ac_cv_path_POSTR=%_bindir/postr
%configure
#    --disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files -f %name.lang
%_libdir/%_name/plugins/*
%_datadir/%_name/plugins/*
%if_enabled postasa
%exclude %_libdir/%_name/plugins/postasa.plugin
%exclude %_libdir/%_name/plugins/libpostasa.so
%endif
%exclude %_libdir/%_name/plugins/libpostr.so
%config %_datadir/glib-2.0/schemas/org.gnome.eog.plugins.exif-display.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.eog.plugins.fullscreenbg.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.eog.plugins.pythonconsole.gschema.xml
%doc AUTHORS NEWS README

%files -n %_name-plugins-postr
%_libdir/%_name/plugins/libpostr.so

%if_enabled postasa
%files -n %_name-plugins-postasa
%_libdir/%_name/plugins/postasa.plugin
%_libdir/%_name/plugins/libpostasa.so
%endif

%exclude %_libdir/%_name/plugins/*.la

%changelog
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

