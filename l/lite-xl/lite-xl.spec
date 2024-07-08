%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define _product org.lite_xl.lite_xl

Name: lite-xl
Version: 2.1.5
Release: alt1

Summary: A lightweight text editor written in Lua
License: MIT
Group: Development/Tools
Url: https://lite-xl.com/
Vcs: https://github.com/lite-xl/lite-xl

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

AutoReq: nolua

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: liblua-devel
BuildRequires: libpcre2-devel
BuildRequires: freetype2-devel
BuildRequires: libSDL2-devel

%description
A lightweight, simple, fast, feature-filled, and extremely
extensible text editor written in C, and Lua, adapted from lite.
Lite XL is derived from lite. It is a lightweight text editor
written mostly in Lua - it aims to provide something practical,
pretty, small and fast easy to modify and extend, or to use
without doing either.
The aim of Lite XL compared to lite is to be more user friendly,
improve the quality of font rendering, and reduce CPU usage.

%prep
%setup

%build
%meson -Duse_system_lua=true
%meson_build

%install
%meson_install

%files
%_bindir/%name
%_datadir/%name/
%_datadir/doc/%name/licenses.md
%_datadir/metainfo/%_product.appdata.xml
%_desktopdir/%_product.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Mon Jul 08 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.5-alt1
- Updated to 2.1.5.

* Thu May 16 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.4-alt1
- Updated to 2.1.4.

* Fri Apr 12 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.3-alt1
- Built for ALT Sisyphus (closes #50000).

