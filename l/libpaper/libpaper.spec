%define soname 2

Name: libpaper
Version: 2.1.2
Release: alt1
Epoch: 2

Summary: Library and tools for handling papersize

# This is the license for the source package:
License: LGPL-2.1-or-later AND ALT-Public-Domain AND GPL-3.0-or-later AND GPL-2.0-only
Group: System/Libraries
Url: https://github.com/rrthomas/libpaper

# Source-url: https://github.com/rrthomas/libpaper/releases/download/v%version/libpaper-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

# Automatically added by buildreq on Sun Jan 08 2006
BuildRequires: gcc-c++ libstdc++-devel

%description
The paper library and accompanying files are intended to provide a simple
way for applications to take actions based on a system- or user-specified
paper size.  This release is quite minimal, its purpose being to provide
really basic functions (obtaining the system paper name and getting
the height and width of a given kind of paper) that applications can
immediately integrate.

%package -n %name%soname
Summary: Library and tools for handling papersize
# The library is licensed under LGPL-2.1-or-later, and the paperspecs file is
# in the public domain.
License: LGPL-2.1-or-later AND ALT-Public-Domain
Group: System/Libraries

%description -n %name%soname
The paper library and accompanying files are intended to provide a simple
way for applications to take actions based on a system- or user-specified
paper size.  This release is quite minimal, its purpose being to provide
really basic functions (obtaining the system paper name and getting
the height and width of a given kind of paper) that applications can
immediately integrate.

%package -n paper
Summary: Query paper size database and retrieve the preferred size
# The paper utility is licensed under GPL-3.0-or-later, and the paperconf is
# licensed under GPL-2.0-only.
License: GPL-3.0-or-later AND GPL-2.0-only
Group: Text tools
Requires: %name%soname = %EVR
# due to /usr/bin/paperconf
Conflicts: libpaper < 1.1.28-alt3

%description -n paper
This package enables users to indicate their preferred paper size, provides
the paper(1) utility to find the user's preferred default paper size and give
information about known sizes, and specifies system-wide and per-user paper
size catalogs, which can be can also be used directly (see paperspecs(5)).

The paper utility is licensed under GPL-3.0-or-later, and the paperconf utility
is licensed under GPL-2.0-only.

%package -n libpaper-devel
Summary: Header files for %name
# The library is licensed under LGPL-2.1-or-later.
License: LGPL-2.1-or-later
Group: Development/Other
Requires: %name%soname = %EVR

%description -n libpaper-devel
This package contains headers and libraries that programmers will need
to develop applications which use libpaper.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
%find_lang libpaper

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%files -n libpaper%soname
%_docdir/libpaper/
%_docdir/libpaper/README
%_libdir/libpaper.so.*
%_sysconfdir/paperspecs
%_man5dir/paperspecs.5*

%files -n paper
%_bindir/paper
%_bindir/paperconf
%_man1dir/paper.1*

%files -n libpaper-devel
%_includedir/paper.h
%_libdir/libpaper.so

%changelog
* Tue Nov 07 2023 Vitaly Lipatov <lav@altlinux.ru> 2:2.1.2-alt1
- new version 2.1.2 (with rpmrb script)

* Fri Jul 28 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:2.1.1-alt3
- NMU:
  - Moved the /etc/paperspecs data file from paper subpackage to the libpaper2
    subpackage.
  - Moved the paperconf utility from the libpaper2 subpackage to the paper
    subpackage.
  - Changed the package licenses according to the upstream README file.

* Mon Jul 24 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:2.1.1-alt2
- NMU:
  - Removed unused patches.
  - Added a call to the %%autoreconf macro to prevent the generation of rpaths
    in the ELF files.
  - libpaper2: removed the 'Obsoletes: libpaper' tag because these packages
    provide completely different sonames, allowing them to be installed
    simultaneously.
  - libpaper2: removed the 'Provides: libpaper' because it doesn't make any
    sense either.
  - libpaper2: added 'Conflicts: libpaper < 1.1.28-alt3' due to conflicting
    versions of the /usr/bin/paperconf utility.
  - Enabled strict mode for the verify-elf check.
  - Enabled rpm-build checks for unpackaged files and stripped files.

* Mon Jul 10 2023 Mikhail Tergoev <fidel@altlinux.org> 2:2.1.1-alt1
- new version 2.1.1 (with rpmgs script)
- build as libpaper2

* Sat Oct 03 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.28-alt1
- new version 1.1.28 (with rpmrb script)

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt1
- new version (1.1.26) with rpmgs script
- update all patches from Fedora project

* Wed Sep 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.24-alt4
- steal Fedora patches for proper papersize setting (ALT #26176)

* Mon Aug 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.24-alt3
- firsttime script added

* Mon Aug 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.24-alt2
- set paper to A4 if not set

* Fri Mar 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.24-alt1
- 1.1.24

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.23-alt1.qa2
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.23-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libpaper
  * postun_ldconfig for libpaper
  * postclean-05-filetriggers for spec file

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt1
- new version 1.1.23 (with rpmrb script)

* Sat Dec 30 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.21-alt0.1
- new version 1.1.21 (with rpmrb script)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.20-alt0.1
- new version 1.1.20 (with rpmrb script)

* Sun Jan 08 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt0.1
- initial build for ALT Linux Sisyphus
