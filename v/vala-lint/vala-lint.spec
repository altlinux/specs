%define _unpackaged_files_terminate_build 1
%define app_id io.elementary.%name
%define api_version 1
%define linter_name %{name}er
%define linter_lib_name lib%linter_name

Name: vala-lint
Version: 0.1.0
Release: alt1.a1d1a7bc.1
Epoch: 1

Summary: Check code-style of Vala code files
License: GPL-2.0-or-later
Group: Development/Tools
Url: https://github.com/vala-lang/vala-lint
Vcs: https://github.com/vala-lang/vala-lint.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: %linter_name = %EVR

BuildRequires (pre): rpm-macros-meson
BuildRequires: rpm-build-vala
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(libvala-0.56)
BuildRequires: pkgconfig(gio-2.0) >= 2.56.4
BuildRequires: pkgconfig(json-glib-1.0)

%description
Small command line tool and library for checking Vala code files for
code-style errors. Based on the elementary Code-Style guidelines.

%package -n %linter_lib_name%api_version
Summary: Vala linter library
Group: Development/C

%description -n %linter_lib_name%api_version
%summary.

%package -n %linter_lib_name-devel
Summary: Vala linter library development files
Group: Development/C

Requires: %linter_lib_name%api_version = %EVR

%description -n %linter_lib_name-devel
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
ln -s %app_id %buildroot%_bindir/%name

%check
%meson_test

%files
%_bindir/%app_id
%_bindir/%name
%doc README.md

%files -n %linter_lib_name%api_version
%_libdir/%linter_lib_name-%api_version.*.so.%api_version
%_libdir/%linter_lib_name-%api_version.*.so.%api_version.*

%files -n %linter_lib_name-devel
%_libdir/%linter_lib_name-%api_version.*.so
%_includedir/%linter_name-%api_version.*/%linter_name.h
%_pkgconfigdir/%linter_name-%api_version.pc
%_vapidir/%linter_name-%api_version.vapi

%changelog
* Wed Sep 03 2025 Vladimir Vaskov <rirusha@altlinux.org> 1:0.1.0-alt1.a1d1a7bc.1
- New snapshot.
- Started using snapshots for package versioning
  (upstream doesn't have tags).
- Added provides to vala-linter.
- Created symlink %app_id -> %name.

* Tue Feb 18 2025 Vladimir Vaskov <rirusha@altlinux.org> 20240828-alt1
- Initial build.
