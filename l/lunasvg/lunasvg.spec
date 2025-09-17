Name:           lunasvg
Version:        3.5.0
Release:        alt1
Summary:        Standalone SVG rendering library in C++
Group:          System/Libraries
License:        MIT
URL:            https://github.com/sammycage/lunasvg
Source0:        %name-%version.tar.gz

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  libstb-devel
BuildRequires:  libplutovg-devel

%description
LunaSVG is a standalone SVG rendering library in C++.

%package        devel
Group:          System/Libraries
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development headers and libraries for %{name}.

%prep
%setup -q

%build

%cmake \
  -DLUNASVG_LIBDIR="%_libdir" \
  -DLUNASVG_BUILD_EXAMPLES=ON \
  -DUSE_SYSTEM_PLUTOVG=ON \
  -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md LICENSE
%_libdir/lib%name.so.3

%files devel
%_includedir/%name/%name.h
%_libdir/lib%name.so
%_libdir/cmake/%name
%_pkgconfigdir/%name.pc

%changelog
* Tue Sep 16 2025 Artyom Bystrov <arbars@altlinux.org> 3.5.0-alt1
- Initial commit for Sisyphus