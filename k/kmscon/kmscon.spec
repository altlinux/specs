%define _unpackaged_files_terminate_build 1

Name: kmscon
Version: 9.0.0
Release: alt1
Summary: KMS/DRM based System Console
Group: Terminals

License: MIT and LGPLv2+
Url: http://www.freedesktop.org/wiki/Software/kmscon/
Source: %name-%version.tar
Patch1: %name-%version.patch

BuildRequires(pre): meson
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: xkeyboard-config
BuildRequires: pkgconfig(libtsm) >= 4.0.0
BuildRequires: pkgconfig(libudev) >= 172
BuildRequires: pkgconfig(libdrm)
BuildRequires: libsystemd-devel pkgconfig(libsystemd)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(pango) pkgconfig(pangoft2)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: xsltproc docbook-style-xsl docbook-dtds

%description
Kmscon is a simple terminal emulator based on Linux kernel mode setting (KMS).
It is an attempt to replace the in-kernel VT implementation with a user-space
console. See kmscon(1) man-page for usage information.

%prep
%setup
%patch1 -p1

%build
# In the development branch upstream fixes this differently.
sed -i '/^systemddir = .*$/'c"systemddir = '/lib/systemd'" meson.build
# Patch out tests we have to skip.
sed -i /"'"output"'"/c"# 'output' needs /dev/dri/card*" tests/meson.build
sed -i /"'"vt"'"/c"# 'vt' hangs in hasher" tests/meson.build

%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc COPYING NEWS README.md
%_bindir/%name
%_unitdir/*.service
%dir %_libdir/%name
%_libdir/%name/mod-*.so
%dir %_libexecdir/kmscon
%_libexecdir/kmscon/kmscon
%_man1dir/%name.1*

%changelog
* Fri Mar 10 2023 Arseny Maslennikov <arseny@altlinux.org> 9.0.0-alt1
- 8.0.40.g01dd0a2 -> 9.0.0.

* Thu Aug 15 2019 Alexey Shabalin <shaba@altlinux.org> 8-alt4.40.g01dd0a2
- disable post/preun scripts

* Thu Aug 01 2019 Alexey Shabalin <shaba@altlinux.org> 8-alt3.40.g01dd0a2
- Update to git snapshot 01dd0a2

* Tue Jan 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8-alt2
- Fixed build with new systemd and glibc.

* Tue Jun 17 2014 Alexey Shabalin <shaba@altlinux.ru> 8-alt1
- initial build
