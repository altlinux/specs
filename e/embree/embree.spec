%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define build_type RelWithDebInfo
%set_verify_elf_method strict

%ifnarch %e2k
%def_with ispc
%else
# no ispc on e2k
%def_without ispc
%endif

%define libsuffix 4
%define soname 4

Name: embree
Version: 4.3.2
Release: alt1
Summary: Collection of high-performance ray tracing kernels developed at Intel
Group: Graphics
License: Apache-2.0
URL: https://embree.github.io

# https://github.com/embree/embree.git
Source: %name-%version.tar

Source1: %name.watch

Patch2000: %name-e2k.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: libgif-devel
%if_with ispc
BuildRequires: ispc
%endif
BuildRequires: pkgconfig(glut)
BuildRequires: pkgconfig(glfw3)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(OpenImageIO)
BuildRequires: pkgconfig(tbb)

# https://github.com/embree/embree/issues/186
ExclusiveArch: aarch64 x86_64 %e2k

%description
A collection of high-performance ray tracing kernels intended to graphics 
application engineers that want to improve the performance of their application.

%package -n lib%{name}%{libsuffix}-%soname
Summary: Collection of high-performance ray tracing kernels developed at Intel
Group: System/Libraries

%description -n lib%{name}%{libsuffix}-%soname
A collection of high-performance ray tracing kernels intended to graphics 
application engineers that want to improve the performance of their application.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%{name}%{libsuffix}-%soname = %EVR

%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%setup
%ifarch %e2k
%patch2000 -p1
%endif

%build
# limit parallel build
#if [ %__nprocs -gt 4 ] ; then
#	export NPROCS=4
#fi

%ifarch %e2k
%add_optflags -Wno-reduced-alignment -Wno-sign-compare -mno-avx
%endif

%cmake \
	-DCMAKE_BUILD_TYPE=%build_type \
	-DCMAKE_STRIP:STRING="" \
	-DEMBREE_IGNORE_CMAKE_CXX_FLAGS=OFF \
	-DEMBREE_TUTORIALS=OFF \
	-DEMBREE_COMPACT_POLYS=ON \
%if_without ispc
	-DEMBREE_ISPC_SUPPORT=OFF \
	-DEMBREE_MAX_ISA=DEFAULT \
%endif
	%nil

%cmake_build

%install
%cmakeinstall_std

# Remove unpackaged files
rm -rf %buildroot%_docdir/%{name}%{libsuffix}
rm -f %buildroot%prefix/%{name}-vars.*

%files -n lib%{name}%{libsuffix}-%soname
%doc LICENSE.txt
%doc README.md CHANGELOG.md readme.pdf third-party-programs-TBB.txt third-party-programs.txt
%_libdir/lib%{name}%{libsuffix}.so.%{soname}

%files devel
%_libdir/lib%{name}%{libsuffix}.so
%_includedir/%{name}%{libsuffix}/
%_libdir/cmake/%name-%version/
%_man3dir/*

%changelog
* Mon Jul 01 2024 L.A. Kostis <lakostis@altlinux.ru> 4.3.2-alt1
- Updated to upstream version 4.3.2.

* Thu Feb 15 2024 L.A. Kostis <lakostis@altlinux.ru> 4.3.1-alt1
- Updated to upstream version 4.3.1.

* Fri Oct 27 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.3.0-alt1.1
- Updated patch for Elbrus.

* Thu Oct 26 2023 L.A. Kostis <lakostis@altlinux.ru> 4.3.0-alt1
- Updated to upstream version 4.3.0.

* Mon Sep 11 2023 L.A. Kostis <lakostis@altlinux.ru> 4.2.0-alt1
- Updated to upstream version 4.2.0.

* Sun Jul 09 2023 L.A. Kostis <lakostis@altlinux.ru> 4.1.0-alt1
- Updated to upstream version 4.1.0.
- enable back ispc support.
- aarch64: enable build.

* Mon Feb 28 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.13.3-alt1
- Updated to upstream version 3.13.3.

* Thu Dec 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.13.2-alt1
- Updated to upstream version 3.13.2.
- Built without ispc.

* Wed Oct 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.13.1-alt2
- Disabled unsupported build for %%ix86 and aarch64 architectures.

* Tue Aug 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.13.1-alt1
- Updated to upstream version 3.13.1.

* Wed Jun 23 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.13.0-alt3
- enabled build on ix86 and aarch64 architectures
- added patch for Elbrus

* Fri Jun 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.13.0-alt2
- Moved man pages to devel package.

* Wed May 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.13.0-alt1
- Updated to upstream version 3.13.0.

* Wed Feb 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.12.2-alt1
- Updated to upstream version 3.12.2.

* Fri Oct 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.12.1-alt1
- Updated to upstream version 3.12.1.

* Wed Oct 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.12.0-alt1
- Updated to upstream version 3.12.0.

* Tue Sep 01 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.0-alt1
- Initial build for ALT.

* Sun Aug 02 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.11.0-4
- Rebuild for ispc 1.14.1 (#1855915)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 3.11.0-2
- Use __cmake_in_source_build

* Thu Jun 25 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.11.0-1
- Update to 3.11.0 (#1850917)

* Tue Jun 09 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.10.0-3
- Enable double indexed polygons

* Tue Jun 09 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.10.0-2
- Rebuild for ispc 1.13.0 and Blender 2.83.0

* Mon May 11 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0 (#1834394)

* Fri Apr 10 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0

* Wed Feb 05 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0 (#1792573)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0 (#1747113)

* Wed Sep 25 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.6.1-2
- Drop renaming libraries parameter on cmake

* Sat Sep 07 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1
- Rebuild for ispc 1.12.0

* Tue Aug 20 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0

* Sat Aug 17 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.6.0-0.1.beta
- Update to 3.6.0-beta.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.2-2
- Rebuilt for ispc 1.11.0

* Fri Mar 22 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2
- Rebuilt for ispc 1.10.0
- Disable tutorials

* Sat Mar 02 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0
- Add glfw dependency

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2.40b9acagit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 3.0.0-1.40b9acagit
- Upstream snapshot compile fix for gcc 8
- Optimize spec file

* Fri Mar 02 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Luya Tshimbalanga  <luya@fedoraproject.org> - 3.0.0-0.1.beta
- Update to 3.0.0-beta.0
- Add manual directory

* Wed Jan 17 2018 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.17.2-1
- Update to 2.17.2 (#1512896)

* Wed Oct 25 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.17.0-2
- Rebase to more current snapshot for LLVM 5.0 support

* Thu Sep 21 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.17.0-1
- Update to 2.17.0 (#1494058)

* Tue Aug 15 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.16.5-1
- Update to 2.16.5 (#1481678)

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 2.16.4-4
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.16.4-1
- Update to 2.16.4 (#1466767)

* Thu Jun 15 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.16.2-1
- Update to 2.16.2 (#1459537)

* Wed May 17 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.16.0-1
- New upstream release

* Tue Mar 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.0-2
- Honor Fedora compilation flags again (rhbz#1436075)

* Wed Mar 22 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.15.0-1
- New upstream release

* Thu Mar 16 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.14.0-3
- Rebuild for ispc

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 09 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.14.0-1
- New upstream release
- Drop patch as the fix is included upstream

* Thu Jan 19 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.13.0-3
- Patch fixing initialization code of the rayStreamFilters sent by upstream (rhbz#1414611)

* Thu Jan 19 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.13.0-2
- Workaround lowering max_ISA to avx on non-Intel CPU (rhbz#1414611)

* Tue Nov 22 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 2.13.0-1
- Upstream update

* Tue Oct 18 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.12.0-1
- Upstream update addressing larger memory consumption

* Sat Sep 24 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.11.0-1
- Latest upstream update

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> 2.10.0-8
- Rebuild for tbb 2017

* Thu Aug 25 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.10.0-7
- Used ExclusiveArch for 64bit Architecture

* Sun Aug 21 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.10.0-6
- Located flags before cmake
- Used libexecdir for subpackages examples
- Pleased rpmlint
- Added examples subpackages

* Sat Aug 20 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.10.0-5
- Silenced all warning message in build
- Added %%check line
- Added examples subpackages

* Sat Aug 20 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.10.0-4
- Added ispc dependency
- Removed ExclusiveArch
- Enabled ispc and tutorials

* Fri Aug 12 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 2.10.0-3
- Use ExclusiveArch tag for 64 bits architectures
- Adjust the lines of descriptions
- Fix bin path
- Add freeglut dependency from upstream

* Sat Aug 6 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 2.10.0-2
- Fixed mixed use space and tabs errors
- Shorten the line of description
- Exclude i686 architecture

* Thu Aug 4 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 2.10.0-1
- Initial build
