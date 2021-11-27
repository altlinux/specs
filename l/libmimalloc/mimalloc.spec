Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
%define oldname mimalloc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%undefine __cmake_in_source_build

Name:           libmimalloc
Version:        2.0.3
Release:        alt1_1
Summary:        A general purpose allocator with excellent performance

License:        MIT
URL:            https://github.com/microsoft/mimalloc
Source0:        %{url}/archive/v%{version}/%{oldname}-%{version}.tar.gz

BuildRequires:  ctest cmake
BuildRequires:  gcc-c++
Source44: import.info
Patch33: mimalloc-2.0.3-alt-soname.patch

%description
mimalloc (pronounced "me-malloc")
is a general purpose allocator with excellent performance characteristics.
Initially developed by Daan Leijen for the run-time systems.

%package -n libmimalloc2
Summary:        Shared library for the %oldname library
Group:          System/Libraries

%description -n libmimalloc2
mimalloc (pronounced "me-malloc")
is a general purpose allocator with excellent performance characteristics.
Initially developed by Daan Leijen for the run-time systems.

This package contains the shared library.

%package -n libmimalloc-devel
Group: Development/C
Summary:        Development environment for %oldname
Requires:       libmimalloc2 = %EVR
Provides: %oldname-devel = %EVR

%description -n libmimalloc-devel
Development package for mimalloc.

%prep
%setup -n %{oldname}-%{version} -q

# Remove unneded binary from sources
rm -rf bin

%if "%version" == "2.0.3"
%patch33 -p1
%else
echo update release in patch
exit 1
%endif

%build
%{fedora_v2_cmake} \
    -DMI_BUILD_OBJECT=OFF \
    -DMI_OVERRIDE=OFF \
    -DMI_INSTALL_TOPLEVEL=ON \
    -DMI_BUILD_STATIC=OFF \
    -DMI_BUILD_TESTS=OFF \
    -DCMAKE_BUILD_TYPE=Release
%fedora_v2_cmake_build


%install
%fedora_v2_cmake_install


%files -n libmimalloc2
%doc --no-dereference LICENSE
%doc readme.md
%_libdir/libmimalloc.so.2
%_libdir/libmimalloc.so.2.*

%files -n libmimalloc-devel
%{_libdir}/lib%{oldname}.so
%{_libdir}/cmake/%{oldname}/
%{_includedir}/*


%changelog
* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 2.0.3-alt1_1
- new version

* Tue Jun 01 2021 Arseny Maslennikov <arseny@altlinux.org> 1.0-alt1.1
- NMU: spec: adapted to new CMake macros.

* Sun Jun 23 2019 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build for ALT

