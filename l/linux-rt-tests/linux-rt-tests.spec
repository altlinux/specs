# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# rt-tests is taken by perl tests for RT
Name:    linux-rt-tests
Version: 2.5
Release: alt1
Summary: Programs that test various rt-linux features
License: GPL-2.0-or-later
Group:   System/Kernel and hardware
Url:     https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/rt-tests
Vcs:     git://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git

Source: %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: libnuma-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: rpm-build-vm
}}

%description
rt-tests is a test suite, that contains programs (such as cyclictest,
hwlatdetect, hackbench) that test various rt-linux features.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%make_build CFLAGS="%optflags" prefix=/usr

%install
%makeinstall_std prefix=/usr

%check
vm-run --kvm=cond %buildroot%_bindir/cyclictest -m -Sp99 -t  -D60 -q

%files
%doc COPYING MAINTAINERS README.markdown src/hwlatdetect/hwlat.txt
%_bindir/*
%python3_sitelibdir_noarch/*.py
%_man8dir/*.8*

%changelog
* Thu Jan 26 2023 Vitaly Chikunov <vt@altlinux.org> 2.5-alt1
- Update to v2.5 (2023-01-20).

* Sun Jul 10 2022 Vitaly Chikunov <vt@altlinux.org> 2.4-alt1
- Updated to v2.4 (2022-07-08).

* Mon Dec 20 2021 Vitaly Chikunov <vt@altlinux.org> 2.3-alt1
- Updated to v2.3 (2021-12-10).

* Fri Sep 03 2021 Vitaly Chikunov <vt@altlinux.org> 2.2-alt1
- Update to v2.2 (2021-08-30).

* Fri Jul 02 2021 Vitaly Chikunov <vt@altlinux.org> 2.1-alt1
- Update to v2.1 (2021-06-29).

* Fri Jun 25 2021 Vitaly Chikunov <vt@altlinux.org> 2.0-alt1
- Update to v2.0 (2021-06-16).

* Mon Dec 28 2020 Vitaly Chikunov <vt@altlinux.org> 1.10-alt1
- Update to v1.10 (2020-12-22).

* Sun Oct 18 2020 Vitaly Chikunov <vt@altlinux.org> 1.9-alt2
- Build for armh.

* Wed Sep 23 2020 Vitaly Chikunov <vt@altlinux.org> 1.9-alt1
- Update to v1.9 (2020-09-18).

* Fri Mar 27 2020 Vitaly Chikunov <vt@altlinux.org> 1.8-alt1
- Update version to v1.8.

* Fri Mar 06 2020 Vitaly Chikunov <vt@altlinux.org> 1.7.0.11.gf240656-alt1
- Update to v1.7-11-gf240656.

* Wed Dec 04 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt4
- Return of the --numa option (for rteval).

* Sun Sep 15 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt3
- Make it compile on other arches.

* Sun Sep 08 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt2
- Add hwlatdetect (required python3).

* Fri Sep 06 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- First build of rt-tests.
