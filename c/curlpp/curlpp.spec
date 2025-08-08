Name:    curlpp
Version: 0.8.1
Release: alt1

Summary: C++ wrapper around libcURL
License: MIT
Group:   Development/C++
Url:     https://www.curlpp.org
Vcs:     https://github.com/jpbarrette/curlpp.git

Source: %name-%version.tar
Patch0: arch-indep-curlpp-config.patch
Patch1: curlpp-missing-version-number.patch
Patch2: fix-build-with-new-curl-version.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libcurl)

%description
%summary

%package -n lib%name
Group:   Development/C++
Summary: Shared library %summary

%description -n lib%name
cURLpp is a %summary

%package -n lib%name-devel
Group:   Development/C++
Summary: %summary development headers and docs

%description -n lib%name-devel
cURLpp is a %summary

%package -n lib%name-devel-static
Group:   Development/C++
Summary: Statically linked %summary library

%description -n lib%name-devel-static
cURLpp is a %summary

%prep
%setup
%autopatch -p1

%build
# Resolve troubles with static library brp-check
%add_optflags -ffat-lto-objects
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%doc *.md doc/{AUTHORS,guide.pdf,LICENSE,TODO}
%_bindir/%name-config
%_includedir/utilspp
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%files -n lib%name-devel-static
%_libdir/lib%name.a

%changelog
* Fri Aug 08 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus.
