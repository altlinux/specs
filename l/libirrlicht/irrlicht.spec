%def_disable static
%define realname irrlicht

Name: libirrlicht
Version: 1.7.1
Release: alt2

Summary: Fast Open-source 3D engine
License: BSD-style
Group: System/Libraries
Url: http://irrlicht.sourceforge.net/
Packager: Damir Shayhutdinov <damir@altlinux.ru>

Source0: %realname-%version.tar.bz2
Patch0: irrlicht-%version-alt-autotools.patch
Patch1: irrlicht-%version-alt-use-system-libs.patch
BuildPreReq: libX11-devel libXxf86vm-devel libGLU-devel libpng-devel gcc-c++ zlib-devel
BuildPreReq: libjpeg-devel pkg-config unzip bzlib-devel


%description
The Irrlicht Engine is a cross-platform high performance realtime 3D
engine written in C++. It is a powerful high level API for creating
complete 3D and 2D applications like games or scientific visualizations.
It comes with an excellent documentation and integrates all the
state-of-the-art features for visual representation like dynamic
shadows, particle systems, character animation, indoor and outdoor
technology, and collision detection. All this is accessible through
a well designed C++ interface, which is extremely easy to use.


%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%package examples
Summary: Examples for %name
Group: Development/C
Requires: %name = %version-%release

%description examples
Examples that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%prep
%setup -q -n %realname-%version
%patch0 -p2
%patch1 -p1

%build
autoreconf -fisv
%configure %{subst_enable static}
%make_build

%install
%makeinstall

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/irrlicht
%doc doc/html doc/index.html
%doc doc/upgrade-guide.txt
%doc readme.txt changes.txt

%files examples
%_bindir/*
%_datadir/irrlicht

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Sat Jan 22 2011 Damir Shayhutdinov <damir@altlinux.ru> 1.7.1-alt2
- Rebuilt with set-provides.

* Tue Mar 30 2010 Damir Shayhutdinov <damir@altlinux.ru> 1.7.1-alt1
- New version.

* Sat Nov 22 2008 Damir Shayhutdinov <damir@altlinux.ru> 1.4.2-alt1
- New version.

* Fri Apr 13 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt4
- Moved docs to devel subpackage. Now libirrlicht is ready for biarch.

* Thu Apr 12 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt3
- Fix license tag (#11483).

* Thu Mar 22 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt2
- Packaged readme.txt and changes.txt.
- Added documentation to -devel package.

* Sat Mar 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt1
- New version. 

* Fri Mar 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.2.0-alt1
- Initial build for ALT Linux.
