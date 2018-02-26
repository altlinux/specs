Name: moment-gst
Version: 1.2.0
Release: alt1
License: GPL
Url: http://momentvideo.org
Source: %name-%version.tar
Summary: GStreamer support module for Moment Video Server
Group: System/Servers
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires: gcc-c++ libmoment-devel gstreamer-devel

%description
GStreamer support module for Moment Video Server

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
This package contains shared libraries used by %name's daemons
and clients.

%package -n lib%name-devel
Summary: Development package that includes the %name header files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The devel package contains the include files

%prep
%setup

%build
./autogen.sh
%configure --disable-static
%make

%install
%make DESTDIR=%buildroot install

%check
#make test

%files -n lib%name
%doc AUTHORS COPYING ChangeLog NEWS README
%_libdir/moment*/*.so.*
%_libdir/moment*/*.la

%files -n lib%name-devel
%_includedir/*
%_libdir/moment*/lib*so
%_pkgconfigdir/*

%changelog
* Thu Nov 24 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.0-alt1
- New version

* Wed Jul 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- Build for ALT
