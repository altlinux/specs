Name: nemiver
Version: 0.9.6
Release: alt7

Summary: A GNOME C/C++ Debugger
Group: Development/Debuggers
License: GPL-2.0
Url: https://wiki.gnome.org/Apps/Nemiver

Source: %name-%version.tar

Requires: gdb

# Automatically added by buildreq on Sat Apr 17 2021
# optimized out: at-spi2-atk dconf fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libat-spi2-core libatk-devel libatkmm-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcairomm-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglibmm-devel libgpg-error libgtk+3-devel libgtkmm3-devel libgtksourceview3-devel libharfbuzz-devel libpango-devel libpangomm-devel libsigc++2-devel libstdc++-devel libwayland-client libwayland-cursor libwayland-egl perl perl-Encode perl-XML-Parser perl-parent pkg-config python2-base python3-base python3-module-libxml2 sh4 shared-mime-info xml-utils
BuildRequires: boost-devel-headers doxygen gcc-c++ intltool itstool libGConf-devel libappstream-glib-devel libgtksourceviewmm3-devel libgtop-devel libsqlite3-devel libvte3-devel libxml2-devel
BuildRequires: yelp-tools

%description
Nemiver is an ongoing effort to write a standalone graphical debugger that
integrates well in the GNOME desktop environment. It currently features a
backend which uses the well known GNU Debugger (gdb) to debug C/C++ programs.

The yelp package must be installed to make use of Nemiver's documentation.

%package devel
Summary: Header files for %name
Group: Development/C
BuildArch: noarch
Requires: %name = %version-%release

%description devel
The %name-devel package contains header files for developing new debugging
backends for Nemiver.

%prep
%setup

%build
%autoreconf
export ac_cv_path_GDB_PROG=%_bindir/gdb
%configure --disable-static
%make_build
make doc

%install
%makeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/*/apps/%{name}*
%_datadir/%name/
%_datadir/appdata/%name.appdata.xml
%_man1dir/*
%doc AUTHORS NEWS README TODO

%files devel
%doc docs/reference/html
%_includedir/%name/

%changelog
* Sat Apr 17 2021 Fr. Br. George <george@altlinux.ru> 0.9.6-alt7
- resurrected from orphans

* Sun Mar 22 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt6
- updated to 0.9.6-105-g9383e12d

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt5
- updated to 0.9.6-80-ge6e41f7

* Sun Oct 02 2016 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt4
- updated to 0.9.6-57-gbe35424

* Mon Jun 13 2016 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt3
- fixed buildreqs

* Thu May 05 2016 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt2
- updated to 0.9.6-39-ge0e4222

* Thu Sep 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6 release

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.6-alt0.1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Nov 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt0.1
- 0.9.6 snapshot (ef396727ad)

* Tue Jun 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt0.2
- rebuilt against libgtop-2.0.so.10

* Sun Dec 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt0.1
- 0.9.5

* Sat Dec 01 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt0.1
- 0.9.4 snapshot (052c7c0629)

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

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

