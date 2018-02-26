%define oname idioskopos
Name: lib%oname
Version: 0.4.1
Release: alt2

Summary: C++ library that simplifies (hopefully) the addition of object reflection and introspection

Group: System/Libraries
License: LGPL
Url: http://idioskopos.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%oname/%oname-%version.tar.bz2

# Warning: buildreq adds all fonts packages :)
# Automatically added by buildreq on Sat Nov 29 2008
BuildRequires: boost-devel gcc-c++ libxml++2-devel rpm-build-java rpm-build-mono rpm-build-seamonkey xorg-sdk


%description
idioskopos (Greek: idio- inward, within, private; -skopos look, aim,
target) is a C++ library that simplifies (hopefully) the addition of
object reflection a The idioskopos library is based heavily on several
concepts used in Gtkmm to wrap the gobject interface. However, it is a
standalone library and depends only on libsigc++.

%package devel
Summary: Libraries/include files for development with %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Libraries/include files for development with %name.

%prep
%setup -q -n %oname-%version

%build
%configure --disable-static

%make_build
#%__subst "s|^Libs:.*|Libs: -lm -l%oname|g" %oname-0.1.pc

%install
%makeinstall_std

%files
%doc AUTHORS
%_libdir/lib*.so.*

%files devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*

%changelog
* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt2
- update buildreq
- cleanup spec

* Sat May 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- new version 0.4.1 (with rpmrb script)
- update buildreqs

* Sat Nov 18 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt0.1
- new version 0.2.1
- fix ldconfig

* Wed Nov 15 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt0.1
- new version 0.2.0 (with rpmrb script)

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.14-alt0.1
- initial build for ALT Linux Sisyphus
- fix libpath in pc file
