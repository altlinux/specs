%define major 1.1

Name: nautilus-python
Version: %major.0
Release: alt1

Summary: Python bindings for Nautilus

License: GPLv2+
Group: Development/Python
Url: http://www.gnome.org/
Provides: python-module-nautilus = %version-%release
Obsoletes: python-module-nautilus

Source: %name-%version.tar

%setup_python_module nautilus
%add_python_lib_path %_libdir/%name

%define nautilus_ver 2.91.0
%define pygobject_ver 3.0

BuildPreReq: rpm-build-gnome gnome-common
BuildPreReq: libnautilus-devel >= %nautilus_ver libnautilus-gir-devel
BuildPreReq: python-module-pygobject3-devel >= %pygobject_ver
BuildRequires: gtk-doc

%description
This package provides Python bindings for the Nautilus extension library.

%package devel
Summary: Development files for %name
Group: Development/Python
Requires: %name = %version-%release
Provides: python-module-nautilus-devel = %version-%release
Obsoletes: python-module-nautilus-devel

%description devel
Development files for %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Python
BuildArch: noarch
Conflicts: %name-devel < %version
Provides: python-module-nautilus-devel-doc = %version-%release
Obsoletes: python-module-nautilus-devel-doc

%description devel-doc
Development documentation for %name.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-static \
    --enable-gtk-doc

%make_build

%install
%make DESTDIR=%buildroot install
mkdir -p %buildroot%_datadir/nautilus-python/extensions
rm -f examples/{Makefile*,README.in}

%files
%nautilus_extdir/*.so
%dir %_datadir/nautilus-python/extensions

%files devel
%_pkgconfigdir/*
%doc README AUTHORS NEWS ChangeLog examples

%files devel-doc
%_datadir/gtk-doc/html/*

%exclude %nautilus_extdir/*.la
%exclude %_docdir/%name

%changelog
* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0
- build with pygobject3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.1
- Rebuild with Python-2.7

* Tue Jun 14 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0
- build for nautilus-3
- only dir /usr/share/nautilus-python/extensions for arch-independent extensions

* Mon Jun 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Mon Jul 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt2
- rename python-module-nautilus to nautilus-python
- cleanup spec
- fix path for nautilus-python extentions

* Sat May 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- new version
- new devel-doc noarch subpackage

* Wed Jan 20 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Jan 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus
