
Name: mysql-connector-net
Version: 6.4.3
Release: alt2

Summary: fully-managed ADO.NET driver written in pure C#
License: GPL
Group: Databases

# bzr branch lp:connectornet
# git bzr add upstream ../mysql-connector-net.bzr/connectornet/
# git bzr fetch upstream

Url: http://www.mysql.com/products/connector/net/5.1.html
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

Source: %name-%version.tar
Source2: MySql.Data.source
Source3: mysql-connector-net.pc

Patch1: %name-%version-alt-build-doc.patch

BuildPreReq: /proc
BuildRequires: mono-devel mono-mcs rpm-build-mono monodoc

%description
Connector/Net lets you easily develop .NET applications that require secure,
high-performance data connectivity with MySQL.
It implements the required ADO.NET interfaces and integrates into ADO.NET aware tools.
Developers can build applications using their choice of .NET languages.
Connector/Net is a fully managed ADO.NET driver written in 100% pure C#.

Connector/Net includes full support for:
 - Features provided by MySQL Server up to and including MySQL Server version 5.5.
 - Large-packet support for sending and receiving rows and BLOBs up to 2 gigabytes in size.
 - Protocol compression, which enables compressing the data stream between the client and server.
 - Connections using TCP/IP sockets, named pipes, or shared memory on Windows.
 - Connections using TCP/IP sockets or Unix sockets on Unix.
 - The Open Source Mono framework developed by Novell.
 - Fully managed, does not utilize the MySQL client library.

%package devel
Summary: Development files %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

%package doc
Summary: Development documentation for %name
Group: Documentation
Provides: %name-monodoc = %version-%release
BuildPreReq: monodoc-devel
Requires: monodoc
BuildArch: noarch

%description doc
This package contains the API documentation for %name in
Monodoc format.

%prep
%setup
%patch1 -p1

%build
# compile & sign lib
xbuild Source/MySql.Data/MySql.Data.csproj

# build API docs
mdoc update \
	-i Source/MySql.Data/MySql.Data.xml \
	-o Source/MySql.Data/bin/Debug/monodocer \
	Source/MySql.Data/bin/Debug/MySql.Data.dll

cd Source/MySql.Data/bin/Debug
mdoc assemble -o MySql.Data monodocer

%install
gacutil -f -package MySql.Data -i Source/MySql.Data/bin/Debug/MySql.Data.dll -root %buildroot/usr/lib

# install doc
mkdir -p %buildroot%_monodocdir
cp Source/MySql.Data/bin/Debug/MySql.Data.tree %buildroot%_monodocdir/
cp Source/MySql.Data/bin/Debug/MySql.Data.zip %buildroot%_monodocdir/
cp %SOURCE2 %buildroot%_monodocdir/

# install pkgconfig file
mkdir -p %buildroot%_pkgconfigdir
cp %SOURCE3 %buildroot%_pkgconfigdir/mysql-connector-net.pc
subst "s/#VERSION#/%version/" %buildroot%_pkgconfigdir/mysql-connector-net.pc

%files
%_monodir/*/MySql.Data.dll
%_monogacdir/*
%doc CHANGES README

%files devel
%_pkgconfigdir/*

%files doc
%_monodocdir/*

%changelog
* Mon Feb 20 2012 Alexey Shabalin <shaba@altlinux.ru> 6.4.3-alt2
- add devel package with pkgconfig file

* Mon Feb 20 2012 Alexey Shabalin <shaba@altlinux.ru> 6.4.3-alt1
- upstream snapshot from lp:connectornet
- add monodoc package

* Fri Jan 11 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 5.1.4-alt1.svn.1150
- 5.1.4 svn rev 1150

* Tue May 15 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 5.0.7-alt1.svn.723
- Initial build for Sisyphus
