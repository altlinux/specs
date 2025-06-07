%define _unpackaged_files_terminate_build 1

%define tmpfiles_cache_dir %_localstatedir/%name
%define tmpfiles_config_dir %_sysconfdir/%name

%define service_id org.altlinux.APM

Name: apm
Version: 0.1.1
Release: alt1

Summary: Atomic Package Manager 
License: GPL-3.0-or-later AND GPL-3.0-only
Group: Other
Url: https://github.com/alt-atomic/apm
Vcs: https://github.com/alt-atomic/apm.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: vendor.tar
Source11: %name.tmpfiles
Patch: %name-%version-%release.patch

Requires: distrobox

BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-golang
BuildRequires: meson
BuildRequires: pkgconfig(systemd)

%description
APM is a universal application for managing both system packages
and packages from distrobox. It consolidates all functions into
a single API, provides interaction via a DBUS service, and offers
optional support for atomic images based on ALT Linux.

%prep
%setup -a1
%autopatch -p1

%build
%meson -Dprofile=prod
%meson_build

%install
%meson_install
install -Dpm644 %SOURCE11 %buildroot%_tmpfilesdir/%name.conf

mkdir -p %buildroot%tmpfiles_cache_dir
mkdir -p %buildroot%tmpfiles_config_dir

%find_lang %name

%post
%post_service %name

%preun
%preun_service %name

%files -f %name.lang
%_tmpfilesdir/%name.conf
%_bindir/%name
%_sysconfdir/dbus-1/system.d/%service_id.conf
%_unitdir/%name.service
%_datadir/dbus-1/services/%service_id.User.service
%_datadir/dbus-1/system-services/%service_id.service
%tmpfiles_cache_dir
%tmpfiles_config_dir
%doc README.en.md
%doc README.md
%doc README.ru.md

%changelog
* Mon Jun 02 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.1.1-alt1
- Initial build.
