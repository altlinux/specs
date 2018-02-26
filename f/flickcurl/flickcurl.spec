Name: flickcurl
Version: 1.14
Release: alt1.1
Summary: Flickcurl C library for the Flickr API
License: LGPL 2.1 / ASL 2.0
Group: Graphics
URL: http://librdf.org/flickcurl/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gtk-doc libcurl-devel libxml2-devel libraptor-devel

%description
Flickcurl is a C library for the Flickr API, handling creating the
requests, signing, token management, calling the API, marshalling request
parameters and decoding responses. It uses libcurl to call the REST
web service and libxml2 to manipulate the XML responses. The current
version supports the majority of the API (see Flickcurl API coverage)
including the functions for photo uploading, browsing, searching, adding
and editing comments, groups, notes, photosets, categories, tags and photo
metadata. It also includes a program flickrdf to turn photo metadata,
tags and machine tags into RDF descriptions of photso and tags.

This package contains utility programs that use the %name library.

%package -n lib%name
Summary: C library for the Flickr API
Group: System/Libraries

%description -n lib%name
Flickcurl is a C library for the Flickr API, handling creating the
requests, signing, token management, calling the API, marshalling request
parameters and decoding responses. It uses libcurl to call the REST
web service and libxml2 to manipulate the XML responses. The current
version supports the majority of the API (see Flickcurl API coverage)
including the functions for photo uploading, browsing, searching, adding
and editing comments, groups, notes, photosets, categories, tags and photo
metadata. It also includes a program flickrdf to turn photo metadata,
tags and machine tags into RDF descriptions of photso and tags.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the developement files for the %name library.

%prep
%setup -q
%patch -p1

%build
gtkdocize
%autoreconf
%configure \
	--enable-gtk-doc \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS NEWS.html
%_bindir/flickcurl
%_bindir/flickrdf
%_man1dir/flickcurl.1*
%_man1dir/flickrdf.1*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name.h
%_bindir/%name-config
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_datadir/gtk-doc/html/%name
%_man1dir/%name-config.1*

%changelog
* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1.1
- Rebuilt with curl 7.21.7

* Sat Oct 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.14-alt1
- 1.14

* Sun Sep 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.13-alt1
- initial release

