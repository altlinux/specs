Name: fcitx5-varnam
Version: 0.0.2
Release: alt2

Summary: Fcitx5 wrapper for Varnam input method
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://varnamproject.com
Vcs: https://github.com/varnamproject/varnam-fcitx5

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: fcitx5-devel
BuildRequires: gcc-c++
BuildRequires: libgovarnam-devel
BuildRequires: pkg-config
BuildRequires: varnam-schemes

%description
Fcitx5 wrapper for Varnam input method. Easily type Indian languages on Linux
desktops.

%prep
%setup

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
* Tue Aug 12 2025 Ulysses Apokin <ulysses@altlinux.org> 0.0.2-alt2
- Used pkg-config.
- Cleaned spec.

* Tue Apr 15 2025 Ulysses Apokin <ulysses@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus.
