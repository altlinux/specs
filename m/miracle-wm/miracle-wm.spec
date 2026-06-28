%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%ifarch x86_64 aarch64
%def_with wasm
%set_verify_elf_skiplist %_libdir/libmiracle-wm-plugins.so
%else
%def_without wasm
%endif

%define _libexecdir %_prefix/libexec

Name: miracle-wm
Version: 0.10.0
Release: alt1

Summary: Wayland tiling window manager built on Mir
License: GPL-3.0-or-later and MIT
Group: Graphical desktop/Other
Url: https://github.com/miracle-wm-org/miracle-wm

Source: %name-%version.tar
Source1: %{name}.yaml

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(miral)
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(yaml-cpp)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: libpcre2-devel-static

%if_with wasm
BuildRequires: wasmedge-devel
%endif

BuildRequires: boost-filesystem-devel

%if_with check
BuildRequires: pkgconfig(gtest)
%endif

%description
miracle-wm is a Wayland compositor based on Mir. It features a tiling 
window manager at its core, very much in the style of i3 and sway. The
intention is to build a compositor that is flashier and more 
feature-rich than either of those compositors, like swayfx.

%package -n lib%{name}
Group: System/Libraries
Summary: Shared library for %{name}

%description -n lib%{name}
This package contains the shared library files for %{name}.

%package -n lib%{name}-devel
Summary: Development files for %{name}
Group: Development/C++
Requires: lib%{name} = %{version}-%{release}
Requires: %{name} = %{version}-%{release}

%description -n lib%{name}-devel
This package contains development files for %{name}.

%prep
%setup
sed -i "s/add_compile_options(-Wimplicit-fallthrough)/add_compile_options(-Wno-return-type)/" CMakeLists.txt
cp -v %SOURCE1 ./config.yaml

%build
%cmake \
%if_with check
       -DGTEST_INCLUDE_DIR=%_includedir/gtest/ \
       -DGTEST_LIBRARY=%_libdir/libgtest.so \
       -DGTEST_MAIN_LIBRARY=%_libdir/libgtest_main.so \
%endif
%if_without wasm
       -DFEATURE_PLUGIN_SYSTEM=OFF \
%endif
       -DSYSTEMD_INTEGRATION=ON
%cmake_build

%install
%cmake_install

# put example yaml file to the docs directory
mkdir -p %buildroot%_datadir/doc/%{name}-%{version}/
cp -av %SOURCE1 %buildroot%_datadir/doc/%{name}-%{version}/

%post
echo "NOTE: miracle-wm needs additional configuration, usually it needs Xwayland."
echo "      See details at https://wiki.miracle-wm.org/latest/ ."
echo "      For quick start copy the example configuration file from"
echo "      %_datadir/doc/%{name}-%{version}/config.yaml to ~/.config/%name/config.yaml"
echo "      then install the following packages which are used in the configuration file:"
echo "        waybar nwg-drawer nwg-bar nwg-panel nwg-dock swaybg nwg-shell-wallpapers"
echo "      then logout and login to Miracle session using your favorite greeter."

%systemd_user_post miracle-wm-session-shutdown.target
%systemd_user_post miracle-wm-session.target
%systemd_user_post miracle-wm-xdg-autostart.target

%preun
%systemd_user_preun miracle-wm-session-shutdown.target
%systemd_user_preun miracle-wm-session.target
%systemd_user_preun miracle-wm-xdg-autostart.target

%postun
%systemd_user_postun miracle-wm-session-shutdown.target
%systemd_user_postun miracle-wm-session.target
%systemd_user_postun miracle-wm-xdg-autostart.target

%check
%_target_platform/tests/miracle-wm-tests

%files
%doc CODE_OF_CONDUCT.md LICENSE README.md RELEASING.md miraclemsg/LICENSE.sway session/LICENSE.sway-systemd config.yaml
%_bindir/miracle-wm
%_bindir/miracle-wm-sensible-terminal
%_bindir/miracle-wm-session
%_bindir/miraclemsg
%_bindir/miracle-wm-basic-error-reporter
%_bindir/miracle-wm-debug-overlay
%_datadir/wayland-sessions/miracle-wm.desktop
%_userunitdir/miracle-wm-session-shutdown.target
%_userunitdir/miracle-wm-session.target
%_userunitdir/miracle-wm-xdg-autostart.target
%_libexecdir/miracle-wm-session-setup
%_libexecdir/miracle-wm-wait-sni-ready
%dir %_datadir/miracle-wm
%dir %_datadir/miracle-wm/shaders
%dir %_datadir/miracle-wm/shaders/output_filter
%_datadir/miracle-wm/shaders/output_filter/gray_scale.frag
%_datadir/miracle-wm/shaders/output_filter/night_light.frag

%files -n lib%{name}
%_libdir/libmiracle-wm-c.so.0*

%if_with wasm
%_libdir/libmiracle-wm-plugins.so
%endif

%files -n lib%{name}-devel
%_libdir/libmiracle-wm-c.so
%dir %_includedir/miracle/
%_includedir/miracle/*
%_pkgconfigdir/miracle-wm-c.pc

%changelog
* Sun Jun 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.10.0-alt1
- New version 0.10.0.

* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Mon Jul 21 2025 Nikolay Strelkov <snk@altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus
