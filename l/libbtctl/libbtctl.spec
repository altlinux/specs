%define ver_major 0.11
%def_disable mono
 
Name: libbtctl
Version: %ver_major.1
Release: alt3.1

Summary: GNOME bluetooth control library
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/GnomeBluetooth
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2

Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

BuildRequires: rpm-build-gnome rpm-build-licenses

# From configure.in
BuildPreReq: intltool >= 0.35.0
BuildPreReq: gettext-tools
BuildPreReq: glib2-devel >= 2.4.0
BuildPreReq: libbluez-devel
BuildPreReq: libgtk+2-devel
BuildPreReq: libopenobex-devel >= 1.2.0
BuildPreReq: python-module-pygtk-devel
BuildPreReq: gtk-doc >= 1.0

%if_enabled mono
BuildRequires: /proc 
BuildRequires: libgtk-sharp-devel libgtk-sharp-gapi mono-devel 
%endif

%description
The GNOME Bluetooth Subsystem control library.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides development files and libraries for %name

%setup_python_module btctl
%package -n python-module-btctl
Summary: Python bindings for %name
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-btctl
This package contains files that are needed to work with Bluetooth in GNOME
from Python.

%if_enabled mono
%package mono
Summary: C# files for %name
Group: Development/Other
Requires: %name = %version-%release

%description mono
This package provides mono files and libraries for %name
%endif

%prep
%setup -q

%build
%configure \
    --enable-gtk-doc \
    --enable-shared \
    %{subst_enable mono} \
	--disable-static

# SMP-incompatible build
%make pydir=%python_sitelibdir

%install
%make_install DESTDIR=%buildroot pydir=%python_sitelibdir install

%find_lang %name

%files -f %name.lang
%_libdir/*.so.*
%doc AUTHORS ChangeLog README NEWS TODO

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%doc %_datadir/gtk-doc/html/*

%files -n python-module-btctl
%python_sitelibdir/btctl.so
%exclude %python_sitelibdir/btctl.la

%if_enabled mono
%files mono
%_libdir/mono/%name/*
%_libdir/mono/gac/*
%_datadir/gapi/btctl-api.xml
%endif

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.1-alt3.1
- Rebuild with Python-2.7

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt3
- buildreqs s/libbluez4-devel//libbluez-devel

* Sat Mar 20 2010 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt2
- go to Sisyphus again

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Alexey Rusakov <ktirf@altlinux.org> 0.11.1-alt1
- New version (0.11.1), ported to Bluez 4.

* Thu Dec 25 2008 Alexey Rusakov <ktirf@altlinux.org> 0.10.0-alt2
- Removed no more needed ldconfig calls in post/postun scripts.
- Added Packager tag.

* Fri Oct 10 2008 Alexey Rusakov <ktirf@altlinux.org> 0.10.0-alt1
- New version (0.10.0).

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 0.9.0-alt1.1
- Rebuilt with python-2.5.

* Fri Dec 28 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.0-alt1
- New version (0.9.0).
- Python module has been moved to a separate subpackage.
- More usage of RPM macros.
- Updated buildreqs.

* Wed Feb 21 2007 Igor Zubkov <icesik@altlinux.org> 0.8.2-alt1
- 0.8.1 -> 0.8.2

* Mon Dec 11 2006 Igor Zubkov <icesik@altlinux.org> 0.8.1-alt2
- fix build for x86_64 (thanks to damir@)

* Wed Oct 25 2006 Igor Zubkov <icesik@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1

* Wed Oct 25 2006 Igor Zubkov <icesik@altlinux.org> 0.8.0-alt1.1
- import to gear 

* Wed Oct 25 2006 Igor Zubkov <icesik@altlinux.org> 0.8.0-alt1
- 0.6.0 -> 0.8.0

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.0-alt1.1
- Rebuilt for new pkg-config dependencies.

* Tue Nov 22 2005 Vital Khilko <vk@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Nov 15 2005 Vital Khilko <vk@altlinux.ru> 0.5.0-alt0.1
- 0.5.0
- added mono subpackage

* Thu Jul 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Mon May 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3-alt0.2
- do not package .la files.

* Sun Nov 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3-alt0.1
- First build for Sisyphus.

