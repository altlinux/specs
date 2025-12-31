%define _unpackaged_files_terminate_build 1

Name: dfl-ipc
Version: 0.3.0
Release: alt1

Summary: Very simple set of IPC classes for inter-process communication
License: GPL-3.0-only
Group: System/Libraries
Url: https://gitlab.com/desktop-frameworks/ipc

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)

%description
%summary

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries

%description -n lib%{name}
%summary

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
%_libdir/libdf6ipc.so.0
%_libdir/libdf6ipc.so.0.3.0

%files -n lib%{name}-devel
%_includedir/DFL/DF6/DFIpcClient.hpp
%_includedir/DFL/DF6/DFIpcServer.hpp
%_includedir/DFL/DF6/DFWayfireIPC.hpp
%_libdir/libdf6ipc.so
%_pkgconfigdir/df6ipc.pc

%changelog
* Mon Dec 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
