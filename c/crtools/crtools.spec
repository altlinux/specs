# FIXME
%define optflags_lto %nil
%ifnarch ppc64le
%def_with amdgpu
%endif

Name: crtools
Version: 3.17
Release: alt1.1

Summary: Utility to checkpoint/restore tasks
License: GPL-2.0-only
Group: System/Configuration/Other
Url: http://criu.org

VCS: git://github.com/checkpoint-restore/criu.git
Source: criu-%version.tar
Source1: criu.watch
# git://git.altlinux.org/gears/c/%%name.git
Patch: %name-%version-%release.patch

Provides: criu = %EVR
ExclusiveArch: x86_64 aarch64 ppc64le

BuildRequires: libnet2-devel
BuildRequires: libprotobuf-c-devel %_bindir/protoc-c
BuildRequires: libprotobuf-devel protobuf-compiler
BuildRequires: asciidoc xmlto %_bindir/a2x
BuildRequires: libnftables-devel
BuildRequires: libgnutls-devel

%description
An utility to checkpoint/restore tasks.

%package -n libcriu2
Summary: Shared library of checkpoint/restore
Group: System/Libraries
License: LGPL-2.1-only
Provides: libcriu

%description -n libcriu2
Shared library of checkpoint/restore.

%package -n libcompel1
Summary: Compel library for CRIU
Group: System/Libraries
License: LGPL-2.1-only
Provides: libcompel

%description -n libcompel1
Compel library for CRIU.

%package -n libcriu-devel
Summary: Files for development with libcriu
Group: Development/C
Requires: libcriu
Requires: libcompel

%description -n libcriu-devel
Files for development with libcriu.

%package -n python3-module-criu
Summary: Python library of checkpoint/restore
Group: System/Libraries
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: glibc-devel
BuildRequires: libprotobuf-c-devel
BuildRequires: libnl-devel
BuildRequires: libcap-devel
BuildRequires: libselinux-devel
BuildRequires(pre): rpm-build-python3
Provides: crit = %EVR
Provides: python-module-criu
Obsoletes: crtools-pycriu
Obsoletes: python-module-criu

%add_python3_self_prov_path %buildroot%python3_sitelibdir_noarch/pycriu/images

%description -n python3-module-criu
Python library library of checkpoint/restore.

%if_with amdgpu
%package plugin-amdgpu
BuildRequires: libdrm-devel
Summary: AMDGPU plugin for checkpoint/restore.
Group: System/Libraries

%description plugin-amdgpu
This package contains the AMDGPU ROCm support plugin for checkpoint/restore.
%endif

%prep
%setup -n criu-%version
%autopatch -p1

%build
# Upstream claims that stack protection break criu
# https://github.com/checkpoint-restore/criu/issues/1744#issuecomment-1031605370
%add_optflags -fno-stack-protector -fno-stack-clash-protection
export CFLAGS="%optflags"
%make_build \
	%ifarch armh
		UNAME-M=armv7l \
	%endif
	PREFIX=%prefix V=1 all docs

%install
%makeinstall_std \
	%ifarch armh
		UNAME-M=armv7l \
	%endif
	PREFIX=%prefix LIBDIR=%_libdir LIBEXECDIR=%_libexecdir SYSTEMDUNITDIR=%_unitdir

ln -s criu %buildroot%_sbindir/crtools
ln -s criu.8 %buildroot%_man8dir/crtools.8

find %buildroot -name 'lib*.a' -delete

%files
%doc README.md COPYING CREDITS
%_sbindir/criu
%_sbindir/criu-ns
%_sbindir/crtools
%_bindir/compel
%_libexecdir/criu
%_libexecdir/compel
%_man1dir/compel.1*
%_man8dir/criu.8*
%_man1dir/criu-ns.1*
%_man8dir/crtools.8*

%files -n python3-module-criu
%_bindir/crit
%python3_sitelibdir_noarch/pycriu
%python3_sitelibdir_noarch/crit-*.egg-info
%_man1dir/crit.1*

%files -n libcriu2
%_libdir/libcriu.so.2*

%files -n libcompel1
%_libdir/libcompel.so.1*

%files -n libcriu-devel
%_includedir/criu
%_includedir/compel
%_libdir/*.so
%_pkgconfigdir/criu.pc

%if_with amdgpu
%files plugin-amdgpu
%doc plugins/amdgpu/README.md
%_man1dir/amdgpu_plugin.1*
%dir %_libdir/criu
%_libdir/criu/amdgpu_plugin.so
%endif

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 3.17-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Fri May 20 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.17-alt1
- Updated to 3.17.
- Built without stack protection (upstream claims it break criu).
- Applied SUSE and Fedora patches.
- Introduced amdgpu plugin.

* Tue Dec 07 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.16.1-alt1
- Updated to 3.16.1.

* Mon Sep 27 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.16-alt1
- Updated to 3.16.

* Tue Jul 13 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.15-alt2
- Do not build on armh (closes #40335).

* Wed Nov 04 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.15-alt1
- Updated to 3.15.

* Mon Aug 03 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.14-alt2
- Fixed FTBFS: fixed uses of deprecated security_context_t.

* Wed Apr 29 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.14-alt1
- Updated to 3.14.
- Built against nftables and gnutls libraries.
- Packed watch file.

* Mon Sep 30 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.13-alt2
- Built for ppc64le.
- Built with SELinux support.

* Tue Sep 17 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.13-alt1
- 3.13.
- Made and packaged crtools as symlink to criu.
- Made and packaged crtools manpage as symlink to criu manpage.
- Packaged compel library into separate package libcompel1.
- python-module-criu -> python3-module-criu.
- Fixed files packaging issues.

* Sat Nov 03 2018 Alexey Shabalin <shaba@altlinux.org> 3.10-alt1
- updated to 3.10
- add patch for build on aarch64

* Mon Jun 25 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.9-alt2
- built for aarch64 too

* Sun Jun 24 2018 Denis Pynkin <dans@altlinux.org> 3.9-alt1
- updated

* Wed May 09 2018 Denis Pynkin <dans@altlinux.org> 3.8.1-alt1
- updated

* Sun Mar 25 2018 Denis Pynkin <dans@altlinux.org> 3.8-alt1
- updated

* Fri Feb 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.7-alt1
- Updated to upstream version 3.7.

* Thu Sep 07 2017 Denis Pynkin <dans@altlinux.org> 3.4-alt1
- updated

* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 3.3-alt1
- updated

* Thu Jun 29 2017 Denis Pynkin <dans@altlinux.org> 3.2.1-alt1
- updated

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.12-alt1
- updated

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.8-alt1
- updated

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 2.7-alt1
- updated

* Mon Sep 26 2016 Denis Pynkin <dans@altlinux.org> 2.6-alt1
- updated

* Mon Aug 29 2016 Denis Pynkin <dans@altlinux.org> 2.5-alt1
- updated

* Wed Apr 13 2016 Denis Pynkin <dans@altlinux.org> 2.1-alt1
- upstream updates and fixes

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 2.0-alt1
- Version update

* Tue Mar 01 2016 Denis Pynkin <dans@altlinux.org> 1.8-alt1
- New upstream version

* Sat Apr 11 2015 Denis Pynkin <dans@altlinux.org> 1.5.1-alt1
- New upstream version
- Subpackage pycriu added
- New utility 'crit' added

* Sun Aug 17 2014 Led <led@altlinux.ru> 1.3-alt0.19
- upstream updates and fixes

* Sun Aug 10 2014 Led <led@altlinux.ru> 1.3-alt0.18
- upstream updates and fixes
- fixed build with protobuf-c >= 1.0

* Sat Jul 26 2014 Led <led@altlinux.ru> 1.3-alt0.17
- upstream updates and fixes

* Fri Jul 11 2014 Led <led@altlinux.ru> 1.3-alt0.16
- upstream updates and fixes

* Sun Jul 06 2014 Led <led@altlinux.ru> 1.3-alt0.15
- upstream updates and fixes

* Thu Jul 03 2014 Led <led@altlinux.ru> 1.3-alt0.14
- upstream updates and fixes

* Tue Jul 01 2014 Led <led@altlinux.ru> 1.3-alt0.13
- upstream updates and fixes

* Fri Jun 20 2014 Led <led@altlinux.ru> 1.3-alt0.12
- upstream updates and fixes

* Wed Jun 18 2014 Led <led@altlinux.ru> 1.3-alt0.11
- 1.3-rc2

* Thu Jun 12 2014 Led <led@altlinux.ru> 1.3-alt0.10
- upstream fixes

* Sun Jun 08 2014 Led <led@altlinux.ru> 1.3-alt0.9
- upstream fixes

* Fri Jun 06 2014 Led <led@altlinux.ru> 1.3-alt0.8
- mnt: Relax checks for top-mount in validate_mounts
- mnt: Fix validation of dumpable mountpoints

* Wed Jun 04 2014 Led <led@altlinux.ru> 1.3-alt0.7
- mnt: Devpts options get corrupted on dump (v2)

* Sat May 31 2014 Led <led@altlinux.ru> 1.3-alt0.6
- upstream fixes

* Sun May 25 2014 Led <led@altlinux.ru> 1.3-alt0.5
- upstream fixes

* Thu May 15 2014 Led <led@altlinux.ru> 1.3-alt0.4
- upstream fixes

* Mon May 12 2014 Led <led@altlinux.ru> 1.3-alt0.3
- upstream fixes

* Thu May 08 2014 Led <led@altlinux.ru> 1.3-alt0.2
- upstream fixes

* Sat Apr 26 2014 Led <led@altlinux.ru> 1.3-alt0.1
- 1.3-rc1

* Wed Feb 26 2014 Led <led@altlinux.ru> 1.2-alt1
- 1.2

* Sat Feb 01 2014 Led <led@altlinux.ru> 1.1-alt1
- 1.1 release

* Sat Jan 25 2014 Led <led@altlinux.ru> 1.1-alt0.3
- upstream fixes

* Thu Jan 23 2014 Led <led@altlinux.ru> 1.1-alt0.2
- 1.1-rc2

* Wed Jan 08 2014 Led <led@altlinux.ru> 1.1-alt0.1
- 1.1-rc1

* Sat Dec 14 2013 Led <led@altlinux.ru> 1.0-alt5
- upstream fixes

* Sat Dec 07 2013 Led <led@altlinux.ru> 1.0-alt4
- upstream fixes

* Sun Dec 01 2013 Led <led@altlinux.ru> 1.0-alt3
- upstream fixes

* Tue Nov 26 2013 Led <led@altlinux.ru> 1.0-alt2
- added TTY_MAJOR to known tty char devices group

* Tue Nov 26 2013 Led <led@altlinux.ru> 1.0-alt1
- initial build
