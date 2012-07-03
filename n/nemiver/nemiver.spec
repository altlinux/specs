%define ver_major 0.9

Name: nemiver
Version: %ver_major.2
Release: alt2

Summary: A GNOME C/C++ Debugger
Group: Development/Debuggers
License: GPLv2+
Url: http://projects.gnome.org/nemiver/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: gdb

BuildRequires: gcc-c++ boost-devel libgtkmm3-devel
BuildRequires: libgtksourceviewmm3-devel libgtop-devel libsqlite3-devel libvte3-devel
BuildRequires: libgdlmm3-devel gsettings-desktop-schemas-devel ghex-devel dconf
BuildRequires: intltool gnome-doc-utils doxygen

%description
Nemiver is an ongoing effort to write a standalone graphical debugger that
integrates well in the GNOME desktop environment. It currently features a
backend which uses the well known GNU Debugger (gdb) to debug C/C++ programs.

The yelp package must be installed to make use of Nemiver's documentation.

%package devel
Summary: Header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains header files for developing new debugging
backends for Nemiver.

%prep
%setup -q

%build
export ac_cv_path_GDB_PROG=%_bindir/gdb
%configure --disable-static \
	--disable-schemas-compile \
	--disable-scrollkeeper

%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_datadir/glib-2.0/schemas/org.nemiver.gschema.xml
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.*
%_datadir/%name/
%_man1dir/*
%doc AUTHORS NEWS README TODO

%files devel
%_includedir/%name/

%changelog
* Thu May 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt2
- rebuilt against newest gdlmm

* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- 0.9.2

* Mon Nov 21 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Fri Jun 18 2010 Fr. Br. George <george@altlinux.ru> 0.7.3-alt4
- Rebuild with new libgtksourceviewmm

* Tue May 11 2010 Fr. Br. George <george@altlinux.ru> 0.7.3-alt3
- Fix repocop warnings

* Wed Apr 28 2010 Fr. Br. George <george@altlinux.ru> 0.7.3-alt2
- Desktop file fix

* Thu Apr 08 2010 Fr. Br. George <george@altlinux.ru> 0.7.3-alt1
- Version up

* Mon May 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.6.7-alt1
- new version from upstream

* Tue Dec 02 2008 Lebedev Sergey <barabashka@altlinux.org> 0.6.4-alt1
- initial build

