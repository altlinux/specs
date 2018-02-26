%define orig_name libopensync-plugin-palm
Name: libopensync0-plugin-palm
Version: 0.22
Release: alt2

Summary: Palm plugin for OpenSync
License: GPL
Group: System/Libraries
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %orig_name-%version.tar.bz2

Requires: libpilot-link
Requires: libopensync0 = %version
# Conflicts: %orig_name

# Automatically added by buildreq on Thu Oct 16 2008
BuildRequires: gcc-c++ gcc-fortran glib2-devel glibc-devel-static libopensync0-devel libpilot-link-devel libxml2-devel

%description
This plugin allows applications using OpenSync to synchronise to and from
Palm based devices.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: System/Libraries
Requires: %name = %version

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.


%prep
%setup -q -n %orig_name-%version

%build
%configure
%make

%install
%makeinstall install DESTDIR=%buildroot
rm -f %buildroot%_libdir/opensync/plugins/*.la
rm -f %buildroot%_libdir/opensync/formats/*.la

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_libdir/opensync/plugins/*.so
%_libdir/opensync/formats/*.so
%_datadir/opensync/defaults/*

%files devel
%_includedir/opensync-1.0/opensync/*.h


%changelog
* Thu Oct 16 2008 Andriy Stepanov <stanv@altlinux.ru> 0.22-alt2
- Stable version.

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.22-alt1
- 0.22

* Mon Feb 12 2007 Alexey Shabalin <shaba@altlinux.ru> 0.21-alt1
- 0.21
- cleanup spec(drop cvs)

* Wed Nov 08 2006 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- release 0.20

* Tue Oct 03 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt2
- release 0.19

* Thu Sep 21 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1cvs20060921
- svn version 20060921
- add package devel 

* Mon May 29 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt3cvs20060529
- svn version 20060529

* Tue Nov 22 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt1
- 0.18 release
- build for Sisyphus
- add Packager SynCE Development Team

* Fri Sep 30 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt0.1.cvs20050930
- Initial package
