Name: scrollkeeper
Version: 0.3.14
Release: alt12
Summary: Open Documentation Cataloging Project
License: LGPLv2.1, FDLv1.1
Group: Development/Tools
Url: http://scrollkeeper.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: glib2-devel intltool libxml2-devel libxslt-devel
BuildPreReq: docbook-dtds perl-Encode-CN perl-Encode-KR

Requires: lib%name = %version-%release

%description
ScrollKeeper is a cataloging system for documentation on open systems.
It manages documentation metadata (as specified by the Open Source
Metadata Framework(OMF)) and provides a simple API to allow help
browsers to find, sort, and search the document catalog. It will also be
able to communicate with catalog servers on the Net to search for
documents which are not on the local system.

%package -n lib%name
Summary: Shared libraries of ScrollKeeper
Group: System/Libraries

%description -n lib%name
ScrollKeeper is a cataloging system for documentation on open systems.
It manages documentation metadata (as specified by the Open Source
Metadata Framework(OMF)) and provides a simple API to allow help
browsers to find, sort, and search the document catalog. It will also be
able to communicate with catalog servers on the Net to search for
documents which are not on the local system.

This package contains shared libraries of ScrollKeeper.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-static=no \
	--disable-rpath \
	--with-libintl-prefix=%prefix \
	--with-partial-db-dir=%_localstatedir/%name
rm -fR intl
%make_build

%install
%makeinstall_std

rm -fR %buildroot%_localstatedir/log
install -d %buildroot%_localstatedir/%name

%find_lang --with-gnome %name

%files -f %name.lang
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README TODO
%_sysconfdir/*
%_bindir/*
%_libdir/*.so
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*
%_datadir/%name
%_datadir/xml/%name
%dir %_localstatedir/%name

%files -n lib%name
%_libdir/*.so.*

%changelog
* Sun Jan 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.14-alt12
- Initial build for Sisyphus

