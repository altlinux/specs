Name: lksctp-tools
Summary: Linux Kernel SCTP tools
Version: 1.0.11
Release: alt2
License: GPL2
Group: System/Kernel and hardware
BuildRequires: glibc-devel-static rpm-build-ruby
Source: %name-%version.tar

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
%_man7dir/*
%_includedir/netinet/sctp.h
%_datadir/lksctp-tools

%files -n liblksctp-devel-static
%_libdir/*.a
%_libdir/lksctp-tools/*.a

%changelog
* Mon Jan 09 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0.11-alt2
- fix build

* Fri Jul 08 2011 Denis Smirnov <mithraen@altlinux.ru> 1.0.11-alt1
- first build for Sisyphus

