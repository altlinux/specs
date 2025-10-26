%define _unpackaged_files_terminate_build 1

Name: ryokucha
Version: 0.3.1
Release: alt1

Summary: A GTK4 library that includes customized widgets
License: LGPL-3.0-or-later
Group: System/Libraries
Url: https://github.com/ryonakano/ryokucha

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk4)

%description
%summary

%package -n lib%{name}-devel
Summary: GTK4 library that includes customized widgets
Group: Development/C

%description -n lib%{name}-devel
Development files for GTK4 library that includes customized widgets

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n lib%{name}-devel
%doc LICENSE README.md
%_includedir/ryokucha.h
%_libdir/libryokucha.so
%_pkgconfigdir/ryokucha.pc
%_datadir/vala/vapi/ryokucha.deps
%_datadir/vala/vapi/ryokucha.vapi

%changelog
* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus
