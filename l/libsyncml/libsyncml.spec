
Name: libsyncml
Version: 0.5.4
Release: alt2

Summary: Library providing support for the SyncML protocol
License: LGPL
Group: System/Libraries
URL:  http://libsyncml.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source0: %name-%version.tar
Source1: cmake.tar
Patch0: %name-%version-%release.patch

BuildRequires: cmake gcc-c++
BuildRequires: glib2-devel >= 2.12
BuildRequires: libopenobex-devel >= 1.1 libbluez-devel
BuildRequires: libsoup-devel  >= 2.3.0.1
BuildRequires: libwbxml2-devel >= 0.10.0
BuildRequires: libcheck-devel >= 0.9.6

%description
Libsyncml is a implementation of the SyncML protocol. It allows
syncronisation programs like OpenSync the synchronization of
SyncML-enabled devices, such as the SonyEricsson P800, as well as
remote OpenSync to OpenSync synchronization over the internet.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C
Requires: %name = %version
Requires: libopenobex-devel libsoup-devel libwbxml2-devel

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%prep
%setup -q
# %patch0 -p1
mkdir cmake
tar -xf %SOURCE1

%build
mkdir build
cd build
cmake \
	-D CMAKE_INSTALL_PREFIX:PATH=%_prefix \
	-D OPENSYNC_LIBEXEC_DIR=%_libexecdir/opensync-1.0 \
%if %{_lib} == lib64
	-D LIB_SUFFIX=64 \
%endif
	-D CMAKE_CXX_FLAGS:STRING="%optflags" \
	-D CMAKE_BUILD_TYPE="Release" \
	-D CMAKE_SKIP_RPATH:BOOL=TRUE ..

%make_build VERBOSE=1

%install
pushd build
%make_install install DESTDIR=%buildroot
popd

%__mkdir_p %buildroot%_man1dir
install tools/*.1 %buildroot%_man1dir/

%files
%_bindir/*
%_libdir/*.so.*
%doc AUTHORS
%_man1dir/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Mar 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5.4-alt2
- rebuild with bluez4

* Tue Sep 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Thu May 14 2009 Alexey Shabalin <shaba@altlinux.ru> 0.5.2-alt1.svn1083
- svn version r1083
- update BuildRequires

* Tue Jan 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- 0.4.6
- cmake build scheme

* Mon Jan 21 2008 Alexey Shabalin <shaba@altlinux.ru> 0.4.5-alt1
- 0.4.5

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.4.4-alt1
- 0.4.4
- add packager

* Mon Feb 12 2007 Alexey Shabalin <shaba@altlinux.ru> 0.4.3-alt2
- add Requires: libopenobex-devel libsoup-devel libwbxml2-devel for devel package

* Mon Feb 12 2007 Alexey Shabalin <shaba@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Wed Nov 08 2006 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Wed Oct 25 2006 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt2
- disable-unit-tests (for build x86_64)

* Mon Oct 09 2006 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- Initial package
