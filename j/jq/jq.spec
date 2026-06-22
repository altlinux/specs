%def_disable static
%def_disable docs
%define soname 1

Name: jq
%define lname lib%name
Version: 1.8.2
Release: alt1
Summary: Command-line JSON processor
Group: Development/Other
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Url: https://stedolan.github.io/jq/
VCS: https://github.com/stedolan/jq
License: BSD
Requires: %lname = %EVR

BuildRequires(pre): rpm-macros-valgrind
BuildRequires: flex  liboniguruma-devel
%ifarch %valgrind_arches
%{?!_disable_check:BuildRequires: valgrind}
%endif
%{?!_disable_check:BuildRequires: /proc}

%description
%name is a command-line JSON processor.

%package -n %lname
Summary: %name shared library
Group: System/Libraries

%description -n %lname
%name shared library.

%package -n %lname-devel
Summary: Files for devel with %name library
Group: Development/C
Requires: %lname = %EVR

%description -n %lname-devel
Files for devel with %name library.

%if_enabled static
%package -n %lname-devel-static
Summary: %name static library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%name static library.
%endif

%prep
%setup
%patch0 -p1
rm scripts/version
printf "#!/bin/sh\necho %version\n" > scripts/version
chmod +x scripts/version

%build
%autoreconf
./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--enable-shared \
	#
%make_build V=1

%install
%makeinstall_std docdir=%_docdir/%name-%version
ln -sf README.md %buildroot%_docdir/%name-%version/README

%check
export LD_LIBRARY_PATH=$PWD/.libs
%make_build check || :
cat ./test-suite.log

%files
%doc %_docdir/%name-%version
%_bindir/*
%_man1dir/*

%files -n %lname
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*

%files -n %lname-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/libjq.pc

%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Jun 22 2026 Anton Farygin <rider@altlinux.org> 1.8.2-alt1
- 1.8.1 -> 1.8.2 (Fixes: CVE-2026-32316, CVE-2026-33947, CVE-2026-33948,
- CVE-2026-39956, CVE-2026-39979, CVE-2026-40164, CVE-2026-40612, CVE-2026-41256,
- CVE-2026-41257, CVE-2026-43894, CVE-2026-43895, CVE-2026-43896, CVE-2026-44777,
- CVE-2026-47770, CVE-2026-49839, CVE-2026-54679)

* Fri Aug 01 2025 Anton Farygin <rider@altlinux.com> 1.8.1-alt1
- 1.8.1 (Fixes: CVE-2025-49014, GHSA-f946-j5j2-4w5m)

* Fri Jul 04 2025 Ivan A. Melnikov <iv@altlinux.org> 1.8.0-alt2
- NMU: don't require valgrind on architectures it does not support
  (fixes FTBFS on loongarch64 and riscv64)

* Tue Jun 03 2025 Anton Farygin <rider@altlinux.com> 1.8.0-alt1
- 1.7.1 -> 1.8.0 (Fixes: CVE-2024-23337, CVE-2024-53427, CVE-2025-48060)

* Sun Apr 28 2024 Anton Farygin <rider@altlinux.ru> 1.7.1-alt2
- removed ruby-tools from BuildRequires (fix FTBFS)

* Sat Dec 30 2023 Anton Farygin <rider@altlinux.ru> 1.7.1-alt1
- 1.7 -> 1.7.1

* Wed Sep 13 2023 Anton Farygin <rider@altlinux.ru> 1.7-alt1
- 1.6 -> 1.7
- fixed URL

* Thu Nov 22 2018 Anton Farygin <rider@altlinux.ru> 1.6-alt2
- fixed build with --disable check 

* Mon Nov 05 2018 Anton Farygin <rider@altlinux.ru> 1.6-alt1
- 1.6

* Thu May 31 2018 Anton Farygin <rider@altlinux.ru> 1.5-alt3
- security update (fixes: CVE-2016-4074)

* Thu Apr 05 2018 Anton Farygin <rider@altlinux.ru> 1.5-alt2
- rebuilt for new liboniguruma

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 1.5-alt1
- new version with security fixes (CVE-2015-8863)

* Sun Jun 15 2014 Led <led@altlinux.ru> 1.4-alt1
- 1.4
- added library subpackages

* Tue Nov 12 2013 Led <led@altlinux.ru> 1.3-alt2
- fixed build with new automake

* Fri Oct 11 2013 Led <led@altlinux.ru> 1.3-alt1
- initial build
