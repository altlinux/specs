%define _name telepathy-farstream

%def_enable python

Name: lib%_name
Version: 0.4.0
Release: alt1

Summary: Telepathy client library to handle call channels
Group: Networking/Instant messaging
License: LGPLv2+
URL: http://telepathy.freedesktop.org/

Source: http://telepathy.freedesktop.org/releases/%_name/%_name-%version.tar.gz

BuildPreReq: glib2-devel >= 2.30.0
BuildPreReq: libtelepathy-glib-devel >= 0.18.0
BuildPreReq: farstream-devel >= 0.1.2
BuildRequires: libdbus-devel libdbus-glib-devel
BuildRequires: gtk-doc
%{?_enable_python:BuildRequires: python-module-gst-devel}

%description
Telepathy Farstream is a Telepathy client library that uses Farstream to
handle Call channels.

%package devel
Summary: Libraries and include files for developing with %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with Telepathy Farstream library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

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
%_libdir/%name.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/telepathy-1.0/%_name/
%_libdir/%name.so
%_libdir/pkgconfig/%_name.pc

%files devel-doc
%_datadir/gtk-doc/html/%_name/

%files -n python-module-%_name
%python_sitelibdir/tpfarstream.so

%exclude %python_sitelibdir/tpfarstream.la

%changelog
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

