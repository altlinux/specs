%define _unpackaged_files_terminate_build 1

%define tmpfiles_cache_dir %_localstatedir/%name
%define tmpfiles_config_dir %_sysconfdir/%name

%define service_id org.altlinux.APM

Name: apm
Version: 0.2.4
Release: alt1

Summary: Atomic Package Manager 
License: GPL-3.0-or-later AND GPL-3.0-only
Group: System/Configuration/Packaging
Url: https://altlinux.space/alt-atomic/apm
Vcs: https://altlinux.space/alt-atomic/apm.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: vendor.tar
Source11: %name.tmpfiles
Patch: %name-%version-%release.patch

# From v0.1.3 distrobox in optional requires
# Requires: distrobox

BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-golang
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: libapt-devel
BuildRequires: pkgconfig(systemd)
BuildRequires: /proc

%description
APM is a universal application for managing both system packages
and packages from distrobox. It consolidates all functions into
a single API, provides interaction via a DBUS service, and offers
optional support for atomic images based on ALT Linux.

%prep
%setup -a1
%autopatch -p1

# Fix go vendoring build
for file in $(find -name "*\[generated\]*"); do
  mv -v "$file" "${file//\[generated\]/}"
done

%build
%meson -Dprofile=prod
%meson_build

%install
%meson_install
install -Dpm644 %SOURCE11 %buildroot%_tmpfilesdir/%name.conf

mkdir -p %buildroot%tmpfiles_cache_dir
mkdir -p %buildroot%tmpfiles_config_dir

%find_lang %name

%files -f %name.lang
%_tmpfilesdir/%name.conf
%_bindir/%name
%_sysconfdir/dbus-1/system.d/%service_id.conf
%_unitdir/%name.service
%_datadir/dbus-1/services/%service_id.User.service
%_datadir/dbus-1/system-services/%service_id.service
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_datadir/polkit-1/actions/%service_id.policy
%tmpfiles_cache_dir
%tmpfiles_config_dir
%doc README.en.md
%doc README.md
%doc README.ru.md

%changelog
* Wed Dec 03 2025 Vladimir Romanov <rirusha@altlinux.org> 0.2.4-alt1
- v0.2.4

* Mon Dec 01 2025 Vladimir Romanov <rirusha@altlinux.org> 0.2.3-alt1
- v0.2.3

* Wed Nov 26 2025 Vladimir Romanov <rirusha@altlinux.org> 0.2.2-alt1
- v0.2.2

* Wed Nov 12 2025 Vladimir Romanov <rirusha@altlinux.org> 0.1.11-alt1
- v0.1.11

* Tue Nov 11 2025 Vladimir Romanov <rirusha@altlinux.org> 0.1.10-alt1
- v0.1.10

* Tue Sep 23 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.6-alt1
- v0.1.6

* Thu Aug 21 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.5-alt1
- v0.1.5

* Mon Jun 02 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.1.1-alt1
- Initial build.
