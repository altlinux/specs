%define oname rem
Name: librem
Version: 0.5.2
Release: alt1

Summary: Library for real-time audio and video processing

License: BSD Revised
Group: System/Libraries
Url: http://www.creytiv.com/re.html


Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.creytiv.com/pub/%oname-%version.tar

# Automatically added by buildreq on Mon Sep 17 2012
BuildRequires: libre-devel libssl-devel zlib-devel

%description
Librem is a portable and generic library for real-time audio and video processing.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %oname-%version

%build
%make_build RELEASE=1

%install
%makeinstall_std LIBDIR=%_libdir
rm -f %buildroot%_libdir/lib%oname.a

%files
%doc docs/*
%_libdir/lib%oname.so

%files devel
%_includedir/%oname/
%_pkgconfigdir/*.pc

%changelog
* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Fri Nov 18 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.7-alt1
- 0.4.7

* Mon May 26 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Mon Sep 17 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- initial build for ALT Linux Sisyphus
