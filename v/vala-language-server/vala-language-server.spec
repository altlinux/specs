%define _unpackaged_files_terminate_build 1

Name: vala-language-server
Version: 0.48.7
Release: alt1

Summary: Code Intelligence for Vala & Genie
License: LGPL-2.1-only
Group: Development/Tools
Url: https://github.com/vala-lang/vala-language-server
Vcs: https://github.com/vala-lang/vala-language-server.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(libvala-0.56)
BuildRequires: pkgconfig(jsonrpc-glib-1.0)
BuildRequires: pkgconfig(gee-0.8)

%description
%summary.

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

%files
%_bindir/%name
%doc README.md

%changelog
* Tue Feb 18 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.48.7-alt1
- Initial build.
