Name: xxhash
Version: 0.8.2
Release: alt1

Summary: Extremely fast hash algorithm
# xxhash.c and xxhash.h are BSD-2-Clause
# xxhsum.c is GPL-2.0-or-later
License: BSD-2-Clause and GPL-2.0-or-later
Group: File tools
Url: http://www.xxhash.com/
Vcs: https://github.com/Cyan4973/xxHash
# git://git.altlinux.org/gears/x/xxhash.git
Source: %name-%version-%release.tar

%description
xxHash is an Extremely fast Hash algorithm, running at RAM speed limits.
It successfully completes the SMHasher test suite which evaluates collision,
dispersion and randomness qualities of hash functions.  Code is highly
portable, and hashes are identical across all platforms (little / big endian).

%package -n lib%name
Summary: Extremely fast hash algorithm - library
License: BSD-2-Clause
Group: System/Libraries

%description -n lib%name
xxHash is an Extremely fast Hash algorithm, running at RAM speed limits.
It successfully completes the SMHasher test suite which evaluates collision,
dispersion and randomness qualities of hash functions.  Code is highly
portable, and hashes are identical across all platforms (little / big endian).

%package -n lib%name-devel
Summary: Extremely fast hash algorithm - development files
License: BSD-2-Clause
Requires: lib%name = %EVR
Group: Development/C

%description -n lib%name-devel
Development files for the xxhash library.

%prep
%setup -n %name-%version-%release

%build
%add_optflags %(getconf LFS_CFLAGS)
%make_build libxxhash xxhsum xxh32sum xxh64sum xxh128sum xxhsum_inlinedXXH \
	MOREFLAGS="$RPM_OPT_FLAGS"
rm xxhsum
mv xxhsum_inlinedXXH xxhsum

%install
export CC=false CXX=false # nothing should be compiled or linked during install
%makeinstall_std PREFIX=%_prefix LIBDIR=%_libdir
rm -rf %buildroot%_libdir/*.a

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%check
make check
make test-xxhsum-c

%files
%_bindir/xxh*sum
%_man1dir/xxh*sum.1*
%doc CHANGELOG LICENSE README.md

%files -n lib%name
%_libdir/libxxhash.so.*
%doc CHANGELOG LICENSE README.md

%files -n lib%name-devel
%_includedir/xxhash.h
%_includedir/xxh3.h
%_libdir/libxxhash.so
%_pkgconfigdir/libxxhash.pc

%changelog
* Fri Dec 15 2023 L.A. Kostis <lakostis@altlinux.ru> 0.8.2-alt1
- 0.8.2.

* Tue Jul 06 2021 Dmitry V. Levin <ldv@altlinux.org> 0.8.0-alt2
- Use default %%_optlevel to fix build on ppc64le (by glebfm@).

* Sun Aug 02 2020 Dmitry V. Levin <ldv@altlinux.org> 0.8.0-alt1
- 0.7.4 -> 0.8.0.

* Thu Jun 25 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.4-alt1
- new version 0.7.4 (with rpmrb script)

* Thu Mar 19 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.3-alt1
- new version 0.7.3 (with rpmrb script)

* Sat Oct 12 2019 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- new version 0.7.2 (with rpmrb script)

* Thu Sep 26 2019 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 0.6.5-alt1
- initial build for ALT Sisyphus

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.5-1
- Update to version 0.6.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.4-1
- Update to version 0.6.4
- Drop previously backported patches

* Thu Oct 19 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.3-2
- Correct License tag (command line tool is GPLv2+)
- Adjust Source tag to get a more descriptive tarfile name

* Wed Oct 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.6.3-1
- Initial packaging
