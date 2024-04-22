%define _unpackaged_files_terminate_build 1

Name: lite-xl-plugin-manager
Version: 1.2.9
Release: alt2

Summary: A lite-xl plugin manager
License: MIT
Group: Development/Tools
Url: https://lite-xl.com/
Vcs: https://github.com/lite-xl/lite-xl-plugin-manager

# doesn't compile in a machine with this weird architecture
ExcludeArch: ppc64le

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: zlib-devel
BuildRequires: libmbedtls-compat-devel
BuildRequires: libgit2-devel
BuildRequires: libzip-devel
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
%meson -Dstatic=true -Dversion="%version"
%meson_build

%install
%__install -pD -m0755 %_target_platform/lpm %buildroot%_bindir/lpm

%files
%doc CHANGELOG.md LICENSE README.md
%_bindir/lpm

%changelog
* Mon Apr 22 2024 Anton Zhukharev <ancieg@altlinux.org> 1.2.9-alt2
- Fixed version detection.

* Mon Apr 22 2024 Anton Zhukharev <ancieg@altlinux.org> 1.2.9-alt1
- Built for ALT Sisyphus (closes: #50115).

