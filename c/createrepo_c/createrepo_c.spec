Summary:  Creates a common metadata repository
Name:     createrepo_c
Version:  0.20.1
Release:  alt1
Group:    System/Configuration/Packaging
License:  GPL-2.0+
URL:      https://github.com/rpm-software-management/createrepo_c
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0:  %name-%version.tar
Patch0:   %name-set-versions.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: doxygen
BuildRequires: expat-devel
BuildRequires: libmagic-devel
BuildRequires: glib2-devel
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: libssl-devel
BuildRequires: librpm-devel
BuildRequires: libsqlite3-devel
BuildRequires: bzip2-devel
BuildRequires: liblzma-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
BuildRequires: libmodulemd-devel

BuildRequires: python3-devel

Requires: lib%name = %version-%release

%description
C implementation of Createrepo.
A set of utilities (createrepo_c, mergerepo_c, modifyrepo_c)
for generating a common metadata repository from a directory of
rpm packages and maintaining it.

%package -n lib%name
Summary:  Library for repodata manipulation
Group:    System/Libraries
Provides: %name-libs

%description -n lib%name
Libraries for applications using the createrepo_c library
for easy manipulation with a repodata.

%package devel
Summary:  Library for repodata manipulation
Group:    Development/C
Requires: lib%name = %version-%release

%description devel
This package contains the createrepo_c C library and header files.
These development files are for easy manipulation with a repodata.

%package -n python3-module-%name
Summary:  Python 3 bindings for the createrepo_c library
Group:    Development/Python3

%description -n python3-module-%name
Python 3 bindings for the createrepo_c library.

%prep
%setup
%patch0 -p1

%build
export CMAKE_CXX_FLAGS="%optflags"
%cmake -DPYTHON_DESIRED=3 \
       -DWITH_ZCHUNK=OFF
%cmake_build

%install
%cmakeinstall_std
ln -s createrepo_c %buildroot%_bindir/createrepo
ln -s mergerepo_c %buildroot%_bindir/mergerepo
ln -s modifyrepo_c %buildroot%_bindir/modifyrepo

%files
%_bindir/*
%_man8dir/*

%files -n lib%name
%_libdir/lib%name.so.*

%files devel
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/%name

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Sat Nov 19 2022 Andrey Cherepanov <cas@altlinux.org> 0.20.1-alt1
- New version.
- Make symlinks without _c suffix.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.11.0-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue Jul 10 2018 Alexey Gladkov <legion@altlinux.ru> 0.11.0-alt1
- New version (0.11.0)

* Thu Sep 28 2017 Alexey Gladkov <legion@altlinux.ru> 0.10.0-alt1
- First build for ALTLinux.

* Fri Aug 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10.0-14
- Rebuilt after RPM update (№ 3)

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10.0-13
- Rebuilt for RPM soname bump

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10.0-12
- Rebuilt for RPM soname bump

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Pavel Raiskup <praiskup@redhat.com> - 0.10.0-9
- backport patches for double-free in --ignore-lock (rhbz#1355720)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.10.0-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.10.0-5
- Make drpm builds conditional

* Sun Apr 10 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.10.0-4
- Don't own python3_sitearch dir in python3 subpkg
- Use %%license macro
- Follow modern packaging guidelines
- Cleanups in spec file
- Follow packaging guidelines about SourceURL
- Fix license

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 8 2016 Orion Poplawski <orion@cora.nwra.com> - 0.10.0-2
- Remove comments causing trouble with post/postun scriptlets

* Tue Jan   5 2016 Tomas Mlcoch <tmlcoch at redhat.com> - 0.10.0-1
- Python 3 support (made by Ralph Bean)
- Modify gen_rst.py to indicate --sqliterepo is an option too (Neal Gompa)
- Do not compress manpages at generation time (Neal Gompa)

* Tue Oct  20 2015 Tomas Mlcoch <tmlcoch at redhat.com> - 0.9.1-1
- Fix double free during parsing broken XML metadata (Issue #33)
- Tests: Add acceptance test for --general-compress-type option
- Fix 'CR_CW_UNKNOWN_COMPRESSION cannot be used' error
- Refactoring: Fix compiler warnings
- Add --general-compress-type option (RhBug 1253850)
- Enable drpm support when drpm library is detected on system (RhBug: 1261031) (Issue #37)
- fix traceback on non-complete datetime information (Jarek Polok)
- parsehdr: Skip broken dependency with bad (non-numerical) epoch and print warning about that
  (https://lists.fedoraproject.org/pipermail/devel/2015-August/213882.html)
- misc: cr_str_to_evr(): Return NULL instead of "0" for bad (non-numerical) epoch
- updateinfo: Fix a typo in the package release attribute (Luke Macken)
- CMake: Don't require CXX compiler
- Tests for different checksum type for RPMs and repodata files (#31)
- Support different checksum type for RPMs and repodata files (#31)

* Tue Jul   7 2015 Tomas Mlcoch <tmlcoch at redhat.com> - 0.9.0-2
- Add drpm as a BuildRequire

* Thu May  28 2015 Tomas Mlcoch <tmlcoch at redhat.com> - 0.9.0-1
- mergerepo_c: Prepend protocol (file://) for URLs in pkgorigins (if --koji is used)
- Update bash completion
- doc: Update manpages
- mergerepo: Fix NVR merging method
- mergerepo: Fix behavior of --all param
- createrepo: Add --cut-dirs and --location-prefix options
- misc: Add cr_cut_dirs()
- mergerepo: Use better version comparison algorithm
- utils: Port cr_cmp_version_str() to rpm's algorithm (rpmvercmp)
- misc: Rename elements in cr_Version structure
- mergerepo: Fix version-release comparison for packages when --all is used
- mergerepo: Show warnings if some groupfile cannot be automatically used
- mergerepo: Exit with error code when a groupfile cannot be copied

* Fri May  15 2015 Tomas Mlcoch <tmlcoch at redhat.com> - 0.8.3-1
- mergerepo: Do not prepend file:// if protocol is already specified

* Thu May  14 2015 Tomas Mlcoch <tmlcoch at redhat.com> - 0.8.2-1
- doc: Add man pages for sqliterepo and update manpages for other tools
- mergerepo: Work only with noarch packages if --koji is used and
  no archlist is specified
- mergerepo: Use file:// protocol in local baseurl
- mergerepo: Do not include baseurl for first repo if --koji is specified (RhBug: 1220082)
- mergerepo_c: Support multilib arch for --koji repos
- mergerepo_c: Refactoring
- Print debug message with version in each tool when --verbose is used
- modifyrepo: Don't override file with itself (RhBug: 1215229)

* Wed May   6 2015 Tomas Mlcoch <tmlcoch at redhat.com> - 0.8.1-1
- Fix bash completion for RHEL 6

* Tue May   5 2015 Tomas Mlcoch <tmlcoch at redhat.com> - 0.8.0-1
- New tool Sqliterepo_c - It generates sqlite databases into repos
  where the sqlite is missing.
- Internal refactoring and code cleanup

* Fri Feb  20 2015 Tomas Mlcoch <tmlcoch at redhat.com> - 0.7.7-1
- Proper directory for temporary files when --local-sqlite is used (Issue #12)
- Bring bash completion install dir and filenames up to date with current bash-completion

* Thu Jan   8 2015 Tomas Mlcoch <tmlcoch at redhat.com> - 0.7.6-1
- Python: Add __contains__ method to Repomd() class

* Sun Dec  28 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.7.5-1
- Python repomd: Support for iteration and indexing by type - e.g. record = repomd['primary']
- Show warning if an XML parser probably parsed a bad type of medata (New XML parser warning type CR_XML_WARNING_BADMDTYPE)
- drpm library: Explicitly try to locate libdrpm.so.0
- deltarpms: Don't show options for delta rpms if support is not available

* Tue Nov  11 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.7.4-1
- createrepo_c, mergerepo_c: Follow redirs by default while downloading remote repos
- mergerepo_c: Fix segfault when a package without sourcerpm is part of metadata and --koji option is used

* Mon Nov  10 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.7.3-1
- xml_parser: Add file path into error messages
- Refactor: Replace g_error() with g_critical() (RhBug: 1162102)

* Thu Nov  06 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.7.2-1
- createrepo_c: New option --local-sqlite

* Fri Oct  31 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.7.1-1
- Mergerepo: Fix mergerepo
- Mergerepo: Add some debugging of metadata read.

* Mon Oct  20 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.7.0-1
- deltarpms: Update module to work with current version of drpm
- mergerepo_c: Add --omit-baseurl option
- craterepo_c: Gen empty repo if empty pkglist is used
- Docs: Output python docs to separate directory
- Several small fixes

* Tue Aug  12 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.6.1-1
- updateinfo: Use Python datetime objects in python bindings

* Tue Aug   5 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.6.0-1
- Support for updateinfo.xml manipulation (including Python bindings)

* Fri Jul  18 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.5.0-1
- Experimental delta rpm (DRPM) support (Disabled in Fedora build).

* Thu Jun  26 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.4.1-1
- Initialize threads correctly on old versions of GLib2 (RhBug: 1108787)
- Do not print log domain (get rid off C_CREATEREPOLIB prefix in log messages)
- Implements support for --cachedir
- New option --retain-old-md-by-age
- Few small API changes

* Tue May   6 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.4.0-1
- Change default behavior of repodata files handling. (RhBug: 1094539)
  See: https://github.com/Tojaj/createrepo_c/wiki/New-File-Handling
  By default, createrepo leaves old groupfiles (comps files)
  in the repodata/ directory during update.
  Createrepo_c did the same thing but the version 0.4.0 changes this behaviour.

* Thu Apr  10 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.3.1-2
- Support for weak and rich dependecies

* Mon Mar  10 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.3.0-1
- Relevant only for developers using createrepo_c library: New approach for
  metadata loading in case of internal high-level parser functions (see commit
  messages for more information: d6ed327595, 0b0e75203e, ad1e8450f5)
- Support for changelog limit value == -1 (include all changelogs)
- Update debug compilation flags
- Update man pages (Add synompsis with usage)
- Update usage examples in help

* Thu Feb  20 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.2.2-1
- Temporary remove deltarepo subpackages
- cmake: Do not install deltarepo stuff yet
- helper: Removed cr_remove_metadata() and cr_get_list_of_md_locations()
- Add module helpers
- Sanitize strings before writting them to XML or sqlitedb (ISSUE #3)

* Mon Jan  27 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.2.1-3
- New expert option: --ignore-lock

* Mon Jan  20 2014 Tomas Mlcoch <tmlcoch at redhat.com> - 0.2.1-2
- More effort to avoid residual .repodata/ directory on error
- Add deltarepo and python-deltarepo subpackages
- Add modifyrepo_c
- Add documentation for python bindings
- Refactored code & a lot of little bug fixes

* Wed Aug  14 2013 Tomas Mlcoch <tmlcoch at redhat.com> - 0.2.1-1
- checksum: Set SHA to be the same as SHA1 (For compatibility with original
  Createrepo)

* Mon Aug   5 2013 Tomas Mlcoch <tmlcoch at redhat.com> - 0.2.0-1
- Speedup (More parallelization)
- Changed C API
- Add python bindings
- A lot of bugfixes
- Add new make targets: tests (make tests - builds c tests) and test
  (make test - runs c and python test suits).
- Changed interface of most of C modules - Better error reporting
  (Add GError ** param).
- Experimental Python bindings (Beware: The interface is not final yet!).
- package: Add cr_package_copy method.
- sqlite: Do not recreate tables and triggers while opening existing db.
- mergerepo_c: Implicitly use --all with --koji.
- Man page update.

* Thu Apr  11 2013 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.17-3
- mergerepo_c: Add --simple-md-filenames and --unique-md-filenames
options. (RhBug: 950994)
- mergerepo_c: Always include noarch while mimic koji
mergerepos. (RhBug: 950991)
- Rename cr_package_parser_shutdown to cr_package_parser_cleanup()
- cr_db_info_update is now safe from sqlinjection.

* Mon Mar  25 2013 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.17-1
- Fix double free() when old metadata parsing failed. (related to RhBug: 920795)
- Convert all strings to UTF-8 while dumping XML. (related RhBug: 920795)

* Mon Mar  11 2013 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.16-2
- Remove creation of own empty rpm keyring for a transaction set.
This is not necessary since rpm-4.8.0-28 (rpm commit
cad147070e5513312d851f44998012e8f0cdf1e3). Moreover, own rpm keyring
causes a race condition in threads (causing double free()) which use
rpmReadPackageFile() called from cr_package_from_rpm().

* Thu Mar  07 2013 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.16-1
- Fix usage of rpm keyring (RhBug:918645)
- More generic interface of repomd module
- Code refactoring
- Add some usage examples into the doxygen documentation and .h files
- Rename version constants in version.h
- New function cr_package_nevra (returns package nevra string)

* Mon Feb  11 2013 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.15-1
- Fix bug in final move from .repodata/ -> repodata/
- Fix warnings from RPM library. RPM library is thread-unsafe. This
includes also reading headers. Use of empty keyring for rpm transaction
should work around the problem.

* Tue Nov  27 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.14-1
- Fix filelists database generation (use '.' instead of '' for current dir)

* Tue Nov  20 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.13-1
- Fix race-condition during task buffering in createrepo_c

* Tue Nov  20 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.12-2
- Fix removing old repomd.xml while --update

* Thu Nov  15 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.12-1
- Fix bug in sqlite filelists database
- Fix memory leak

* Fri Nov  09 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.11-1
- Deterministic output! Packages in output repodata are now sorted
by ASCII value
- Support for Koji mergerepos behaviour in mergerepo_c
(new --koji, --groupfile and --blocked params)
- Better atomicity while finall move .repodata/ -> repodata/
- Repomd module supports pkgorigins record
- Some new functions in misc module
- Small changes in library interface

* Wed Oct  03 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.10-1
- Another memory usage optimalization

* Mon Sep  03 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.9-1
- Some changes in library interface
- Memory usage optimalization
- Fix a segfault and a race condition
- New cmd options: --read-pkgs-list and --retain-old-md param
- Few other bugfixes

* Wed Aug  15 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.8-1
- New interface of repomd module
- New cmd options: --repo --revision --distro --content --basedir
- New createrepo_c specific cmd option --keep-all-metadata
- Few bugfixes

* Thu Jul  26 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.7-1
- SQLite support
- Bash completion
- createrepo_c support for --compress-type param
- Improved logging
- Subpackages -devel and -libsi
- Relicensed to GPLv2
- Doxygen documentation in devel package
- README update

* Mon Jun  11 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.5-1
- Support for .xz compression
- Unversioned .so excluded from installation

* Mon Jun   4 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.4-1
- New mergerepo params: --all, --noarch-repo and --method
- Fix segfault when more than one --excludes param used

* Mon May  28 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.3-1
- Set RelWithDebInfo as default cmake build type

* Wed May  23 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.2-1
- Add version.h header file

* Wed May  23 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.1-1
- Add license

* Wed May  9 2012 Tomas Mlcoch <tmlcoch at redhat.com> - 0.1.0-1
- First public release
