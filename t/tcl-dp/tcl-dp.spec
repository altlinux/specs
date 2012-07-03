%def_without test

%define teaname dp
%define teaversion 40
%define teasubversion b2

Name: tcl-dp
Version: 4.0b2
Release: alt1

Summary: The package provides UDP, TCP, IP-multicast, and RPC for Tcl
Summary(ru_RU.UTF-8): Пакет, добавляет возможности UDP, TCP, IP-multicast и RPC к языку Tcl
License: Specific, see LICINSE
Group: Development/Tcl
Url: http://www.ncnr.nist.gov/xtal/software/tclpkgs82linux.html
Packager: Malo Skryleve <malo@altlinux.org>

Source: %name-%version.tar.bz2
Patch: tcl-dp-4.0b2-alt1-fix-includes.patch
Patch1: tcl-dp-4.0b2-alt1-remove-tcphassockets.patch
Patch2: tcl-dp-4.0b2-alt1-fix-tcl-version-check.patch
Patch3: tcl-dp-4.0b2-alt1-fix-configure.patch
Patch4: tcl-dp-4.0b2-alt1-fix-syntax.patch
Patch5: tcl-dp-4.0b2-alt1-remove-bad-tests.patch
Patch6: tcl-dp-4.0b2-alt1-fix-serial-module.patch
Patch7: tcl-dp-4.0b2-alt1-pkgindex.patch

BuildPreReq: rpm-build-tcl
BuildRequires: tcl-devel
Requires: tcl >= 8.0 tcl <= 9.0

%description
This package contains a freely distributable extension to Tcl/Tk
called Tcl Distributed Programming (Tcl-DP).  Tcl-DP adds TCP, UDP, and
IP-multicast connection management, remote procedure call (RPC), and
distributed object protocols to Tcl/Tk.  A C interface to the RPC
primitives is also provided.

%description -l ru_RU.UTF-8
Пакет называется Распределённое программрование в Tcl(Tcl-DP) и содержит
свободно распространяеое дополение к среде Tcl/Tk. Он добавляет
протоколы UDP, TCP, управление соединениями IP-multicast, вызов
удалённых процедур (RPC) и распределённых объектов к среде Tcl/Tk. Также
даются примеры доступа к RPC используя интерфейсы языка C.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%teapatch
sed 's,@lib@,%_lib,' -i tekilib/pkgIndex.tcl

%build
%define _configure_script unix/configure
%configure --with-tcl=%_tcldatadir/tcl8 --enable-shared
%make
%if_with test
%make tests TCLSH_ENV='LD_LIBRARY_PATH=unix'
%endif

%install
%define pkg_dir %buildroot%_tcldatadir/%teaname%teaversion%teasubversion
mkdir -p %buildroot%_tcllibdir %buildroot%_docdir \
	%pkg_dir/library %pkg_dir/api \
	%pkg_dir/examples/conference/ \
	%pkg_dir/examples/ftp/ \
	%pkg_dir/examples/tictactoe/ \
	%pkg_dir/examples/whiteboard/
install -p -m0644 library/*.tcl %pkg_dir/library/
install -p -m0644 api/* %pkg_dir/api/
install -p -m0644 examples/conference/* %pkg_dir/examples/conference/
install -p -m0644 examples/ftp/* %pkg_dir/examples/ftp/
install -p -m0644 examples/tictactoe/* %pkg_dir/examples/tictactoe/
install -p -m0644 examples/whiteboard/* %pkg_dir/examples/whiteboard/
install *.so %buildroot%_tcllibdir/
install tekilib/pkgIndex.tcl %pkg_dir/

%files
%doc CHANGES LICENSE FAQ README TODO doc/
%_tcldatadir/*
%_tcllibdir/lib%teaname%teaversion.so

%changelog
* Sun Feb 13 2011 Malo Skryleve <malo@altlinux.org> 4.0b2-alt1
- initial build for ALT Linux Sisyphus

