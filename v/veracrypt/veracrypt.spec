%define _unpackaged_files_terminate_build 1

Name: veracrypt
Version: 1.26.29
Release: alt2

Summary: Disk encryption software

License: Apache-2.0
Group: File tools
Url: https://www.veracrypt.fr

# Source-url: https://github.com/veracrypt/VeraCrypt/archive/VeraCrypt_%version.tar.gz?/VeraCrypt_%version.tar.gz
Source: %name-%version.tar
# ALT bug #48560: mount to the TMPDIR of the user who started sudo
Patch1: veracrypt-user-tmpdir.patch

ExcludeArch: %ix86 ppc64le

BuildRequires: pkgconfig(fuse)
BuildRequires: libpcsclite-devel
#BuildRequires: makeself
BuildRequires: libwxGTK3.2-devel
BuildRequires: gcc-c++
BuildRequires: yasm
BuildRequires: nasm

# executed via sudo for mounting by a non-root user (ALT bug #48561)
Requires: /usr/bin/sudo

%description
Free disk encryption software based on TrueCrypt.

%prep
%setup
%patch1 -p1

%build
%make_build NOSTRIP=1 DEBUGGER=1 -C src

%install
%makeinstall_std -C src

# upstream install skips 128x128
install -Dm0644 src/Resources/Icons/VeraCrypt-128x128.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

rm -rv %buildroot%_bindir/%name-uninstall.sh

%files
%doc %_docdir/veracrypt/
%_bindir/veracrypt
%_sbindir/mount.veracrypt
%_desktopdir/veracrypt.desktop
%_pixmapsdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/mime/packages/veracrypt.xml
%dir %_datadir/veracrypt/
%_datadir/veracrypt/languages/


%changelog
* Sat Oct 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.26.29-alt2
- fix mounted volumes not shown to a non-root user with pam_mktemp:
  pass the user TMPDIR to the sudo core service and mount there (closes: #48560)
- add Requires: /usr/bin/sudo, used for mounting by a non-root user (closes: #48561)

* Tue Oct 06 2026 Vitaly Lipatov <lav@altlinux.ru> 1.26.29-alt1
- new version 1.26.29

* Wed Jul 30 2025 Vitaly Lipatov <lav@altlinux.ru> 1.26.24-alt1
- new version 1.26.24 (with rpmrb script)
- switch to libwxGTK3.2-devel

* Wed Mar 12 2025 Vitaly Lipatov <lav@altlinux.ru> 1.26.20-alt1
- new version 1.26.20 (with rpmrb script)

* Sun Jan 26 2025 Vitaly Lipatov <lav@altlinux.ru> 1.26.18-alt1
- new version 1.26.18 (with rpmrb script)

* Wed Dec 04 2024 Vitaly Lipatov <lav@altlinux.ru> 1.26.15-alt1
- new version 1.26.15 (with rpmrb script)

* Sun Aug 04 2024 Egor Ignatov <egori@altlinux.org> 1.26.7-alt1
- 1.26.7

* Thu Nov 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.25.9-alt1
- initial build for ALT Sisyphus (thanks, ROSA!)
