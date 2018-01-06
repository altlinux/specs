%def_disable snapshot
%define ver_major 1.2

%def_enable gtk_doc

Name: nautilus-python
Version: %ver_major
Release: alt1

Summary: Python bindings for Nautilus

License: GPLv2+
Group: Development/Python
Url: http://www.gnome.org/
Provides: python-module-nautilus = %version-%release
Obsoletes: python-module-nautilus

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%setup_python_module nautilus
%add_python_lib_path %nautilus_extdir

%define nautilus_ver 3.0.0
%define pygobject_ver 3.0

BuildRequires(pre): rpm-build-gnome
BuildRequires: libnautilus-devel >= %nautilus_ver libnautilus-gir-devel
BuildRequires: python-module-pygobject3-devel >= %pygobject_ver
%{?_enable_gtk_doc:BuildRequires: gtk-doc}

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
%setup

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	LIBS="$(python-config --libs)"
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/nautilus-python/extensions
rm -f examples/{Makefile*,README.in}

%files
%nautilus_extdir/*.so
%dir %_datadir/nautilus-python/extensions

%files devel
%_pkgconfigdir/*
%doc README AUTHORS NEWS examples

%files devel-doc
%_datadir/gtk-doc/html/*

%exclude %nautilus_extdir/*.la
%exclude %_docdir/%name

%changelog
* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Sun Jul 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt2
- fixed %%add_python_lib_path

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
