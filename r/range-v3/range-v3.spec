# Check also https://github.com/EasyCoding/range-v3/blob/master/range-v3.spec

%def_with test

Name: range-v3
Version: 0.12.0
Release: alt1

Summary: Range library for C++14/17/20, basis for C++20's std::ranges

License: Boost
Group: Development/C++
Url: https://github.com/ericniebler/range-v3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ericniebler/range-v3/archive/%version.tar.gz
Source: %name-%version.tar

# https://bugzilla.altlinux.org/show_bug.cgi?id=37930
# https://bugzilla.altlinux.org/show_bug.cgi?id=38830
Patch: a91f0e1be27a31c446452a753001d4518ef83a6b.patch

BuildArch: noarch

BuildRequires: gcc-c++

BuildRequires(pre): rpm-build-intro >= 2.1.14
BuildRequires: cmake
BuildRequires: boost-devel-static

%if_with test
BuildRequires: ctest
%endif

%description
Range library for C++14/17/20. This code was the basis
of a formal proposal to add range support to the C++ standard library.
That proposal evolved through a Technical Specification,
and finally into P0896R4 "The One Ranges Proposal"
which was merged into the C++20 working drafts in November 2018.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Provides: %name-static = %version-%release

%description -n lib%name-devel
Range library for C++14/17/20. This code was the basis
of a formal proposal to add range support to the C++ standard library.
That proposal evolved through a Technical Specification,
and finally into P0896R4 "The One Ranges Proposal"
which was merged into the C++20 working drafts in November 2018.

%prep
%setup
#patch -p1
%__subst 's|DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/range-v3|DESTINATION share/cmake/range-v3|g' CMakeLists.txt
%__subst '/-Werror/d' cmake/ranges_flags.cmake

%build
# needed for test
%cmake_insource \
%if_without test
    -DRANGE_V3_TESTS:BOOL=OFF \
%endif
    -DRANGE_V3_DOCS:BOOL=OFF
%make_build

%check
%if_with test
ctest --output-on-failure
%endif

%install
%makeinstall_std
rm -vf %buildroot%_includedir/module.modulemap

%files -n lib%name-devel
%doc README.md CREDITS.md TODO.md
%doc LICENSE.txt
%_includedir/meta/
%_includedir/range/
%_includedir/concepts
%_includedir/std
%_datadir/cmake/%name

%changelog
* Sun Aug 28 2022 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version 0.12.0 (with rpmrb script)

* Fri Apr 23 2021 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt2
- build with gcc10 on Sisyphus

* Thu Aug 20 2020 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt3
- build range-v3 in any case, use gcc8

* Sat Jan 25 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt2
- rewrite spec
- build test with cmake and run it
- move headers direct to /usr/include
- disable build on aarch64 and ppc64le (see bug 37930)

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Thu Oct 03 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- new version 0.4.0 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.3.6-alt1
- new version 0.3.6 (with rpmrb script)

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 0.3.5-alt1
- new version 0.3.5 (with rpmrb script)

* Sun Dec 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1.20171112git0b0dd88
- initial build for ALT Sisyphus

* Fri Dec 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1.20171112git0b0dd88
- Initial SPEC release.
