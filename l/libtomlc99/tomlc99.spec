%define unpackaged_files_terminate_build 1
%define _name tomlc99
%define major 1
%define soversion %major.0

Name: lib%_name
Version: %soversion
Release: alt1.git5221b3d

Summary: C-library for toml-files parsing
License: %mit
Group: Development/C
Url: https://github.com/cktan/tomlc99
Source0: %name-%version.tar
Patch: %name-%version-alt1.git5221b3d-makefile-fixes.patch

BuildRequires(pre): rpm-build-licenses

%description
C library for parsing toml files.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %EVR
%description devel
Development package for %name

%package devel-static
Summary: Static variant of %name library for parsing toml files
Group: Development/C
%description devel-static
Static variant of %name library for parsing toml files

%prep
%setup -q
%patch -p1

%build
%make_build

%install
%makeinstall_std prefix=%_prefix LIBDIR=%_lib
ln -s libtoml.so.%{soversion} %buildroot%_prefix/%_lib/libtoml.so

%files
%_prefix/%_lib/libtoml.so.%{soversion}

%files devel
%_prefix/%_lib/libtoml.so
%_pkgconfigdir/libtoml.pc
%_includedir/toml.h

%files devel-static
%_prefix/%_lib/libtoml.a

%changelog
* Tue Nov 19 2024 Aleksey Saprunov <sav@altlinux.org> 1.0-alt1.git5221b3d
- Initial build.
