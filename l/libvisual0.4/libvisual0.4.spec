%define srcname libvisual

Name: %{srcname}0.4
Version: 0.4.0
Release: alt3

Summary: Libvisual is an abstraction library that comes between applications and audio visualisation plugins
License: LGPL
Group: System/Libraries
Url: http://%srcname.sourceforge.net/
Source: %srcname-%version.tar.bz2

Packager: Valery Inozemtsev <shrek@altlinux.ru>

# Automatically added by buildreq on Sun May 28 2006
BuildRequires: gcc-c++ pkg-config

%description
Libvisual is an abstraction library that comes between applications and
audio visualisation plugins.

Often when it comes to audio visualisation plugins or programs that
create visuals, they depend on a player or something else; basically,
there is no general framework that enabled application developers to
easily access cool audio visualisation plugins. Libvisual wants to
change this by providing an interface towards plugins and applications;
through this easy to use interface applications can easily access
plugins and, since the drawing is done by the application, it also
enables the developer to draw the visual anywhere he wants.

The framework also allows you to morph to different plugins and mix two
at once; all kinds of neat tricks are possible using this method.

%package devel
Summary: Development environment for %srcname
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required for building
%srcname-based software.

%package devel-static
Summary: Static %srcname library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains development files required for building
statically linked %srcname-based software.

%def_disable static

%prep
%setup -n %srcname-%version

%build
%configure \
    %{subst_enable static}

%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_libdir/%srcname-0.4/{actor,input,morph}

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/*.so.*
%dir %_libdir/%srcname-0.4
%dir %_libdir/%srcname-0.4/actor
%dir %_libdir/%srcname-0.4/input
%dir %_libdir/%srcname-0.4/morph

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3
- Rebuilt for debuginfo

* Fri Oct 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt2
- Rebuilt for soname set-versions

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libvisual0.4
  * postun_ldconfig for libvisual0.4

* Sun May 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri Nov 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.7-alt1
- First build for Sisyphus. 
