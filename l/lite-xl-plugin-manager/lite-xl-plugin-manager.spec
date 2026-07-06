%define _unpackaged_files_terminate_build 1

Name: lite-xl-plugin-manager
Version: 1.4.7
Release: alt1

Summary: A lite-xl plugin manager
License: MIT
Group: Development/Tools
Url: https://lite-xl.com/
Vcs: https://github.com/lite-xl/lite-xl-plugin-manager

# doesn't compile in a machine with this weird architecture
ExcludeArch: ppc64le

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

# Lua autoreq generates bad dependencies.
# While it is broken, it should be disabled.
AutoReq: nolua
Requires: lite-xl

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: zlib-devel
BuildRequires: libmbedtls-compat-devel
BuildRequires: libgit2-devel
BuildRequires: libzip-devel
BuildRequires: liblzma-devel
BuildRequires: liblua-devel

%description
A standalone binary that provides an easy way of installing, and uninstalling
plugins from lite-xl, as well as different version of lite-xl.

Can be used by a package manager plugin that works from inside the editor and
calls this binary.

Also contains a plugin_manager.lua plugin to integrate the binary with lite-xl
in the form of an easy-to-use GUI.

Conforms to SCPS3.

%prep
%setup
%autopatch -p1

%build
%meson -Dstatic=true -Dversion="%version" -Dinstall_plugin=true
%meson_build

%install
%meson_install

%files
%doc CHANGELOG.md LICENSE README.md
%_bindir/lpm
%_datadir/lite-xl/plugins/welcome.lua
%_datadir/lite-xl/plugins/plugin_manager/

%changelog
* Mon Jul 06 2026 Anton Zhukharev <ancieg@altlinux.org> 1.4.7-alt1
- Updated to 1.4.7.

* Wed Feb 19 2025 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Mon Dec 09 2024 Anton Zhukharev <ancieg@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.

* Mon Apr 22 2024 Anton Zhukharev <ancieg@altlinux.org> 1.2.9-alt2
- Fixed version detection.

* Mon Apr 22 2024 Anton Zhukharev <ancieg@altlinux.org> 1.2.9-alt1
- Built for ALT Sisyphus (closes: #50115).
