%define _unpackaged_files_terminate_build 1

Name: dfl-sni
Version: 0.3.0
Release: alt1

Summary: Implementation of the XDG Status Notification Specifications
License: GPL-3.0-only
Group: System/Libraries
Url: https://gitlab.com/desktop-frameworks/status-notifier

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(dbusmenu-lxqt)

%description
%summary

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries

%description -n lib%{name}
Implementation of the XDG Status Notification Specifications.
DFL::StatusNotifierWatcher and DFL::StatusNotifierItem classes make it
easy to create a system tray applications.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: lib%{name} = %version-%release

%description -n lib%{name}-devel
Development files for %{name}.

Implementation of the XDG Status Notification Specifications.
DFL::StatusNotifierWatcher and DFL::StatusNotifierItem classes make it
easy to create a system tray applications.

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
%_libdir/libdf6sni.so.0
%_libdir/libdf6sni.so.0.3.0

%files -n lib%{name}-devel
%_includedir/DFL/DF6/DFSNITypes.hpp
%_includedir/DFL/DF6/DFStatusNotifierItem.hpp
%_includedir/DFL/DF6/DFStatusNotifierWatcher.hpp
%_libdir/libdf6sni.so
%_pkgconfigdir/df6sni.pc

%changelog
* Mon Dec 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
