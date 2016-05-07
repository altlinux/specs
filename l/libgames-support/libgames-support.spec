%define ver_major 1.0
%define api_ver 1.0

Name: libgames-support
Version: %ver_major.2
Release: alt1

Summary: Shared library for GNOME games
Group: System/Libraries
License: GPLv3 LGPLv3

Url: https://wiki.gnome.org/Apps/Games
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.40
%define gtk_ver 3.20.0

BuildRequires: intltool libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgee0.8-devel vala-tools

%description
%name provides code that's useful for different GNOME games.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libgee0.8-devel

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_libdir/%name.so.*
%doc README NEWS

%files devel
%_includedir/gnome-games/
%_libdir/%name.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.vapi


%changelog
* Sat May 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Fri Apr 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Wed Mar 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.91-alt1
- 0.91

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

