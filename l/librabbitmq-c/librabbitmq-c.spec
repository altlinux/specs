Name:           librabbitmq-c
Version:        0.5.2
Release:        alt1.git20140830
Summary:        This is a C-language AMQP client library for use with AMQP servers speaking protocol versions 0-9-1
Group:          System/Libraries
License:        MIT
URL:            https://github.com/alanxz/rabbitmq-c
# https://github.com/alanxz/rabbitmq-c.git
Source:         %name-%version.tar
# https://github.com/rabbitmq/rabbitmq-codegen.git
Source1:				codegen.tar

BuildRequires: python-module-json libpopt-devel xmlto cmake ctest libssl-devel doxygen
BuildPreReq: graphviz

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
%setup
tar -xf %SOURCE1

%build
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=NO \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
	-DBUILD_API_DOCS=ON \
	-DREGENERATE_AMQP_FRAMING:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DBUILD_TOOLS_DOCS:BOOL=ON

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
%_man1dir/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_man7dir/*

%changelog
* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20140830
- Version 0.5.2

* Fri Sep 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt2
- add test

* Fri Sep 27 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt1
- new version

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.0.1-alt1
- first build for ALT Linux
