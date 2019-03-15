Name: wf-config
Version: 0.1
Release: alt1

Summary: A library for managing wayfire configuration files

License: MIT
Group: System/Configuration/Other
Url: https://github.com/WayfireWM/wf-config

Source: %name-%version.tar
# git://git.altlinux.org/gears/w/wf-config.git
Patch1: %name-%version-%release.patch

# Automatically added by buildreq on Fri Mar 15 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel ninja-build pkg-config python-base python-modules python3 python3-base python3-module-pkg_resources sh4 xz
BuildRequires: gcc-c++ libevdev-devel libwlroots-devel meson

%package -n lib%name
Summary: A library for managing wayfire configuration files
Group: System/Libraries

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C++

%description
%summary.

%description -n lib%name
%summary.

%description -n lib%name-devel
%summary.

This package contains development files.

%prep
%setup
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n lib%name
%_libdir/lib%name.so.0*

%files -n lib%name-devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/lib%name.so

%changelog
* Fri Mar 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt1
- Initial build for Sisyphus.


