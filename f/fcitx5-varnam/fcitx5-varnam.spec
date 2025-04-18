Name: fcitx5-varnam
Version: 0.0.2
Release: alt1

Summary: Fcitx5 wrapper for Varnam input method
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://varnamproject.com
Vcs: https://github.com/varnamproject/varnam-fcitx5

Source: %name-%version.tar

Patch: fix-fcitx5-varnam-0.02-ALT-CMakeLists.txt.patch

BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires(pre): cmake extra-cmake-modules gcc-c++

BuildRequires: libgovarnam-devel varnam-schemes fcitx5-devel pkg-config

%description
Fcitx5 wrapper for Varnam input method. Easily type Indian languages on Linux
desktops.

%prep
%setup
%patch

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_libdir/fcitx5/libvarnamfcitx.so
%_datadir/fcitx5/addon/varnamfcitx.conf
%_datadir/fcitx5/inputmethod/varnamfcitx.conf
%_iconsdir/hicolor/48x48/apps/varnam*.png
%_metainfodir/com.varnamproject.Fcitx5.Addon.varnamfcitx.metainfo.xml

%changelog
* Tue Apr 15 2025 Ulysses Apokin <ulysses@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus.
