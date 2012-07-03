%define _name baobab
%define ver_major 3.4

Name: gnome-disk-usage
Version: %ver_major.1
Release: alt1

Summary: The GNOME disk usage analyser.
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org/projects/Baobab

Source: %gnome_ftp/%name/%ver_major/%_name-%version.tar.xz

Provides: baobab = %version-%release

%define gtk_ver 3.3.7
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildRequires: rpm-build-gnome libgtop-devel intltool yelp-tools itstool xmllint

%description
Baobab is a graphical tool to analyse disk usage in local and remote
filesystems.

%prep
%setup -n %_name-%version

%build
%configure
%make_build

%install
%makeinstall_std

pushd %buildroot%_bindir
ln -s baobab gnome-disk-usage
popd

%find_lang --with-gnome %_name

%files -f %_name.lang
%_bindir/%_name
%_bindir/gnome-disk-usage
%_desktopdir/%_name.desktop
%_datadir/%_name/
%_iconsdir/hicolor/*/apps/%_name.*
%_man1dir/%_name.1.*
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml


%changelog
* Thu Apr 05 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Feb 22 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2

