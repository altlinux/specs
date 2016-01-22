
%define _libexecdir %prefix/libexec
%define sover 1
%define libsignon_glib libsignon-glib%sover

Name: signon-glib
Version: 1.13
Release: alt1

Group: System/Libraries
Summary: Single signon authentication library for GLib applications
Url: https://gitlab.com/accounts-sso/libsignon-glib
License: LGPLv2+

Source: %name-%version.tar

# Automatically added by buildreq on Thu Oct 15 2015 (-bi)
# optimized out: elfutils glib2-devel gnu-config gobject-introspection gtk-doc libgio-devel pkg-config python-base python-devel python-module-google python-modules python-modules-compiler python-modules-encodings python-modules-xml python3 python3-base rpm-build-gir ruby ruby-stdlibs xml-utils
#BuildRequires: dconf glib-networking glibc-devel-static gobject-introspection-devel gtk-doc-mkpdf libGConf rpm-build-python3 rpm-build-ruby rpm-build-vala signon-devel time
#BuildRequires: dconf glib-networking glibc-devel gobject-introspection-devel gtk-doc-mkpdf rpm-build-vala signon-devel
BuildRequires: glibc-devel gobject-introspection-devel gtk-doc-mkpdf rpm-build-vala signon-devel

%description
This project is a library for managing single signon credentilas which can be
used from GLib applications. It is effectively a GLib binding for the D-Bus API
provided by signond. It is part of the accounts-sso project.

%package -n %libsignon_glib
Group: System/Libraries
Summary: %name library
#Requires: %name-common = %version-%release
%description -n %libsignon_glib
%summary.

%package devel
Group: Development/Other
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

NOCONFIGURE=1 ./autogen.sh

%build
%configure
%make -j1

%install
%make install DESTDIR=%buildroot

%files -n %libsignon_glib
%doc README NEWS
%_libdir/libsignon-glib.so.%sover
%_libdir/libsignon-glib.so.*

%files devel
%_includedir/libsignon-glib/
%_libdir/lib*.so
%_pkgconfigdir/libsignon-glib.pc
%_datadir/vala/vapi/signon.vapi
%_typelibdir/Signon-1.0.typelib
%_girdir/Signon-1.0.gir

%changelog
* Fri Jan 22 2016 Sergey V Turchin <zerg@altlinux.org> 1.13-alt1
- new version

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 1.12-alt2
- redefine libexecdir

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 1.12-alt1
- initial build
