# magpie subproject
%def_enable snapshot
# for ring
%define optflags_lto %nil

%define binary_name missioncenter
%define ver_major 1.1
%define rdn_name io.missioncenter.MissionCenter
# nvtop for magpie
# subprojects/magpie/platform-linux/3rdparty/nvtop/nvtop.json
%define nvtop_ver 339ee0b10a64ec51f43d27357b0068a40f16e9e4

%def_disable bootstrap

%def_disable check

Name: mission-center
Version: %ver_major.0
Release: alt1

Summary: Mission Center
License: GPL-3.0-or-later
Group: Monitoring
Url: https://missioncenter.io/

Vcs: https://gitlab.com/mission-center-devs/mission-center.git

%if_disabled snapshot
Source: https://gitlab.com/mission-center-devs/mission-center/-/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

Source1: %name-%version-cargo.tar
Source2: https://github.com/Syllo/nvtop/archive/%nvtop_ver.tar.gz

ExcludeArch: %ix86 armh ppc64le

%define glib_ver 2.86
%define gtk_ver 4.20
%define adwaita_ver 1.8

Requires: dconf
# no dmidecode required since 1.0.0
# Requires:  /usr/sbin/dmidecode

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler protobuf-compiler
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver gir(Adw) = 1
BuildRequires: python3(sqlite3)
# for nvtop
BuildRequires: cmake gcc-c++
BuildRequires: libudev-devel libdrm-devel libgbm-devel libglvnd-devel
BuildRequires: pkgconfig(dbus-1)

%description
Monitor your CPU, Memory, Disk, Network and GPU usage with Mission Center.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1} -a2
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor --no-delete -s subprojects/magpie/Cargo.toml \
| sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%define nvtop_dir subprojects/magpie/platform-linux/3rdparty/nvtop

pushd nvtop-%nvtop_ver
for p in ../%nvtop_dir/patches/*.patch; do
patch -p1 < $p; done
popd

mkdir -p %__builddir/subprojects/magpie/src/debug/build/native
mv nvtop-%nvtop_ver %__builddir/subprojects/magpie/src/debug/build/native/nvtop-%nvtop_ver

# hardcode dmidecode path
#sed -i 's|"\(dmidecode"\)|"/usr/sbin/\1|' src/sys_info_v2/mem_info.rs

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output %name.lang %binary_name

%check
%__meson_test

%files -f %name.lang
%_bindir/%binary_name
%_bindir/%binary_name-magpie
%_desktopdir/%rdn_name.desktop
%_datadir/%binary_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Fri Nov 14 2025 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sun May 25 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sat May 03 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- updated to v1.0.0-3-gf17f715

* Wed Oct 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- updated to v0.6.2-1-gbef908b

* Mon Oct 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Sun Sep 29 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- updated to v0.6.0-3-gaf370dc

* Mon Jun 17 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Sun Jun 09 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Sat Jun 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Sun Apr 21 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.5.2-alt1
- v0.4.5-2

* Thu Apr 11 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt2
- updated to v0.4.4-2-65-g8a1122d (ALT #49691)

* Sun Feb 11 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- updated to v0.4.4-2

* Fri Dec 15 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Dec 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2
- added dmidecode to runtime dependencies
  src/sys_info_v2/mem_info.rs: hardcode dmidecode path

* Sun Dec 10 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Fri Dec 08 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Wed Oct 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- first build for Sisyphus


