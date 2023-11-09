Name: lager
Version: 0.1.1
Release: alt1

Group: System/Libraries
Summary: C++ library to assist value-oriented design
Url: https://sinusoid.es/lager/
License: MIT

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ boost-devel boost-system-devel catch2-devel immer-devel zug-devel

%description
lager is a C++ library to assist value-oriented design by implementing the
unidirectional data-flow architecture. It is heavily inspired by Elm and Redux,
and enables composable designs by promoting the use of simple value types and
testable application logic via pure functions.

%package devel
Group: Development/C++
Summary: C++ library to assist value-oriented design
%description devel
lager is a C++ library to assist value-oriented design by implementing the
unidirectional data-flow architecture. It is heavily inspired by Elm and Redux,
and enables composable designs by promoting the use of simple value types and
testable application logic via pure functions.

%prep
%setup

%build
%cmake \
    -Dlager_BUILD_EXAMPLES:BOOL=FALSE \
    -Dlager_BUILD_DEBUGGER_EXAMPLES:BOOL=FALSE \
    -Dlager_BUILD_DOCS:BOOL=FALSE \
    #
%cmake_build

%install
%cmake_install

%files devel
%doc LICENSE README.rst
%_includedir/lager/
%_libdir/cmake/Lager/

%changelog
* Wed Nov 08 2023 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- initial build
