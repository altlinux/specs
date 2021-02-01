%def_disable snapshot
%define ver_major 1.2

%def_enable gtk_doc

Name: nautilus-python
Version: %ver_major.3
Release: alt2

Summary: Python bindings for Nautilus
Group: Development/Python3
License: GPLv2+
Url: http://www.gnome.org/

Provides: python-module-nautilus = %version-%release
Obsoletes: python-module-nautilus

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Patch: gcc10.patch

%add_python3_path %nautilus_extdir

%define nautilus_ver 3.0.0
%define pygobject_ver 3.0

BuildRequires(pre): rpm-build-gnome rpm-build-python3
BuildRequires: libnautilus-devel >= %nautilus_ver libnautilus-gir-devel
BuildRequires: python3-devel python3-module-pygobject3-devel >= %pygobject_ver
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
%patch -p1

%build
%autoreconf
export PYTHON=%__python3
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	LIBS="$(python3-config --libs)"
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
* Mon Feb 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.3-alt2
- Fixed build with gcc10.

* Thu Jul 18 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sun Apr 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt2
- updated to NAUTILUS_PYTHON_1_2_2-11-g13d40c1
- switched to python3

* Mon Jan 15 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

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
