%define _sysusersdir %_prefix/lib/sysusers.d
%define _libexecdir %_prefix/libexec

Name: deepin-anything
Version: 7.0.39
Release: alt1

Summary: The lightning-fast filename search for Deepin

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-anything
VCS: https://github.com/linuxdeepin/deepin-anything

# Source-url: https://github.com/linuxdeepin/deepin-anything/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-7.0.7-alt-gcc15.patch

BuildRequires(pre): rpm-macros-dqt6 rpm-build-kernel
BuildRequires: cmake glib2-devel libgio-devel libdtk6core-devel libmount-devel libnl-devel libpcre-devel libudisks2-qt6-devel boost-devel libspdlog-devel liblucene++-devel dqt6-base-devel libstdc++-devel-static

%description
%summary.
It is provides offline search functions.

%package -n kernel-source-%name
Summary: Kernel source for %name module
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
This is the source of the kernel %name module.

%prep
%setup
%patch0 -p1
%if "%(rpmquery --qf '%%{VERSION}' gcc-c++)" >= "15"
%patch1 -p2
%endif

%build
%DQ6build \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
#

%install
%DQ6install
install -Dm644 archlinux/deepin-anything-server.sysusers %buildroot%_sysusersdir/deepin-anything-server.conf
cd %kernel_srcdir
tar -cJhf %name-0.0.tar.xz %name-0.0/
rm -rf %name-0.0/

%files
%doc README.md LICENSE debian/changelog
%_bindir/deepin-anything-searcher
%_libexecdir/deepin-anything-daemon
%_libexecdir/deepin-anything-server
%_libexecdir/deepin-anything-logger
%_userunitdir/deepin-anything-daemon.service
%_unitdir/deepin-anything-logger.service
%_sysusersdir/*.conf
%_sysconfdir/modules-load.d/anything.conf
%dir %_datadir/deepin-anything-server/
%_datadir/deepin-anything-server/pinyin.txt
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.anything/
%_datadir/dsg/configs/org.deepin.anything/org.deepin.anything.json
%_datadir/dsg/configs/org.deepin.anything/org.deepin.anything.logger.json

%files -n kernel-source-%name
%dir %_usrsrc/kernel/
%_usrsrc/kernel/*

%changelog
* Mon May 04 2026 Leontiy Volodin <lvol@altlinux.org> 7.0.39-alt1
- New version 7.0.39.
- Fixed build on gcc15.

* Fri Aug 01 2025 Leontiy Volodin <lvol@altlinux.org> 7.0.23-alt1
- New version 7.0.23.
- Enabled build on i586.

* Fri Apr 25 2025 Leontiy Volodin <lvol@altlinux.org> 7.0.11-alt1
- New version 7.0.11.
- Switched to dqt6.

* Fri Feb 07 2025 Leontiy Volodin <lvol@altlinux.org> 7.0.6-alt1
- New version 7.0.6.

* Fri Jan 17 2025 Leontiy Volodin <lvol@altlinux.org> 7.0.5-alt1
- New version 7.0.5.
- Added vcs tag.
- Packaged sources for the kernel module.

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 6.1.9-alt1
- New version 6.1.9.
- Built via separate qt5 instead system (ALT #48138).

* Fri Nov 17 2023 Leontiy Volodin <lvol@altlinux.org> 6.1.5-alt1
- New version 6.1.5.
- Fixed summary and description.
- Cleanup BRs.

* Tue Apr 04 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.4-alt1
- New version 6.0.4.

* Thu Dec 29 2022 Leontiy Volodin <lvol@altlinux.org> 6.0.3-alt1
- New version (6.0.3).

* Wed Oct 05 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.18-alt1
- New version (5.0.18).

* Tue Aug 16 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.13-alt2
- Changed default paths.

* Fri Feb 25 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.13-alt1
- New version (5.0.13).

* Mon May 31 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.9-alt1
- New version (5.0.9) with rpmgs script.

* Mon Feb 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.7-alt1
- New version (5.0.7) with rpmgs script.

* Tue Sep 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.1-alt1
- Initial build for ALT Sisyphus (thanks archlinux for the patch).
