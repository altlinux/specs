%define _name girara
%define gtk_ver 2

Name: lib%_name
Version: 0.1.3
Release: alt1

Summary: GTK-based minimalistic user interface library
License: %bsdstyle
Group: System/Libraries
URL: http://pwmt.org/projects/girara
# git://pwmt.org/girara.git
Source: %name-%version.tar

Patch: %_name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgtk+%{gtk_ver}-devel
BuildRequires: intltool

%description
girara is a library that implements a user interface that focuses on
simplicity and minimalism.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libgtk+%{gtk_ver}-devel

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
export CFLAGS="%optflags"
%make_build VERBOSE=1 PREFIX=%prefix LIBDIR=%_libdir GIRARA_GTK_VERSION=%gtk_ver

%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_libdir
%find_lang %name-gtk%gtk_ver-1

%files -f %name-gtk%gtk_ver-1.lang
%doc AUTHORS README
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%exclude %_libdir/*.a

%changelog
* Wed Jun 13 2012 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- Updated to 0.1.3.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.

* Thu Mar 15 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Initial build.

