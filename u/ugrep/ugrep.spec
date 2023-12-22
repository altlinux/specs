# SPDX-License-Identifier: MIT
# Copyright (c) 2020 SUSE LLC
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: ugrep
Version: 4.4.1
Release: alt1

Summary: Universal grep: a feature-rich grep implementation with focus on speed
License: BSD-3-Clause
Group: File tools

Url: https://ugrep.com
Vcs: https://github.com/Genivia/ugrep
Source0: https://github.com/Genivia/ugrep/archive/v%version.tar.gz#/%{name}-%{version}.tar.gz
Source100: ugrep.watch
AutoReq: noshell

BuildRequires: bzlib-devel
BuildRequires: gcc-c++
BuildRequires: hardlink
BuildRequires: libbrotli-devel
BuildRequires: liblz4-devel
BuildRequires: liblzma-devel
BuildRequires: libpcre2-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel

%description
Ugrep supports an interactive query UI and can search file systems, source
code, text, binary files, archives, compressed files, documents and use
fuzzy search.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%ifarch %e2k
# cpuid.h is x86-specific
%add_optflags -UHAVE_SSE2 -UHAVE_AVX2
# can be fixed with this, but performance may be worse
#sed -i "/<cpuid.h>/{N;s/.*/#define cpuidex __cpuidex/}" include/reflex/simd.h
%endif
%configure
%make_build

%install
%makeinstall_std
hardlink -v %buildroot%_bindir

%check
bin/ugrep --version | bin/ugrep '^%name \Q%version\E\s'
%make_build test

%files
%doc README.md LICENSE.txt
%_bindir/*
%_man1dir/*.1*
%_datadir/%name
%_datadir/bash-completion/completions/ug*
%_datadir/fish/vendor_completions.d/ug*
%_datadir/zsh/site-functions/_ug*

%changelog
* Fri Dec 22 2023 Vitaly Chikunov <vt@altlinux.org> 4.4.1-alt1
- Update to 4.4.1 (2023-12-22).
- Added shell completion scripts (bash, fish, zsh).

* Fri Dec 08 2023 Vitaly Chikunov <vt@altlinux.org> 4.3.5-alt1
- Update to 4.3.5 (2023-12-08).

* Mon Nov 27 2023 Vitaly Chikunov <vt@altlinux.org> 4.3.4-alt1
- Update to 4.3.4 (2023-11-27).

* Thu Nov 16 2023 Vitaly Chikunov <vt@altlinux.org> 4.3.3-alt1
- Update to 4.3.3 (2023-11-16).

* Sun Oct 15 2023 Vitaly Chikunov <vt@altlinux.org> 4.3.0-alt1
- Update to 4.3.0 (2023-10-15).

* Sat Sep 23 2023 Vitaly Chikunov <vt@altlinux.org> 4.2.0-alt1
- Update to 4.2.0 (2023-09-23).

* Tue Aug 22 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.0.0-alt2.1
- Fixed build for Elbrus.

* Mon Aug 21 2023 Vitaly Chikunov <vt@altlinux.org> 4.0.0-alt2
- Enabled LFS on 32-bit systems.
- Enabled support for lz4 and zstd.
- Enabled AVX support (it does have runtime dispatch by CPU features).
- spec: Remove BR on pkgconfig() because build does not use pkg-config to handle
  these libs. Replaced with BR to appropriate -devel packages.
- spec: configure --enable-color is deprecated by upstream (and is enabled by
  default).
- spec: Make 'ug' and 'ugrep' hardlinked to save space.
- spec: AR: noshell to avoid creating dependence on optional tools (antiword,
  pandoc, and pdftotext).

* Fri Aug 18 2023 Michael Shigorin <mike@altlinux.org> 4.0.0-alt1
- new version (watch file uupdate)

* Tue Aug 15 2023 Michael Shigorin <mike@altlinux.org> 3.12.7-alt1
- new version (watch file uupdate)

* Mon Aug 07 2023 Michael Shigorin <mike@altlinux.org> 3.12.6-alt1
- new version (watch file uupdate)

* Tue Jul 18 2023 Michael Shigorin <mike@altlinux.org> 3.12.4-alt1
- new version (watch file uupdate)

* Mon Jul 10 2023 Michael Shigorin <mike@altlinux.org> 3.12.2-alt1
- new version (watch file uupdate)

* Mon Jun 05 2023 Michael Shigorin <mike@altlinux.org> 3.12.1-alt1
- new version (watch file uupdate)

* Sun Jun 04 2023 Michael Shigorin <mike@altlinux.org> 3.12.0-alt1
- new version (watch file uupdate)

* Mon Apr 10 2023 Michael Shigorin <mike@altlinux.org> 3.11.2-alt1
- new version (watch file uupdate)

* Mon Apr 03 2023 Michael Shigorin <mike@altlinux.org> 3.11.1-alt1
- new version (watch file uupdate)

* Sun Mar 19 2023 Michael Shigorin <mike@altlinux.org> 3.11.0-alt1
- new version (watch file uupdate)

* Sat Mar 18 2023 Michael Shigorin <mike@altlinux.org> 3.10.1-alt1
- new version (watch file uupdate)

* Sat Mar 04 2023 Michael Shigorin <mike@altlinux.org> 3.10.0-alt1
- new version (watch file uupdate)

* Wed Feb 01 2023 Michael Shigorin <mike@altlinux.org> 3.9.7-alt1
- new version (watch file uupdate)

* Thu Jan 26 2023 Michael Shigorin <mike@altlinux.org> 3.9.6-alt1
- new version (watch file uupdate)

* Mon Jan 16 2023 Michael Shigorin <mike@altlinux.org> 3.9.5-alt1
- new version (watch file uupdate)

* Thu Jan 05 2023 Michael Shigorin <mike@altlinux.org> 3.9.4-alt1
- new version (watch file uupdate)

* Thu Dec 29 2022 Michael Shigorin <mike@altlinux.org> 3.9.3-alt1
- new version (watch file uupdate)

* Fri Aug 26 2022 Michael Shigorin <mike@altlinux.org> 3.9.2-alt1
- new version (watch file uupdate)

* Mon Aug 15 2022 Michael Shigorin <mike@altlinux.org> 3.9.1-alt1
- new version (watch file uupdate)

* Sun Aug 14 2022 Michael Shigorin <mike@altlinux.org> 3.9.0-alt1
- new version (watch file uupdate)

* Fri Jul 01 2022 Michael Shigorin <mike@altlinux.org> 3.8.3-alt1
- new version (watch file uupdate)

* Tue Jun 14 2022 Michael Shigorin <mike@altlinux.org> 3.8.2-alt1
- new version (watch file uupdate)

* Wed Jun 08 2022 Michael Shigorin <mike@altlinux.org> 3.8.1-alt1
- new version (watch file uupdate)

* Mon May 30 2022 Michael Shigorin <mike@altlinux.org> 3.8.0-alt1
- new version (watch file uupdate)

* Sun May 15 2022 Michael Shigorin <mike@altlinux.org> 3.7.11-alt1
- new version (watch file uupdate)

* Fri Apr 08 2022 Michael Shigorin <mike@altlinux.org> 3.7.9-alt1
- new version (watch file uupdate)

* Wed Apr 06 2022 Michael Shigorin <mike@altlinux.org> 3.7.8-alt1
- new version (watch file uupdate)

* Sat Apr 02 2022 Michael Shigorin <mike@altlinux.org> 3.7.7-alt1
- new version (watch file uupdate)

* Wed Mar 16 2022 Michael Shigorin <mike@altlinux.org> 3.7.6-alt1
- new version (watch file uupdate)

* Mon Mar 14 2022 Michael Shigorin <mike@altlinux.org> 3.7.5-alt1
- new version (watch file uupdate)

* Thu Feb 24 2022 Michael Shigorin <mike@altlinux.org> 3.7.4-alt1
- new version (watch file uupdate)

* Sun Feb 20 2022 Michael Shigorin <mike@altlinux.org> 3.7.3-alt1
- new version (watch file uupdate)

* Fri Feb 11 2022 Michael Shigorin <mike@altlinux.org> 3.7.2-alt1
- new version (watch file uupdate)

* Tue Feb 01 2022 Michael Shigorin <mike@altlinux.org> 3.7.1-alt1
- new version (watch file uupdate)

* Fri Jan 14 2022 Michael Shigorin <mike@altlinux.org> 3.6.0-alt1
- new version (watch file uupdate)

* Mon Jan 10 2022 Michael Shigorin <mike@altlinux.org> 3.5.0-alt1
- new version (watch file uupdate)

* Mon Dec 20 2021 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- new version (watch file uupdate)

* Sun Dec 12 2021 Michael Shigorin <mike@altlinux.org> 3.3.12-alt1
- new version (watch file uupdate)

* Wed Dec 08 2021 Michael Shigorin <mike@altlinux.org> 3.3.11-alt1
- new version (watch file uupdate)

* Sat Dec 04 2021 Michael Shigorin <mike@altlinux.org> 3.3.10-alt1
- new version (watch file uupdate)

* Wed Dec 01 2021 Michael Shigorin <mike@altlinux.org> 3.3.9-alt1
- new version (watch file uupdate)

* Sun Oct 24 2021 Michael Shigorin <mike@altlinux.org> 3.3.8-alt1
- new version (watch file uupdate)

* Sat Aug 07 2021 Michael Shigorin <mike@altlinux.org> 3.3.7-alt1
- new version (watch file uupdate)

* Tue Jul 27 2021 Michael Shigorin <mike@altlinux.org> 3.3.6-alt1
- new version (watch file uupdate)

* Wed Jul 21 2021 Michael Shigorin <mike@altlinux.org> 3.3.5-alt1
- new version (watch file uupdate)

* Thu Jun 24 2021 Michael Shigorin <mike@altlinux.org> 3.3.4-alt1
- new version (watch file uupdate)

* Sun Jun 20 2021 Michael Shigorin <mike@altlinux.org> 3.3.3-alt1
- new version (watch file uupdate)

* Wed Jun 09 2021 Michael Shigorin <mike@altlinux.org> 3.3.2-alt1
- new version (watch file uupdate)

* Fri Jun 04 2021 Michael Shigorin <mike@altlinux.org> 3.3.1-alt1
- new version (watch file uupdate)

* Sat May 29 2021 Michael Shigorin <mike@altlinux.org> 3.3-alt1
- new version (watch file uupdate)

* Fri May 14 2021 Michael Shigorin <mike@altlinux.org> 3.2.2-alt1
- new version (watch file uupdate)

* Thu May 06 2021 Michael Shigorin <mike@altlinux.org> 3.2.1-alt1
- new version (watch file uupdate)

* Sun May 02 2021 Michael Shigorin <mike@altlinux.org> 3.2-alt1
- new version (watch file uupdate)

* Thu Apr 29 2021 Michael Shigorin <mike@altlinux.org> 3.1.15-alt1
- new version (watch file uupdate)

* Wed Apr 28 2021 Michael Shigorin <mike@altlinux.org> 3.1.14-alt1
- new version (watch file uupdate)

* Sun Apr 25 2021 Michael Shigorin <mike@altlinux.org> 3.1.12-alt1
- new version (watch file uupdate)

* Sun Apr 04 2021 Michael Shigorin <mike@altlinux.org> 3.1.11-alt1
- new version (watch file uupdate)

* Wed Mar 24 2021 Michael Shigorin <mike@altlinux.org> 3.1.10-alt1
- new version (watch file uupdate)

* Sat Feb 27 2021 Michael Shigorin <mike@altlinux.org> 3.1.9-alt1
- new version (watch file uupdate)

* Thu Feb 25 2021 Michael Shigorin <mike@altlinux.org> 3.1.8-alt1
- new version (watch file uupdate)

* Sat Feb 06 2021 Michael Shigorin <mike@altlinux.org> 3.1.7-alt1
- new version (watch file uupdate)

* Fri Jan 15 2021 Michael Shigorin <mike@altlinux.org> 3.1.3-alt1
- new version (watch file uupdate)

* Mon Jan 11 2021 Michael Shigorin <mike@altlinux.org> 3.1.2-alt1
- new version (watch file uupdate)

* Wed Dec 23 2020 Michael Shigorin <mike@altlinux.org> 3.1.1-alt1
- new version (watch file uupdate)

* Tue Dec 15 2020 Michael Shigorin <mike@altlinux.org> 3.1.0-alt1
- new version (watch file uupdate)

* Mon Dec 07 2020 Michael Shigorin <mike@altlinux.org> 3.0.6-alt1
- new version (watch file uupdate)

* Wed Nov 18 2020 Michael Shigorin <mike@altlinux.org> 3.0.5-alt1
- new version (watch file uupdate)

* Sun Oct 25 2020 Michael Shigorin <mike@altlinux.org> 3.0.4-alt1
- new version (watch file uupdate)

* Wed Oct 14 2020 Michael Shigorin <mike@altlinux.org> 3.0.2-alt1
- new version (watch file uupdate)

* Fri Oct 09 2020 Michael Shigorin <mike@altlinux.org> 3.0.1-alt1
- new version (watch file uupdate)

* Fri Oct 02 2020 Michael Shigorin <mike@altlinux.org> 3.0.0-alt1
- new version (watch file uupdate)

* Tue Sep 22 2020 Michael Shigorin <mike@altlinux.org> 2.5.6-alt1
- new version (watch file uupdate)

* Wed Sep 02 2020 Michael Shigorin <mike@altlinux.org> 2.5.5-alt1
- new version (watch file uupdate)

* Wed Sep 02 2020 Michael Shigorin <mike@altlinux.org> 2.5.4-alt1
- new version (watch file uupdate)

* Wed Aug 19 2020 Michael Shigorin <mike@altlinux.org> 2.5.3-alt1
- new version (watch file uupdate)

* Wed Aug 12 2020 Michael Shigorin <mike@altlinux.org> 2.5.2-alt1
- new version (watch file uupdate)

* Mon Aug 10 2020 Michael Shigorin <mike@altlinux.org> 2.5.1-alt1
- new version (watch file uupdate)

* Tue Jul 28 2020 Michael Shigorin <mike@altlinux.org> 2.5.0-alt1
- 2.5.0
- added debian watch file

* Wed Jul 15 2020 Michael Shigorin <mike@altlinux.org> 2.4.1-alt2
- E2K: ftbfs workaround (SIMD related)

* Wed Jul 15 2020 Michael Shigorin <mike@altlinux.org> 2.4.1-alt1
- initial build (thx opensuse)

