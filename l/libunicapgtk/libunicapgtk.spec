Summary: Library to access different kinds of (video) capture devices
Name: libunicapgtk
Version: 0.9.8
Release: alt2
License: GPLv2+
Group: Development/C
Url: http://www.unicap-imaging.org/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: libunicapgtk-%version.tar

BuildRequires: gtk-doc intltool libucil-devel libunicap-devel gtk+2-devel libXext-devel libXv-devel

%description
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
The included ucil library provides easy to use functions to render text
and graphic overlays onto video images.
This package provides libunicapgtk library

%package devel
Summary: Development files for the unicap library
Group: Development/C
Requires: %name = %version-%release

%description devel
The libunicap-devel package includes header files and libraries necessary for
for developing programs which use the unicap, unicapgtk and ucil library. It
contains the API documentation of the library, too.
This package provides libunicapgtk library development files

%prep
%setup -q
%autoreconf

%build
%configure
%make_build

%install
%makeinstall_std

# Don't install any static .a and libtool .la files
rm -f %buildroot%_libdir/{,unicap2/cpi/}*.{a,la}

%find_lang unicapgtk

%files -f unicapgtk.lang
%doc AUTHORS ChangeLog COPYING README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/unicap/*
%_datadir/gtk-doc/html/*

%changelog
* Tue Dec 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt2
- rebuild for soname set-version

* Wed May 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt1
- initial
