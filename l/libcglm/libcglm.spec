%define proj cglm

Name: lib%proj
Version: 0.8.9
Release: alt1

Summary: CGLM is highly optimized graphics math (glm) for C
License: MIT
Group: System/Libraries

Url: https://cglm.readthedocs.io/
# Vcs-Source: https://github.com/recp/%proj/archive/refs/tags/v%version.tar.gz
Source: %name-%version-%release.tar
# sisyphus_check insists on @altlinux.*, let Packager: be a comment
# Spec-Author: Igor Molchanov <akemi_homura@kurisa.ch>



BuildRequires(Pre): rpm-macros-meson
BuildRequires: meson

%description
cglm is optimized 3D math library written in C99 (compatible with C89).
It is similar to original glm library except this is mainly for C.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package includes the files necessary for developing programs
which will use the %name library.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_libdir/%name.so.*

%files devel
%_includedir/cglm
%_includedir/%proj/*
%_pkgconfigdir/%proj.pc
%_libdir/%name.so

%changelog
* Wed Feb 22 2023 Artyom Bystrov <arbars@altlinux.org> 0.8.9-alt1
- update to new version

* Sat Jan 15 2022 Artyom Bystrov <arbars@altlinux.org> 0.8.7-alt1
- update to new version

* Sat Jan 15 2022 Michael Shigorin <mike@altlinux.org> 0.8.4-alt2
- built for sisyphus

* Fri Jan 14 2022 Igor Molchanov <akemi_homura@kurisa.ch> 0.8.4-alt1
- Initial build.
