%define _unpackaged_files_terminate_build 1
%define _libexecdir %_usr/libexec

Name: vdo
Version: 6.2.6.14
Release: alt1

Summary: Management tools for Virtual Data Optimizer
License: GPLv2
Group: System/Base

Url: http://github.com/dm-vdo/vdo
Source: %name-%version.tar
Patch0: %name-%version.patch
Patch1: vdo-6.2.4-e2k.patch

ExclusiveArch: x86_64 aarch64 ppc64le ppc64 s390 s390x %e2k

Requires: lvm2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libdevmapper-devel libdevmapper-event-devel
BuildRequires: libuuid-devel libblkid-devel
BuildRequires: zlib-devel

%description
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

This package provides the user-space management tools for VDO.

%package support
Summary: Support tools for Virtual Data Optimizer
Group: System/Base
Requires: libuuid >= 2.23

%description support
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

This package provides the user-space support tools for VDO.

%prep
%setup
%patch0 -p1
%patch1 -p1
%ifarch %e2k
# as of lcc 1.25.12
sed -i 's,-Werror,& -Wno-error=ignored-qualifiers,' utils/vdo/base/Makefile
%endif

%build
%make

%install
%make install DESTDIR=%buildroot INSTALLOWNER= name=%name \
  bindir=%_bindir defaultdocdir=%_defaultdocdir libexecdir=%_libexecdir \
  mandir=%_mandir presetdir=%_presetdir \
  python3_sitelib=%python3_sitelibdir sysconfdir=%_sysconfdir \
  unitdir=%_unitdir

# Fix installed
mkdir -p %buildroot{%_udevrulesdir,%_datadir/bash-completion/completions}
mv %buildroot%_sysconfdir/udev/rules.d/* %buildroot%_udevrulesdir/
mv %buildroot%_sysconfdir/bash_completion.d/* %buildroot%_datadir/bash-completion/completions/

%post
%post_service vdo

%preun
%preun_service vdo

%files
%_bindir/vdo
%_bindir/vdo-by-dev
%_bindir/vdodmeventd
%_bindir/vdodumpconfig
%_bindir/vdoforcerebuild
%_bindir/vdoformat
%_bindir/vdosetuuid
%_bindir/vdostats
%_libexecdir/vdoprepareforlvm
%python3_sitelibdir/*
%_unitdir/*
%_presetdir/97-vdo.preset
%_udevrulesdir/69-vdo-start-by-dev.rules
%dir %_defaultdocdir/%name
%doc %_defaultdocdir/%name/COPYING
%_defaultdocdir/%name/examples
%_man8dir/vdo.8*
%_man8dir/vdodmeventd.8*
%_man8dir/vdodumpconfig.8*
%_man8dir/vdoforcerebuild.8*
%_man8dir/vdoformat.8*
%_man8dir/vdoprepareforlvm.8*
%_man8dir/vdosetuuid.8*
%_man8dir/vdostats.8*
%_datadir/bash-completion/completions/vdo*

%files support
%_bindir/adaptLVMVDO.sh
%_bindir/vdoaudit
%_bindir/vdodebugmetadata
%_bindir/vdodumpblockmap
%_bindir/vdodumpmetadata
%_bindir/vdolistmetadata
%_bindir/vdoreadonly
%_bindir/vdoregenerategeometry
%_man8dir/adaptlvm.8*
%_man8dir/vdoaudit.8*
%_man8dir/vdodebugmetadata.8*
%_man8dir/vdodumpblockmap.8*
%_man8dir/vdodumpmetadata.8*
%_man8dir/vdolistmetadata.8*
%_man8dir/vdoreadonly.8*
%_man8dir/vdoregenerategeometry.8*

%changelog
* Tue Apr 26 2022 Alexey Shabalin <shaba@altlinux.org> 6.2.6.14-alt1
- 6.2.6.14

* Thu Jan 13 2022 Alexey Shabalin <shaba@altlinux.org> 6.2.6.7-alt1
- 6.2.6.7

* Fri Nov 12 2021 Alexey Shabalin <shaba@altlinux.org> 6.2.6.3-alt1
- 6.2.6.3

* Fri Sep 03 2021 Alexey Shabalin <shaba@altlinux.org> 6.2.5.74-alt1
- 6.2.5.74

* Sun Aug 29 2021 Michael Shigorin <mike@altlinux.org> 6.2.5.41-alt1.1
- E2K: added arch support patch by Ilya Kurdyukov (64 bit cacheline)
- minor spec cleanup

* Mon Jul 05 2021 Alexey Shabalin <shaba@altlinux.org> 6.2.5.41-alt1
- 6.2.5.41

* Wed Dec 16 2020 Alexey Shabalin <shaba@altlinux.org> 6.2.4.14-alt1
- 6.2.4.14

* Mon Sep 07 2020 Alexey Shabalin <shaba@altlinux.org> 6.2.3.114-alt1
- 6.2.3.114
- add vdo-support package

* Sat Apr 11 2020 Alexey Shabalin <shaba@altlinux.org> 6.2.2.117-alt1
- 6.2.2.117

* Thu Dec 12 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.2.33-alt1
- 6.2.2.33

* Tue Oct 22 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.2.18-alt1
- 6.2.2.18

* Sun Aug 11 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.1.134-alt1
- 6.2.1.134

* Thu Feb 21 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.0.293-alt1
- initial build for ALT
