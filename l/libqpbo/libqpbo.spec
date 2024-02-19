%define        _unpackaged_files_terminate_build 1
%define        origname qpbo

Name:          lib%{origname}
Version:       1.5.0
Release:       alt1
Summary:       QPBO implementation by Vladimir Kolmogorov as a system library
License:       BSD-2-Clause
Group:         Sciences/Mathematics
Url:           https://github.com/fgrsnau/libqpbo
Vcs:           https://github.com/fgrsnau/libqpbo.git

Source:        %name-%version.tar
Patch:         %name-%version-%release.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc-common

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%ifarch x86_64 %ix86
%add_optflags -msse2
%endif

%description
Ready-to-use QPBO adaptation for OpenGM (original code courtesy of V.
Kolmogorov)

Implements algorithms for minimizing functions of binary variables with unary
and pairwise terms based on roof duality described in the following papers.


%package       devel
Group:         Development/C++
Summary:       QPBO implementation by Vladimir Kolmogorov as a system library development files.

%description   devel
Ready-to-use QPBO adaptation for OpenGM (original code courtesy of V.
Kolmogorov)

Implements algorithms for minimizing functions of binary variables with unary
and pairwise terms based on roof duality described in the following papers.


%package       devel-static
Group:         Development/C++
Summary:       QPBO implementation by Vladimir Kolmogorov as a system library static files.

%description   devel-static
Ready-to-use QPBO adaptation for OpenGM (original code courtesy of V.
Kolmogorov)

Implements algorithms for minimizing functions of binary variables with unary
and pairwise terms based on roof duality described in the following papers.


%prep
%setup
%autopatch -p1

%build
%cmake_insource
%cmake_build

%install
%cmakeinstall_std


%files
%doc CHANGES.TXT
%_libdir/%{name}*.so.*

%files         devel
%doc CHANGES.TXT
%_libdir/%{name}*.so
%_includedir/%{origname}*
%_pkgconfigdir/%origname.pc
%_libdir/cmake/%origname/%origname-config.*
%_libdir/cmake/%origname/%origname-targets*

%files         devel-static
%doc CHANGES.TXT
%_libdir/%{name}*.a
%_libdir/cmake/%origname/%origname-static-*


%changelog
* Sun Feb 11 2024 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- initial build v1.5.0 for Sisyphus
