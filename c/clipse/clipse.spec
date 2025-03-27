Name: clipse
Version: 1.1.0
Release: alt1
License: MIT

Summary: Configurable TUI clipboard manager for Unix

Group: Text tools

Url: https://github.com/savedra1/clipse

# Source-url: https://github.com/savedra1/clipse/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
clipse is a configurable, TUI-based clipboard manager application written in Go
with minimal dependency. Though the app is optimized for a Linux OS using
a dedicated window manager, clipse can also be used on any Unix-based system.

%prep
%setup -a1

# Optimize the default configuration
subst 's|Type:      "basic"|Type: "kitty"|' config/constants.go

%build
%gobuild -mod=vendor

%install
install -D -m 0755 ./clipse %buildroot/%_bindir/clipse

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/clipse

%changelog
* Thu Mar 27 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.1.0-alt1
- Initial build
