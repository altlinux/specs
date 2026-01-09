%define _unpackaged_files_terminate_build 1

Name: dfl-utils
Version: 0.3.0
Release: alt1

Summary: Some utilities for DFL
License: GPL-3.0-only
Group: System/Libraries
Url: https://gitlab.com/desktop-frameworks/utils

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)

%description
%summary. Simple logging support for DFL.

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries

%description -n lib%{name}
%summary. Simple logging support for DFL.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: lib%{name} = %version-%release

%description -n lib%{name}-devel
Development files for %{name}.

%summary. Simple logging support for DFL.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n lib%{name}
%doc ChangeLog LICENSE README.md ReleaseNotes
%_libdir/libdf6utils.so.0
%_libdir/libdf6utils.so.0.3.0

%files -n lib%{name}-devel
%_includedir/DFL/DF6/DFUtils.hpp
%_libdir/libdf6utils.so
%_pkgconfigdir/df6utils.pc

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
