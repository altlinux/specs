Name: lksctp-tools
Summary: Linux Kernel SCTP tools
Version: 1.0.17
Release: alt2
License: GPL2
Group: System/Kernel and hardware
BuildRequires: glibc-devel-static
Url: http://lksctp.sourceforge.net/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%package -n liblksctp
Summary: Linux Kernel SCTP library
Group: System/Kernel and hardware

%description -n liblksctp
Linux Kernel SCTP library

%package -n liblksctp-devel
Summary: Linux Kernel SCTP library
Group: System/Kernel and hardware

%description -n liblksctp-devel
Linux Kernel SCTP library

%package -n liblksctp-devel-static
Summary: Linux Kernel SCTP library
Group: System/Kernel and hardware

%description -n liblksctp-devel-static
Linux Kernel SCTP library

%description
Linux Kernel SCTP tools


%prep
%setup
%patch -p1

%build
%autoreconf -fisv
%configure
%make_build

%install
mkdir -p %buildroot
%makeinstall install

%files
%_man3dir/*
%_bindir/*

%files -n liblksctp
%_libdir/*.so.*
%dir %_libdir/lksctp-tools
%_libdir/lksctp-tools/*.so.*

%files -n liblksctp-devel
%_libdir/*.so
%_libdir/lksctp-tools/*.so
%_libdir/lksctp-tools/*.la
%_man7dir/*
%_includedir/netinet/sctp.h
%_datadir/lksctp-tools
%_pkgconfigdir/*.pc

%files -n liblksctp-devel-static
%_libdir/*.a
%_libdir/lksctp-tools/*.a

%changelog
* Sat Apr 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.17-alt2
- NMU: fixed warning: Installed (but unpackaged) file(s) found:
- /usr/lib64/pkgconfig/libsctp.pc

* Tue May 10 2016 Cronbuild Service <cronbuild@altlinux.org> 1.0.17-alt1
- new version 1.0.17

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 1.0.16-alt1
- new version 1.0.16

* Wed May 15 2013 Cronbuild Service <cronbuild@altlinux.org> 1.0.15-alt1
- new version 1.0.15

* Fri Apr 12 2013 Denis Smirnov <mithraen@altlinux.ru> 1.0.14-alt1
- new version 1.0.14

* Fri Feb 01 2013 Denis Smirnov <mithraen@altlinux.ru> 1.0.13-alt2
- add gear-cronbuild support

* Fri Feb 01 2013 Denis Smirnov <mithraen@altlinux.ru> 1.0.13-alt1
- new version 1.0.13

* Mon Jan 09 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0.11-alt2
- fix build

* Fri Jul 08 2011 Denis Smirnov <mithraen@altlinux.ru> 1.0.11-alt1
- first build for Sisyphus

