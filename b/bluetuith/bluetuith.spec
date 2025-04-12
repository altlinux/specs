Name: bluetuith
Version: 0.2.3
Release: alt1
License: MIT

Summary: A TUI bluetooth manager for Linux

Group: System/Configuration/Hardware

Url: https://github.com/bluetuith-org/bluetuith
Vcs: https://github.com/bluetuith-org/bluetuith.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
bluetuith is a TUI-based bluetooth connection manager,
which can interact with bluetooth adapters and devices.
It aims to be a replacement to most bluetooth managers.

%prep
%setup -a1

%build
%gobuild -mod=vendor

%install
install -D -m 0755 ./%name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Sat Apr 12 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.3-alt1
- Initial build
