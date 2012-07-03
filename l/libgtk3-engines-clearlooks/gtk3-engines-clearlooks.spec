%define ver_major 2.91
%define _name gtk-theme-engine-clearlooks
%define engine_prefix libgtk3-engine

# Clearlooks animation takes some CPU cycles, so it's done optional.
%def_disable animation

Name: %{engine_prefix}s-clearlooks
Version: %ver_major.5
Release: alt1

Summary: GTK+3 theme engine Clearlooks
License: %lgpl2plus
Group: Graphical desktop/GNOME
Url: http://gtk.themes.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.bz2

%define gtk_ver 3.0.1
%define gtk_binary_ver 3.0.0
%define gtk_api_ver 3.0

BuildPreReq: rpm-build-gnome rpm-build-licenses
BuildPreReq: intltool >= 0.31.0
BuildPreReq: libgtk+3-devel >= %gtk_ver

%description
These are the ClearLooks graphical engine for the various GTK+3 toolkit themes.

%prep
%setup -q -n %_name-%version

%build
%configure \
    %{subst_enable animation}

%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install
%find_lang --output=%_name.lang %_name

%define engines_dir %_libdir/gtk-%gtk_api_ver/%gtk_binary_ver/theming-engines
%define engines_data_dir %_datadir/%_name/%gtk_api_ver

%files
%dir %_datadir/%_name/%gtk_api_ver
%_datadir/gtk-theme-engine-clearlooks/%gtk_api_ver/clearlooks.xml
%engines_dir/libclearlooks.so
%doc AUTHORS README NEWS

%exclude %engines_dir/libclearlooks.la

%changelog
* Sun Feb 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1
- first build for Sisyphus


