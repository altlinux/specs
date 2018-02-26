%def_enable static
%def_with vbetest

Name: lrmi
Version: 0.10
Release: alt4

Summary: Linux Real Mode Interface
License: Public domain
Group: System/Libraries

Url: http://sourceforge.net/projects/lrmi
Source: %name-%version.tar
Patch0: %name-0.10-link.patch
Patch1: %name-0.10-linux-defs.patch

ExclusiveArch: %ix86

%define lname lib%name

%description
Linux Real Mode Interface library provides a DPMI like interface under
Linux and *BSD systems using vm86.
%if_with vbetest
There is also a VBE (VESA Bios Extension) interface utility called
vbetest.
%endif

%package -n %lname
Summary: Linux Real Mode Interface library
Group: System/Libraries
Provides: %name = %version-%release

%description -n %lname
Linux Real Mode Interface library provides a DPMI like interface under
Linux and *BSD systems using vm86.

%package -n %lname-devel
Summary: Linux Real Mode Interface library header
Group: Development/C
Requires: %lname = %version-%release

%description -n %lname-devel
Linux Real Mode Interface library provides a DPMI like interface under
Linux and *BSD systems using vm86.
This package contains header file for development with %lname.

%if_enabled static
%package -n %lname-devel-static
Summary: Linux Real Mode Interface static library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
Linux Real Mode Interface library provides a DPMI like interface under
Linux and *BSD systems using vm86.
This package contains static library for development with %lname.
%endif

%if_with vbetest
%package -n vbetest
Summary: VBE interface utility
Group: System/Configuration/Hardware
Requires: %lname = %version

%description -n vbetest
VBE (VESA Bios Extension) interface utility.
%endif

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%add_optflags %optflags_shared
%make_build CFLAGS="%optflags" CC=%__cc %lname.so %{?_enable_static:%lname.a} %{?_with_vbetest:vbetest}

%install
install -pdm0755 %buildroot{%_libdir,%_includedir}
install -pm0644 %lname.so.0.* %{?_enable_static:%lname.a} %buildroot%_libdir/
ln -sf %lname.so.0 %buildroot%_libdir/%lname.so
install -pm0644 %name.h %buildroot%_includedir/
%{?_with_vbetest:install -pDm0755 {,%buildroot%_sbindir/}vbetest}

%files -n %lname
%doc README
%_libdir/*.so.*

%files -n %lname-devel
%_includedir/*
%_libdir/*.so

%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif

%if_with vbetest
%files -n vbetest
%_sbindir/*
%endif

%changelog
* Sun Jan 08 2012 Michael Shigorin <mike@altlinux.org> 0.10-alt4
- rebuilt for Sisyphus (thx Speccyfighter for the reminder)

* Tue Sep 16 2008 Led <led@altlinux.ru> 0.10-alt3
- added:
  + %name-0.10-link.patch
  + %name-0.10-linux-defs.patch

* Fri Jul 14 2006 Led <led@altlinux.ru> 0.10-alt2
- removed x86_64 from ExclusiveArch

* Thu Jul 13 2006 Led <led@altlinux.ru> 0.10-alt1
- initial build
