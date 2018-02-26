%define oname plotmm
Name: libplotmm
Version: 0.1.2
Release: alt2

Summary: PlotMM - GTKmm plot widget for scientific applications

License: LGPL
Group: System/Libraries
Url: http://plotmm.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/plotmm/%oname-%version.tar
Patch: %name-as-needed.patch
Patch1: %name-sigc.patch

# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: doxygen gcc-c++ glibc-devel libgtkmm2-devel

%description
PlotMM is an extension to the gtkmm library.  It contains widgets
which are primarily useful for technical and scientifical purposes.
Initially, this is a 2-D plotting widget.

PlotMM is based in part on the work of the Qwt project 
(http://qwt.sf.net).

%package -n %name-devel
Summary: Headers and development files of %name library
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n %name-devel
This package contains the headers and various development files needed
for compiling or development of applications that wants C++ interface
of %name library.

%prep
%setup -n %oname-%version
%patch
%patch1 -p1

%build
%autoreconf
%configure --disable-static

%make_build

%install
%makeinstall_std
( cd %buildroot%_bindir ; mv curves %oname-curves; mv simple %oname-simple; cd - )

%files
%doc README NEWS
%_libdir/*.so.*

%files -n %name-devel
%_bindir/%oname-*
%doc AUTHORS ChangeLog NEWS doc/html
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Mar 30 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt2
- cleanup spec, update buildreqs

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libplotmm
  * postun_ldconfig for libplotmm
  * postclean-05-filetriggers for spec file

* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt1
- fix build with new libsigc
- cleanup spec

* Wed Apr 19 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt0.2
- add patch against ld --as-needed

* Sun Nov 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt0.1
- initial build for ALT Linux Sisyphus

