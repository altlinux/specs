# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-suse-compat
BuildRequires: gcc-c++ libtinfo-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#
# spec file for package diskscan
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           diskscan
Version:        0.20
Release:        alt1_1.2
Summary:        Scan disk for bad or near failure sectors
License:        GPL-3.0+
Group:          System/Kernel and hardware
Url:            http://blog.disksurvey.org/proj/diskscan/
Source0:        https://github.com/baruch/diskscan/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.0.2
BuildRequires:  gcc-c++-common
BuildRequires:  python-module-yaml
BuildRequires:  python-module-BeautifulSoup
BuildRequires:  python-module-markdown
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)
Source44: import.info

%description
DiskScan is a Unix/Linux tool to scan a block device and check
if there are unreadable sectors, in addition it uses read
latency times as an assessment for a near failure as sectors
that are problematic to read usually entail many retries. This
can be used to assess the state of the disk and maybe decide
on a replacement in advance to its imminent failure. The disk
self test may or may not pick up on such clues depending on
the disk vendor decision making logic.

%prep
%setup -q

%build
%{suse_cmake}
%{suse_make_jobs}

%install
%{suse_cmake_install}

%files
%doc COPYING README*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_1.2
- new version

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_3.1
-new version

