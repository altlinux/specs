%def_disable snapshot

%define ver_major 0.6

%def_enable libcap
%def_enable x11
%def_enable xcb_icccm
%def_enable xwayland
%def_disable xcb_errors
%def_enable examples

%def_enable check

Name: wlroots
Version: %ver_major.0
Release: alt1

Summary: Modular Wayland compositor library
License: MIT
Group: System/Libraries
Url: https://github.com/swaywm/wlroots

%if_disabled snapshot
Source: %url/archive/%name-%version.tar.gz
%else
# VCS: https://github.com/swaywm/wlroots.git
Source: %name-%version.tar
%endif

BuildRequires(pre): meson
BuildRequires: ctags
BuildRequires: libwayland-server-devel libwayland-client-devel
BuildRequires: libwayland-egl-devel wayland-protocols
BuildRequires: libEGL-devel libGLES-devel libdrm-devel libgbm-devel
BuildRequires: libinput-devel libxkbcommon-devel
BuildRequires: libudev-devel libpixman-devel
BuildRequires: pkgconfig(systemd)
%{?_enable_libcap:BuildRequires: libcap-devel}
%{?_enable_x11:BuildRequires: pkgconfig(x11-xcb) pkgconfig(xcb) pkgconfig(xcb-xinput) pkgconfig(xcb-xfixes)}
%{?_enable_xwayland:BuildRequires: pkgconfig(xcb) pkgconfig(xcb-composite) pkgconfig(xcb-render) pkgconfig(xcb-xfixes)}
%{?_enable_xcb_icccm:BuildRequires: pkgconfig(xcb-icccm)}
%{?_enable_xcb_errors:BuildRequires: pkgconfig(xcb-errors)}
%{?_enable_examples:BuildRequires: libwayland-cursor-devel}

%description
%summary

%package -n lib%name
Summary: Modular Wayland compositor library
Group: System/Libraries

%description -n lib%name
This package provides shared %name library.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides development files for %name library.

%prep
%setup -n %name-%version

%build
%meson
%meson_build %{?_disable_examples:-Dexamples=false}

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -n lib%name
%_libdir/lib%name.so.*
%doc README.md LICENSE

%files -n lib%name-devel
%_includedir/wlr/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Fri May 24 2019 Alexey Gladkov <legion@altlinux.ru> 0.6.0-alt1
- New version (0.6.0)

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

