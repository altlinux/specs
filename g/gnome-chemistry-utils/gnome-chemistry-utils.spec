%define ver_major 0.12
%define _libexecdir %_prefix/libexec
%def_enable mozilla
%def_enable gnumeric
%if_enabled gnumeric
%define gnumeric_api_ver 1.10
%define gnumeric_plugindir %(pkg-config --variable PluginDir libspreadsheet-%gnumeric_api_ver)
%endif

Name: gnome-chemistry-utils
Version: %ver_major.10
Release: alt2

Summary: A set of chemical utilities
Group: Sciences/Chemistry
License: GPLv2+
Url: http://gchemutils.nongnu.org/

Source: http://mirrors.zerg.biz/nongnu/gchemutils/%ver_major/%name-%version.tar.xz
Patch1: %name-0.10.12-alt-mozplugindir.patch

Requires: bodr chemical-mime-data

BuildRequires: gcc-c++ doxygen docbook-dtds
BuildRequires: gnome-doc-utils gnome-common intltool
BuildRequires: libgio-devel libgnomeoffice-devel
%{?_enable_gnumeric:BuildRequires: libspreadsheet-devel}
BuildRequires: libgsf-devel libgtkglext-devel libopenbabel-devel
BuildRequires: bodr chemical-mime-data scrollkeeper
%{?_enable_mozilla:BuildRequires: xulrunner-devel browser-plugins-npapi-devel}

%description
The Gnome chemistry Utils are a collection of libraries and programs for
the GNOME desktop which migh be useful for chemists and science
students.

This package provides.
* A 3D molecular structure viewer (GChem3D).
* A Chemical calculator (GChemCalc).
* A 2D structure editor (GChemPaint).
* A periodic table of the elements application (GChemTable).
* A crystalline structure editor (GCrystal).
* A spectra viewer (GSpectrum).

%package -n mozilla-plugin-%name
Summary: Gnome chemistry Utils browser plugin
Group: Sciences/Chemistry
Requires: %name = %version-%release

%description -n mozilla-plugin-%name
This package contains Gnome chemistry Utils plugin for xullrunner-based
browsers.

%package -n gnumeric-plugin-%name
Summary: Gnome chemistry Utils plugin for Gnumeric
Group: Sciences/Chemistry
Requires: %name = %version-%release

%description -n gnumeric-plugin-%name
This package contains Gnome chemistry Utils plugin for Gnumeric
spreadsheet program.

%prep
%setup -q
%patch1 -b .mozplugindir

[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure --disable-update-databases \
           --disable-schemas-compile \
           --disable-scrollkeeper \
           %{?_disable_mozilla:--disable-mozilla-plugin} \
           %{?_enable_mozilla:--with-mozilla-libdir=%browser_plugins_path}
%make_build

%install
%make DESTDIR=%buildroot install

%define apps gchem3d-%ver_major gchemcalc-%ver_major gchempaint-%ver_major gchemtable-%ver_major gcrystal-%ver_major gspectrum-%ver_major

%find_lang --with-gnome --output=%name.lang gchemutils-%ver_major %apps

%files -f %name.lang
%_bindir/*
%_libdir/gchemutils
%_libdir/goffice/*/plugins/gchemutils
%_libdir/libgccv-%ver_major.so.*
%_libdir/libgcp-%ver_major.so.*
%_libdir/libgcu-%ver_major.so.*
%_datadir/applications/*
%_datadir/gchemutils
%_datadir/icons/hicolor/*/*/*
%_datadir/mime/packages/gchemutils.xml
%_man1dir/*
%_datadir/glib-2.0/schemas/org.gnome.gchemutils.crystal.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.gchemutils.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.gchemutils.paint.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.gchemutils.paint.plugins.arrows.gschema.xml

%doc AUTHORS NEWS README TODO

%exclude %_libdir/*.so
%exclude %_datadir/mimelnk/

%if_enabled mozilla
%files -n mozilla-plugin-%name
%_libexecdir/chem-viewer
%browser_plugins_path/libmozgcu.so
%exclude %browser_plugins_path/libmozgcu.la
%endif

%if_enabled gnumeric
%files -n gnumeric-plugin-%name
%gnumeric_plugindir/gchemutils/
%exclude %gnumeric_plugindir/gchemutils/*.la
%endif

%changelog
* Wed Jun 20 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.10-alt2
- used GSettings instead GConf as in libgnomeoffice-0.8.17-alt2

* Fri Dec 16 2011 Michael Shigorin <mike@altlinux.org> 0.12.10-alt1.1
- NMU: rebuilt against current openbabel

* Mon Nov 28 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.10-alt1
- 0.12.10
- updated buildreqs
- new gnumeric-plugin-%%name subpackage

* Thu Aug 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.8-alt1
- 0.12.8

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sat Mar 20 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.12-alt2
- build mozilla-plugin subpackage

* Mon Mar 15 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.12-alt1
- first build for Sisyphus


