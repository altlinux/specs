%define _unpackaged_files_terminate_build 1
%define app_id io.elementary.%name
%define linter_name %{name}er
%define linter_name_versioned %linter_name-1
%define linter_name_versioned_full %linter_name_versioned.0
%define linter_lib_name lib%linter_name
%define linter_lib_name_versioned_full lib%linter_name_versioned_full

Name: vala-lint
Version: 20240828
Release: alt1

Summary: Check code-style of Vala code files
License: GPL-2.0-or-later
Group: Development/Tools
Url: https://github.com/vala-lang/vala-lint
Vcs: https://github.com/vala-lang/vala-lint.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

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

%package -n %linter_lib_name
Summary: Vala linter library
Group: Development/C

%description -n %linter_lib_name
%summary.

%package -n %linter_lib_name-devel
Summary: Vala linter library development files
Group: Development/C

Requires: %linter_lib_name = %EVR

%description -n %linter_lib_name-devel
%summary.

%package -n %linter_lib_name-devel-vala
Summary: Vala linter library vala development files
Group: Development/Other

BuildArch: noarch
Requires: %linter_lib_name-devel = %EVR

%description -n %linter_lib_name-devel-vala
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_bindir/%app_id
%doc README.md

%files -n %linter_lib_name
%_libdir/%linter_lib_name_versioned_full.so.*

%files -n %linter_lib_name-devel
%_libdir/%linter_lib_name_versioned_full.so
%_includedir/%linter_name_versioned_full/%linter_name.h
%_pkgconfigdir/%linter_name_versioned.pc

%files -n %linter_lib_name-devel-vala
%_vapidir/%linter_name_versioned.vapi

%changelog
* Tue Feb 18 2025 Vladimir Vaskov <rirusha@altlinux.org> 20240828-alt1
- Initial build.
