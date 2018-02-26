
%define msn_sover 0.3
%define beta %nil
Name: libmsn
Version: 4.1
Release: alt2

Group: Development/C++
Summary: Reusable, open-source and fully documented library for MSN
Url: http://sourceforge.net/projects/libmsn
License: GPLv2+

Source: %name-%version%beta.tar.bz2
Patch1: libmsn-4.1-alt-fix-compile.patch

# Automatically added by buildreq on Mon Jan 19 2009 (-bi)
BuildRequires: cmake gcc-c++ libcom_err-devel libssl-devel

%description
Libmsn is a reusable, open-source, fully documented library for
connecting to Microsoft's MSN Messenger service.

%package -n libmsn%msn_sover
Summary: %name library
Group: System/Libraries
%description -n libmsn%msn_sover
%name library

%package test
Summary: Connection test utility
Group: Development/C++
%description test
Connection test utility.

%package devel
Summary: Devel stuff for %name
Group: Development/C++
Requires: libmsn%msn_sover = %version-%release
%description devel
Files needed to build applications based on %name.


%prep
%setup -q -n %name-%version%beta
%patch1 -p1


%build
mkdir -p build
pushd build
cmake ../ \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
%ifarch x86_64
        -DLIB_SUFFIX=64 \
%endif		
	-DCMAKE_SKIP_RPATH=YES \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_BUILD_TYPE="Release" \
	-DENABLE_INOTIFY:BOOL=ON \
	-DENABLE_DBUS:BOOL=ON
popd
%make_build -C build VERBOSE=1


%install
%make -C build install DESTDIR=%buildroot


%files -n libmsn%msn_sover
%_libdir/libmsn.so.%{msn_sover}*

%files test
%_bindir/*

%files devel
%doc doc/html doc/OVERVIEW README THANKS TODO
%_libdir/pkgconfig/*
%_includedir/msn
%_libdir/libmsn.so

%changelog
* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.1-alt2
- rebuilt with new ssl

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.1-alt0.M51.1
- build for M51

* Fri Apr 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.1-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.0-alt1
- 4.0 release

* Mon Jan 19 2009 Sergey V Turchin <zerg at altlinux dot org> 4.0-alt0.1
- 4.0-beta2
- initial specfile
