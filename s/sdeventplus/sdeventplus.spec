Name:    sdeventplus
Version: 0.1
Release: alt2.git18db9a3

Summary: A c++ wrapper around the systemd sd_event apis meant to provide c++ ergonomics to their usage
License: Apache-2.0
Group:   Development/Other
Url:     https://www.openbmc.org
Vcs:     https://github.com/openbmc/sdeventplus.git

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(stdplus)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(sdbusplus)
BuildRequires: function2-devel

%description
%summary

%package -n lib%name
Group:   Development/Other
Summary: %summary

%description -n lib%name
A C++ wrapper library around the systemd sd_event apis meant to provide
C++ ergonomics to their usage.

%package -n lib%name-devel
Group:   Development/Other
Summary: %summary

%description -n lib%name-devel
A C++ development files around the systemd sd_event apis meant to provide
C++ ergonomics to their usage.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%doc *.md
%_libdir/lib%name.so
%_includedir/%name
%_pkgconfigdir/%name.pc

%changelog
* Tue Aug 26 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1-alt2.git18db9a3
- NMU: Downgraded to commit from revision list.

* Thu Apr 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.1-alt1
- Initial build for Sisyphus.
