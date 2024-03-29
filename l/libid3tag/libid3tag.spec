%define _unpackaged_files_terminate_build 1
%define sover 0
Name: libid3tag
Version: 0.16.3
Release: alt1
Summary: ID3 Tag manipulation library
Summary(ru_RU.UTF-8): Библиотека для работы с тегами ID3
License: GPL-2.0-or-later
Group: Sound
Url: https://codeberg.org/tenacityteam/libid3tag
VCS: https://codeberg.org/tenacityteam/libid3tag.git
Source: %name-%version.tar

BuildRequires: gcc-c++ gperf libstdc++-devel zlib-devel cmake

%description
%name is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.

%description -l ru_RU.UTF-8
%name -- это библиотека для чтения и записи тегов ID3v1 и ID3v2.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains development files required for packaging software
using %name library.

%description devel -l ru_RU.UTF-8
В этом пакете находятся файлы, необходимые для использования %name
в разработке приложений.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc CHANGES README CREDITS COPYRIGHT
%_libdir/*.so.%sover
%_libdir/*.so.%sover.*

%files devel
%_libdir/*.so
%_libdir/cmake/id3tag
%_pkgconfigdir/*
%_includedir/*

%changelog
* Mon Jan 29 2024 Anton Farygin <rider@altlinux.ru> 0.16.3-alt1
- 0.16.3

* Thu Dec 24 2020 Dmitry V. Levin <ldv@altlinux.org> 0.15.1b-alt10
- NMU.
- Fixed License tag.
- Removed libtool_1.5 from build dependencies.

* Mon Oct 19 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.1b-alt9
- Applied patches from Debian and Gentoo (Fixes: CVE-2004-2779).

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.1b-alt8
- Fixed build with gcc-6

* Fri Apr 22 2011 Dmitry V. Levin <ldv@altlinux.org> 0.15.1b-alt7.2
- Rebuilt for debuginfo.

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 0.15.1b-alt7.1
- Rebuilt for soname set-versions.

* Thu Nov 12 2009 Mykola Grechukh <gns@altlinux.ru> 0.15.1b-alt7
- patched with rcc

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.15.1b-alt6.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libid3tag
  * postun_ldconfig for libid3tag

* Sat May 17 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.15.1b-alt6
- Fix CVE-2008-2109.

* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.15.1b-alt5
- Added autoreconf.
- Minor spec cleanup.
- Changed packager field.

* Thu Jun 17 2004 Andrey Astafiev <andrei@altlinux.ru> 0.15.1b-alt4
- Fixed bug #3292: gpref is required for building.

* Thu Jun 10 2004 Andrey Astafiev <andrei@altlinux.ru> 0.15.1b-alt3
- Fixed bug #3405: Typo in russian summary.

* Thu Mar 04 2004 Andrey Astafiev <andrei@altlinux.ru> 0.15.1b-alt2
- 0.15.1b

* Wed Nov 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.15.0b-alt4.1
- fixed buildreqs.
- don't package .la files.

* Fri Nov 21 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt4
- Repaired changelog.

* Thu Nov 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.15.0b-alt3.1
- use libtool_1.4

* Fri Nov 14 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt3
- Fixed build on SMP systems.

* Mon Nov 03 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt2
- Added patch for pkgconfig.

* Fri Jun 06 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt1
- libid3tag is now in separate tarball.

* Sat Mar 15 2003 Andrey Astafiev <andrei@altlinux.ru> 0.14.2b-alt4
- Library libid3tag moved to separate binary package.

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.14.2b-alt3
- rebuild with gcc-3.2
- Packager tag added.

* Tue Feb 12 2002 Andrey Astafiev <andrei@altlinux.ru> 0.14.2b-alt2
- Packager field fixed.

* Fri Nov 09 2001 Andrey Astafiev <andrei@altlinux.ru> 0.14.2b-alt1
- 0.14.2b

* Tue Oct 23 2001 Andrey Astafiev <andrei@altlinux.ru> 0.14.1b-alt1
- 0.14.1b

* Fri Oct 19 2001 Andrey Astafiev <andrei@altlinux.ru> 0.14.0b-alt1
- 0.14.0b

* Mon Sep 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.13.0b-alt2
- Blind minor specfile cleanup.

* Mon Sep 3 2001 Andrey Astafiev <andrei@altlinux.ru> 0.13.0b-alt1
- First version of RPM package.

