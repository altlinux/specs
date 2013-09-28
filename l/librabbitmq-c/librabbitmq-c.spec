Name:           librabbitmq-c
Version:        0.4.1
Release:        alt2
Summary:        This is a C-language AMQP client library for use with AMQP servers speaking protocol versions 0-9-1
Group:          System/Libraries
License:        MIT
URL:            https://github.com/alanxz/rabbitmq-c
Source:         %name-%version.tar

BuildRequires: python-module-json libpopt-devel xmlto cmake ctest libssl-devel doxygen

%description
This is a C-language AMQP client library for use with AMQP servers
speaking protocol versions 0-9-1.

%package	devel
Summary:        Development files for %name
Group:          System/Libraries
Requires:       pkgconfig, %name = %version-%release

%description   devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=NO \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
	-DBUILD_API_DOCS=ON \
	-DREGENERATE_AMQP_FRAMING:BOOL=ON

%cmake_build

%install
%cmakeinstall_std

%check
pushd BUILD
	ctest -VV
popd

%files
%doc AUTHORS CONTRIBUTING.md ChangeLog.md LICENSE-MIT README.md THANKS TODO
%_bindir/*
%_libdir/librabbitmq.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Fri Sep 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt2
- add test

* Fri Sep 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt1
- new version

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.0.1-alt1
- first build for ALT Linux
