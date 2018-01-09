%def_disable static
%def_disable swig

Name: libhid
Version: 0.2.16
Release: alt3

Summary: A user-space USB HID access library
License: GPL
Group: System/Libraries
Url: http://libhid.alioth.debian.org/

Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: libusb-compat-devel
%if_enabled swig
BuildRequires: swig python-dev
%endif

%description
Libhid provides a generic and flexible way to access and interact with 
USB HID devices, much like libusb does for plain USB devices. 
It is based on libusb 0.1, thus it requires no special HID support in 
the kernel.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%if_enabled swig
%package python
Summary: Python bindings for %name
Group: Development/Other
Requires: %name = %version-%release

%description python
Python bindings for %name

%endif

%prep
%setup
%patch1 -p1

%build
%autoreconf
%__subst "s/get_config_vars('LIBPL',/get_config_vars('LIBDIR',/" configure
%configure %{subst_enable static} --enable-werror=no
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall

%files
%_bindir/*
%_libdir/*.so.*
%_man1dir/*.1*
%doc AUTHORS README NEWS COPYING ChangeLog INSTALL TODO doc/www/index.html

%files devel
%_libdir/*.so
%_includedir/*.h
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/%name.a
%endif

%if_enabled swig
%files python
%python_sitelibdir/%name
%doc swig/test_*.py
%endif

%changelog
* Tue Jan 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.16-alt3
- Fixed build.

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.16-alt2.2
- Fixed build

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.16-alt2.1
- Removed bad RPATH

* Sat Apr 18 2009 Michael A. Kangin <prividen@altlinux.org> 0.2.16-alt2
- Rebuild with libusb-compat

* Thu Mar 19 2009 Michael A. Kangin <prividen@altlinux.org> 0.2.16-alt1
- Initial build


