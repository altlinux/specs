%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libslirp
Version: 4.8.0
Release: alt2
Summary: A general purpose TCP-IP emulator
Group: System/Libraries
License: BSD-3-Clause
Url: https://gitlab.freedesktop.org/slirp/libslirp
Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: glib2-devel

%description
libslirp is a user-mode networking library used by virtual machines,
containers, and various tools.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
echo "%version" > .tarball-version

%build
%meson
%meson_build --verbose

%install
%meson_install

%check
grep -Fx '#define SLIRP_VERSION_STRING "%version"' %buildroot%_includedir/slirp/libslirp-version.h
%meson_test

%files
%doc README.md COPYRIGHT CHANGELOG.md
%_libdir/%name.so.0*

%files devel
%_includedir/slirp
%_libdir/%name.so
%_pkgconfigdir/slirp.pc

%changelog
* Sat Jun 01 2024 Vitaly Chikunov <vt@altlinux.org> 4.8.0-alt2
- spec: Add post-build checks.

* Fri May 31 2024 Alexey Shabalin <shaba@altlinux.org> 4.8.0-alt1
- New version 4.8.0.

* Fri Jun 03 2022 Alexey Shabalin <shaba@altlinux.org> 4.7.0-alt1
- new version 4.7.0

* Mon Jul 19 2021 Alexey Shabalin <shaba@altlinux.org> 4.6.1-alt1
- new version 4.6.1 (Fixes: CVE-2021-3592, CVE-2021-3593, CVE-2021-3594, CVE-2021-3595)

* Fri Dec 11 2020 Alexey Shabalin <shaba@altlinux.org> 4.4.0-alt1
- new version 4.4.0 (Fixes: CVE-2020-29129, CVE-2020-29130)

* Fri Aug 07 2020 Alexey Shabalin <shaba@altlinux.org> 4.3.1-alt1
- new version 4.3.1 (Fixes: CVE-2020-10756)

* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 4.3.0-alt1
- new version 4.3.0 (Fixes: CVE-2020-1983)

* Fri Mar 20 2020 Alexey Shabalin <shaba@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sun Aug 18 2019 Alexey Shabalin <shaba@altlinux.org> 4.0.0.0.16.g7646-alt1
- Initial package master snapshot
