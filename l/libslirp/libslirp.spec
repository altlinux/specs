
Name: libslirp
Version: 4.8.0
Release: alt1
Summary: A general purpose TCP-IP emulator
Group: System/Libraries
License: BSD-3-Clause
Url: https://gitlab.freedesktop.org/slirp/%name
Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: glib2-devel

%description
A general purpose TCP-IP emulator used by virtual machine hypervisors
to provide virtual networking services.

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
%meson_build

%install
%meson_install

%files
%doc README.md COPYRIGHT
%_libdir/%name.so.0*

%files devel
%_includedir/slirp
%_libdir/%name.so
%_pkgconfigdir/slirp.pc

%changelog
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
