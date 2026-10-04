%define _unpackaged_files_terminate_build 1
%def_with check
%define mod_name peel_gen

Name: peel
Version: 0.1.0
Release: alt1.8fa6897a.1
Summary: Modern C++ bindings for GObject-based libraries, including GTK and GStreamer
License: MIT
Group: Development/C
Url: https://gitlab.gnome.org/bugaevc/peel
VCS: https://gitlab.gnome.org/bugaevc/peel.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-python3
BuildRequires: meson
BuildRequires: rpm-build-python3

%if_with check
BuildRequires: gir(GObject) = 2.0
%endif

%description
Peel provides modern C++ bindings for GObject-based libraries.
It notably makes some different design choices from the existing bindings.

%package -n lib%name-devel
Summary: Development files for peel
Group: Development/C
Requires: %name = %EVR

%description -n lib%name-devel
%summary.

%prep
%setup

%build
%meson -Dpython.purelibdir=%python3_sitelibdir
%meson_build -v

%install
%meson_install

%check
%__meson_test

%files
%doc README.* COPYING
%_bindir/%name-gen
%_datadir/%name
%python3_sitelibdir/%mod_name

%files -n lib%name-devel
%_includedir/peel
%_cmakedir/%name
%_pkgconfigdir/peel.pc
%_pkgconfigdir/peel.pc

%changelog
* Sun Oct 04 2026 Vasiliy Doylov <neko@altlinux.org> 0.1.0-alt1.8fa6897a.1
- Initial build for ALT.
