%define _unpackaged_files_terminate_build 1

Name: dfl-applications
Version: 0.3.0
Release: alt1

Summary: Thin wrapper around QApplication, QGuiApplication and QCoreApplication
License: GPL-3.0-only
Group: System/Libraries
Url: https://gitlab.com/desktop-frameworks/applications

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(df6ipc)

%description
%summary.

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries

%description -n lib%{name}
%summary.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: lib%{name} = %version-%release

%description -n lib%{name}-devel
Development files for %{name}.

%summary

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
%_libdir/libdf6application.so.0
%_libdir/libdf6application.so.0.3.0
%_libdir/libdf6coreapplication.so.0
%_libdir/libdf6coreapplication.so.0.3.0
%_libdir/libdf6guiapplication.so.0
%_libdir/libdf6guiapplication.so.0.3.0

%files -n lib%{name}-devel
%_includedir/DFL/DF6/DFApplication.hpp
%_includedir/DFL/DF6/DFCoreApplication.hpp
%_includedir/DFL/DF6/DFGuiApplication.hpp
%_libdir/libdf6application.so
%_libdir/libdf6coreapplication.so
%_libdir/libdf6guiapplication.so
%_pkgconfigdir/df6application.pc
%_pkgconfigdir/df6coreapplication.pc
%_pkgconfigdir/df6guiapplication.pc

%changelog
* Mon Dec 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
