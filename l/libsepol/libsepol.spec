%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global optflags_lto %optflags_lto -ffat-lto-objects

%def_disable check

Name: libsepol
Epoch: 1
Version: 3.7
Release: alt1
Summary: SELinux binary policy manipulation library
License: LGPLv2+
Group: System/Libraries
Url: https://github.com/SELinuxProject/selinux

Source: %name-%version.tar

Conflicts: libsetools < 3.3.8-alt6

%{!?_disable_check:BuildRequires: CUnit-devel}
BuildRequires: flex

%description
libsepol provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
libsepol provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

This package contains development library and header files for %name.

%package devel-static
Summary: Static development files for %name
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
libsepol provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

This package contains static library.

%package utils
Summary: Utils for checking and mainplating policy binaries Security-enhanced Linux
Group: System/Configuration/Other
Provides: chkcon = %EVR
Requires: %name = %EVR

%description utils
libsepol provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%make_build CFLAGS="%optflags" LIBDIR=%_libdir SHLIBDIR=%_libdir all

%install
%makeinstall_std LIBDIR=%_libdir SHLIBDIR=%_libdir

%check
%make_build test

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/sepol
%_pkgconfigdir/*
%_man3dir/*

%files devel-static
%_libdir/*.a

%files utils
%_bindir/*
%_man8dir/*
%exclude %_man8dir/genpol*

%changelog
* Mon Sep 16 2024 Anton Zhukharev <ancieg@altlinux.org> 1:3.7-alt1
- (NMU) Updated to 3.7.
  + Applied usrmerge paths changes.

* Mon Dec 25 2023 Anton Zhukharev <ancieg@altlinux.org> 1:3.6-alt1
- (NMU) Updated to 3.6.
  + Removed man-pages localizations that had been dropped by upstream.

* Wed Sep 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.2-alt2
- Fixed build with LTO.

* Mon Mar 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.2-alt1
- Updated to upstream version 3.2.

* Fri Jul 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.1-alt1
- Updated to upstream version 3.1.

* Mon Mar 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.0-alt1
- Updated to upstream version 3.0.

* Mon Mar 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.9-alt1
- Updated to upstream version 2.9.

* Mon Dec 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.8-alt2
- Added man pages translation by Olesya Gerasimenko.

* Thu Aug 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.8-alt1
- Updated to upstream version 2.8.

* Mon Feb 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.7-alt1
- Updated to upstream version 2.7.

* Thu Oct 27 2016 Anton Farygin <rider@altlinux.ru> 1:2.5-alt1
- new version

* Thu Sep 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:2.3-alt1
- downgraded due regression (closes: #32254)

* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 2.4-alt1
- new version

* Thu Feb 05 2015 Anton Farygin <rider@altlinux.ru> 2.3-alt1
- new version

* Tue Nov 19 2013 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- New version

* Thu Jun 27 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.9-alt1
- New version

* Sun Sep 23 2012 Led <led@altlinux.ru> 2.1.8-alt1
- 2.1.8
- cleaned up spec

* Thu Nov 10 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0.42-alt1.1
- Fixed packaging of manpages.
- Rebuilt for debuginfo.

* Wed Dec 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.42-alt1
- Updated to 2.0.42.

* Wed Nov 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.41-alt2
- fix build and install sections.
- Set LIBDIR and SHLIBDIR for make while build.
- use tar instead of tgz for sources.
- fix Url.
- Drop redundant information from description.

* Wed Feb 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.41-alt1
- new version

* Thu May 07 2009 Anton Farygin <rider@altlinux.ru> 2.0.36-alt1
- new version

* Mon Dec 22 2008 Anton Farygin <rider@altlinux.ru> 2.0.34-alt1
- new version

* Fri Dec 19 2008 Anton Farygin <rider@altlinux.ru> 2.0.30-alt1
- new (development) version
- specfile cleanup

* Sun Mar 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.16.12-alt1
- Initial build
