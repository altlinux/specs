%def_enable snapshot
%define optflags_lto %nil

%define binary_name missioncenter
%define ver_major 0.5
%define rdn_name io.missioncenter.MissionCenter
# src/sys_info_v2/gatherer/3rdparty/nvtop/nvtop.json
%define nvtop_ver 45a1796375cd617d16167869bb88e5e69c809468

%def_disable bootstrap

%def_disable check

Name: mission-center
Version: %ver_major.1
Release: alt1

Summary: Mission Center
License: GPL-3.0
Group: Monitoring
Url: https://missioncenter.io/

%if_disabled snapshot
Source: https://gitlab.com/mission-center-devs/mission-center/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.com/mission-center-devs/mission-center.git
Source: %name-%version.tar
%endif

Source1: %name-%version-cargo.tar
Source2: https://github.com/Syllo/nvtop/archive/%nvtop_ver.tar.gz

ExcludeArch: %ix86 armh ppc64le

%define glib_ver 2.76
%define gtk_ver 4.10
%define adwaita_ver 1.2

Requires: dconf /usr/sbin/dmidecode

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
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
cargo vendor --no-delete -s src/sys_info_v2/gatherer/Cargo.toml \
| sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

pushd nvtop-%nvtop_ver
for p in ../src/sys_info_v2/gatherer/3rdparty/nvtop/patches/*.patch; do
patch -p1 < $p; done
popd

mkdir -p %__builddir/src/sys_info_v2/gatherer/src/debug/build/native
mv nvtop-%nvtop_ver %{__builddir}/src/sys_info_v2/gatherer/src/debug/build/native/nvtop-%nvtop_ver

# hardcode dmidecode path
sed -i 's|"\(dmidecode"\)|"/usr/sbin/\1|' src/sys_info_v2/mem_info.rs

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
%_bindir/%binary_name-gatherer
%_desktopdir/%rdn_name.desktop
%_datadir/%binary_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
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


