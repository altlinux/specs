%def_with static

Name: hwinfo
%define lname lib%name
Version: 18.5
Release: alt3
Summary: Hardware detection tool
License: GPL2
Group: System/Kernel and hardware
URL: http://download.opensuse.org/source/factory/repo/oss/suse/src
# http://download.opensuse.org/source/factory/repo/oss/suse/src/%name-%version-2.1.src.rpm
Source: %name-%version.tar
Patch0: %name-14.19-kbd.c-tiocgdev_undefined.patch
Patch1: %name-13.57-as-needed.patch
Patch2: %name-14.19-makefile.patch
Patch3: %name-14.19-alt.patch
Patch4: %name-alt-no-hal.patch
Requires: %lname = %version-%release
Packager: Fr. Br. George <george@altlinux.ru>
# Automatically added by buildreq on Thu Sep 25 2008 (-bi)
BuildRequires: doxygen flex perl-XML-Parser perl-XML-Writer perl-devel
BuildRequires: rpm-build-licenses

BuildPreReq: libdbus-devel libx86emu-devel

%description
A simple program that lists results from the hardware detection
library.


%package utils
Summary: Hardware Detection utils
Group: System/Kernel and hardware

%description utils
Hardware Detection utils.


%package -n %lname
Summary: Hardware Detection library
Group: System/Libraries
Provides: libhd = %version-%release

%description -n %lname
This library collects information about the hardware installed on a
system.


%package -n %lname-doc
Summary: Documentation for Hardware Detection library
Group: Documentation
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description -n %lname-doc
Documentation for Hardware Detection library.


%package -n %lname-devel
Summary: Hardware Detection library (development files)
Group: Development/C
Obsoletes: %name-devel < %version-%release
Provides: %name-devel = %version-%release
Provides: libhddev
Requires: %lname = %version-%release

%description -n %lname-devel
Development files for %lname.


%if_with static
%package -n %lname-devel-static
Summary: Hardware Detection static library
Group: Development/C
Requires: %lname-devel = %version-%release
Conflicts: %name-devel < %version-%release

%description -n %lname-devel-static
This static library collects information about the hardware installed
on a system.
%endif


%prep
%setup
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p2


%build
%make RPM_OPT_FLAGS="%optflags"
%make_build doc
bzip2 --best --keep --force changelog


%install
%make DESTDIR=%buildroot LIBDIR=%_libdir install
install -d -m 0755 %buildroot{%_man8dir,%_docdir/%lname-%version/html,%_localstatedir/hardware/udi}
install -m 0644 doc/*.8 %buildroot%_man8dir/
install -m 0644 doc/libhd/html/* %buildroot%_docdir/%lname-%version/html/
%{?_with_static:install -m 0644 src/lib*.a %buildroot%_libdir/}


%files
%doc changelog.* README
%_sbindir/%name
%_man8dir/*


%files utils
%_sbindir/getsysinfo
%_sbindir/mk_isdnhwdb
%_sbindir/check_hd
%_sbindir/convert_hd


%files -n %lname
%_libdir/*.so.*
%dir %_localstatedir/hardware
%dir %_localstatedir/hardware/udi
%_datadir/%name


%files -n %lname-devel
%_libdir/*.so
%_pkgconfigdir/*
%_includedir/*


%files -n %lname-doc
%_docdir/%lname-%version/html


%if_with static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%changelog
* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 18.5-alt3
- %name-utils: avoid requirement on hal

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 18.5-alt2
- Rebuilt as hwinfo

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 18.5-alt1
- Version 18.5 (new soname version)
- Built without hal

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.26-alt1.1
- Rebuilt for soname set-versions

* Mon Mar 30 2009 Fr. Br. George <george@altlinux.ru> 15.26-alt1
- Version up
- Upstream locateion is moved

* Thu Sep 25 2008 Fr. Br. George <george@altlinux.ru> 14.19-alt1
- Changes via led@:
-   clean up spec
+   %name-14.19-makefile.patch
+   %name-14.19-alt.patch
-   group fix
-   update %name-14.19-kbd.c-tiocgdev_undefined.patch

* Sun May 25 2008 Fr. Br. George <george@altlinux.ru> 13.57-alt2
- #14572 fixed

* Fri Oct 12 2007 Fr. Br. George <george@altlinux.ru> 13.57-alt1
- Initial ALT build (Open SUSE hwinfo-13.57-2)
- MDV patch applied

