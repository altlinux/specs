Name: fuse3-compat
Version: 3.16.2
Release: alt3

%define oname fuse3
%define abiversion 3

Summary: a tool for creating virtual filesystems
License: GPL-2.0-or-later
Group: System/Kernel and hardware

Url: https://github.com/libfuse/

Source: %oname-%version.tar
Source1: fuserumount3
Source2: alternatives
Patch: %oname-%version-alt.patch

BuildRequires(pre): rpm-macros-alternatives

Requires(pre): fuse-common >= 1.1.3 alternatives

BuildRequires: meson >= 0.51 ninja-build libudev-devel
Conflicts: fuse < 2.9.9-alt5

%description
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort
as well as for using them.

%package -n lib%{oname}_%abiversion
Group: System/Kernel and hardware
Summary: tool for creating virtual filesystems
License: LGPL-2.1-or-later
Obsoletes: lib%oname < %version-%release

%description -n lib%{oname}_%abiversion
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort.

This package contains shared libraries.

%prep
%setup -n %oname-%version
%patch -p1

%build
%meson -Duseroot=false
%meson_build

%install
%meson_install

rm -fr %buildroot%_sysconfdir
rm -fr %buildroot%_bindir
rm -fr %buildroot%_mandir
rm -fr %buildroot%_sbindir
rm -fr %buildroot%_udevrulesdir
rm -fr %buildroot%_includedir
rm -fr %buildroot%_libdir/lib%oname.so
rm -fr %buildroot%_pkgconfigdir

%files -n lib%{oname}_%abiversion
%_libdir/lib%oname.so.*

%changelog
* Sat Jan 24 2026 Evgeny Sinelnikov <sin@altlinux.org> 3.16.2-alt3
- build compatibility library libfuse3_3 with libfuse3.so.3 and
  libfuse3.so.3.16.2 files only according to Shared Libs Policy

* Tue Feb 18 2025 Evgeny Sinelnikov <sin@altlinux.org> 3.16.2-alt2
- added the ability to select the fusermount3/fuserumount3 version using
  alternatives by default (thx Korney Gedert) (fixes: 52316).

* Fri Mar 29 2024 Alexey Shabalin <shaba@altlinux.org> 3.16.2-alt1
- 3.16.2 (Fixed ALT#49805)
- move library from /lib to /usr/lib, drop support non-usrmerge

* Sun Mar 28 2021 Evgeny Sinelnikov <sin@altlinux.org> 3.10.2-alt1
- update to latest release requires by newest gvfs from gnome project (fixes: 39759)

* Sun Mar 28 2021 Evgeny Sinelnikov <sin@altlinux.org> 3.4.1-alt3
- update build with upstream history

* Mon Feb 04 2019 Rustem Bapin <rbapin@altlinux.org> 3.4.1-alt2
- added fuserumount3 script
- added pre- and postinstall scriptlets that take account mode of already installed fuse package

* Mon Jan 14 2019 Evgeny Sinelnikov <sin@altlinux.org> 3.4.1-alt1
- update to latest release

* Tue Jul 25 2017 Denis Smirnov <mithraen@altlinux.ru> 3.1.0-alt1
- first build for Sisyphus (ALT#33529)
