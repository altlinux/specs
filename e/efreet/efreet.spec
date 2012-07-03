%def_disable static

Name: efreet
Version: 1.2.0
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: FreeDesktop specifications for E
License: BSD
Group: System/Libraries
Url: http://www.enlightenment.org/pages/efreet.html

Source:  http://download.enlightenment.org/releases/%name-%version.tar.bz2

BuildRequires: libecore-devel >= 1.2.0 libeina-devel >= 1.2.0 libeet-devel >= 1.6.0

%package -n lib%name
Group: System/Libraries
Summary: FreeDesktop specifications for E library.

%description -n lib%name
Implementation of several specifications from freedesktop.org:
 o Base Directory
 o Desktop Entry
 o Icon Theme
 o Menu

%description
Implementation of several specifications from freedesktop.org:
 o Base Directory
 o Desktop Entry
 o Icon Theme
 o Menu

%package -n lib%name-devel
Summary: Efreet headers and development libraries
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Efreet development files

%prep
%ifdef beta
%setup -q -n %name-%version.%beta
%else
%setup -q
%endif

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*
%dir %_libdir/%name/
%_libdir/%name/efreet_desktop_cache_create
%_libdir/%name/efreet_icon_cache_create
%doc AUTHORS COPYING* README TODO

%files -n lib%name-devel
%_bindir/*
%_libdir/*.so
%_datadir/efreet
%_pkgconfigdir/*
%_includedir/efreet-1

%changelog
* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt2
- used %%autoreconf to fix RPATH problem

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt5
- rebuilt for debuginfo

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt4
- 1.0.0 release

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt3.beta2
- 1.0.0.beta2

* Tue Nov 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2.beta
- rebuild for update dependencies

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.beta
- 1.0.0.beta

* Mon Jan 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.0.063-alt1
- 0.5.0.063

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 0.5.0.062-alt1
- new version
- removed obsolete %%post{,un}_ldconfig

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 0.5.0.050-alt1
- 0.5.0.050

* Mon Sep 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.3.006-alt1.20070917
- CVS from 20070917.

* Thu Sep 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.3.006-alt1.20070905
- CVS from 20070905.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.3.005-alt1.20070731
- CVS from 20070731.

* Wed May 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.3.002-alt1.20070509
- Initial build for Sisyphus.
- CVS from 20070509.

