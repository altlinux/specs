Name: libdwarf
Version: 0.7.0
Release: alt1
Epoch: 1

Summary: Library to access the DWARF Debugging file format
License: LGPL-2.1
Group: System/Libraries
Url: http://www.prevanders.net/dwarf.html

Source: %name-%version.tar

BuildRequires: gcc-c++ meson libelf-devel libzstd-devel zlib-devel

%package devel
Summary: Library and header files of libdwarf
Group: Development/C

%package tools
Summary: Tools for accessing DWARF debugging information
Group: Development/Tools

%description
Library to access the DWARF debugging file format which supports
source level debugging of a number of procedural languages, such as C, C++,
and Fortran.  Please see http://www.dwarfstd.org for DWARF specification.

%description devel
Development package containing library and header files of libdwarf.

%description tools
C++ version of dwarfdump (dwarfdump2) command-line utilities
to access DWARF debug information.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc ChangeLog COPYING README
%_libdir/libdwarf.so.*

%files devel
%_libdir/libdwarf.so
%_includedir/libdwarf-0
%_pkgconfigdir/libdwarf.pc

%files tools
%_bindir/dwarfdump
%_datadir/dwarfdump
%_man1dir/dwarfdump.1*

%changelog
* Sun Sep 22 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1:0.7.0-alt1
- 0.7.0 released

* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 20200114-alt2
- fix conflict with libwf-devel (ALT bug 37935)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 20200114-alt1
- new version 20200114 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 20180527-alt1
- new version 20180527 (with rpmrb script)

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 20180129-alt1
- new version 20180129 (with rpmrb script)

* Wed Dec 13 2017 Vitaly Lipatov <lav@altlinux.ru> 20170709-alt1
- new version 20170709 (with rpmrb script)

* Sun Aug 14 2016 Vitaly Lipatov <lav@altlinux.ru> 20160613-alt1
- new version 20160613 (with rpmrb script)

* Tue Aug 19 2014 Denis Kirienko <dk@altlinux.org> 20140805-alt1
- Update to 20140805, built for ALT Linux

* Tue Feb  4 2014 Tom Hughes <tom@compton.nu> - 20140131-2
- Link libdwarf.so with libelf

* Sun Feb  2 2014 Tom Hughes <tom@compton.nu> - 20140131-1
- Update to 20140131 upstream release

* Tue Jan  7 2014 Tom Hughes <tom@compton.nu> - 20130729-2
- Update upstream URLs to point at new site

* Wed Jul 31 2013 Tom Hughes <tom@compton.nu> - 20130729-1
- Update to 20130729 release

* Fri Feb  8 2013 Tom Hughes <tom@compton.nu> - 20130207-1
- Update to 20130207 release

* Sun Jan 27 2013 Tom Hughes <tom@compton.nu> - 20130126-1
- Update to 20130126 release
- Revert soname to libdwarf.so.0

* Sat Jan 26 2013 Tom Hughes <tom@compton.nu> - 20130125-1
- Update to 20130125 release
- Bump soname to libdwarf.so.1

* Mon Dec  3 2012 Tom Hughes <tom@compton.nu> - 20121130-1
- Update to 20121130 release

* Thu Nov 29 2012 Tom Hughes <tom@compton.nu> - 20121127-1
- Update to 20121127 release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120410-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Tom Hughes <tom@compton.nu> - 20120410-1
- Update to 20120410 release
- Drop the 0. from the version - the dates are the upstream versions
- Remove explicit dependencies on elfutils-libelf

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110612-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110612-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 13 2011 Parag Nemade <paragn AT fedoraproject DOT org> - 0.20110612-1
- Update to 20110612 release

* Wed Mar 09 2011 Parag Nemade <paragn AT fedoraproject DOT org> - 0.20110113-1
- Update to 20110113 release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100629-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 06 2010 Parag Nemade <paragn AT fedoraproject.org> - 0.20100629-1
- Update to 20100629 release
- Add -static subpackage as request in rh#586807

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090324-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 - Suravee Suthikulpanit <suravee.suthikulpanit@amd.com>
- 0.20090324-4
- Adding _smp_mflags for libdwarf build
- Move CFLAGS override from configure to make
 
* Mon Mar 30 2009 - Suravee Suthikulpanit <suravee.suthikulpanit@amd.com>
- 0.20090324-3
- Remove AutoreqProv no

* Thu Mar 26 2009 - Suravee Suthikulpanit <suravee.suthikulpanit@amd.com>
- 0.20090324-2
- Drop the C implementation of dwarfdump. (dwarfdump1)
- Since the doc package is small, we combined the contents into the devel package.
- Fix the version string.
- Drop the static library.
- Add release number to "Requires".
- Fix licensing (v2 instead of v2+)
- Change linking for libdwarf.so and libdwarf.so.0

* Wed Mar 25 2009 - Suravee Suthikulpanit <suravee.suthikulpanit@amd.com>
- 20090324-1
- Initial Revision
