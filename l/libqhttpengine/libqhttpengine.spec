%define soversion 1
%define oname qhttpengine

Name: libqhttpengine
Version: 1.0.1
Release: alt3
Summary: HTTP server for Qt applications

Group: System/Libraries
License: MIT
Url: https://github.com/nitroshare/qhttpengine
Vcs: https://github.com/nitroshare/qhttpengine

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: libssl-devel
BuildRequires: python3-dev
BuildRequires: qt5-base-devel

%{?!_without_check:%{?!_disable_check:BuildRequires: ctest}}

%description
Simple set of classes for developing HTTP server applications in Qt.

%package -n libqhttpengine%soversion
Summary: Library for multicast DNS as per RFC 676
Group: System/Libraries
Obsoletes: libqhttpengine < 1.0.1

%description -n libqhttpengine%soversion
Simple set of classes for developing HTTP server applications in Qt.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: libqhttpengine%soversion = %EVR

%description devel
HTTP server for Qt applications.
This package contains the development files.

%prep
%setup

%build
%cmake -DBUILD_DOC=ON -DBUILD_TESTS=ON
%cmake_build

%check
pushd %_cmake__builddir
%make_build test
popd

%install
%cmakeinstall_std
# Non-standard path of installing docs in ALT
rm -rv %buildroot%_datadir/doc/%oname

%files -n libqhttpengine%soversion
%_libdir/libqhttpengine.so.%{soversion}*

%files devel
%doc LICENSE.txt examples/ %_cmake__builddir/doc/html/
%_includedir/%oname
%_libdir/cmake/%oname
%_libdir/libqhttpengine.so
%_libdir/pkgconfig/%oname.pc

%changelog
* Wed Sep 24 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0.1-alt3
- fixed FTBFS
- moved docs to the devel package
- enabled check

* Mon Oct 19 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2
- NMU: proper shared libs policy (closes: #38976)

* Tue Sep 22 2020 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt1
- 1.0.1 & build according to shared libs policy (altbug #38976)

* Sun Sep 20 2020 Motsyo Gennadi <drool@altlinux.ru> 1.0.0-alt1
- initial build
