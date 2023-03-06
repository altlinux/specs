%define _unpackaged_files_terminate_build 1

%global sover 4

Name: rabbitmq-c
Version: 0.13.0
Release: alt1

Summary: RabbitMQ C client
Group: System/Libraries
License: MIT
URL: https://github.com/alanxz/rabbitmq-c

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

Obsoletes: librabbitmq-c < %EVR

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ctest xmlto
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libssl-devel
BuildRequires: libpopt-devel

%description
This is a C-language AMQP client library for use with v2.0+ of the
RabbitMQ broker.

%package -n librabbitmq-c%sover
Summary: Libraries for %name
Group: System/Libraries
Provides: librabbitmq-c = %EVR
Conflicts: librabbitmq-c

%description -n librabbitmq-c%sover
%summary

%package -n librabbitmq-c-devel
Summary: Development files for %name
Group: System/Libraries
Requires: pkgconfig

%description -n librabbitmq-c-devel
%summary

%prep
%setup
%patch0 -p1

%build
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=NO \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
	-DBUILD_API_DOCS=ON \
	-DBUILD_TOOLS:BOOL=ON \
	-DBUILD_TOOLS_DOCS:BOOL=ON

%cmake_build

%install
%cmake_install
rm -f %buildroot%_libdir/*.a

%check
pushd %_cmake__builddir
	ctest -VV
popd

%files
%doc AUTHORS CONTRIBUTING.md ChangeLog.md LICENSE README.md THANKS
%_bindir/*
%_man1dir/*
%_man7dir/*

%files -n librabbitmq-c%sover
%_libdir/librabbitmq.so.*

%files -n librabbitmq-c-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_libdir/cmake

%changelog
* Tue Feb 07 2023 Egor Ignatov <egori@altlinux.org> 0.13.0-alt1
- 0.13.0

* Mon Apr 11 2022 Egor Ignatov <egori@altlinux.org> 0.11.0-alt5
- 1f6ff5e tools/common.c: die on failed rpc in make_connection

* Fri Apr 01 2022 Egor Ignatov <egori@altlinux.org> 0.11.0-alt4
- f54668b tools: multiple tries to make a connection

* Tue Jan 25 2022 Egor Ignatov <egori@altlinux.org> 0.11.0-alt3
- 49a0ba4 tools: print verbose error message when failed to open a socket
- f194b49 tools: enable ssl in connection_info if --ssl used with --server

* Fri Jan 21 2022 Egor Ignatov <egori@altlinux.org> 0.11.0-alt2
- Rename package: librabbitmq-c -> rabbitmq-c
- Split tools and libraries into different packages (Closes: #41742)

* Wed Jun 30 2021 Grigory Ustinov <grenka@altlinux.org> 0.11.0-alt1
- Build new version (Closes: #40331).

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.9.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Fri Mar 01 2019 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.5.2-alt1.git20140830.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20140830
- Version 0.5.2

* Fri Sep 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt2
- add test

* Fri Sep 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt1
- new version

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.0.1-alt1
- first build for ALT Linux
