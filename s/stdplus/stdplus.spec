# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    stdplus
Version: 0.1
Release: alt3.git9b9648d.1

Summary: The minimum set of features needed by the OpenBMC project
License: Apache-2.0
Group:   Development/Other
URL:     https://www.openbmc.org
Vcs:     https://github.com/openbmc/stdplus.git

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(liburing)
BuildRequires: function2-devel
BuildRequires: pkgconfig(gtest)

%description
%name is a C++ project containing commonly used classes and functions for
the Linux platform.

%package -n lib%name
Group: Development/Other
Summary: %summary

%description -n lib%name
Library that provides the minimum set of features needed by the OpenBMC project
and other users.

%package -n lib%name-devel
Group: Development/Other
Summary: %summary

%description -n lib%name-devel
Development files that provides the minimum set of features needed by the
OpenBMC project and other users.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files -n lib%name
%_libdir/lib%name.so.*
%_libdir/lib%name-*.so.*

%files -n lib%name-devel
%doc *.md
%_bindir/run_with_tmp
%_libdir/lib%name.so
%_libdir/lib%name-*.so
%_includedir/%name
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%name-*.pc

%changelog
* Thu Jun 25 2026 Anatoly Mukosey <mukav@altlinux.org> 0.1-alt3.git9b9648d.1
- New snapshot.
- Enable tests.

* Tue Aug 26 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1-alt2.gitd8e0af5
- NMU: Downgraded to commit from revision list.

* Thu Apr 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.1-alt1
- Initial build for Sisyphus.
