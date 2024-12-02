%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define soname 0

Name: libfilediff
Version: 0.2.1
Release: alt1

Summary: A library that finds corrupted files
License: GPL-3.0
Group: System/Libraries
URL: https://github.com/qualimock/libfilediff
VCS: https://github.com/qualimock/libfilediff

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libxxhash)

%description
%summary.

%package -n %name%soname
Summary: %{summary %name}
Group: System/Libraries

%description -n %name%soname
%{description %name}.

%package devel
Group: Development/C++
Summary: Headers files and library symbolic links for %name
Requires: %name%soname = %EVR

%description devel
This package contains headers and libs
required for building programs with %name.

%prep
%setup
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %name%soname
%_libdir/libfilediff.so.%{soname}*

%files devel
%_libdir/libfilediff.so
%_includedir/filediff.h
%_includedir/filediff_directory.h

%changelog
* Mon Dec 2 2024 Alexey Volkov <qualimock@altlinux.org> 0.2.1-alt1
- Initial build for ALT
