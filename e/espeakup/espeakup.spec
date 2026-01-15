%define _unpackaged_files_terminate_build 1

Name:    espeakup
Version: 0.90
Release: alt3

Summary: A light weight connector for espeak-ng and speakup
License: GPL-3.0
Group:   Accessibility
Url:     https://github.com/linux-speakup/espeakup

Source: %name-%version.tar
Source1: %name-start.sh
Source2: %name.in

# Debian patches
Patch0: systemd
Patch1: nice
Patch2: flow_control
Patch3: punct
Patch4: error

# ALT patches
Patch10: change-to-start-with-script.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: meson
BuildRequires: cmake 
BuildRequires: libespeak-ng-devel
BuildRequires: libalsa-devel
BuildRequires: ronn
BuildRequires: libsystemd-devel

%description
espeakup is a program which makes it possible for speakup to use
the espeak-ng software synthesizer.  It does this by reading speakup's
softsynth device and passing the text to espeak-ng which actually speaks.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch10 -p1

%build
%meson -Dsystemd=enabled -Dman=enabled
%meson_build

%install
%meson_install

install -Dm 755 %SOURCE1 %buildroot%_sbindir/%name-start
install -Dm 644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc *.md
%config(noreplace) %_sysconfdir/sysconfig/%name
%_bindir/%name
%_sbindir/%name-start
%_systemd_dir/system/%name.service
%_mandir/man8/%name.8.xz

%changelog
* Thu Jan 15 2026 Artem Semenov <savoptik@altlinux.org> 0.90-alt3
- Added autodidect language

* Thu Aug 01 2024 Artem Semenov <savoptik@altlinux.org> 0.90-alt2
- Build man and systemd service

* Wed May 15 2024 Artem Semenov <savoptik@altlinux.org> 0.90-alt1
- Initial build for Sisyphus (ALT bug: 50362)
