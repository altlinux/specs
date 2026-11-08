%define _unpackaged_files_terminate_build 1

Name: pragtical-plugin-manager
Version: 1.8.0
Release: alt1
Summary: A pragtical plugin manager
License: MIT
Group: Development/Tools
Url: https://pragtical.com/
Vcs: https://github.com/pragtical/plugin-manager
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
Requires: pragtical
BuildRequires(pre): rpm-macros-meson
# Automatically added by buildreq on Fri Nov 06 2026
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libgpg-error libhttp-parser libmbedx509-9 libp11-kit libtfpsacrypto-devel lua5.4 ninja-build openssl-config p11-kit-trust perl pkg-config python3 python3-base sh5 xz
BuildRequires: libgit2-devel liblzma-devel libmbedtls-devel libzip-devel lua-devel meson zlib-devel

%description
`ppm` manages Pragtical plugins, colors, fonts, and editor installations. It
includes the Plugin Manager UI for searching, filtering, and managing addons.

%prep
%setup
%autopatch -p1

%build
%meson \
  -Dstatic=true \
  -Drelease_version="%version" \
  -Dinstall_plugin=true \

%meson_build

%install
%meson_install

%add_findreq_skiplist %_datadir/pragtical/plugins/plugin_manager/*
%files
%doc CHANGELOG* LICENSE* README* SPEC*
%_bindir/*
%_datadir/pragtical/plugins/plugin_manager/

%changelog
* Sat Nov 07 2026 Ildar Mulyukov <ildar@altlinux.ru> 1.8.0-alt1
- Initial build for Sisyphus
