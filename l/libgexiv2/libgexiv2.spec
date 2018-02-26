Name: libgexiv2
Version: 0.4.1
Release: alt1
Summary: GObject-based Exiv2 wrapper

Group: System/Libraries
License: GPL2
Url: http://trac.yorba.org/wiki/gexiv2

# Cloned from git://yorba.org/gexiv2
Source: %name-%version.tar

BuildRequires: libexiv2-devel glib2-devel gcc-c++ gcc-fortran libgio-devel

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

%package devel
Group: Development/C
Requires: %name = %version
Summary: GObject-based Exiv2 wrapper - development files
%description devel
%summary

%prep
%setup -q

%build
./configure --prefix=%_usr
%make_build

%install
%makeinstall_std LIB=%_lib

%files
%_libdir/%name.so.*
%doc AUTHORS COPYING README THANKS

%files devel
%_includedir/gexiv2
%_libdir/%name.so
%_pkgconfigdir/gexiv2.pc
%_datadir/vala/vapi/gexiv2.vapi

%changelog
* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.4.1-alt1
- New version 0.4.1

* Thu Nov 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.3.1-alt1
- New version 0.3.1

* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2.2-alt1
- New version 0.2.2

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.1-alt1
- New version 0.2.1

* Tue Jul 27 2010 Vladimir Lettiev <crux@altlinux.ru> 0.1.0-alt1
- initial build

