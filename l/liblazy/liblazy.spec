%def_disable static

Name: liblazy
Version: 0.2
Release: alt3

Summary: D-Bus methods provided for convenience
License: LGPL
Group: System/Libraries

Packager: Damir Shayhutdinov <damir@altlinux.ru>
URL: http://www.freedesktop.org/wiki/Software/liblazy
Source0: http://people.freedesktop.org/~homac/liblazy/%name-%version.tar.bz2
Patch1: %name-%version-upstream.patch

BuildRequires: libdbus-devel pkg-config doxygen

%description
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%prep
%setup
%patch1 -p1
%build
autoreconf -fisv
%configure %{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%doc docs/autodocs/html

%if_enabled static
%files -n devel-static
%_libdir/%name.a
%endif

%changelog
* Tue Nov 09 2010 Damir Shayhutdinov <damir@altlinux.ru> 0.2-alt3
- Rebuilt to generate symbol provides

* Mon Nov 09 2009 Damir Shayhutdinov <damir@altlinux.ru> 0.2-alt2
- Removed obsolete ldconfig calls from post/postun

* Sun Apr 06 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.2-alt1.1
- Updated to more recent upstream version (needed for powersave)

* Sun Apr 06 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.2-alt1
- New version

* Sat Oct 20 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux

