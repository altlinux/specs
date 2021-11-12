%define sover 157

Name: libplacebo
Version: 4.157.0
Release: alt0.1
Summary: libplacebo is essentially the core rendering algorithms and ideas of mpv turned into a library
Group: System/Libraries
License: LGPL-2.1+
Url: https://github.com/haasn/libplacebo
Source0: %url/%name/archive/v%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: glslang-devel libspirv-tools-devel libvulkan-devel python3-module-mako libepoxy-devel liblcms2-devel gcc-c++

%description
libplacebo is essentially the core rendering algorithms and ideas of mpv turned
into a library.

%package -n %{name}%{sover}
Summary: %name is essentially the core rendering algorithms and ideas of mpv turned into a library
Group: System/Libraries

%description -n %{name}%{sover}
libplacebo is essentially the core rendering algorithms and ideas of mpv turned
into a library.

%package -n %name-devel
Summary: Development files for %name
Group: Development/C
Requires: %{name}%{sover} = %EVR

%description -n %name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
%meson

%install
%meson_install

%files -n %{name}%{sover}
%_libdir/%name.so.%{sover}

%files -n %name-devel
%_includedir/*
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Fri Nov 12 2021 L.A. Kostis <lakostis@altlinux.ru> 4.157.0-alt0.1
- v4.157.0.
- Update soname.

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 3.120.1-alt0.1
- v3.120.1.

* Mon Jul 20 2020 L.A. Kostis <lakostis@altlinux.ru> 2.88.0-alt0.1
- Initial build for ALTLinux.

