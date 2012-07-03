Name: libtiger
Version: 0.3.4
Release: alt1
Summary: rendering library for Kate streams
Group: System/Libraries
License: LGPLv2+
URL: http://www.xiph.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libkate-devel libpango-devel

%description
This is libtiger, a rendering library for Kate streams using Pango and Cairo

%package devel
Summary: Files for tiger application development
Group: Development/C
Requires: %name = %version-%release

%description devel
The libtiger-devel package contains the header files and documentation
needed to develop applications with Tiger

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS README
%_libdir/%name.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sun Jan 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Wed Nov 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.3.3-alt2
- rebuild

* Tue Aug 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.3-alt1
- initial release


