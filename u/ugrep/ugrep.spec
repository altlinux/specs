#
# spec file for package ugrep
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name: ugrep
Version: 3.9.5
Release: alt1

Summary: Universal grep: a feature-rich grep implementation with focus on speed
License: BSD-3-Clause
Group: File tools

Url: https://github.com/Genivia/ugrep
Source0: https://github.com/Genivia/ugrep/archive/v%version.tar.gz#/<project>-%{version}.tar.gz
Source100: ugrep.watch

BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(zlib)

%description
Ugrep supports an interactive query UI and can search file systems, source
code, text, binary files, archives, compressed files, documents and use
fuzzy search.

%prep
%setup

%build
%ifarch %e2k
# cpuid.h is x86-specific
%add_optflags -UHAVE_SSE2
%endif
%configure \
	--disable-avx \
	--enable-color
%make_build

%install
%makeinstall_std

%check
%make_build test

%files
%doc README.md LICENSE.txt
%_bindir/*
%_man1dir/*.1*
%_datadir/%name

%changelog
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

