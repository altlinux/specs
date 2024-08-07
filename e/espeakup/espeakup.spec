%define _unpackaged_files_terminate_build 1

Name:    espeakup
Version: 0.90
Release: alt2

Summary: A light weight connector for espeak-ng and speakup
License: GPL-3.0
Group:   Accessibility
Url:     https://github.com/linux-speakup/espeakup

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ninja
BuildRequires: meson
BuildRequires: cmake 
BuildRequires: libespeak-ng-devel
BuildRequires: libalsa-devel
BuildRequires: ronn
BuildRequires: libsystemd-devel

%description
%summary

%prep
%setup

%build
%meson -Dsystemd=enabled -Dman=enabled
%meson_build

%install
%meson_install

%post
%post_service %name

%preun
%preun_service %name

%files
%doc *.md
%_bindir/%name
%_systemd_dir/system/%name.service
%_mandir/man8/%name.8.xz

%changelog
* Thu Aug 01 2024 Artem Semenov <savoptik@altlinux.org> 0.90-alt2
- Build man and systemd service

* Wed May 15 2024 Artem Semenov <savoptik@altlinux.org> 0.90-alt1
- Initial build for Sisyphus (ALT bug: 50362)
