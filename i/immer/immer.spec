Name: immer
Version: 0.8.1
Release: alt1

Group: System/Libraries
Summary: Persistent and immutable data structures written in C++
Url: https://sinusoid.es/immer/
License: BSL-1.0

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++ boost-devel libgc-devel catch2-devel

%description
immer is a library of persistent and immutable data structures written in C++.
These enable whole new kinds of architectures for interactive and concurrent
programs.

%package devel
Group: Development/C++
Summary: Persistent and immutable data structures written in C++
%description devel
immer is a library of persistent and immutable data structures written in C++.
These enable whole new kinds of architectures for interactive and concurrent
programs.

%prep
%setup

%build
%cmake \
    -DDISABLE_WERROR:BOOL=TRUE \
    -Dimmer_BUILD_DOCS:BOOL=FALSE \
    -Dimmer_BUILD_EXAMPLES:BOOL=FALSE \
    -Dimmer_BUILD_EXTRAS:BOOL=FALSE \
    #

%cmake_build

%install
%cmake_install

%files devel
%doc LICENSE README.rst
%_includedir/immer/
%_libdir/cmake/Immer/

%changelog
* Wed Nov 08 2023 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt1
- initial build
