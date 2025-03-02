%def_enable snapshot
%define srcname libvisual
%define api_ver 0.4

%def_disable static
%def_disable lv_tool
%def_disable examples

Name: %{srcname}%api_ver
Version: 0.4.2
Release: alt1

Summary: Libvisual is an abstraction library that comes between applications and audio visualisation plugins
License: LGPL-2.1-or-later
Group: System/Libraries
Url: http://%srcname.sourceforge.net/

Vcs: https://github.com/Libvisual/libvisual.git

%if_disabled snapshot
#Source: https://download.sourceforge.net/%srcname/%srcname-%version.tar.bz2
Source: https://github.com/Libvisual/libvisual/archive/%version/%srcname-%version.tar.bz2
%else
Source: %srcname-%version.tar
%endif

BuildRequires: autoconf-archive gcc-c++
%{?_enable_lv_tool:BuildRequires: pkgconfig(sdl) >= 1.2.0}

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
Requires: %name = %EVR

%description devel
This package contains development files required for building
%srcname-based software.

%package devel-static
Summary: Static %srcname library
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
This package contains development files required for building
statically linked %srcname-based software.

%def_disable static

%prep
%setup -n %srcname-%version/%srcname

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{subst_enable examples} \
    %{?_disable_lv_tool:--disable-lv-tool}
%nil
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_libdir/%srcname-%api_ver/{actor,input,morph}
%find_lang %srcname-%api_ver

%files -f %srcname-%api_ver.lang
%{?_enable_lv_tool:%_bindir/lv-tool}
%_libdir/*.so.*
%dir %_libdir/%srcname-%api_ver
%dir %_libdir/%srcname-%api_ver/actor
%dir %_libdir/%srcname-%api_ver/input
%dir %_libdir/%srcname-%api_ver/morph
%{?_disable_lv_tool:%exclude %_man1dir/lv-tool-%{api_ver}.1*}
%doc AUTHORS ChangeLog NEWS  README TODO

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sun Mar 02 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

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
