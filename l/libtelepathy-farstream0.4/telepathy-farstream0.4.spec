%define _name telepathy-farstream
%define ver_major 0.4
%def_enable python

Name: lib%_name%ver_major
Version: %ver_major.0
Release: alt3

Summary: Telepathy client library to handle call channels
Group: Networking/Instant messaging
License: LGPLv2+
URL: http://telepathy.freedesktop.org/

Source: http://telepathy.freedesktop.org/releases/%_name/%_name-%version.tar.gz

BuildRequires(pre): glib2-devel >= 2.30.0
BuildRequires(pre): libtelepathy-glib-devel >= 0.18.0
BuildRequires(pre): pkgconfig(farstream-0.1)
BuildRequires: libdbus-devel libdbus-glib-devel
BuildRequires: gtk-doc
%{?_enable_python:BuildRequires: pkgconfig(gst-python-0.10)}

%description
Telepathy Farstream is a Telepathy client library that uses Farstream to
handle Call channels. This is a compatibility package providing the obsolete
library for old Farstream.

%package devel
Summary: Libraries and include files for developing with %name
Group: Development/C
Requires: %name = %version-%release
Conflicts: libtelepathy-farstream-devel
%description devel
This package provides the necessary development libraries and include
files to allow you to develop with Telepathy Farstream library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release
Conflicts: libtelepathy-farstream-devel-doc
%description devel-doc
This package contains development documentation for the Telepathy
Farstream library.

%setup_python_module tpfarstream
%package -n python-module-%_name
Summary: Python bindings for %_name
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%_name
This package contains Python bindings for the Telepathy Farstream
library.


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static \
	%{subst_enable python}

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/lib%_name.so.*

%files devel
%_includedir/telepathy-1.0/%_name/
%_libdir/lib%_name.so
%_libdir/pkgconfig/%_name.pc

%files devel-doc
%_datadir/gtk-doc/html/%_name/

%files -n python-module-%_name
%python_sitelibdir/tpfarstream.so

%exclude %python_sitelibdir/tpfarstream.la

%changelog
* Wed Oct 31 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt3
- package devel files

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt2
- compatibility package

* Sat Apr 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sat Mar 24 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Sun Feb 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt2
- used %%autoreconf to fix RPATH problem

* Mon Nov 21 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus

