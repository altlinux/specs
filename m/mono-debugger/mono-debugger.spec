%def_with xsp

Name: mono-debugger
Version: 2.10
Release: alt1
License: %mit
URL: http://www.go-mono.com/
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Summary: A debugger for Mono
Source:	http://go-mono.com/sources/mono-debugger/%name-%version.tar

Patch1: %name-%version-alt-cecil.patch
Patch2: %name-%version-alt-fixes.patch
Patch3: %name-%version-alt-termcap.patch

BuildPreReq: rpm-build-licenses rpm-build-mono
BuildRequires: /proc

BuildPreReq: mono-devel >= 2.8 libmono-devel >= 2.8
BuildPreReq: glib2-devel >= 2.0.0
BuildPreReq: mono-nunit-devel
%{?_with_xsp:BuildPreReq: xsp-devel >= 2.8}
BuildRequires: libtinfo-devel mono-mcs mono-web-devel monodis

%description
A debugger is an important tool for development. The Mono
Debugger (MDB) can debug both managed and unmanaged applications.
It provides a reusable library that can be used to add debugger
functionality to different frontends. The debugger package
includes a console debugger named "mdb", and MonoDevelop
provides a GUI interface to the debugger.

%package devel
Summary: Development tools and headers for mono-debugger
Group: Development/Other
Requires: %name = %version-%release

%description devel
Libraries and header files for developing against mono-debugger.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure \
	%{?_with_xsp:--with-xsp} \
	--disable-static \
	--disable-dependency-tracking \

%make

%install
%make_install DESTDIR=%buildroot install
# install -m 644 build/mdb.exe.config %buildroot%_monodir/2.0/

%files
%doc AUTHORS README NEWS ChangeLog
%_bindir/*
%_monodir/%name
%_monodir/2.0/*.exe*
%_monogacdir/*

# lib
%_libdir/*.so.*

%files devel
#for devel
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Feb 09 2012 Alexey Shabalin <shaba@altlinux.ru> 2.10-alt1
- 2.10

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 2.6.3-alt2
- fix buildreq

* Wed Mar 17 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Wed Dec 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6-alt1
- 2.6

* Mon Dec 14 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Tue Aug 18 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2.1-alt2
- fix buildreq

* Tue Jul 07 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2.1-alt1
- 2.4.2.1
- add devel package

* Wed Jul 01 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Mon Apr 13 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4

* Fri Jan 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2
- removed obsolete pre/post macros

* Tue Oct 07 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0 release

* Fri Sep 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.rc1
- 2.0 RC1

* Tue Aug 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.pre1
- 2.0 preview1

* Wed Jul 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.60-alt2
- fix build (patch4)

* Wed Jan 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.60-alt1
- initial package for ALTLinux

