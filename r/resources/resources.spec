%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 1.5
%define rdn_name net.nokyan.Resources

%def_enable check
%def_disable bootstrap

Name: resources
Version: %ver_major.1
Release: alt1

Summary: System monitor
License: GPL-3.0-or-later
Group: Monitoring
Url: https://github.com/nokyan/resources

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/nokyan/resources.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

ExcludeArch: ppc64le

%define gtk_ver 4.10
%define adwaita_ver 1.5

Requires: dconf /usr/sbin/dmidecode polkit

# nvml-wrapper requires libnvidia-ml.so (ALT #49236)
%ifarch %ix86 x86_64 aarch64
Requires: %_libdir/libnvidia-ml.so
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson git rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Resources is a simple yet powerful monitor for your system resources and
processes, written in Rust and using GTK 4 and libadwaita for its GUI.
It's capable of displaying usage and details of your CPU, memory, GPUs,
network interfaces and block devices. It's also capable of listing and
terminating running graphical applications as well as processes.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

# hardcode dmidecode path
sed -i 's|"\(dmidecode"\)|"/usr/sbin/\1|' src/utils/memory.rs

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name-kill
%_libexecdir/%name/%name-processes
%_desktopdir/%{rdn_name}*.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%{rdn_name}*.gschema.xml
%_datadir/polkit-1/actions/%{rdn_name}*.policy
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%{rdn_name}*.metainfo.xml
%doc README*


%changelog
* Sun Jul 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Tue Jun 25 2024 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- updated to v1.5.0-8-g1108d43

* Mon Apr 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Wed Jan 31 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt2.1
- added %%_libdir/libnvidia-ml.so to runtime dependencies (ALT #49236)

* Mon Jan 29 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt2
- updated to v1.3.0-47-g7eeafb0
- added dmidecode to runtime dependencies
- src/utils/memory.rs: hardcode dmidecode path

* Sun Jan 14 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- first build for Sisyphus (v1.3.0-38-g98a8a6d)


