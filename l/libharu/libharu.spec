# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%define soname 2.4
Name: libharu
Version: 2.4.4
Release: alt1
Summary: C library for generating PDF files
Group: System/Libraries
License: zlib-acknowledgement
Url: http://libharu.org
VCS: https://github.com/libharu/libharu
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: ctest cmake
BuildRequires: libpng-devel
BuildRequires: zlib-devel

%description
libHaru is a library for generating PDF files.
It is free, open source, written in ANSI C and cross platform.

%package -n libharu%soname
Summary: %summary
Group: System/Libraries

%description -n libharu%soname
libHaru is a library for generating PDF files.
It is free, open source, written in ANSI C and cross platform.


%package devel
Group: Development/Other
Summary: Development files for %name
Requires: %name%soname = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%cmake -DLIBHPDF_STATIC=NO

%cmake_build

%install
%cmake_install

%files -n libharu%soname
%doc README.md  LICENSE
%_libdir/libhpdf.so.%soname
%_libdir/libhpdf.so.%soname.*
%exclude %_datadir/%name

%files devel
%_includedir/*
%_libdir/libhpdf.so

%changelog
* Fri Jan 19 2024 Anton Farygin <rider@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Tue Apr 04 2023 Anton Farygin <rider@altlinux.ru> 2.4.3-alt1
- new version
- built from upstream git
- use SPDX for license tag
- cleanup spec from autoimport artefacts
- added soname patch from fedora

* Tue Apr 27 2021 Igor Vlasenko <viy@altlinux.org> 2.3.0-alt2_13
- dropped python2 examples (closes: #39982)

* Fri Sep 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_12
- fixed build

* Wed Sep 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt2_3
- Applied patches from Gentoo.

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_3
- new version

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_9
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_8
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2
- update to new release by fcimport

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2_3
- spec cleanup thanks to ldv@

* Fri Dec 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_3
- converted by srpmconvert script

