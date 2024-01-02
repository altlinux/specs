# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define commit 5d43fc0e2f8ff2908624d111c0adbaf2

Name: unl0kr
Version: 2.0.3
Release: alt1

Summary: Framebuffer-based disk unlocker for the initramfs based on LVGL
License: GPL-3.0-or-later
Group: System/Base

Url: https://gitlab.com/cherrypicker/unl0kr
# Source-url: https://gitlab.com/cherrypicker/unl0kr/uploads/%commit/unl0kr-%version.tar.gz
Source: %name-%version.tar
Patch: unl0kr-conf-alt.patch

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(inih)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(scdoc)

Requires: xkeyboard-config
Requires: libinput

%description
%summary.

%prep
%setup
%patch -p2

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/%name
%_man1dir/%name.1.*
%_man5dir/%name.conf.5.*
%config(noreplace) %_sysconfdir/%name.conf
%doc README.md CHANGELOG.md COPYING

%changelog
* Tue Jan 02 2023 Anton Midyukov <antohami@altlinux.org> 2.0.3-alt1
- Initial build
