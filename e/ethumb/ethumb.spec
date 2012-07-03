%define _libexecdir %_prefix/libexec
%def_disable epdf

Name: ethumb
Version: 1.0.1
Release: alt1

Summary: Ethumb - Thumbnail generation library
Group: Graphical desktop/Enlightenment
License: LGPLv2+
Url: http://www.enlightenment.org

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

Requires: lib%name = %version-%release

BuildRequires: doxygen edje libedbus-devel libedje-devel libeet-devel libemotion-devel libexif-devel
%{?_enable_epdf:BuildRequires: libepdf-devel}

%description
Ethumb is a EFL thumbnail generation library that
 * create thumbnails with a predefined frame (possibly an edje frame);
 * have an option to create fdo-like thumbnails;
 * have a client/server utility.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
Ethumb is a EFL thumbnail generation library that
 * create thumbnails with a predefined frame (possibly an edje frame);
 * have an option to create fdo-like thumbnails;
 * have a client/server utility.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%{name}d
%_bindir/%{name}d_client
%_libexecdir/%{name}d_slave
%_libdir/%name/
%exclude %_libdir/%name/*/*.la
%_datadir/dbus-1/services/org.enlightenment.Ethumb.service
%_datadir/%name/

%files -n lib%name
%_libdir/lib%{name}*.so.*
%doc COPYING README

%files -n lib%name-devel
%_includedir/%{name}*/
%_libdir/lib%{name}*.so
%_pkgconfigdir/%{name}*.pc

%changelog
* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.1.65643-alt2
- used %%autoreconf to fix RPATH problem

* Tue Dec 06 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.1.65643-alt1
- first build for Sisyphus

