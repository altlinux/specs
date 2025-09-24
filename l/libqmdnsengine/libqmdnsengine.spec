%define oname qmdnsengine

# The project has a correct soname, which has a value of 0. However,
# the previous maintainer specified the ABI version as 1. In order
# not to break the package maintenance style, we will add marcos abiversion.
%define abiversion 1
%define soversion 0

Name: libqmdnsengine
Version: 0.2.1
Release: alt1

Summary: Library for multicast DNS as per RFC 676
Group: System/Libraries
License: MIT
Url: https://github.com/nitroshare/qmdnsengine
Vcs: https://github.com/nitroshare/qmdnsengine

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: libssl-devel
BuildRequires: python3-dev
BuildRequires: qt5-base-devel

%{?!_without_check:%{?!_disable_check:BuildRequires: ctest}}

%description
This library provides an implementation of multicast DNS as per [RFC 6762]

%package -n libqmdnsengine%abiversion
Summary: Library for multicast DNS as per RFC 676
Group: System/Libraries
Obsoletes: libqmdnsengine < 0.2.0

%description -n libqmdnsengine%abiversion
This library provides an implementation of multicast DNS as per [RFC 6762]

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: libqmdnsengine%abiversion = %EVR

%description devel
Library for multicast DNS as per RFC 676.
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

%files -n libqmdnsengine%abiversion
%_libdir/libqmdnsengine.so.%{soversion}*

%files devel
%doc LICENSE.txt examples/ %_cmake__builddir/doc/html/
%_includedir/%oname
%_libdir/cmake/%oname/
%_libdir/libqmdnsengine.so

%changelog
* Wed Sep 24 2025 Ulysses Apokin <ulysses@altlinux.org> 0.2.1-alt1
- 0.2.1
- fixed FTBFS
- moved docs to the devel package
- enabled check

* Tue Sep 22 2020 Motsyo Gennadi <drool@altlinux.ru> 0.2.0-alt1
- 0.2.0
- build according to shared libs policy

* Sun Sep 20 2020 Motsyo Gennadi <drool@altlinux.ru> 0.1.0-alt1
- initial build
