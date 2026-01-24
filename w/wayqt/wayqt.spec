%define _unpackaged_files_terminate_build 1

Name: wayqt
Version: 0.3.0
Release: alt2

Summary: Qt-based wrapper for various wayland protocols
License: MIT
Group: System/Libraries
Url: https://gitlab.com/desktop-frameworks/wayqt

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6WaylandClient)
BuildRequires: pkgconfig(libpng)

%description
%summary

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries

%description -n lib%{name}
The Qt-based library to handle Wayland and Wlroots protocols to be used
with any Qt project.
Additionally, Wayfire's private protocol as well is supported. As the
project develops, support for custom protocols may be added.
This work is heavily inspired by the wrapland project. Instead of using
qtwaylandscanner to generate Qt classes for the wayland protocols, we use
the raw C structs, as in the Wrapland project. While this is a general
purpose library, it is built to cater the needs of DesQ and PaperDE
projects.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: lib%{name} = %version-%release

%description -n lib%{name}-devel
Development files for %{name}.

The Qt-based library to handle Wayland and Wlroots protocols to be used
with any Qt project.
Additionally, Wayfire's private protocol as well is supported. As the
project develops, support for custom protocols may be added.
This work is heavily inspired by the wrapland project. Instead of using
qtwaylandscanner to generate Qt classes for the wayland protocols, we use
the raw C structs, as in the Wrapland project. While this is a general
purpose library, it is built to cater the needs of DesQ and PaperDE
projects.

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

%files -n lib%{name}
%doc ChangeLog LICENSE README.md ReleaseNotes
%_libdir/libwayqt-qt6.so.0
%_libdir/libwayqt-qt6.so.0.3.0

%files -n lib%{name}-devel
%doc examples
%dir %_includedir/DFL/DF6/wayqt
%_includedir/DFL/DF6/wayqt/*.hpp
%_libdir/libwayqt-qt6.so
%_pkgconfigdir/wayqt-qt6.pc

%changelog
* Sat Jan 24 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt2
- Fix FTBFS by defining private_headers as bool in meson.build.

* Mon Dec 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
