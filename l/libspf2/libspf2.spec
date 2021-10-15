%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libspf2
Version: 1.2.11
Release: alt1.git.4915c30
Summary: Implementation of the SPF specification
License: LGPLv2.1+
Group: System/Libraries
URL: https://www.libspf2.org/

# https://github.com/shevek/libspf2.git
Source: %name-%version.tar

Patch1: libspf2-alt-disable-static-binaries.patch
Patch2: libspf2-alt-glibc-compat.patch
Patch3: libspf2-alt-print-format.patch

# Automatically added by buildreq on Mon Nov 03 2008
BuildRequires: gcc-c++

%description
Libspf2 is an implementation of the SPF specification as found at
http://tools.ietf.org/html/rfc7208

%package tools
Summary: Tools distributed with libspf2
Group: Networking/Other
Requires: %name = %EVR

%description tools
Tools distributed with libspf2; at the time of writing: spf_example,
spf_example_2mx, spfd, spfquery and spftest.

%package devel
Summary: Development files for libspf2 library
Group: Development/C
Requires: %name = %EVR

%description devel
Development files for libspf2 library.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%autoreconf
%configure \
	--disable-static \
	%nil

# fix rpath libtool issues
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool || exit 1
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool || exit 1
%make_build

%install
%makeinstall_std

%files
%doc LICENSES
%_libdir/lib*.so.*

%files tools
%_bindir/*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Fri Oct 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.11-alt1.git.4915c30
- Updated to latest upstream snapshot

* Wed Sep 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.10-alt4
- Fixed build with LTO.

* Mon Jun 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.10-alt3
- Fix build with gcc-6

* Tue Nov 04 2014 Anton Gorlov <stalker@altlinux.ru> 1.2.10-alt2
- replace draft with rfc in description

* Mon Nov 03 2014 Anton Gorlov <stalker@altlinux.ru> 1.2.10-alt1
- New version 

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 1.2.9-alt4
- Fix RPATH issue.

* Tue May 10 2011 Victor Forsiuk <force@altlinux.org> 1.2.9-alt3
- Rebuilt for debuginfo.

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1.2.9-alt2
- Rebuilt for soname set-versions.

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 1.2.9-alt1
- 1.2.9

* Mon Nov 03 2008 Victor Forsyuk <force@altlinux.org> 1.2.8-alt1
- 1.2.8
- Security fix for CVE-2008-2469.

* Tue Jul 12 2005 Victor Forsyuk <force@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Tue Jan 18 2005 Victor Forsyuk <force@altlinux.ru> 1.0.4-alt1
- Initial build for Sysiphus.
- Fix for case-sensitivity bug and "config.cache trick" from Mandrake spec.
