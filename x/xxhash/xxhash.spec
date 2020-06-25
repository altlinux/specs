Name: xxhash
Version: 0.7.4
Release: alt1

Summary: Extremely fast hash algorithm

#		The source for the library (xxhash.c and xxhash.h) is BSD
#		The source for the command line tool (xxhsum.c) is GPLv2+
License: BSD and GPLv2+
Group: File tools
Url: http://www.xxhash.com/

# Source-url:	https://github.com/Cyan4973/xxHash/archive/v%version/%name-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

%description
xxHash is an Extremely fast Hash algorithm, running at RAM speed
limits. It successfully completes the SMHasher test suite which
evaluates collision, dispersion and randomness qualities of hash
functions. Code is highly portable, and hashes are identical on all
platforms (little / big endian).

%package -n lib%name
Summary: Extremely fast hash algorithm - library
License: BSD
Group: System/Libraries

%description -n lib%name
xxHash is an Extremely fast Hash algorithm, running at RAM speed
limits. It successfully completes the SMHasher test suite which
evaluates collision, dispersion and randomness qualities of hash
functions. Code is highly portable, and hashes are identical on all
platforms (little / big endian).

%package -n lib%name-devel
Summary: Extremely fast hash algorithm - development files
License: BSD
Requires: lib%name = %EVR
Group: Development/C

%description -n lib%name-devel
Development files for the xxhash library

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix LIBDIR=%_libdir
rm -f %buildroot/%_libdir/libxxhash.a

%check
make check
make test-xxhsum-c

%files
%_bindir/xxh*sum
%_man1dir/xxh*sum.1*
%doc LICENSE
%doc README.md

%files -n lib%name
%_libdir/libxxhash.so.*
%doc LICENSE
%doc README.md

%files -n lib%name-devel
%_includedir/xxhash.h
%_includedir/xxh3.h
%_libdir/libxxhash.so
%_pkgconfigdir/libxxhash.pc

%changelog
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
