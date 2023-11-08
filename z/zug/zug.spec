Name: zug
Version: 0.1.1
Release: alt1

Group: System/Libraries
Summary: Transducers for C++
License: BSL-1.0
Url: https://sinusoid.es/zug/

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ boost-devel catch2-devel

%description
zug is a C++ library providing transducers. Transducers are composable
sequential transformations independent of the source. They can be used to
express algorithms over pull-based sequences (iterators, files) but also push
based sequences (signals, events, asynchronous streams) in a generic way.

%package devel
Group: Development/C++
Summary: Transducers for C++
%description devel
zug is a C++ library providing transducers. Transducers are composable
sequential transformations independent of the source. They can be used to
express algorithms over pull-based sequences (iterators, files) but also push
based sequences (signals, events, asynchronous streams) in a generic way.

%prep
%setup

%build
%cmake \
    -Dzug_BUILD_EXAMPLES=FALSE \
    -Dzug_BUILD_DOCS:BOOL=FALSE \
    #

%cmake_build

%install
%cmake_install

%files devel
%doc LICENSE README.rst
%_includedir/zug/
%_libdir/cmake/Zug/

%changelog
* Wed Nov 08 2023 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- initial build
