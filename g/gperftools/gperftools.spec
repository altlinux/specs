%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
# LFS cannot be used due to hooks.
%set_verify_elf_method strict,lfs=relaxed,lint=relaxed

Name: gperftools
Version: 2.15
Release: alt1.1

Provides: google-perftools

Summary: Performance tools for C++ (pprof)
Group: Development/C++
Url: https://github.com/gperftools/gperftools
License: BSD-3-Clause

Source: %name-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: libunwind-devel

%description
gperftools is a collection of a high-performance multi-threaded
malloc() implementation, plus some pretty nifty performance analysis
tools.

%package -n lib%name
Summary: Performance tools for C++ (tcmalloc) - shared libraries
Group: System/Libraries
Provides: libgoogle-perftools

%description -n lib%name
The lib%name package is part of %name. It contains shared libraries
for analize the performance of C++ programs.

%package -n lib%name-devel
Summary: Performance tools for C++ (tcmalloc)
Group: Development/C++
Requires: lib%name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
The lib%name-devel package contains static and debug libraries and header
files for developing applications that use the %name package.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc %_defaultdocdir/%name
%_bindir/pprof*
%_man1dir/pprof.*

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%exclude %_includedir/google
%_includedir/%name
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%changelog
* Wed May 08 2024 Ivan A. Melnikov <iv@altlinux.org> 2.15-alt1.1
- NMU: full build on loongarch64

* Wed Mar 27 2024 Vitaly Chikunov <vt@altlinux.org> 2.15-alt1
- Update to 2.15 (2024-03-27).

* Thu Jul 20 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.10-alt2
- Basic support of LoongArch: build only tcmalloc (heap profiler and
  checker are not ported yet). Useful since many packages require tcmalloc.

* Thu Jun 16 2022 Fr. Br. George <george@altlinux.org> 2.10-alt1
- Autobuild version bump to 2.10

* Wed Mar 24 2021 Fr. Br. George <george@altlinux.ru> 2.9.1-alt1
- Autobuild version bump to 2.9.1

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 2.7-alt1
- Autobuild version bump to 2.7

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 2.6.3-alt1
- Autobuild version bump to 2.6.3

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 2.6.1-alt1
- Autobuild version bump to 2.6.1

* Mon May 29 2017 Fr. Br. George <george@altlinux.ru> 2.5.93-alt1
- Autobuild version bump to 2.5.93

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 2.5-alt1
- Autobuild version bump to 2.5

* Wed Jan 20 2016 Fr. Br. George <george@altlinux.ru> 2.4-alt2
- Fix build

* Mon Sep 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4-alt1
- Updated to 2.4.

* Wed Aug 21 2013 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Autobuild version bump to 2.1

* Thu Jun 27 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt2
- rebuilt with recent libunwind

* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.1
- Fixed build with gcc 4.7

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Autobuild version bump to 2.0
- Upstream renamed

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 1.9.1-alt1
- Autobuild version bump to 1.9.1

* Tue Aug 30 2011 Fr. Br. George <george@altlinux.ru> 1.8.3-alt1
- Autobuild version bump to 1.8.3

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 1.8.2-alt1
- Autobuild version bump to 1.8.2

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 1.8.1-alt1
- Autobuild version bump to 1.8.1

* Tue Jul 19 2011 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Autobuild version bump to 1.8

* Tue Feb 15 2011 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Mon Sep 20 2010 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Version up

* Tue Apr 13 2010 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Version up

* Sat Sep 19 2009 Alexey Voinov <voins@altlinux.ru> 1.4-alt1
- new version (1.4)
- obsolete tag added [#19117]

* Thu Jul 16 2009 Alexey Voinov <voins@altlinux.ru> 1.3-alt1
- new version (1.3)
- file-lists simplified

* Thu Dec 04 2008 Yuriy Kashirin <uka@altlinux.ru> 0.99.2-alt1
- New version
- Removed unneeded patches
- Updated home URL
- Updated BuildRequires

* Tue Dec 02 2008 Yuriy Kashirin <uka@altlinux.ru> 0.97-alt2
- Replaced manual Requires gcc-c++ by binutils
- Removed old 'as-needed' patch
- Fixed build in sisyphus
- Moved shared libraries to separate package
- Renamed %name-devel to lib%name-devel

* Tue Apr 22 2008 Avramenko Andrew <liks@altlinux.ru> 0.97-alt1
- New version

* Thu Oct 11 2007 Avramenko Andrew <liks@altlinux.ru> 0.93-alt1
- New version

* Fri Jul 27 2007 Avramenko Andrew <liks@altlinux.ru> 0.92-alt1
- New version

* Thu May 31 2007 Avramenko Andrew <liks@altlinux.ru> 0.91-alt3
- Buildrequires libunwind-devel for ALL archs

* Fri May 25 2007 Avramenko Andrew <liks@altlinux.ru> 0.91-alt2
- Add dependencies on libunwind to fix x86_64 build

* Wed Apr 25 2007 Avramenko Andrew <liks@altlinux.ru> 0.91-alt1
- New version
- Moved to git
- Disable static
- Spec cleanup
- x86_64 build fixed

* Fri Mar 30 2007 Avramenko Andrew <liks@altlinux.ru> 0.8-alt1
- Initial build for Sisyphus

* Fri Mar 11 2005 <opensource@google.com>
- First draft
