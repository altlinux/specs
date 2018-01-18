%define _name libcdio
%define soname 16

Name: %_name%soname
Version: 0.94
Release: alt2

Summary: CD-ROM/CD-image access library
License: GPLv3+
Group: System/Libraries
Url: http://www.gnu.org/software/%_name/

Source: ftp://ftp.gnu.org/gnu/%_name/%_name-%version.tar.gz

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
* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 0.94-alt2
- compat libcdio libraries
