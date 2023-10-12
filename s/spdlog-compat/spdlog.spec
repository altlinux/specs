%define rname spdlog

Name: %rname-compat
Version: 1.10.0
Release: alt2

Summary: Super fast C++ logging library

Group: Development/Other
License: MIT
Url: https://github.com/gabime/spdlog

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/gabime/%rname/archive/v%version.tar.gz
Source: %rname-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: libbenchmark-devel libfmt-devel

%description
This is a packaged version of the gabime/spdlog header-only C++
logging library available at Github.

%package -n lib%rname
Summary: Super fast C++ logging library
Group: Development/C++

%description -n lib%rname
This is a packaged version of the gabime/spdlog header-only C++
logging library available at Github.

%prep
%setup -n %rname-%version
rm -rfv include/spdlog/fmt/bundled/

%build
%cmake -DSPDLOG_BUILD_SHARED=ON \
       -DSPDLOG_FMT_EXTERNAL=ON \
       -DSPDLOG_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install
# enable external libfmt using
%__subst "s|// #define SPDLOG_FMT_EXTERNAL|#define SPDLOG_FMT_EXTERNAL|" %buildroot%_includedir/spdlog/tweakme.h
%__rm -rf %buildroot%_includedir
%__rm -rf %buildroot%_libdir/libspdlog.so
%__rm -rf %buildroot%_libdir/cmake
%__rm -rf %buildroot%_pkgconfigdir

%check
export LD_LIBRARY_PATH=$(pwd)/%_cmake__builddir
%cmake_build --target test

%files -n lib%rname
%_libdir/libspdlog.so.*

%changelog
* Thu Oct 12 2023 Nazarov Denis <nenderus@altlinux.org> 1.10.0-alt2
- Build as compat

* Tue Jul 19 2022 Vladimir Didenko <cow@altlinux.ru> 1.10.0-alt1
- 1.10.0 released

* Mon Nov 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.9.2-alt1
- 1.9.2 released

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt2
- remove bundled fmt, use _cmake__builddir

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 1.8.5-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- new version 1.8.5 (with rpmrb script)

* Mon Mar 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- new version 1.8.2 (with rpmrb script)

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Thu Jan 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- patch tweakme.h to use external libfmt for the library clients (ALT bug 37969)

* Tue Jan 28 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)
- build a library, with external libfmt

* Sun Feb 10 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 1.2.1-alt2
- Fixed %_libdir/cmake/spdlog directory ownership.

* Sun Nov 18 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Wed Aug 22 2018 Paul Wolneykien <manowar@altlinux.org> 1.1.0-alt1
- New version: 1.1.0.

* Wed Aug 22 2018 Paul Wolneykien <manowar@altlinux.org> 0.17.0-alt2
- Build the package. Install missing development configuration
  files. Run tests.

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.17.0-alt1
- new version 0.17.0 (with rpmrb script)

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- initial build for ALT Sisyphus

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 04 2016 Daniel Kopecek <dkopecek@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Fri Jul 08 2016 Daniel Kopecek <dkopecek@redhat.com> - 0-8.20160703git34bb86b
- update to rev 34bb86b

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20151110gitcbc8ba7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-6.20151110gitcbc8ba7
- update to rev cbc8ba7

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.20150410git211ce99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-4.20150410git211ce99
- don't build the base package
- remove a dot from the release tag
- corrected -devel subpackage description

* Mon Apr 20 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-3.20150410git.211ce99
- use the -p option when copying the header files

* Tue Apr 14 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-2.20150410git.211ce99
- don't build the debuginfo subpackage
- require libstdc++-devel
- don't generate a distribution specific pkg-config file

* Fri Apr 10 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-1.20150410git.211ce99
- Initial package
