%define _unpackaged_files_terminate_build 1

Name: clipman
Version: 1.6.5
Release: alt1

Summary: Simple clipboard manager for Wayland
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/chmouel/clipman

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang

BuildRequires: golang

Requires: wl-clipboard

%description
%summary.

%prep
%setup -a1
%patch -p1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm755 %name %buildroot%_bindir/%name

%files
%doc CHANGELOG.md COPYING README.md
%_bindir/clipman

%changelog
* Mon Dec 29 2025 Nikolay Strelkov <snk@altlinux.org> 1.6.5-alt1
- Initial build for Sisyphus
