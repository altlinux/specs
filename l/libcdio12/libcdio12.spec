%define _name libcdio
%define soname 12

Name: %_name%soname
Version: 0.82
Release: alt3

Summary: CD-ROM/CD-image access library
License: GPLv3+
Group: System/Libraries
Url: http://www.gnu.org/software/%_name/


# ftp://ftp.gnu.org/gnu/libcdio/%_name-%version.tar.gz
Source: %_name-%version.tar
# git://git.altlinux.org/gears/l/libcdio.git
Patch: %_name-0.82-alt-build.patch

BuildRequires: gcc-c++ libcddb-devel libncurses-devel makeinfo

%description
This library is to encapsulate CD-ROM reading and control. Applications
wishing to be oblivious of the OS- and device-dependant properties of a
CD-ROM can use this library.

%package -n libcdio%{soname}++
Summary: C++ wrappers to the CD-ROM/CD-image access library
Group: System/Libraries
Requires: %name = %version-%release

%description -n libcdio%{soname}++
These C++ libraries provide object-oriented wrappers to the libcdio APIs.

%prep
%setup -n %_name-%version
%patch -p1
# don't build broken and usless info-pages
subst 's|\(SUBDIRS = \)doc|\1|' Makefile.am

%build
%autoreconf
%configure \
	--enable-maintainer-mode \
	--disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README NEWS THANKS TODO
%_libdir/*.so.*
%exclude %_libdir/libudf.so.*
%exclude %_libdir/*++.so.*

%files -n libcdio%{soname}++
%_libdir/*++.so.*


%changelog
* Sun Jan 24 2016 Yuri N. Sedunov <aris@altlinux.org> 0.82-alt3
- fixed buildreqs

* Mon Aug 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.82-alt2
- exclude libudf

* Mon Aug 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.82-alt1
- compat libraries without -devel packages

