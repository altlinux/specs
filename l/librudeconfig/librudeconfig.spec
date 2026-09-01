%define oname rudeconfig
Name: librudeconfig
Version: 6.1.0
Release: alt1

Summary: Library (C++ API) for reading and writing configuration/.ini files

Group: System/Libraries
License: GPL-2.0-or-later
Url: https://github.com/mflood/rudeconfig

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mflood/%oname/archive/v%version/%oname-%version.tar.gz
Source: %oname-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ /usr/bin/ctest

%description
%name is a library that allows applications to read, modify
and create configuration/.ini files.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
%name is a library that allows applications to read, modify
and create configuration/.ini files. The %name-devel package
contains libraries, header files, and documentation needed
to develop C++ applications using %name.

%prep
%setup -n %oname-%version

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DRUDECONFIG_BUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc AUTHORS COPYING README NEWS ChangeLog
%_libdir/*.so.*

%files devel
%dir %_includedir/rude/
%_includedir/rude/config.h
%_libdir/*.so
%_pkgconfigdir/rudeconfig.pc
%dir %_libdir/cmake
%_libdir/cmake/rudeconfig/
%_man3dir/*

%changelog
* Tue Sep 01 2026 Vitaly Lipatov <lav@altlinux.ru> 6.1.0-alt1
- new version 6.1.0
- Switch to the CMake build system and enable tests.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 5.0.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Sep 03 2010 Vitaly Lipatov <lav@altlinux.ru> 5.0.5-alt1
- initial build for ALT Linux Sisyphus (thanks, Fedora)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Caolán McNamara <caolanm@redhat.com> - 5.0.5-6
- include cstdio for EOF

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.0.5-4
- fix compile with gcc43

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.0.5-3
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.0.5-2
- Autorebuild for GCC 4.3

* Thu Feb 01 2007 Matt Flood <matt@rudeserver.com>
- 5.0.5-1
- Renamed header include guards in config.h
	- From INCLUDED_CONFIG_H to INCLUDED_RUDE_CONFIG_H

* Thu Feb 01 2007 Matt Flood <matt@rudeserver.com>
- 5.0.4-3
- Minor amendments to build-related scripts
	- Added missing include directory to specfile

* Thu Feb 01 2007 Matt Flood <matt@rudeserver.com>
- 5.0.4-2
- Minor amendments to build-related scripts
	- Fixed minor typo in changelog (ChangeLog and rudeconfig.spec)
	- Added --disable-static to configure directive in rudeconfig.spec

* Fri Jan 19 2007 Matt Flood <matt@rudeserver.com>
- 5.0.4-1
- Created rudeconfig.3 MAN page

* Mon Jul 31 2006 Matt Flood <matt@rudeserver.com>
- 5.0.3-1
- Minor changes to facilitate Windows builds
    * changed #include's of  <cstring> to <string.h>
    * added .c_str() to a string object to correct shorthand if statement ( a ? x : y )

* Thu Apr 10 2006 Matt Flood <matt@rudeserver.com>
- 5.0.2-1
- First RPM Release

* Fri Sep 2 2005 Matt Flood <matt@rudeserver.com>
- 5.0.2-0
- Modified source code for DataLine.cpp - removed 'using namespace std' which Visual Studio is too dumb to ignore.
- Fixed ParserJuly2004::chompEOL() - was not returning a value - (TODO: consider making the function void)
