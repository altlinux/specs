%def_disable static
%define sname keybinder
%define luaver 5.1

Name: libkeybinder
Version: 0.3.0
Release: alt5.git20120617

Summary: keybinder is a library for registering global keyboard shortcuts
License: GPLv2
Group: System/Libraries
Url: http://kaizer.se/wiki/keybinder/

BuildRequires: libgtk+2-devel xorg-server-common python-dev liblua5.1-devel
BuildRequires: python-module-pygtk-devel libXext-devel
BuildRequires: gobject-introspection-devel
BuildPreReq: gtk-doc
# https://github.com/engla/keybinder.git
Source: %name-%version.tar

%description
keybinder is a library for registering global keyboard shortcuts.
Keybinder works with GTK-based applications using the X Window System.
The library contains:
 - A C library, libkeybinder
 - Lua bindings, lua-keybinder
 - Python bindings, python-keybinder
 - An examples directory with programs in C, Lua, Python and Vala.


%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%package -n python-module-keybinder
Summary: Python binding to %name
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%sname
Python binding to %name

%package -n lua5-%name
Summary: Lua5 binding to %name
Group: Development/Other
Requires: %name = %version-%release

%description -n lua5-%name
Lua5 binding to %name

%prep
%setup

%build
%autoreconf -I m4
%configure %{subst_enable static} \
	--enable-gtk-doc \
	--with-html-dir=%_docdir
%make_build V=1

%install
%makeinstall_std

%files
%doc AUTHORS README NEWS
%_libdir/*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc
%doc %_docdir/%sname

%if_enabled static
%files devel-static
%_libdir/lib%name.a
%endif

%files -n python-module-%sname
%python_sitelibdir/%sname

%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*

#files -n lua5-%name
#_libdir/lua/%luaver/*.so


%changelog
* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt5.git20120617
- Updated build dependencies

* Fri Jun 5 2015 Vladimir Didenko <cow at altlinux.org> 0.3.0-alt4.git20120617
- don't require gtk3

* Wed Jun 3 2015 Vladimir Didenko <cow at altlinux.org> 0.3.0-alt3.git20120617
- add gir packages

* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2.git20120617
- Disabled lua5-libkeybinder (ALT #27509)

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20120617
- Version 0.3.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.2-alt2.1
- Rebuild with Python-2.7

* Mon Apr 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.2-alt2
- fix build

* Thu Dec 30 2010 Alexey Morsov <swi@altlinux.ru> 0.2.2-alt1
-  initial build for Sisyphus

