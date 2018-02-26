%define ver_major 3.4

Name: gnome-dictionary
Version: %ver_major.0
Release: alt1

Summary: Gnome client for MIT dictionary server
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://www.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Requires: libgdict = %version-%release

%define glib_ver 2.28.0
%define gtk_ver 3.0.0

BuildPreReq: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: rpm-build-gnome intltool gtk-doc gnome-doc-utils

%description
GNOME Dictionary - look up an online dictionary for definitions and
correct spelling of words.

%package -n libgdict
Summary: GNOME Dictionary Library.
Group: System/Libraries

%description -n libgdict
This package provides a shared GNOME Dictionary Library.

%package -n libgdict-devel
Summary: Development files for GNOME Dictionary Library.
Group: Development/C
Provides: gnome-dictionary-devel = %version-%release
Requires: libgdict = %version-%release

%description -n libgdict-devel
Files necessary to develop applications that use GNOME Dictionary.

%package -n libgdict-devel-doc
Summary: Development documentation for GNOME Dictionary.
Group: Development/C
BuildArch: noarch
Provides: gnome-dictionary-devel-doc = %version-%release
Conflicts: libgdict < %version

%description -n libgdict-devel-doc
Documentation necessary to develop applications that use GNOME
Dictionary Library.


%prep
%setup
[ ! -d m4 ] && mkdir m4

%build
gnome-doc-prepare -f
%autoreconf
%configure \
	--enable-gtk-doc \
	--enable-ipv6

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/gnome-dictionary
%_datadir/gnome-dictionary
%_desktopdir/gnome-dictionary.desktop
%_man1dir/gnome-dictionary.*
%config %_datadir/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%doc NEWS

%files -n libgdict
%_libdir/libgdict-1.0.so.*
%dir %_datadir/gdict-1.0
%_datadir/gdict-1.0/sources

%files -n libgdict-devel
%dir %_includedir/gdict-1.0
%_includedir/gdict-1.0/gdict
%_libdir/libgdict-1.0.so
%_libdir/pkgconfig/gdict-1.0.pc

%files -n libgdict-devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Fri Mar 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2 snapshot


