%define ver_major 0.1
%define api_ver 1.0

Name: libgames-support
Version: %ver_major
Release: alt1

Summary: Shared library for GNOME games
Group: System/Libraries
License: GPLv3 LGPLv3

Url: https://wiki.gnome.org/Apps/Games
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.40
%define gtk_ver 3.12

BuildRequires: intltool libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgee0.8-devel vala-tools

%description
%name provides code that's useful for different GNOME games.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

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
* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

