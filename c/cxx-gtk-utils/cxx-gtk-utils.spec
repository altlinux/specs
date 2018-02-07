%define major 2.2
%define oname c++-gtk-utils

Name: cxx-gtk-utils
Version: %major.15
Release: alt1

Summary: lightweight library for programming GTK+ programs using C++ in POSIX (unix-like) environment

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPLv2
Group: System/Libraries
Url: http://cxx-gtk-utils.sourceforge.net

Source: http://downloads.sourceforge.net/cxx-gtk-utils/cxx-gtk-utils/%version/%oname-%version.tar

# Automatically added by buildreq on Wed Apr 25 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel pkg-config
BuildRequires: gcc-c++ glibc-devel libgtk+3-devel

%define libname lib%name
%define develname %libname-devel

%description
c++-gtk-utils is a lightweight library containing
a number of classes and functions for programming
GTK+ programs using C++ in POSIX (unix-like) environments,
where the user does not want to use a full-on wrapper such
as gtkmm or wxWidgets, or is concerned about exception safety
or thread safety of the wrapper and their documentation.
It is parallel installable for both GTK+2 and GTK+3.

%package -n %libname
Summary: A library containing a number of classes and functions for programming GTK+ programs using C++
Group: System/Libraries

%description -n %libname
c++-gtk-utils is a lightweight library containing
a number of classes and functions for programming
GTK+ programs using C++ in POSIX (unix-like) environments,
where the user does not want to use a full-on wrapper such
as gtkmm or wxWidgets, or is concerned about exception safety
or thread safety of the wrapper and their documentation.
It is parallel installable for both GTK+2 and GTK+3.

%package -n %develname
Summary: Development files for %name
Group: Development/C++
Requires: %libname = %version-%release

%description -n %develname
Development files for %name

%prep
%setup -n %oname-%version

%build
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_docdir/

%files -n %libname
%doc README NEWS BUGS
%_libdir/libcxx-gtk-utils-3-%major.so.*

%files -n %develname
%doc docs/html/ PORTING*
%dir %_includedir/%oname-3-%major/
%dir %_includedir/%oname-3-%major/%oname/
%_includedir/%oname-3-%major/%oname/*.h
%_includedir/%oname-3-%major/%oname/*.tpp
%_pkgconfigdir/*.pc
%_libdir/libcxx-gtk-utils-3-%major.so

%changelog
* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.15-alt1
- new version 2.2.15 (with rpmrb script)

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2.14.1-alt1
- new version 2.2.14.1 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 2.2.13-alt1
- new version 2.2.13 (with rpmrb script)

* Sat Apr 23 2016 Vitaly Lipatov <lav@altlinux.ru> 2.2.12-alt1
- new version 2.2.12 (with rpmrb script)

* Wed Apr 25 2012 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- initial build for ALT Linux Sisyphus

* Tue Jan 17 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.0.4-1
+ Revision: 761934
- so.0 moved from develname to libname
- imported package c++-gtk-utils

